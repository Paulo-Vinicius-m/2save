// Função para preencher a tabela com os dados da API
function preencherTabela(pedidos) {
    const tabelaPedidos = document.getElementById('tabela-pedidos');
    tabelaPedidos.innerHTML = ''; // Limpa a tabela antes de adicionar os novos dados

    pedidos.forEach(pedido => {
        // Cria uma nova linha na tabela
        const tr = document.createElement('tr');

        // Cria as células para a imagem, número do pedido, produto, valor e endereço
        tr.innerHTML = `
            <td><img src="${pedido.imagem}" alt="Imagem do pedido" width="50" height="50"></td>
            <td id=${pedido.id}> N° do Pedido ${pedido.id}</td>
            <td id=${pedido.produto}>${pedido.produto}</td>
            <td id=${pedido.valor}>R$ ${pedido.valor}</td>
            <td id=${pedido.endereco}>${pedido.endereco}</td>
            <td>
                <img src="/assets/img/pedido/icon-confirm.png" alt="Icone de confirma">
                <img src="/assets/img/pedido/icon-lixeira.png" alt="Icone da lixeira">
            </td>
        `;

        // Adiciona a linha à tabela
        tabelaPedidos.appendChild(tr);
    });
}

// Função para fazer a requisição e obter os dados da API
function obterPedidos() {
    fetch('/assets/js/pedidos.json') 
        .then(response => response.json())
        .then(data => {
            const pedidos = data.refeicoes;
            preencherTabela(pedidos);
        })
        .catch(error => console.error('Erro ao carregar os pedidos:', error));
}

// Chama a função para obter os pedidos ao carregar a página
document.addEventListener('DOMContentLoaded', obterPedidos());

// Menu Hamburguer
const navbarToggle = document.querySelector('.navbar-toggler');
    const menu = document.getElementById('navbarMenu');
    
    navbarToggle.addEventListener('click', () => {
        menu.classList.toggle('show');
});
