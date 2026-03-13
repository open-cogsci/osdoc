title: OpenSesame


OpenSesame is a program to create experiments for psychology, neuroscience, and experimental economics. The latest $status$ version is $version$ *$codename$* ([release notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


<div class="btn-group" role="group" aria-label="...">
  <a role="button" class="btn btn-success" id="btn-download" onclick="showQuickOptions('download')">
    <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
    Download
    </a>
  <a role="button" class="btn btn-success" id="btn-tutorial" onclick="showQuickOptions('tutorial')">
  <span class="glyphicon glyphicon-education" aria-hidden="true"></span>
    Tutorial
  </a>
  <a role="button" class="btn btn-success" id="btn-support" onclick="showQuickOptions('support')">
  <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
    Get support
  </a>
</div>


<div class="quick-options" id="quick-options-download" style="display: none;">
  <p>
  Let's get started!
  </p>  
  <p class="quick-options-download-windows" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-windows-exe-py3$">
    Standard Windows installer (.exe)
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Mac OS package (.dmg)
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  There are various ways to install OpenSesame on Linux/ Ubuntu. Please see the download and installation options below.
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:download%">
    More download and installation options
    </a>
  </p>
</div>

<div class="quick-options" id="quick-options-tutorial" style="display: none;">
  <p>
  Great! What do you want to learn?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner%">
    How to build a basic experiment (beginner)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    <b>New!</b> 🌟 How to work effectively with SigmundAI (beginner)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    How to use Python script in my experiment (intermediate)</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-sigmund%">
    <b>New!</b> 🌟 How to use SigmundAI to write Python script (intermediate)
    </a>
  </p>  
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    How to use JavaScript in my online experiment (intermediate)</a>
  </p>
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    We're here to help! What kind of support are you looking for?
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    Community support forum (free)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI (monthly subscription)
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://professional.cogsci.nl">
    Professional support (paid)
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
  // Hide all quick options
  const allOptions = document.querySelectorAll('.quick-options');
  allOptions.forEach(opt => opt.style.display = 'none');
  
  // Reset all buttons to btn-success
  const allButtons = document.querySelectorAll('.btn-group .btn');
  allButtons.forEach(btn => {
    btn.classList.remove('btn-primary');
    btn.classList.add('btn-success');
  });
  
  // Show selected option
  const selectedOption = document.getElementById('quick-options-' + option);
  if (selectedOption.style.display === 'none') {
    selectedOption.style.display = 'block';
    
    // Update button style
    const selectedButton = document.getElementById('btn-' + option);
    selectedButton.classList.remove('btn-success');
    selectedButton.classList.add('btn-primary');
    
    // If download option, show OS-specific content
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


## Features

- __A user-friendly interface__ — a modern, professional, and easy-to-use graphical [interface](%link:manual/interface%)
- __Online experiments__ — run your experiment in a browser with [OSWeb](%link:manual/osweb/workflow%)
- __Python__ — add the power of [Python](%link:manual/python/about%) to your experiment
- __JavaScript__ — add the power of [JavaScript](%link:manual/python/about%) to your experiment
- __Use your devices__ — use your [eye tracker](%link:pygaze%), [button box](%link:buttonbox%), [EEG equipment](%link:parallel%), and more.
- __SigmundAI__ — build and debug experiments together with [an AI expert](%link:beginner-sigmund%)
- __Free__ — released under the GPL3
- __Crossplatform__ — Windows, Mac OS, and Linux

## Citations

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Related preprint (not identical to published manuscript)](https://doi.org/10.31234/osf.io/wnryc)</small>