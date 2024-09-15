document.addEventListener("DOMContentLoaded", function () {

    const particleContainer = document.getElementById('particles');
    const totalParticles = 15 / 2;
    const animations = ['float', 'floatReverse', 'float2', 'floatReverse2'];

    for (let i = 0; i < totalParticles; i++) {
        const particle = document.createElement('span');
        particle.classList.add('particle');

        // Randomize particle properties
        const width = Math.floor(Math.random() * 15) + 150; // Increase size for better overlap
        const speed = Math.floor(Math.random() * 30) + 30;
        const delay = Math.random() * 10 * 0.1;
        const opacity = 1; // Set opacity to 1 to ensure they blend together
        const anim = animations[Math.floor(Math.random() * animations.length)];

        particle.style.width = width + 'px';
        particle.style.height = width + 'px';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.opacity = opacity;
        particle.style.animation = `${anim} ${speed}s infinite forwards`;
        particle.style.animationDelay = `${delay}s`;

        particleContainer.appendChild(particle);
    }





    let installPrompt = null;
    const installButton = document.querySelector("#install");

    window.addEventListener("beforeinstallprompt", (event) => {
        event.preventDefault();
        installPrompt = event;
        installButton.classList.remove("disabled");
    });

    installButton.addEventListener("click", async () => {
        if (!installPrompt) {
            return;
        }
        const result = await installPrompt.prompt();
        console.log(`Install prompt was: ${result.outcome}`);
    });


    window.addEventListener("appinstalled", () => {
        disableInAppInstallPrompt();
    });

    function disableInAppInstallPrompt() {
        installPrompt = null;
        installButton.setAttribute("hidden", "");
    }



});