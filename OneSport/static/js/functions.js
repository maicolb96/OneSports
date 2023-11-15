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

$('.ui.dropdown').dropdown();

$(document).ready(function() {
  $('#new_event_btn').click(function() {
      $('#cuentas-contenido').load('new_event/');
      $('.cuentas-modal').modal('show');
  });
});
$(document).ready(function() {
  $('#login-btn').click(function() {
      $('#cuentas-contenido').load('login/');
      $('.cuentas-modal').modal('show');
  });
});
$(document).ready(function() {
    $('#registro-btn').click(function() {
        $('#cuentas-contenido').load('registro/');
        $('.cuentas-modal').modal('show');
    });
  });

  function inicioSesion(){
    document.getElementById('login-btn').click()
  }
  function registroM(){
    document.getElementById('registro-btn').click()
  }

  document.getElementById('formPost').addEventListener('submit', function (event) {
    event.preventDefault();
    if (usuarioAutenticado) {
        console.log('tuki tuki ñeñe')
        this.submit();
    } else {
        inicioSesion();
    }
});