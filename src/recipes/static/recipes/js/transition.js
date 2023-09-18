function applyFadeInTransition() {
    document.body.style.opacity = "1";
}

function applyFadeOutTransition(event) {
    event.preventDefault();
    document.body.style.opacity = "0";
    
    setTimeout(() => {
        if (event.target && event.target.tagName === "A") {
            window.location.href = event.target.href;
        } else {
            window.location.reload();
        }
    }, 1000);  
}

document.addEventListener('DOMContentLoaded', applyFadeInTransition);
document.addEventListener('click', function(event) {
    if (event.target.tagName === "A") {
        applyFadeOutTransition(event);
    }
});
