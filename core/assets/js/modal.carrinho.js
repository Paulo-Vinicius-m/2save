// função para abrir o modal do carrinho
function abrirModal() {

    const modalCarrinho = document.getElementById('modal-carrinho');
    
    modalCarrinho.classList.add('ativo');

}

function fecharModal() {
    const modalCarrinho = document.getElementById('modal-carrinho');

    modalCarrinho.classList.remove('ativo')
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