
async function cadastro(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const email2 = document.getElementById("confirmacao-email").value.trim();
    const password = document.getElementById("password").value;
    const identificador = document.getElementById("cpf").value.trim();
    const tipo = document.querySelector('input[name="tipo"]:checked').value;

    if (email !== email2) {
        alert("Os emails não conferem.");
        return;
    }

    const userData = { 
        name,
        email, 
        email2, 
        password, 
        tipo, 
        identificador, 
    };

    try {
        const response = await fetch("/api/users/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        const result = await response.json();

        if (response.ok) {
            alert("Cadastro realizado com sucesso!");
            localStorage.setItem("authToken", result.token);
            window.location.href = "/";
        } else {
            alert(`Erro no cadastro: ${result.message || "Erro desconhecido."}`);
        }

    } catch (error) {
        console.error("Erro no cadastro:", error);
        alert("Erro ao tentar realizar o cadastro. Tente novamente mais tarde.");
    } 
}

let formularioCadastro = document.getElementById('formulario-cadastro');
formularioCadastro.addEventListener('submit', cadastro);