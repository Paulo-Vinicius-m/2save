// Função para alternar a visibilidade do menu
function toggleMenu(event) {
    const menu = document.getElementById('menu');
    const currentDisplay = window.getComputedStyle(menu).visibility;
    
    // Alterna a classe 'show' para animar a transição
    if (currentDisplay === 'hidden') {
      menu.classList.add('show');
      // Adiciona um ouvinte de evento para fechar o menu quando clicar fora dele
      document.addEventListener('click', closeMenuOnClickOutside);
    } else {
      menu.classList.remove('show');
      // Remove o ouvinte de evento quando o menu for fechado
      document.removeEventListener('click', closeMenuOnClickOutside);
    }
  }
  
  // Função para fechar o menu quando clicar fora dele
  function closeMenuOnClickOutside(event) {
    const menu = document.getElementById('menu');
    const menuIcon = document.querySelector('.menu-icon');
    
    // Verifica se o clique foi fora do menu e do ícone do menu
    if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
      menu.classList.remove('show');
      document.removeEventListener('click', closeMenuOnClickOutside);
    }
  }
  
  