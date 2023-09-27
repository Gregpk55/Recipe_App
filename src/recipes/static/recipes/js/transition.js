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
        
        if (event.target.matches('.search-form')) {
            
            return;
        }
        
        if (event.submitter.name === 'show_all') {
            console.log('Show All clicked, Form Data: ', event.target.elements);
        } else {
            console.log('Another submit button clicked');
            applyFadeOutTransition(event, () => {
                event.target.submit();
            });
        }
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

