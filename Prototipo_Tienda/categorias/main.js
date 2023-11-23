document.addEventListener('DOMContentLoaded', function() {
  const productImages = document.querySelectorAll('.product img');
  const modal = document.getElementById('productModal');
  const modalImg = document.getElementById('modalImg');

  productImages.forEach(img => {
    img.addEventListener('click', function() {
      modal.style.display = 'block';
      modalImg.src = this.src;
    });
  });

  const closeModal = document.querySelector('.close');

  closeModal.addEventListener('click', function() {
    modal.style.display = 'none';
  });

  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});
