title: OSWeb
hash: d0eed8ce85e569f15d774ecf9cc4dff90b02dffd12470987bae00484d0c05865
locale: zh
language: Chinese

[TOC]

## 关于OSWeb

OSWeb是用于OpenSesame实验的在线运行环境。它是一个JavaScript库，可以在浏览器中执行OpenSesame实验。要使用OSWeb，您需要`opensesame-extension-osweb`包，该包预装在OpenSesame的Windows和macOS发行版中。

## 在网络浏览器中执行实验

要使用OSWeb在网络浏览器中运行实验，请按照以下步骤操作：

1. 打开实验属性，并在“运行实验”部分选择“在浏览器中使用OSWeb（osweb）”。
2. 点击任何“运行”按钮开始实验。
3. 如果实验与OSWeb不兼容，将出现详细说明兼容性问题的错误消息。（参见下面“支持的功能”部分以获取更多详细信息。）
4. 如果没有兼容性问题，实验将在新的浏览器窗口中打开。请注意，即使实验在网络浏览器中运行，它仍在您自己的计算机上本地执行。 要在网上托管实验，您需要将它发布到[JATOS](％url：jatos％)。
5. 实验结束后，数据将以`.json`格式下载。然后可以将此数据文件[转换为`.xlsx`或`.csv`格式](％url：manual/osweb/data％)，以进行进一步分析。

%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Open the Experiment Properties and select 'In a browser with OSWeb (osweb)' under 'Run experiment'.
--%

## OSWeb 控制面板

为更好地控制OSWeb实验，您可以从工具菜单访问OSWeb和JATOS控制面板。此面板提供了一系列配置选项：

- **可能的主题数字：** 在从JATOS中运行实验时，会从此列表中随机选择一个主题编号。您可以使用逗号（例如，“1,2,3”）或数字范围（例如，“1-10”）指定单个数字。 在从OpenSesame中运行实验时，此选项不适用，因为在实验开始时指定了主题编号。
- **使浏览器全屏：**此选项决定当实验在JATOS中开始时，是否应切换到全屏模式。 如果你直接从OpenSesame运行一个实验，这个选项将被忽视；相反，你可以通过使用常规的运行按钮来全屏运行实验，而快速运行按钮则不启用全屏。
- **显示OSWeb欢迎屏幕：** 这个切换控制参与者在实验开始之前是否会看到欢迎屏幕。 欢迎屏幕可以向参与者传达重要信息。 此外，它还具有技术目的-由于浏览器安全策略，媒体播放和某些功能只有在实验由用户操作启动时才可用。 因此，建议通常启用此选项。
- **跳过兼容性检查：** 启用此选项可允许您在OSWeb兼容性检查失败时运行实验。 请注意，这样做不会自动解决兼容性问题！
- **欢迎文字：**此字段允许你自定义显示给参与者的欢迎屏幕上的欢迎消息。
- **外部库：**此字段允许您指定应与实验一起加载的任何外部库。 下面的章节将更详细地解释外部库的使用。

%--
figure:
 id: FigOSWebControlPanel
 source: osweb-control-panel.png
 caption: The OSWeb and JATOS control panel offers a range of configuration options for your OSWeb experiments.
--%

## 支持的功能

当你从OpenSesame中运行实验时，会自动执行一个兼容性检查。 然而，这个检查相当肤浅。 支持的功能的更完整概述如下。

- `advanced_delay`
- `feedback`
    - 参见 `sketchpad`
- `form_consent` (支持版本 >= v1.4)
- `form_text_display` (支持版本 >= 1.4)
- `form_text_input` (支持版本 >= 1.4)
    - 不支持：全屏模式
- `form_multiple_choice` (支持版本 >= 1.4)
- `inline_html` (支持版本 >= 1.4)
- `inline_javascript`
- `keyboard`
    - 不支持：键释放
    - 不支持：HSV，HSL，以及 CIELab 色彩空间
- `logger`
- `loop`
    - 不支持：休息后恢复
    - 不支持：禁用第一周期评估
    - 不支持：约束（伪随机化）
    - 支持版本 >= 1.4：文件源
- `mouse`
    - 不支持：鼠标释放
    - 不支持：关联 sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - 支持版本 >= 1.4.12：声音平移，音调和淡入效果
    - 支持版本 >= 1.4.12：在 Safari 上的 Mac OS 或任何 iOS 浏览器上的声音播放
    - 不支持：停止后
- `sequence`
- `sketchpad`
    - 不支持：命名元素
    - 支持版本 >= 1.4：图像旋转
    - 不支持：HSV，HSL，以及 CIELab 色彩空间 
- `touch_response`

兼容性检查也可能指示以下类型的错误：

> 项目 new_logger 的准备阶段被连续多次调用

这个错误是由于实验的结构导致的，特别是链接复制的使用。这个错误的来源并不总是容易理解，但是您可以在[这篇文章](%url:prepare-run%)中了解更多关于准备-运行策略。作为一种解决方案，你可以将有问题的项目放到一个虚拟的 LOOP 中，也就是一个仅仅调用一次该项目的 LOOP 。

## 包含外部JavaScript包

您可以通过在标有 'External JavaScript libraries' 的输入字段中输入这些包的 URL （每行一个 URL ）来包含外部 JavaScript 包。然后，这些包将通过在 HTML 头部的 `<script>` 标签进行包含。

比如，您可以通过输入以下链接来包含矛盾：

```
https://webgazer.cs.brown.edu/webgazer.js
```


## 调试

见：

- %link:debugging%