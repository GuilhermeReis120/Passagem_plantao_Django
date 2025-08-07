// Responsividade e melhorias para mobile

document.addEventListener('DOMContentLoaded', function() {
    // Ajusta o grid para 1 coluna em telas pequenas
    function ajustarGrid() {
        const grid = document.querySelector('.main-form-grid');
        if (!grid) return;
        if (window.innerWidth <= 600) {
            grid.style.gridTemplateColumns = '1fr';
        } else if (window.innerWidth <= 900) {
            grid.style.gridTemplateColumns = '1fr 1fr';
        } else {
            grid.style.gridTemplateColumns = 'repeat(3, 1fr)';
        }
    }
    ajustarGrid();
    window.addEventListener('resize', ajustarGrid);

    // Ajusta padding do container para mobile
    function ajustarPadding() {
        const container = document.querySelector('.container-plantao');
        if (!container) return;
        if (window.innerWidth <= 600) {
            container.style.padding = '10px';
        } else {
            container.style.padding = '40px';
        }
    }
    ajustarPadding();
    window.addEventListener('resize', ajustarPadding);
});
