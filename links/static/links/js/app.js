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