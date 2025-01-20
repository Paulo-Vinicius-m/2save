document.addEventListener("DOMContentLoaded", () => {
  const inputBusca = document.getElementById('input-busca');
  const listaResultados = document.getElementById('lista-resultados');

  const itens = [
      'Sopa de Legumes',
      'Salada Caesar',
      'Frango Grelhado',
      'Lasanha',
      'Suco de Laranja',
      'Chá Gelado'
  ];
  inputBusca.addEventListener('input', () => {
      const termoBusca = inputBusca.value.toLowerCase();
      listaResultados.innerHTML = ''; // Limpa resultados anteriores

      itens.forEach(item => {
          if (item.toLowerCase().includes(termoBusca)) {
              const li = document.createElement('li');
              li.textContent = item;
              listaResultados.appendChild(li);
          }
      });
  });
});
