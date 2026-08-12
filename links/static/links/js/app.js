/**
 * Shortify — Application JavaScript
 */


/* =========================================
   Copy Short URL — Home Page
========================================= */

function copyShortURL() {
    const urlElement = document.getElementById("short-url");

    if (!urlElement) {
        return;
    }

    navigator.clipboard
        .writeText(urlElement.href)
        .then(() => {
            const button = document.querySelector(".copy-button");

            if (!button) {
                return;
            }

            const originalHTML = button.innerHTML;

            button.innerHTML =
                '<i class="bi bi-check-lg"></i> Copied';

            setTimeout(() => {
                button.innerHTML = originalHTML;
            }, 2000);
        })
        .catch(() => {
            console.error("Unable to copy URL.");
        });
}


/* =========================================
   Copy URL — Detail Page
========================================= */

function copyText(button) {
    const text = button.dataset.url;

    if (!text) {
        return;
    }

    navigator.clipboard
        .writeText(text)
        .then(() => {
            const originalHTML = button.innerHTML;

            button.innerHTML =
                '<i class="bi bi-check-lg"></i> Copied';

            setTimeout(() => {
                button.innerHTML = originalHTML;
            }, 2000);
        })
        .catch(() => {
            console.error("Unable to copy URL.");
        });
}