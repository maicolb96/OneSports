var posicionado_sobre_imagen = document.getElementById('posicionado_sobre_imagen');
var inputOculto_event = document.getElementById('inputOculto_event');
var imgToPus_event = document.getElementById('imgToPus_event');

posicionado_sobre_imagen.addEventListener('click', function () {
    inputOculto_event.click();
});

inputOculto_event.addEventListener('change', function () {
    const file = inputOculto_event.files[0];
    if (file) {
        
        const reader = new FileReader();
        reader.onload = function (e) {
            imgToPus_event.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});