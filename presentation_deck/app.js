document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentSlide = 1;

  const counterEl = document.getElementById('slide-counter');
  const progressBar = document.getElementById('progress-bar');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnGrid = document.getElementById('btn-grid');
  const btnTheme = document.getElementById('btn-theme');
  const btnFullscreen = document.getElementById('btn-fullscreen');
  const gridModal = document.getElementById('grid-modal');
  const btnCloseGrid = document.getElementById('btn-close-grid');
  const slideGrid = document.getElementById('slide-grid');

  function updateSlide(slideNum) {
    if (slideNum < 1) slideNum = 1;
    if (slideNum > totalSlides) slideNum = totalSlides;

    currentSlide = slideNum;

    slides.forEach((slide, idx) => {
      if (idx + 1 === currentSlide) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    counterEl.textContent = `${currentSlide} / ${totalSlides}`;
    progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;

    // Update grid active state
    document.querySelectorAll('.grid-thumb').forEach((thumb, idx) => {
      if (idx + 1 === currentSlide) {
        thumb.classList.add('active');
      } else {
        thumb.classList.remove('active');
      }
    });
  }

  function nextSlide() {
    if (currentSlide < totalSlides) {
      updateSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      updateSlide(currentSlide - 1);
    }
  }

  // Populate Grid Overview
  slides.forEach((slide, idx) => {
    const num = idx + 1;
    const titleEl = slide.querySelector('.slide-title, .hero-title');
    const titleText = titleEl ? titleEl.textContent : `Slide ${num}`;

    const thumb = document.createElement('div');
    thumb.className = `grid-thumb ${num === 1 ? 'active' : ''}`;
    thumb.innerHTML = `
      <div class="thumb-num">SLIDE ${num}</div>
      <div class="thumb-title">${titleText}</div>
    `;
    thumb.addEventListener('click', () => {
      updateSlide(num);
      gridModal.classList.remove('active');
    });
    slideGrid.appendChild(thumb);
  });

  // Event Listeners
  btnPrev.addEventListener('click', prevSlide);
  btnNext.addEventListener('click', nextSlide);

  btnGrid.addEventListener('click', () => {
    gridModal.classList.add('active');
  });

  btnCloseGrid.addEventListener('click', () => {
    gridModal.classList.remove('active');
  });

  btnTheme.addEventListener('click', () => {
    const html = document.documentElement;
    if (html.getAttribute('data-theme') === 'dark') {
      html.setAttribute('data-theme', 'light');
      btnTheme.textContent = '☀️ Theme';
    } else {
      html.setAttribute('data-theme', 'dark');
      btnTheme.textContent = '🌙 Theme';
    }
  });

  btnFullscreen.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.log(err));
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (gridModal.classList.contains('active')) {
      if (e.key === 'Escape') {
        gridModal.classList.remove('active');
      }
      return;
    }

    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      nextSlide();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      prevSlide();
    } else if (e.key.toLowerCase() === 'g') {
      gridModal.classList.add('active');
    } else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      } else {
        document.exitFullscreen();
      }
    }
  });

  // Initialize first slide
  updateSlide(1);
});
