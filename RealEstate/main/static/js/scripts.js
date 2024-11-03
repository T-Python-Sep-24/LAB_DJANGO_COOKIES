// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');

    // Check for stored mode preference
    if (localStorage.getItem('mode') === 'dark') {
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-mode');
        document.body.style.backgroundImage = "url('/static/images/skyscraper-dark.jpg')";
    } else {
        document.body.classList.add('light-mode');
        document.body.style.backgroundImage = "url('/static/images/skyscraper.jpeg')";
    }

    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        document.body.classList.toggle('light-mode');

        // Update background image based on the mode
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('mode', 'dark');
            document.body.style.backgroundImage = "url('/static/images/skyscraper-dark.jpg')";
        } else {
            localStorage.setItem('mode', 'light');
            document.body.style.backgroundImage = "url('/static/images/skyscraper.jpeg')";
        }
    });
});
