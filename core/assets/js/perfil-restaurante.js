const navbarToggle = document.querySelector('.navbar-toggler');
    const menu = document.getElementById('navbarMenu');
    
    navbarToggle.addEventListener('click', () => {
        menu.classList.toggle('show');
});

document.addEventListener("DOMContentLoaded", async () => {
    try {
      const response = await fetch('assets/js/perfil-restaurante.json');
      const userInfo = await response.json();
      
      // Atualizando os elementos no DOM
      document.getElementById("user-image").src = userInfo.imagem;
      document.getElementById("user-name").textContent = userInfo.nome;
      document.getElementById("user-email").textContent = userInfo.email;
      document.getElementById("user-cpf").textContent = userInfo.cpf;
      document.getElementById("user-company").textContent = userInfo.empresa;
      
      
    }catch (error) {
        console.error('Erro ao carregar dados:', error);
    }
 
});
