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


  function modalEditEvent(id) {
    $('#cuentas-contenido').load('editar_evento/' + id);
    $('.cuentas-modal').modal('show');
  }


  function inicioSesion(){
    document.getElementById('login-btn').click()
  }
  function registroM(){
    document.getElementById('registro-btn').click()
  }

  document.getElementById('formPost').addEventListener('submit', function (event) {
    event.preventDefault();
    if (usuarioAutenticado) {
        this.submit();
    } else {
        inicioSesion();
    }
});
function busqueda_top(){
  if (document.getElementById('input_busqueda_top').value != ''){
    var busqueda = document.getElementById('input_busqueda_top').value
    let url = '/search/top/' + busqueda;
    window.location.href = url;
  }
}
document.getElementById('input_busqueda_top').addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
      busqueda_top();
  }
});
document.getElementById('search_icon').addEventListener('click',busqueda_top())