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
        const response = await fetch('/api/restaurantes');
        const restaurantes = await response.json();

        // referencias das secoes
        const secaoRestaurantes = document.getElementById('secao1');
        const secaoBebidas = document.getElementById('secao2');
        const secaoRefeicoes = document.getElementById('secao3');

        // Limpa as seções antes de adicionar os novos dados
        secaoRestaurantes.innerHTML = '';
        secaoBebidas.innerHTML = '';
        secaoRefeicoes.innerHTML = '';

        for(const restaurante of restaurantes) {
            // Criação do card para restaurante
            const cardRestaurante = document.createElement('div');
            cardRestaurante.className = 'card-custom';

            // Fetch para obter a logo do restaurante
            let logoURL = restaurante.logo;
            if(logoURL) {
                try{
                    const logoResponse = await fetch(logoURL);
                    if(logoResponse.ok) {
                        logoURL = logoResponse.url;
                    } else {
                        logoURL = '/assets/img/tela-inicial/restaurante.png';
                    }
                } catch(error) {
                    console.error('Erro ao carregar a logo:', error);
                    logoURL = '/assets/img/tela-inicial/restaurante.png';
                }
            }else {
                logoURL = '/assets/img/tela-inicial/restaurante.png';
            }

            // HTML do card do restaurante
            cardRestaurante.innerHTML = `
                <div class="container-imagem">
                    <img src="${logoURL}" alt="Logo do restaurante ${restaurante.username}">
                </div>
                <div class="container-informacoes">
                    <h2>${restaurante.username}</h2>
                </div>
            `;

            secaoRestaurantes.appendChild(cardRestaurante);

            // Adiciona os pratos do restaurante
            restaurante.pratos.forEach(prato => {
                const cardPrato = document.createElement('div');
                cardPrato.className = 'card-custom';
                cardPrato.innerHTML = `
                    <div class="container-imagem">
                        <img src="${prato.imagem || '/assets/img/tela-inicial/refeicoes.png'}" alt="Imagem do prato ${prato.nome}">
                    </div>
                    <div class="container-informacoes">
                        <h2>${prato.nome}</h2>
                        <p>${prato.descricao}</p>
                        <p>Preço: R$ ${prato.preco}</p>
                    </div>
                `;
                secaoRefeicoes.appendChild(cardPrato);
            });

            // Adiciona as bebidas do restaurante
            restaurante.bebidas.forEach(bebida => {
                const cardBebida = document.createElement('div');
                cardBebida.className = 'card-custom';
                cardBebida.innerHTML = `
                    <div class="container-imagem">
                        <img src="${bebida.imagem || '/assets/img/tela-inicial/bebida.png'}" alt="Imagem da bebida ${bebida.nome}">
                    </div>
                    <div class="container-informacoes">
                        <h2>${bebida.nome}</h2>
                        <p>${bebida.descricao}</p>
                        <p>Preço: R$ ${bebida.preco}</p>
                    </div>
                `;
                secaoBebidas.appendChild(cardBebida);
            });
            
        }

    } catch(error) {
        console.error('Erro ao carregar os dados dos restaurantes:', error);
    }
}


