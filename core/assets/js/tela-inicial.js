// Função que muda o texto do titulo h2 e a cor do botão
function mudaTitulo(event) {
    const botaoClicado = event.target;
    const texto = botaoClicado.getAttribute('data-texto');

    // Atualiza o titulo do h2
    document.getElementById('titulo').textContent = texto;

    // Remove a classe 'selecionado' de todos os botões
    document.querySelectorAll('.custom-btn').forEach(botao => {
        botao.classList.remove('selecionado');
    });

    // Adiciona a classe 'selecionado' ao botão clicado
    botaoClicado.classList.add('selecionado');

}


document.addEventListener('DOMContentLoaded', () => {
    const botaoSelecionado = document.querySelector('.custom-btn.selecionado');
    const textoInicial = botaoSelecionado.getAttribute('data-texto');

    document.getElementById('titulo').textContent = textoInicial;

    document.querySelectorAll('.custom-btn').forEach(botao => {
        botao.addEventListener('click', mudaTitulo);
    });

});

