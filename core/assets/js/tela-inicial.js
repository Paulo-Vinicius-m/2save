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

// evento de ao carregar a página vai deixar selecionado já um botão e um texto
document.addEventListener('DOMContentLoaded', () => {
    const botaoSelecionado = document.querySelector('.custom-btn.selecionado');
    const textoInicial = botaoSelecionado.getAttribute('data-texto');

    document.getElementById('titulo').textContent = textoInicial;

    document.querySelectorAll('.custom-btn').forEach(botao => {
        botao.addEventListener('click', mudaTitulo);
    });

    carregarDados();
    mudarSecoes(); 

});

// função que muda as seções ao clicar no botão
function mudarSecoes() {
    const botoes = document.querySelectorAll('.custom-btn');
    const secoes = document.querySelectorAll('.secao-container');

    // Define uma seção inicial ao carregar a página
    document.getElementById('secao1').classList.add('active');

    // Adiciona evento de clique para cada botão
    botoes.forEach(botao => {
        botao.addEventListener('click', () => {
            const botaoClicado = botao.getAttribute('data-target');

            // esconde todas as secoes 
            secoes.forEach(secao => {
                secao.classList.remove('active');
            });

            // mostra a secao clicada
            const secaoAtiva = document.getElementById(botaoClicado);
            secaoAtiva.classList.add('active');

        });
    });
}

async function carregarDados() {
    try {
        const response = await fetch('assets/js/tela-inicial.json');
        const dados = await response.json();

        const secoes = {
            restaurantes: document.getElementById('secao1'),
            bebidas: document.getElementById('secao2'),
            refeicoes: document.getElementById('secao3')
        };

        for (const [categoria, items] of Object.entries(dados)) {
            items.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card-custom';
                card.innerHTML = `
                    <div class="container-imagem">
                        <img src="${item.imagem}" alt="Imagem ${categoria}">
                    </div>
                    <div class="container-informacoes">
                        <h2>${item.nome}</h2>
                        <p>${item.descricao}</p>
                        ${item.preco ? `<p>${item.preco}</p>` : ''}
                    </div>
                `;
                secoes[categoria].appendChild(card);
            });
        }
    } catch (error) {
        console.error('Erro ao carregar dados:', error);
    }
}

