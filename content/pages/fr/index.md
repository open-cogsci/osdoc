title: OpenSesame
hash: 0da5cd23c8c071ca84bb0818de0aafb330af2b50da3d8c681bde73bb60136602
locale: fr
language: French

OpenSesame est un programme permettant de créer des expériences pour la psychologie, les neurosciences et l’économie expérimentale. La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


<div class="btn-group" role="group" aria-label="...">
  <a role="button" class="btn btn-success" id="btn-download" onclick="showQuickOptions('download')">
    <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
    Télécharger
    </a>
  <a role="button" class="btn btn-success" id="btn-tutorial" onclick="showQuickOptions('tutorial')">
  <span class="glyphicon glyphicon-education" aria-hidden="true"></span>
    Tutoriel
  </a>
  <a role="button" class="btn btn-success" id="btn-support" onclick="showQuickOptions('support')">
  <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
    Obtenir de l’aide
  </a>
</div>


<div class="quick-options" id="quick-options-download" style="display: none;">
  <p>
  Commençons !
  </p>  
  <p class="quick-options-download-windows" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-windows-exe-py3$">
    Installateur Windows standard (.exe)
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Package Mac OS (.dmg)
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  Il existe plusieurs façons d’installer OpenSesame sur Linux/ Ubuntu. Veuillez consulter les options de téléchargement et d’installation ci-dessous.
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:download%">
    Plus d’options de téléchargement et d’installation
    </a>
  </p>
</div>

<div class="quick-options" id="quick-options-tutorial" style="display: none;">
  <p>
  Super ! Que voulez-vous apprendre ?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner%">
    Comment créer une expérience simple (débutant)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    <b>Nouveau !</b> 🌟 Comment travailler efficacement avec SigmundAI (débutant)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    Comment utiliser un script Python dans mon expérience (intermédiaire)</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-sigmund%">
    <b>Nouveau !</b> 🌟 Comment utiliser SigmundAI pour écrire un script Python (intermédiaire)
    </a>
  </p>  
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    Comment utiliser JavaScript dans mon expérience en ligne (intermédiaire)</a>
  </p>
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    Nous sommes là pour vous aider ! Quel type d’assistance recherchez-vous ?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    Forum d’assistance communautaire (gratuit)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI (abonnement mensuel)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://professional.cogsci.nl">
    Assistance professionnelle (payante)
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
  return 'linux'; // par défaut, linux si inconnu
}

function showQuickOptions(option) {
  // Masquer toutes les options rapides
  const allOptions = document.querySelectorAll('.quick-options');
  allOptions.forEach(opt => opt.style.display = 'none');
  
  // Réinitialiser tous les boutons à btn-success
  const allButtons = document.querySelectorAll('.btn-group .btn');
  allButtons.forEach(btn => {
    btn.classList.remove('btn-primary');
    btn.classList.add('btn-success');
  });
  
  // Afficher l'option sélectionnée
  const selectedOption = document.getElementById('quick-options-' + option);
  if (selectedOption.style.display === 'none') {
    selectedOption.style.display = 'block';
    
    // Mettre à jour le style du bouton
    const selectedButton = document.getElementById('btn-' + option);
    selectedButton.classList.remove('btn-success');
    selectedButton.classList.add('btn-primary');
    
    // Si option de téléchargement, afficher le contenu spécifique à l'OS
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


## Fonctionnalités

- __Une interface conviviale__ — une [interface](%link:manual/interface%) graphique moderne, professionnelle et facile à utiliser
- __Expériences en ligne__ — exécutez votre expérience dans un navigateur avec [OSWeb](%link:manual/osweb/workflow%)
- __Python__ — ajoutez la puissance de [Python](%link:manual/python/about%) à votre expérience
- __JavaScript__ — ajoutez la puissance de [JavaScript](%link:manual/python/about%) à votre expérience
- __Utilisez vos appareils__ — utilisez votre [eye tracker](%link:pygaze%), [boîte de boutons](%link:buttonbox%), [équipement EEG](%link:parallel%), et plus encore.
- __SigmundAI__ — créez et déboguez des expériences avec [un expert IA](%link:beginner-sigmund%)
- __Gratuit__ — distribué sous licence GPL3
- __Multiplateforme__ — Windows, Mac OS et Linux

## Citations

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame : un créateur d’expériences graphique open source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Réaliser des expériences linguistiques en ligne avec OpenSesame et OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Préimpression associée (différente du manuscrit publié)](https://doi.org/10.31234/osf.io/wnryc)</small>