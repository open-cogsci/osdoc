title: OpenSesame
hash: 9ab882d14433c23e7f81044baa2279aa743cdd9b414f30c82091495ab6226904
locale: es
language: Spanish

OpenSesame es un programa para crear experimentos de psicología, neurociencia y economía experimental. La versión más reciente $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


<div class="btn-group" role="group" aria-label="...">
  <a role="button" class="btn btn-success" id="btn-download" onclick="showQuickOptions('download')">
    <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
    Descargar
    </a>
  <a role="button" class="btn btn-success" id="btn-tutorial" onclick="showQuickOptions('tutorial')">
  <span class="glyphicon glyphicon-education" aria-hidden="true"></span>
    Tutorial
  </a>
  <a role="button" class="btn btn-success" id="btn-support" onclick="showQuickOptions('support')">
  <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
    Obtener ayuda
  </a>
</div>


<div class="quick-options" id="quick-options-download" style="display: none;">
  <p>
  ¡Empecemos!
  </p>  
  <p class="quick-options-download-windows" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-windows-exe-py3$">
    Instalador estándar de Windows (.exe)
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Paquete para Mac OS (.dmg)
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  Hay varias formas de instalar OpenSesame en Linux/ Ubuntu. Consulta las opciones de descarga e instalación a continuación.
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:download%">
    Más opciones de descarga e instalación
    </a>
  </p>
</div>

<div class="quick-options" id="quick-options-tutorial" style="display: none;">
  <p>
  ¡Genial! ¿Qué quieres aprender?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner%">
    Cómo crear un experimento básico (principiante)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    Cómo trabajar eficazmente con SigmundAI (principiante)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    Cómo usar un script de Python en mi experimento (intermedio)</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-sigmund%">
    Cómo usar SigmundAI para escribir un script de Python (intermedio)
    </a>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    Cómo usar JavaScript en mi experimento en línea (intermedio)</a>
  </p>
  </p> 
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/sigmund-guided-generation%">
    <b>¡Nuevo!</b> 🌟 ¡Aprende a crear cualquier experimento usando generación guiada con SigmundAI!
    </a>
  </p> 
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    ¡Estamos aquí para ayudar! ¿Qué tipo de ayuda estás buscando?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    Foro de ayuda de la comunidad (gratis)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI (suscripción mensual)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://professional.cogsci.nl">
    Ayuda profesional (de pago)
    </a>
  </p>
</div>

<script>
function detectOS() {
  const userAgent = navigator.userAgent.toLowerCase();
  const platform = navigator.platform.toLowerCase();
  
  if (platform.indexOf('win') !== -1 || userAgent.indexOf('windows') !== -1) {
    return 'windows';
  } else if (platform.indexOf('mac') !== -1 || userAgent.indexOf('mac') !== -1) {
    return 'macos';
  } else if (platform.indexOf('linux') !== -1 || userAgent.indexOf('linux') !== -1 || userAgent.indexOf('x11') !== -1) {
    return 'linux';
  }
  return 'linux'; // default to linux if unknown
}

function showQuickOptions(option) {
  // Ocultar todas las opciones rápidas
  const allOptions = document.querySelectorAll('.quick-options');
  allOptions.forEach(opt => opt.style.display = 'none');
  
  // Restablecer todos los botones a btn-success
  const allButtons = document.querySelectorAll('.btn-group .btn');
  allButtons.forEach(btn => {
    btn.classList.remove('btn-primary');
    btn.classList.add('btn-success');
  });
  
  // Mostrar la opción seleccionada
  const selectedOption = document.getElementById('quick-options-' + option);
  if (selectedOption.style.display === 'none') {
    selectedOption.style.display = 'block';
    
    // Actualizar el estilo del botón
    const selectedButton = document.getElementById('btn-' + option);
    selectedButton.classList.remove('btn-success');
    selectedButton.classList.add('btn-primary');
    
    // Si es la opción de descarga, mostrar contenido específico del SO
    if (option === 'download') {
      const os = detectOS();
      const windowsOption = document.querySelector('.quick-options-download-windows');
      const macosOption = document.querySelector('.quick-options-download-macos');
      const linuxOption = document.querySelector('.quick-options-download-linux');
      
      windowsOption.style.display = 'none';
      macosOption.style.display = 'none';
      linuxOption.style.display = 'none';
      
      if (os === 'windows') {
        windowsOption.style.display = 'block';
      } else if (os === 'macos') {
        macosOption.style.display = 'block';
      } else {
        linuxOption.style.display = 'block';
      }
    }
  }
}
</script>


## Características

- __Una interfaz fácil de usar__ — una interfaz gráfica [moderna, profesional y fácil de usar](%link:manual/interface%)
- __Experimentos en línea__ — ejecuta tu experimento en un navegador con [OSWeb](%link:manual/osweb/workflow%)
- __Python__ — añade el poder de [Python](%link:manual/python/about%) a tu experimento
- __JavaScript__ — añade el poder de [JavaScript](%link:manual/python/about%) a tu experimento
- __Utiliza tus dispositivos__ — utiliza tu [eye tracker](%link:pygaze%), [caja de botones](%link:buttonbox%), [equipo EEG](%link:parallel%) y más.
- __SigmundAI__ — crea y depura experimentos junto con [un experto en IA](%link:beginner-sigmund%)
- __Gratis__ — liberado bajo la licencia GPL3
- __Multiplataforma__ — Windows, Mac OS y Linux

## Citas

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un constructor de experimentos gráficos de código abierto para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Realización de experimentos lingüísticos en línea con OpenSesame y OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Prepublicación relacionada (no idéntica al manuscrito publicado)](https://doi.org/10.31234/osf.io/wnryc)</small>