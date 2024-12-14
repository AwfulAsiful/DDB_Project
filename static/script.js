// Get elements
const openSidebarButton = document.getElementById("openSidebar");
const closeSidebarButton = document.getElementById("closeSidebar");
const sidebar = document.getElementById("sideNav");
const overlay = document.getElementById("overlay");
let currentIndex = 0;
const cards = document.querySelector('.carousel');
const totalCards = 12; // Adjust based on the number of cards you have

// Select navigation buttons
const prevButton = document.querySelector('.fa-chevron-left');
const nextButton = document.querySelector('.fa-chevron-right');

// Update the transform property to show the correct card
// Open sidebar
openSidebarButton.addEventListener("click", () => {
  sidebar.classList.remove("-translate-x-full");
  overlay.classList.remove("hidden");
});

// Close sidebar
const closeSidebar = () => {
  sidebar.classList.add("-translate-x-full");
  overlay.classList.add("hidden");
};

closeSidebarButton.addEventListener("click", closeSidebar);
overlay.addEventListener("click", closeSidebar);

// Close sidebar on Escape key press
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeSidebar();
  }
});

