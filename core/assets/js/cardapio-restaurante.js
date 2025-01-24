// Menu Hamburguer
const navbarToggle = document.querySelector('.navbar-toggler');
const menu = document.getElementById('navbarMenu');
    
navbarToggle.addEventListener('click', () => {
    menu.classList.toggle('show')
        
});

const containerModal = document.getElementById('container-modal');

// Abrir Modal
function abrirModal() {
    
    containerModal.classList.add('ativo');
}

// Fechar Modal
function fecharModal() {
    
    containerModal.classList.remove('ativo');
}

const btnAdicionarProduto = document.getElementById('btn-adicionar-produto');
btnAdicionarProduto.addEventListener('click', abrirModal);

const iconFecharModal = document.getElementById('icon-fechar-modal');
iconFecharModal.addEventListener('click', fecharModal);

async function enviarProduto(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value.trim();
    const descricao = document.getElementById('descricao').value.trim();
    const preco = Number(document.getElementById('preco').value);
    const imagem = document.getElementById('imagem');
    const tipo = document.getElementById('tipo').value.trim();
    
    // Criando o FormData
    const formData = new FormData();
    formData.append('nome', nome);
    formData.append('descricao', descricao);
    formData.append('preco', preco);
    formData.append('tipo', tipo);
    formData.append('imagem', imagem.files[0]); // Adiciona o arquivo da imagem

    try{
        const response = await fetch('/api/alterar-cardapio', {
            method: "POST",
            credentials: "include", 
            body: formData, 
        });

        if (response.ok) {
            const dados = await response.json();
            console.log("Produto cadastrado com sucesso:", dados);
            adicionarProdutoNaTela(dados);
            alert("Produto cadastrado com sucesso!");
            limparInputs(); // Limpa os campos após envio
        } else if (response.status === 401) {
            alert("Não autorizado. Verifique seu token de autenticação.");
        } else if (response.status === 400) {
            alert("Erro nos dados enviados. Verifique as informações.");
        } else {
            throw new Error("Erro inesperado.");
        }
    } catch(error){
        console.error("Erro no cadastro:", error);
       // alert("Erro ao tentar cadastrar os pedidos. Tente novamente mais tarde.");
        alert(`Erro ao tentar cadastrar os pedidos: ${error.message}. Tente novamente mais tarde.`);
    }
}

// Função para limpar os inputs do formulário
function limparInputs() {
    document.getElementById('nome').value = '';
    document.getElementById('descricao').value = '';
    document.getElementById('preco').value = '';
    document.getElementById('imagem').value = null;
    document.getElementById('tipo').value = '';
}

// Função para adicionar o produto dinamicamente na tela
function adicionarProdutoNaTela(dadosProduto) {
    const containerCardapio = document.getElementById('container-cardapio');

    const novoProduto = document.createElement('div');
    novoProduto.classList.add('produto');
    novoProduto.id = 'produto';

    novoProduto.innerHTML = `
        <div class="protudo-img">
            <img src="${dadosProduto.imagem || '/assets/img/tela-inicial/bebida.png'}" alt="Imagem da Comida">
            </div>
            <p class="produto-informacoes" id="produto-nome">${dadosProduto.nome || 'Produto'}</p>
            <p class="produto-informacoes" id="produto-valor">R$ ${dadosProduto.preco?.toFixed(2) || '0,00'}</p>
            <p class="produto-informacoes" id="produto-tempo">${dadosProduto.tempo_preparo || '30 min'}</p>
            <div class="icon-mais">
            <img src="/assets/img/cardapio-restaurante/icon-mais.png" alt="Icone Mais">
            </div>
            <div class="icon-lixeira">
            <img src="/assets/img/cardapio-restaurante/icon-lixeira.png" alt="Icone Lixeira">
        </div>
    `;

    containerCardapio.appendChild(novoProduto);
}

const formCadastroProduto = document.getElementById('form-cadastro-produto');
formCadastroProduto.addEventListener('submit', enviarProduto);

// função abrir modal para atualizar os campos do formulario
function atualizarProduto(produto) {
   // document.getElementById('produto-id').value = produto.id;
    document.getElementById('nome').value = produto.nome;
    document.getElementById('descricao').value = produto.descricao;
    document.getElementById('preco').value = produto.preco;
    document.getElementById('tipo').value = produto.tipo;
    abrirModal();
}

const iconMais = document.getElementById('icon-mais');
iconMais.addEventListener('click', atualizarProduto);

// Função para enviar os dados atualizados para a API
async function atualizarDadosProduto(event) {
    event.preventDefault();

    const id = document.getElementById('produto-id').value;
    const nome = document.getElementById('nome').value.trim();
    const descricao = document.getElementById('descricao').value.trim();
    const preco = Number(document.getElementById('preco').value);
    const tipo = document.getElementById('tipo').value.trim();
    const imagem = document.getElementById('imagem').files[0];

    const formData = new FormData();
    formData.append('id', id);
    formData.append('nome', nome);
    formData.append('descricao', descricao);
    formData.append('preco', preco);
    formData.append('tipo', tipo);
    if (imagem) {
        formData.append('imagem', imagem);
    }

    try {
        const response = await fetch('/api/alterar-cardapio', {
            method: 'PUT',
            credentials: 'include',
            body: formData,
        });

        if (response.ok) {
            const dados = await response.json();
            console.log('Produto atualizado com sucesso:', dados);
            alert('Produto atualizado com sucesso!');
            // Atualize a lista de produtos na página conforme necessário
            modal.style.display = 'none';
        } else if (response.status === 401) {
            alert('Não autorizado. Verifique seu token de autenticação.');
        } else if (response.status === 400) {
            alert('Erro nos dados enviados. Verifique as informações.');
        } else {
            throw new Error('Erro inesperado.');
        }
    } catch (error) {
        console.error('Erro na atualização:', error);
        alert('Erro ao tentar atualizar o produto. Tente novamente mais tarde.');
    }
}

async function deletarProduto(produtoId) {
    if (!confirm("Tem certeza que deseja excluir este produto?")) return;

    try {
        const response = await fetch('/api/alterar-cardapio', {
            method: 'DELETE',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: produtoId }),
        });

        if (response.ok) {
            console.log(`Produto com ID ${produtoId} deletado com sucesso.`);
            alert("Produto deletado com sucesso!");
            removerProdutoDaTela(produtoId);
        } else if (response.status === 401) {
            alert("Não autorizado. Verifique seu token de autenticação.");
        } else if (response.status === 400) {
            alert("Erro nos dados enviados. Verifique as informações.");
        } else {
            throw new Error("Erro inesperado.");
        }
    } catch (error) {
        console.error("Erro ao deletar o produto:", error);
        alert("Erro ao tentar deletar o produto. Tente novamente mais tarde.");
    }
}