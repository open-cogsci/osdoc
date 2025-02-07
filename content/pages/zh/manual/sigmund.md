title: SigmundAI助理
hash: 068066429b87ece4165a56d9298972b751462edb129261bcda7b23fb49f2dcf5
locale: zh
language: Chinese

SigmundAI Copilot目前处于公开测试阶段
{:.page-notification}

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%

[SigmundAI.eu](https://sigmundai.eu) 是一个专为帮助您使用OpenSesame而设计的AI研究助手。您可以通过安装扩展程序直接从OpenSesame中使用Sigmund。

[TOC]

## 入门

### 登录Sigmund

使用Sigmund需要每月订阅，可以随时取消。请访问<https://sigmundai.eu>进行订阅。

&#128150; 您的订阅支持开源软件的发展！

一旦您登录Sigmund，聊天界面就会变得可见。聊天界面会自动侦听来自OpenSesame的传入连接。

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%

### 在OpenSesame中安装Sigmund扩展

要在OpenSesame中连接到Sigmund，您需要安装`opensesame-extension-sigmund`包。您可以通过在OpenSesame控制台中输入以下命令来完成此操作：

```
pip install opensesame-extension-sigmund
```

在Windows上，您需要以管理员身份运行上述命令，或传递`--user`标志：

```
pip install opensesame-extension-sigmund --user
```

安装扩展后，重启OpenSesame。Sigmund图标现在应该出现在主工具栏中。通过点击Sigmund图标激活SigmundAI Copilot。

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame is connecting to Sigmund.
--%

几秒钟后，应建立连接。浏览器中的Sigmund聊天界面显示它已连接到OpenSesame。在OpenSesame中，会出现一个集成的聊天界面。

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame is connected to Sigmund.
--%

### 解决常见问题

Sigmund正在积极开发中。如果您遇到问题，首先确保您已应用所有更新，这些更新会通过OpenSesame中的自动更新程序出现。

如果Sigmund图标（一个黄色的机器人脸）没有出现在主工具栏中，这可能意味着Sigmund扩展没有安装。请参阅[此页面](https://rapunzel.cogsci.nl/manual/environment/)了解有关如何在OpenSesame中管理包的更多信息。

如果您持续看到消息：“Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect”，这可能意味着<https://sigmundai.eu>没有在网络浏览器中打开或没有激活。许多浏览器会自动停用未使用的页面。打开（或重新加载）Sigmund AI选项卡应重新激活页面。

如果您看到消息“Failed to listen to Sigmund. Maybe another application is already listening?”，这可能意味着您启动了两次OpenSesame。一次只能有一个OpenSesame实例连接到Sigmund。此消息的一个不太可能的原因是另一个（无关）进程正在使用系统上的端口8080。要对此进行调试，只需询问Sigmund：“我正在使用[您的操作系统]。我认为某个进程正在使用端口8080。我如何能发现是否确实如此，如果是，哪个进程正在使用端口8080？”

## 功能

### Sigmund可以编辑项目和脚本

首先，在OpenSesame中通过在概览区域中点击它来选择一个项目。接下来，您可以询问有关它的问题，甚至可以要求Sigmund直接修改项目。

例如，如果您要求Sigmund将SKETCHPAD上的文本颜色更改为红色，Sigmund会提出对SKETCHPAD脚本的简单修改。此更改将出现在一个所谓的diff查看器中，您可以在其中审核并决定是否要应用更改。如果您点击Ok，更改将被应用，文本将变为红色。

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%

### 西格蒙德可以修复实验中的错误

如果在运行实验时发生错误，您可以请西格蒙德修复错误。西格蒙德将分析错误，并可能建议更改以修复错误。

%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%