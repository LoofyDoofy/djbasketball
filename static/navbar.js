const toggleButton = document.getElementsByClassName('toggle-button')[0];
const navbarLinks = document.getElementsByClassName('navbar-links')[0];

toggleButton.addEventListener('click', () => {
  // toggle between the classes of navbarLinks, which is the class navbar-links
  navbarLinks.classList.toggle('active');
});
