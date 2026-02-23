title: 开放芝麻
hash: c1aa13ed52abdabe508b561e062e8092d5335f7f46f7867e757c20994d706313
locale: zh
language: Chinese

OpenSesame 是一个用于心理学、神经科学和实验经济学实验设计的程序。最新 $status$ 版本为 $version$ *$codename$* ([发行说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


<div class="btn-group" role="group" aria-label="...">
  <a role="button" class="btn btn-success" id="btn-download" onclick="showQuickOptions('download')">
    <span class="glyphicon glyphicon-download" aria-hidden="true"></span>
    下载
    </a>
  <a role="button" class="btn btn-success" id="btn-tutorial" onclick="showQuickOptions('tutorial')">
  <span class="glyphicon glyphicon-education" aria-hidden="true"></span>
    教程
  </a>
  <a role="button" class="btn btn-success" id="btn-support" onclick="showQuickOptions('support')">
  <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
    获取支持
  </a>
</div>


<div class="quick-options" id="quick-options-download" style="display: none;">
  <p>
  让我们开始吧！
  </p>  
  <p class="quick-options-download-windows" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-windows-exe-py3$">
    标准 Windows 安装程序 (.exe)
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Mac OS 安装包 (.dmg)
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  在 Linux/ Ubuntu 上安装 OpenSesame 有多种方式。请参阅下方的下载和安装选项。
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:download%">
    更多下载和安装选项
    </a>
  </p>
</div>

<div class="quick-options" id="quick-options-tutorial" style="display: none;">
  <p>
  太好了！你想学习什么？
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner%">
    如何建立基础实验（初学者）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    <b>新！</b> 🌟 如何高效使用 SigmundAI（初学者）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    如何在实验中使用 Python 脚本（中级）</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    如何在在线实验中使用 JavaScript（中级）</a>
  </p>
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    我们随时为您提供帮助！您需要哪种支持？
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    社区支持论坛（免费）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI（月度订阅）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://professional.cogsci.nl">
    专业支持（付费）
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

## 功能特点

- __用户友好的界面__ — 现代、专业且易于使用的图形[界面](%link:manual/interface%)
- __在线实验__ — 使用 [OSWeb](%link:manual/osweb/workflow%) 在浏览器中运行实验
- __Python__ — 为实验添加 [Python](%link:manual/python/about%) 的强大功能
- __JavaScript__ — 为实验添加 [JavaScript](%link:manual/python/about%) 的强大功能
- __使用您的设备__ — 使用您的[眼动仪](%link:pygaze%)、[按键盒](%link:buttonbox%)、[脑电设备](%link:parallel%)等
- __SigmundAI__ — 与[AI专家](%link:beginner-sigmund%)一起协作构建和调试实验
- __免费__ — 基于 GPL3 协议发布
- __跨平台__ — 适用于 Windows、Mac OS 和 Linux

## 参考文献

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[相关预印本（与正式发表手稿不完全一致）](https://doi.org/10.31234/osf.io/wnryc)</small>