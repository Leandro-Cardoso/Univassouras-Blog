function toggleMenu(id) {

    const menu = document.getElementById(id);
    
    menu.classList.toggle('hide');

}

document.addEventListener('DOMContentLoaded', () => {
    const commentToggleButtons = document.querySelectorAll('.toggle-comments');
    commentToggleButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = button.getAttribute('data-target');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.classList.toggle('hide');
                if (targetElement.classList.contains('hide')) {
                    button.textContent = 'Comentários';
                } else {
                    button.textContent = 'Ocultar Comentários';
                }
            }
        });
    });
});
