title: 开放芝麻
hash: 0da5cd23c8c071ca84bb0818de0aafb330af2b50da3d8c681bde73bb60136602
locale: zh
language: Chinese

OpenSesame 是一个用于创建心理学、神经科学和实验经济学实验的程序。最新的 $status$ 版本是 $version$ *$codename$*（[发行说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$)）。


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
    标准 Windows 安装程序（.exe）
    </a>
  </p>  
  <p class="quick-options-download-macos" style="display: none;">
    <a role="button" class="btn btn-primary" href="$url-osx-dmg-x64-py3$">
    Mac OS 安装包（.dmg）
    </a>
  </p>
  <p class="quick-options-download-linux" style="display: none;">
  在 Linux/ Ubuntu 上安装 OpenSesame 有多种方式。请参阅下面的下载和安装选项。
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
    如何构建一个基础实验（初学者）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/beginner-sigmund%">
    <b>New!</b> 🌟 如何高效地使用 SigmundAI（初学者）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate%">
    如何在我的实验中使用 Python script（中级）</a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-sigmund%">
    <b>New!</b> 🌟 如何使用 SigmundAI 编写 Python script（中级）
    </a>
  </p>  
  <p>
    <a role="button" class="btn btn-primary" href="%url:tutorials/intermediate-javascript%">
    如何在我的在线实验中使用 JavaScript（中级）</a>
  </p>
</div>

<div class="quick-options" id="quick-options-support" style="display: none;">
  <p>
    我们随时为您提供帮助！您在寻找哪种支持？
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://forum.cogsci.nl">
    社区支持论坛（免费）
    </a>
  </p>
  <p>
    <a role="button" class="btn btn-primary" href="https://sigmundai.eu">
    SigmundAI（按月订阅）
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
  return 'linux'; // 如果未知，则默认使用 linux
}

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