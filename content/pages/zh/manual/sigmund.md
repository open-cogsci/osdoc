title: SigmundAI助理
hash: 7a5ad3e4d415e7ac0275d30a2a31a4805bf4ac5d702bfbad1b3ff4319dd6b942
locale: zh
language: Chinese

SigmundAI Copilot 目前处于公开测试阶段
{:.page-notification}

[SigmundAI.eu](https://sigmundai.eu) 是一个旨在帮助您使用 OpenSesame 的 AI 研究助手。你可以通过安装一个扩展直接在 OpenSesame 中使用 Sigmund。使用 Sigmund 需要订阅。

[TOC]

## 安装 Sigmund 扩展

首先，安装 `opensesame-extension-sigmund` 包：

```
pip install opensesame-extension-sigmund
```

在 Windows 上，你需要以管理员身份运行上述命令，或者添加 `--user` 标志：

```
pip install opensesame-extension-sigmund --user
```

有关安装包的更多信息，请参见：

- <https://rapunzel.cogsci.nl/manual/environment/>

## 连接 Sigmund

登录到 <https://sigmunai.eu/>Sigmund</a>。聊天界面现在应该可见。聊天界面会自动监听来自 OpenSesame 的传入链接。

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: SigmundAI.eu 的聊天界面。
--%

在 OpenSesame 中，通过点击主工具栏中的机器人图标激活 SigmundAI Copilot。OpenSesame 现在尝试连接到 Sigmund 聊天界面。

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame 正在连接到 Sigmund。
--%

几秒钟后，应该建立连接。浏览器中的 Sigmund 聊天界面会显示它已连接到 OpenSesame。在 OpenSesame 内部，会出现一个集成的聊天界面。

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame 已连接到 Sigmund。
--%

## 功能

### 编辑项目和脚本

首先，通过在概览区域中点击 OpenSesame 中的项目来选择它。接下来，你可以就其提出问题，甚至可以直接让 Sigmund 修改该项目。

例如，如果你让 Sigmund 将 SKETCHPAD 上文本的颜色改为红色，Sigmund 会提出一个简单的 SKETCHPAD 脚本更改。此更改将出现在所谓的差异查看器中，你可以在此查看更改并决定是否应用此更改。如果你点击确定，该更改将被应用，文本现在将变为红色。

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: 当 Sigmund 建议更改时，你可以先查看更改再决定是否接受它们。
--%

### 修复错误

如果在运行实验时出现错误，你可以请 Sigmund 修复该错误。然后，Sigmund 将分析错误，并可能建议更改来修复它。

%--
figure:
 id: FigError
 source: error.png
 caption: 你可以请 Sigmund 修复实验中的错误。
--%