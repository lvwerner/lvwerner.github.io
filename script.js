document.addEventListener('DOMContentLoaded', function () {
  var themeToggle = document.getElementById('theme-toggle');

  themeToggle.addEventListener('click', function () {
    var body = document.body;
    body.classList.toggle('light-theme');
    body.classList.toggle('dark-theme');
  });
});
