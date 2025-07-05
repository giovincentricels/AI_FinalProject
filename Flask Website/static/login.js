// Toggle the visibility of the menu when the hamburger icon is clicked
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const authContainer = document.querySelector('.auth-container');

signUpButton.addEventListener('click', () => {
  authContainer.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
  authContainer.classList.remove('right-panel-active');
});

document.getElementById('signInForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission
  alert('Sign In Successful'); // Display the success alert
  location.reload(); // Refresh the page
});

document.getElementById('signUpForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission
  alert('Sign Up Successful'); // Display the success alert
  location.reload(); // Refresh the page
});