title: OSWeb
hash: 9fc0b6a63aa91000243df7d41fe843fc7eb52f30b3e6ac866728b5e0e8ebde0a
locale: zh
language: Chinese

[TOC]

## 关于 OSWeb

OSWeb 是用于在线运行 OpenSesame 实验的运行时库。也就是说，它是一个用于解释和执行 OpenSesame 实验的 JavaScript 库。


## OSWeb 扩展

OpenSesame 的 OSWeb 扩展（%FigOSWebExtension）允许您在浏览器中测试实验，并将实验导出为可以导入 [JATOS](%url:jatos%) 的格式。

%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: OpenSesame中的OSWeb扩展
--%


## 在浏览器中测试

- 在 OpenSesame 中打开 OSWeb 扩展（菜单 → 工具 → OSWeb）。
- 扩展将执行一个简单（且不完整）的检查，以查看您的实验是否与 OSWeb 兼容。
- 如果没有检测到问题，点击“在外部浏览器中测试实验”，或者点击主工具栏中的相应按钮。
- 这将在您的默认浏览器中打开实验，以便您检查实验是否按预期运行（%FigTestRun）。
- 您还可以点击主工具栏中的“在浏览器中运行”按钮（Alt+Ctrl+W）。

%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: 在浏览器中测试实验时的OSWeb欢迎屏幕
--%


## 调试

首先，请确保您的实验仅使用受支持的功能，如下所示。接下来，在 OpenSesame 中以传统的（非浏览器）方式运行实验。这将为您提供可用于调试的最有用的错误消息。

如您的实验仅使用受支持的功能并在 OpenSesame 正常运行，则您可以使用浏览器控制台查看 JavaScript 错误消息。这些消息的信息量远不及 OpenSesame 的错误消息，但它们仍然可能有帮助。每个浏览器访问控制台的方式都不同。在 Chrome 中，您可以通过右键单击某个位置，选择 Inspect（`Ctrl+Shift+I`），然后切换到 Console 标签（见 %FigChromeConsole）。在 Firefox 中，您可以通过点击右上角的菜单图标，然后选择 Web Developer → Web Console（`Ctrl+Shift+I`）访问控制台。

如果您的实验使用了 INLINE_JAVASCRIPT 项目，浏览器控制台也是调试脚本的强大工具，如下所述：

- %link:manual/javascript/about%

%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: Chrome的浏览器控制台
--%



## 受支持的功能

您可以使用兼容性检查（%FigOSWebExtension）检查您的实验是否与 OSWeb 兼容。这个兼容性检查相当肤浅。下面提供了受支持功能的更完整概述。

__注意__：许多受支持的功能在 OSWeb 1.4 中已添加。因此，请检查您的 OSWeb 版本与以下概述的版本。

- `advanced_delay`
- `feedback`
    - 参见 `sketchpad`
- `form_consent`（支持 >= v1.4）
- `form_text_display`（支持 >= 1.4）
- `form_text_input`（支持 >= 1.4）
    - 不支持：全屏模式
- `form_multiple_choice`（支持 >= 1.4）
- `inline_html`（支持 >= 1.4）
- `inline_javascript`
- `keyboard`
    - 不支持：按键释放
    - 不支持：HSV、HSL 和 CIELab 色彩空间
- `logger`
- `loop`
    - 不支持：在中断后恢复
    - 不支持：禁用第一次循环的评估
    - 不支持：约束条件（伪随机化）
    - 支持 >= 1.4：文件来源
- `mouse`
    - 不支持：鼠标释放
    - 不支持：关联的 sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - 支持 >= 1.4.12: 合成声音、音调和淡入
    - 支持 >= 1.4.12：在 Safari for Mac OS 或任何 iOS 浏览器上的声音回放
    - 不支持：停止后
- `sequence`
- `sketchpad`
    - 不支持：命名元素
    - 支持 >= 1.4：图像旋转
    - 不支持：HSV、HSL 和 CIELab 色彩空间
- `touch_response`

兼容性检查可能还会显示以下类型的错误：

```bash
项目new_logger的准备阶段被连续调用多次
项目new_logger的运行阶段被连续调用多次
```

此错误是由实验的结构以及特别是链接副本的使用所导致的。这个错误的来源并不总是容易理解，但您可以在[这篇文章](%url:prepare-run%)中了解更多关于准备-运行策略的信息。作为一种解决方法，您可以将有问题的项目放在一个虚拟的循环中，也就是说，一个只调用项目一次的循环。

## 支持的浏览器

以下浏览器和操作系统组合已经过与最新版本的OSWeb的兼容性测试。较旧的浏览器版本、操作系统和OSWeb版本可能可以使用，但近期未经过充分测试。某些扩展，如广告拦截器或脚本拦截器，可能会阻止OSWeb运行。

### 完全支持

- Chrome >= 101 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Edge >= 101 (Windows 11, Mac OS Monterey)
- Firefox >= 99 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Opera >= 86 (Windows 11) 
- Chromium >= 101 (iOS 15.2)
- Firefox >= 99 (iOS 15.2)
- Opera >= 86 (Mac OS Monterey) 
- Safari >= 15 (iOS 15.2, Mac OS Monterey)

### 不支持

- Internet Explorer >= 11 (Windows 10) 


## 升级OSWeb

OSWeb正在积极开发中。如果您想确保您正在运行的是最新版本，可以升级名为`opensesame-extension-osweb`的OSWeb扩展。从OpenSesame 3.3开始，您可以在控制台中运行以下命令来实现：

```bash
conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

或：

```bash
pip install --pre opensesame-extension-osweb --upgrade
```

另请参阅：

- <https://rapunzel.cogsci.nl/manual/environment/>


## 包含外部JavaScript包

新增于OSWeb v1.4.6.1
{:.page-notification}

您可以通过在标签为“外部JavaScript库”的输入字段中输入这些包的网址（每行一个网址）来包含外部JavaScript包。然后，这些包将通过HTML头部的`<script>`标签包含。

例如，您可以通过输入以下链接将[WebGazer](%url:webgazer%)包含到浏览器中:

```
https://webgazer.cs.brown.edu/webgazer.js
```