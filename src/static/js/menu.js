// Find all the necessary elements
const menuToggle = document.querySelector(".menu-toggle");
const mobileMenu = document.querySelector(".mobile-menu");
const container = document.querySelector(".container");
const footer = document.querySelector("footer");

// Function to toggle the visibility of the mobile menu
menuToggle.addEventListener("click", () => {
    // Toggle the visibility of the mobile menu
    mobileMenu.classList.toggle("show");

    // Toggle shifting of the content and footer
    if (mobileMenu.classList.contains("show")) {
        container.classList.add("shifted");
        footer.classList.add("shifted");
    } else {
        container.classList.remove("shifted");
        footer.classList.remove("shifted");
    }
});

// Add an event listener for window resizing
window.addEventListener("resize", () => {
    // If the window is wider than 768px, automatically hide the mobile menu and remove the shifting
    if (window.innerWidth > 768) {
        if (mobileMenu.classList.contains("show")) {
            mobileMenu.classList.remove("show");
        }
        if (container.classList.contains("shifted")) {
            container.classList.remove("shifted");
            footer.classList.remove("shifted");
        }
    }
});
