// Toggle the visibility of the menu when the hamburger icon is clicked
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}

document.querySelector('form').addEventListener('submit', function () {
    const submitButton = document.querySelector('form button[type="submit"]');
    submitButton.textContent = 'Predicting...';
    submitButton.disabled = true;
  });