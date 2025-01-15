async function login(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    const loginDate = {
        email,
        password,
    }

    try {
        const response = await fetch("/api/users/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(loginDate)
        });

        const result = await response.json();

        if(response.ok) {
            alert("Login realizado com sucesso!");
            console.log("Token de acesso:", result.token);

            localStorage.setItem("authToken", result.token);

            window.location.href = "/inicio";

        } else {
            alert(`Erro no login: ${result.message || "Email ou senha inválidos."}`);
        }
    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro ao tentar realizar login. Tente novamente mais tarde.");
    }

}

let formularioLogin = document.getElementById('formulario-login');
formularioLogin.addEventListener('submit', login)