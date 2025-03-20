document.addEventListener('DOMContentLoaded', () => {
    const campoSenha = document.querySelector('#senha');
    const botaoMostrarSenha = document.querySelector('.mostrar-senha');

    botaoMostrarSenha.addEventListener('click', () => {
        if (campoSenha.type === 'password') {
            campoSenha.type = 'text';
            botaoMostrarSenha.classList.remove('bi-eye');
            botaoMostrarSenha.classList.add('bi-eye-slash');
        } else {
            campoSenha.type = 'password';
            botaoMostrarSenha.classList.remove('bi-eye-slash');
            botaoMostrarSenha.classList.add('bi-eye');
        }
    });
});
