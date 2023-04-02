// Get the Masters degree checkbox
const mastersCheckbox = document.getElementById('masters');

// Get the Masters degree title text box
const mastersTitleTextbox = document.getElementById('masters-title');

// Add event listener to Masters degree checkbox
mastersCheckbox.addEventListener('change', function() {
  // If checkbox is checked, display Masters degree title text box
  if (mastersCheckbox.checked) {
    mastersTitleTextbox.style.display = 'block';
  }
  // If checkbox is unchecked, hide Masters degree title text box
  else {
    mastersTitleTextbox.style.display = 'none';
  }
});

// Get the Masters degree checkbox
const jobCheckbox = document.getElementById('working');

// Get the Masters degree title text box
const jobTitleTextbox = document.getElementById('working-title');

// Add event listener to Job title checkbox
jobCheckbox.addEventListener('change', function() {
  // If checkbox is checked, display Job title text box
  if (jobCheckbox.checked) {
  jobTitleTextbox.style.display = 'block';
  }
  // If checkbox is unchecked, hide Job title text box
  else {
  jobTitleTextbox.style.display = 'none';
  }
});

const certificateCheckbox = document.getElementById('certificate');

// Get the Masters degree title text box
const certificateTitleTextbox = document.getElementById('certificate-title');

// Add event listener to Certificate checkbox
certificateCheckbox.addEventListener('change', function() {
  // If checkbox is checked, display Certificate title text box
  if (certificateCheckbox.checked) {
  certificateTitleTextbox.style.display = 'block';
  }
  // If checkbox is unchecked, hide Certificate title text box
  else {
  certificateTitleTextbox.style.display = 'none';
  }
  });
  