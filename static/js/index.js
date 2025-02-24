document.addEventListener('DOMContentLoaded', function() {
    const cells = document.querySelectorAll('td');
    cells.forEach(cell => {
        cell.addEventListener('click', function() {
            // Remove 'clicked' class from all cells
            cells.forEach(c => c.classList.remove('clicked'));
            // Add 'clicked' class to the clicked cell
            this.classList.add('clicked');
        });
    });
});