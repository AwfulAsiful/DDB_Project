// Get elements
const openSidebarButton = document.getElementById("openSidebar");
const closeSidebarButton = document.getElementById("closeSidebar");
const sidebar = document.getElementById("sideNav");
const overlay = document.getElementById("overlay");

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
