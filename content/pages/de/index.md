title: OpenSesame
hash: 0da5cd23c8c071ca84bb0818de0aafb330af2b50da3d8c681bde73bb60136602
locale: de
language: German

OpenSesame ist ein Programm zur Erstellung von Experimenten für Psychologie, Neurowissenschaften und experimentelle Ökonomie. Die neueste $status$ Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


<div class="btn-group" role="group" aria-label="...">
  <a role="button" class="btn btn-success" id="btn-download" onclick="showQuickOptions('download')">
    <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
    Herunterladen
    </a>
  <a role="button" class="btn btn-success" id="btn-tutorial" onclick="showQuickOptions('tutorial')">
  <span class="glyphicon glyphicon-education" aria-hidden="true"></span>
    Tutorial
  </a>
  <a role="button" class="btn btn-success" id="btn-support" onclick="showQuickOptions('support')">
  <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
    Support erhalten
  </a>
</div>


<div class="quick-options" id="quick-options-download" style="display: none;">
  <p>
  Los geht's!
  </p>  
  <p class="quick-options-download-windows" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-windows-exe-py3$">
    Standard-Windows-Installer (.exe)
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Mac OS-Paket (.dmg)
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  Es gibt verschiedene Möglichkeiten, OpenSesame unter Linux/ Ubuntu zu installieren. Bitte sehen Sie sich unten die Download- und Installationsoptionen an.
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:download%">
    Weitere Download- und Installationsoptionen
    </a>
  </p>
</div>

<div class="quick-options" id="quick-options-tutorial" style="display: none;">
  <p>
  Großartig! Was möchten Sie lernen?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner%">
    Wie man ein einfaches Experiment erstellt (Anfänger)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    <b>Neu!</b> 🌟 Wie man effektiv mit SigmundAI arbeitet (Anfänger)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    Wie man Python-Skript in meinem Experiment verwendet (Fortgeschrittene)</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-sigmund%">
    <b>Neu!</b> 🌟 Wie man SigmundAI zum Schreiben von Python-Skript verwendet (Fortgeschrittene)
    </a>
  </p>  
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    Wie man JavaScript in meinem Online-Experiment verwendet (Fortgeschrittene)</a>
  </p>
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    Wir sind hier, um zu helfen! Welche Art von Unterstützung suchen Sie?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    Community-Support-Forum (kostenlos)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI (monatliches Abonnement)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://professional.cogsci.nl">
    Professioneller Support (kostenpflichtig)
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
  return 'linux'; // standardmäßig linux, falls unbekannt
}

function showQuickOptions(option) {
  // Alle Schnelloptionen ausblenden
  const allOptions = document.querySelectorAll('.quick-options');
  allOptions.forEach(opt => opt.style.display = 'none');
  
  // Alle Buttons auf btn-success zurücksetzen
  const allButtons = document.querySelectorAll('.btn-group .btn');
  allButtons.forEach(btn => {
    btn.classList.remove('btn-primary');
    btn.classList.add('btn-success');
  });
  
  // Ausgewählte Option anzeigen
  const selectedOption = document.getElementById('quick-options-' + option);
  if (selectedOption.style.display === 'none') {
    selectedOption.style.display = 'block';
    
    // Button-Stil aktualisieren
    const selectedButton = document.getElementById('btn-' + option);
    selectedButton.classList.remove('btn-success');
    selectedButton.classList.add('btn-primary');
    
    // Wenn Download-Option, dann betriebssystemspezifischen Inhalt anzeigen
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


## Funktionen

- __Eine benutzerfreundliche Oberfläche__ — eine moderne, professionelle und einfach zu bedienende grafische [Oberfläche](%link:manual/interface%)
- __Online-Experimente__ — führe dein Experiment im Browser mit [OSWeb](%link:manual/osweb/workflow%) aus
- __Python__ — bringe die Leistung von [Python](%link:manual/python/about%) in dein Experiment ein
- __JavaScript__ — bringe die Leistung von [JavaScript](%link:manual/python/about%) in dein Experiment ein
- __Nutze deine Geräte__ — verwenden Sie Ihren [Eyetracker](%link:pygaze%), [Buttonbox](%link:buttonbox%), [EEG-Ausrüstung](%link:parallel%) und mehr.
- __SigmundAI__ — entwickle und debugge Experimente zusammen mit [einem KI-Experten](%link:beginner-sigmund%)
- __Kostenlos__ — veröffentlicht unter der GPL3
- __Plattformübergreifend__ — Windows, Mac OS und Linux

## Zitationen

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Ein quelloffener, grafischer Experiment-Builder für die Sozialwissenschaften. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Sprachwissenschaftliche Experimente online durchführen mit OpenSesame und OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Verwandter Preprint (nicht identisch mit dem veröffentlichten Manuskript)](https://doi.org/10.31234/osf.io/wnryc)</small>