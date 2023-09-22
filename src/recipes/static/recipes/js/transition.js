document.addEventListener('DOMContentLoaded', applyFadeInTransition);

document.addEventListener('click', function(event) {
    if (event.target.tagName === "A") {
        applyFadeOutTransition(event, () => {
            window.location.href = event.target.href;
        });
    }
});

document.addEventListener('submit', function(event) {
    if (event.target.tagName === "FORM") {
        applyFadeOutTransition(event, () => {
            event.target.submit();
        });
    }
});

function applyFadeInTransition() {
    document.body.style.opacity = "1";
}

function applyFadeOutTransition(event, callback) {
    event.preventDefault();
    document.body.style.opacity = "0";
    
    setTimeout(() => {
        callback();
    }, 1000);
}

