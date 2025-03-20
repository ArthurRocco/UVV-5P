document.addEventListener('DOMContentLoaded', () => {
    const campoSenha = document.querySelector('#senha');
    const botaoMostrarSenha = document.querySelector('.mostrar-senha');

    botaoMostrarSenha.addEventListener('click', () => {
        // Alterna o tipo do campo de senha
        if (campoSenha.type === 'password') {
            campoSenha.type = 'text';
            botaoMostrarSenha.classList.add('bi-eye-slash');
            botaoMostrarSenha.classList.remove('bi-eye');
        } else {
            campoSenha.type = 'password';
            botaoMostrarSenha.classList.add('bi-eye');
            botaoMostrarSenha.classList.remove('bi-eye-slash');
        }
    });
});
