function randomizeEmails() {
    const emailItems = document.querySelectorAll('.email-item');
    emailItems.forEach(emailItem => {
        const randomNum = Math.random();
        if (randomNum < 0.2) {
            emailItem.classList.add('malicious-email');
            emailItem.querySelector('.email-icon').innerHTML = '!';
        } else if (randomNum > 0.8) {
            emailItem.classList.add('validated-email');
            emailItem.querySelector('.email-icon').innerHTML = '&#10004;';
        }
    });
}

randomizeEmails();
