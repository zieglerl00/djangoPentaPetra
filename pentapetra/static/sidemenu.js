const sidemenu = document.getElementById("sidemenu");

const sidemenuToggler = document.getElementById("sidemenu-toggler");
sidemenuToggler?.addEventListener("click", () => {
    toggleSidemenu();
});

function toggleSidemenu() {
    if (sidemenu?.getAttribute("aria-expanded") === "true") {
        sidemenuToggler.innerHTML = "open";
        sidemenu?.setAttribute("aria-expanded", "false")
    } else {
        sidemenuToggler.innerHTML = "close";
        sidemenu?.setAttribute("aria-expanded", "true")
    }
}

