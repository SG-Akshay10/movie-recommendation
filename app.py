import pickle
import requests
import pandas as pd
import flask
import pymysql
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# MySQL configurations
app.secret_key = "3yLj3t5EYr%9#ZyP7cGc0"
conn = pymysql.connect(host="localhost", user="root", password="sriheera", database="mlcia2")
cursor = conn.cursor()

movie_dict = pickle.load(open('dataset/movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('dataset/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=598f57fe33ee4dfc4551dfc280a49d2b&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        data = cursor.fetchone()
        if data:
            session['loggedin'] = True
            session['id'] = data[0]
            session['username'] = data[1]
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:
        movie_title = movies['title'].values
        return render_template('home.html',movie_title=movie_title)
    else:
        return redirect(url_for('login'))

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_movie_name = request.form['movie-select']
    print(selected_movie_name)
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    print(recommended_movie_names)
    return render_template('recommend.html', recommended_movie_names=recommended_movie_names, recommended_movie_posters=recommended_movie_posters)

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        user_id = session.get('id')
        cursor.execute("SELECT * FROM users WHERE email = %s", (user_id))
        data = cursor.fetchone()
        if data:
            if new_password == confirm_password:
                cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
                conn.commit()
                return redirect(url_for('home'))
            else:
                return "New password and confirm password does not match."
        else:
            return "Incorrect current password."
    return render_template('forgot.html')

if __name__ == '__main__':
    app.run(debug=True)
