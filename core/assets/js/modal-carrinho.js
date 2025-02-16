// função para abrir o modal do carrinho
function abrirModal() {

    const modalCarrinho = document.getElementById('modal-carrinho');
    
    modalCarrinho.classList.add('ativo');

    // Adicionar o evento ao botão "Finalizar Compra" quando o modal for aberto
    const pagamento = document.getElementById('pagamento');
    if (pagamento) {
        pagamento.addEventListener('click', telaPagamento);
    }

}

function fecharModal() {
    const modalCarrinho = document.getElementById('modal-carrinho');

    modalCarrinho.classList.remove('ativo');

    // Remover o evento de clique no botão "Finalizar Compra" quando o modal for fechado
    const pagamento = document.getElementById('pagamento');
    if (pagamento) {
        pagamento.removeEventListener('click', telaPagamento);
    }
}


const iconCarrinho = document.getElementById('icon-carrinho');
iconCarrinho.addEventListener('click', abrirModal);

const iconFecharmModal = document.getElementById('icon-fechar-modal');
iconFecharmModal.addEventListener('click', fecharModal);

// Fechar o modal ao clicar fora dele
document.addEventListener('click', function(event) {
    const modalCarrinho = document.getElementById('modal-carrinho');
    
    // Verifica se o clique foi fora do modal
    if (!modalCarrinho.contains(event.target) && event.target !== iconCarrinho) {
        modalCarrinho.classList.remove('ativo'); // Fecha o modal
    }
});

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

function telaPagamento() {
    window.location.href = "/pagamento";
}


