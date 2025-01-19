// função para atualizar os itens da lista do carrinho e exibir o total 
document.addEventListener("DOMContentLoaded", () => {
    // Função para atualizar o total
    const atualizarTotal = () => {
      let total = 0;
      const itens = document.querySelectorAll(".item");
  
      itens.forEach((item) => {
        const quantidadeElemento = item.querySelector(".quantidade-item");
        const valorElemento = item.querySelector(".valor-item");
        const quantidade = parseInt(quantidadeElemento.textContent);
        const valor = parseFloat(valorElemento.textContent.replace("R$", "").replace(",", "."));
  
        total += quantidade * valor;
      });
  
      // Atualizar o valor total
      const valorTotalElemento = document.querySelector(".valor-total");
      valorTotalElemento.textContent = `R$ ${total.toFixed(2).replace(".", ",")}`;
    };
  
    // Adicionar eventos para os botões
    const btnMais = document.querySelectorAll(".btn-mais");
    const btnMenos = document.querySelectorAll(".btn-menos");
  
    btnMais.forEach((btn) => {
      btn.addEventListener("click", () => {
        const quantidadeElemento = btn.parentElement.querySelector(".quantidade-item");
        let quantidade = parseInt(quantidadeElemento.textContent);
        quantidade += 1;
        quantidadeElemento.textContent = quantidade;
  
        atualizarTotal();
      });
    });
  
    btnMenos.forEach((btn) => {
      btn.addEventListener("click", () => {
        const quantidadeElemento = btn.parentElement.querySelector(".quantidade-item");
        let quantidade = parseInt(quantidadeElemento.textContent);
  
        if (quantidade > 0) {
          quantidade -= 1;
          quantidadeElemento.textContent = quantidade;
        }
  
        atualizarTotal();
      });
    });
  
    // Inicializar o total na carga da página
    atualizarTotal();
});