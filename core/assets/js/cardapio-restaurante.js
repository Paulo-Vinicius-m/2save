// Menu Hamburguer
const navbarToggle = document.querySelector('.navbar-toggler');
    const menu = document.getElementById('navbarMenu');
    
    navbarToggle.addEventListener('click', () => {
        menu.classList.toggle('show');
});

