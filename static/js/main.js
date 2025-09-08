// static/main.js

// Flash message auto-hide after 4 seconds
document.addEventListener("DOMContentLoaded", () => {
    const flashes = document.querySelectorAll(".flash");
    if (flashes.length > 0) {
        setTimeout(() => {
            flashes.forEach(flash => {
                flash.style.opacity = "0";
                setTimeout(() => flash.remove(), 500);
            });
        }, 4000);
    }
});

// File upload preview (dashboard)
const uploadInput = document.getElementById("file-upload");
if (uploadInput) {
    uploadInput.addEventListener("change", () => {
        const fileName = uploadInput.files.length > 0 ? uploadInput.files[0].name : "No file selected";
        const label = document.querySelector(".file-label");
        if (label) {
            label.textContent = `Selected: ${fileName}`;
        }
    });
}

// Button hover animation
const buttons = document.querySelectorAll("button, .btn-login, .btn-register");
buttons.forEach(btn => {
    btn.addEventListener("mouseover", () => {
        btn.classList.add("glow");
    });
    btn.addEventListener("mouseleave", () => {
        btn.classList.remove("glow");
    });
});
