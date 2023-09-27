document.addEventListener('DOMContentLoaded', function() {
    applyFadeInTransition();

    
    var showAllBtn = document.getElementById('showAllBtn');
    if (showAllBtn) {
        showAllBtn.addEventListener('click', function(event) {
            // Prevent the default action
            event.preventDefault();

            // Construct the URL with only the required parameters
            var graphDataType = document.querySelector('select[name="graph_data_type"]').value;
            var newUrl = '?show_all=true&graph_data_type=' + graphDataType;

            // Apply the transition 
            applyFadeOutTransition(event, () => {
                window.location.href = newUrl;
            });
        });
    }
});

document.addEventListener('click', function(event) {
    if (event.target.tagName === "A" && event.target.id !== 'showAllBtn') { 
        // Check to avoid applying the transition twice for the "Show All" button
        applyFadeOutTransition(event, () => {
            window.location.href = event.target.href;
        });
    }
});

document.addEventListener('submit', function(event) {
    if (event.target.tagName === "FORM") {
        if (event.target.matches('.search-form')) {
            if (event.submitter.name !== 'show_all') {
                // If it's not the "Show All" button, apply the transition
                applyFadeOutTransition(event, () => {
                    event.target.submit();
                });
            }
            return;
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
