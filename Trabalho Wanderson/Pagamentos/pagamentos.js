document.addEventListener('DOMContentLoaded', () => {
    // Seleção do plano
    const selecionarButtons = document.querySelectorAll('.selecionar-plano');
    const paymentFormSection = document.querySelector('.payment-form-section');
    const planoSelecionadoSpan = document.querySelector('#planoSelecionado');
    let selectedPlan = '';
  
    selecionarButtons.forEach(button => {
      button.addEventListener('click', () => {
        selectedPlan = button.getAttribute('data-plano');
        const price = button.getAttribute('data-preco');
        planoSelecionadoSpan.textContent = `${selectedPlan} - R$ ${price}/mês`;
        // Exibe o formulário de pagamento
        paymentFormSection.classList.remove('d-none');
        paymentFormSection.scrollIntoView({ behavior: 'smooth' });
      });
    });
  
    // Simulação do processamento de pagamento
    const paymentForm = document.getElementById('paymentForm');
    const paymentStatus = document.getElementById('paymentStatus');
  
    paymentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      paymentStatus.textContent = 'Processando pagamento...';
      paymentStatus.style.color = 'white';
  
      // Simulação de chamada a uma API de pagamento (por exemplo, com fetch)
      setTimeout(() => {
        // Aqui você poderia integrar uma API real de pagamento
        paymentStatus.textContent = 'Pagamento realizado com sucesso!';
        paymentStatus.style.color = 'lime';
        paymentForm.reset();
      }, 2000);
    });
  });
  