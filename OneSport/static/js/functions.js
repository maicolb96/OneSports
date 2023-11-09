var icon_img = document.getElementById('boton-disparador');
var inputOculto = document.getElementById('inputOculto');
var imgToPush = document.getElementById('img_to_pus');
var div_img_to_push = document.getElementById('div_img_to_push');

icon_img.addEventListener('click',function(){
    inputOculto.click();
});  

inputOculto.addEventListener('change', function () {
    const file = inputOculto.files[0];
    if (file) {
        
        const reader = new FileReader();
        reader.onload = function (e) {
            imgToPush.src = e.target.result;
        };
        reader.readAsDataURL(file);
        div_img_to_push.style.display = 'block';
    }
});