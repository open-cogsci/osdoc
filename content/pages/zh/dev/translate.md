title: the following text:

Welcome to our study! In this experiment, you will be presented with different stimuli on the screen and you will need to indicate your responses using the keyboard or the mouse.

Please make sure you are in a quiet location and are not disturbed during the course of the experiment.

Press SPACEBAR to continue.

Remember: Do not lean back, and do not move your head back and forth.

First, you will see a series of letters appearing on the screen. When you see the letter 'X', press the SPACEBAR as quickly as possible.

During some trials, you may hear a tone either before, during, or after the letters are displayed. Do not let this distract you from the task.

Once you have completed the experiment, you will be asked to fill in a short questionnaire.
hash: 6c70867370aa97b006209d57e083504cd28b4f73a9eb715aae26ff5532faaf08
locale: zh
language: Chinese

如果您想提供翻译，建议您先发送电子邮件至 <s.mathot@cogsci.nl>，或在[论坛](https://forum.cogsci.nl/)上发送消息，确保您的语言还没有在进行中。

参与翻译所需的技术技能非常少！

[TOC]

## 用指定语言启动 OpenSesame

默认情况下，如果有可用的翻译，OpenSesame 使用您的操作系统的默认区域设置，如果没有翻译，则使用英语。要使用特定语言启动 OpenSesame，您可以在菜单 → 工具 → 首选项下更改“语言”选项。

## 如何翻译

### 翻译 Markdown 选项卡

#### 如何翻译 Markdown 选项卡

Markdown 选项卡是呈现文本和基本选项的类似于网站的选项卡。Markdown 选项卡的一个例子是启动 OpenSesame 时会看到的 "Get Started" 选项卡。

要翻译 Markdown 选项卡，请首先找到未翻译（英文）的 `.md` 文件。对于 "Get Started" 选项卡，这是：

- `opensesame_extensions\get_started\get_started.md`

接下来，将此原始文件复制到 `[original folder]\locale\[your locale code]\get_started.md`。因此，如果您正在进行法语 (`fr_FR`) 翻译，则需要将原始的 `get_started.md` 复制到（如果尚不存在这些子文件夹，则创建它们）：

- `opensesame_extensions\get_started\locale\fr_FR\get_started.md`

最后，只需用文本编辑器打开要翻译的 `get_started.md`，然后进行翻译。

#### 需要翻译的 Markdown 选项卡列表

在[OpenSesame 源代码](https://github.com/smathot/opensesame)中：

- `opensesame_extensions/update_checker/failed.md`
- `opensesame_extensions/update_checker/update-available.md`
- `opensesame_extensions/update_checker/up-to-date.md`
- `opensesame_extensions/toolbar_menu/system-information.md`
- `opensesame_extensions/help/offline_help.md`
- `opensesame_extensions/bug_report/failure.md`
- `opensesame_extensions/bug_report/report.md`
- `opensesame_extensions/bug_report/success.md`
- `opensesame_extensions/after_experiment/finished.md`
- `opensesame_extensions/system_information/system-information.md`
- `opensesame_extensions/get_started/get_started.md`
- `opensesame_extensions/opensesame_3_notifications/new-user.md`
- `opensesame_extensions/opensesame_3_notifications/old-experiment.md`
- `opensesame_extensions/opensesame_3_notifications/new-experiment.md`
- `opensesame_plugins/notepad/notepad.md`
- `opensesame_plugins/port_reader/port_reader.md`
- `opensesame_plugins/repeat_cycle/repeat_cycle.md`
- `opensesame_plugins/quest_staircase_init/quest_staircase_init.md`
- `opensesame_plugins/parallel/parallel.md`
- `opensesame_plugins/advanced_delay/advanced_delay.md`
- `opensesame_plugins/joystick/joystick.md`
- `opensesame_plugins/reset_feedback/reset_feedback.md`
- `opensesame_plugins/fixation_dot/fixation_dot.md`
- `opensesame_plugins/touch_response/touch_response.md`
- `opensesame_plugins/external_script/external_script.md`
- `opensesame_plugins/quest_staircase_next/quest_staircase_next.md`
- `opensesame_plugins/video_player/video_player.md`
- `opensesame_resources/help/missing.md`
- `opensesame_resources/help/new_item_warning.md`

在[Rapunzel 源代码](https://github.com/smathot/rapunzel)中：

- `opensesame_extensions/RapunzelWelcome/rapunzel_welcome.md`

### 翻译源代码和用户界面

#### 第 1 步：下载 translatables.ts

如果您从头开始翻译，那么您将从 `translatables.ts` 开始，该文件包含所有要翻译的字符串。OpenSesame 和 Rapunzel 每个都有自己的这个文件的版本，都需要翻译。

在 [OpenSesame 源代码](https://github.com/smathot/OpenSesame/)中，此文件可以在以下位置找到：

- `opensesame_resources/ts/translatables.ts`

在 [Rapunzel 源代码](https://github.com/smathot/rapunzel/)中，此文件可以在：

- `opensesame_extensions/RapunzelLocale/translatables.ts`

您可以下载或克隆源代码并直接打开这些文件。或者您可以通过GitHub查看它们。在最后一种情况下，在“文件”左上角，您将看到一个“Raw”链接。右键单击此链接，选择“另存为”（或您的浏览器上的类似选项）将该文件保存在磁盘上。

#### 步骤2：安装Qt Linguist

Qt Linguist是一个图形工具，可以帮助您进行翻译过程。它易于使用，允许您简单地选择一段英文并输入翻译。

__Windows__

您可以从这里下载Qt Linguist的独立版本：

- <https://github.com/thurask/Qt-Linguist/releases>

__Mac OS__

您可以从这里下载Qt Linguist的独立版本： 
- <https://github.com/lelegard/qtlinguist-installers/releases>

__Linux__

在Linux上，Qt Linguist通常可以从仓库获得。例如，在Ubuntu上，可以通过以下命令安装：

	sudo apt-get install qttools5-dev-tools

#### 步骤3：在Qt Linguist中打开translatables.ts

现在启动Qt Linguist并打开`translatables.ts`。首先，您会被要求输入源语言和目标语言。保留源语言为："POSIX/Any country"。目标语言应设置为您将要将OpenSesame翻译成的语言。将国家/地区选项保留为 "Any country"。稍后可以通过菜单→编辑→翻译文件设置来更改这些设置。

现在您可以开始翻译了！在左侧，您会看到一个"contexts"列表。这些表示文本显示的上下文，这是非常有帮助的。要进行翻译，只需点击第一个上下文中第一个源文本字符串，输入适当的翻译，然后按`Ctrl+Enter`前进到下一个字符串。

某些字符串将包含HTML标签，如下所示：

	Size<br /><i>in pixels</i>

在这种情况下，请只更改文本，保留HTML标签不变。因此，对于荷兰语翻译，这将变为：

	大小<br /><i>以像素为单位</i>

此外，有些字符串包含通配符，如下所示：

	Tell me more about the %s item

这些`%s`（以及`%d`、`%f`、`{}`等）通配符是由OpenSesame在运行时填充的空白。请尊重这些（删除一个通配符会导致程序崩溃！）并尝试围绕它们构建适当的翻译。因此，对于荷兰语翻译，这将变为：

	告诉我更多关于%s项目的信息

#### 步骤4：将翻译编译为`.qm`并进行测试

OpenSesame不直接使用`.ts`文件，而是需要一种`.qm`格式的文件。您可以通过Qt Linguist简单地选择“文件→发布为”来创建这个文件。创建一个与原始文件（除了扩展名）同名的`.qm`文件。

对于 OpenSesame，这个文件应保存为 (修改 `fr_FR` 为适当的语言代码)：

- `opensesame_resources/locale/fr_FR.qm`

对于 Rapunzel，这个文件应保存为 (修改 `fr_FR` 为适当的语言代码)：

- `opensesame_extensions/RapunzelLocale/fr_FR.qm`

##保存并提交您的翻译

###通过电子邮件发送

一旦您对翻译满意，请将翻译后的`.ts`文件和所有翻译后的`md`文件发送到<s.mathot@cogsci.nl>。

###通过GitHub提交

您还可以通过GitHub提交（和更新）您的翻译。首先，将您的翻译添加到OpenSesame的分支，作为`opensesame_resources/ts/ll_RR.ts`，其中`ll`对应于语言，`RR`对应于地区。例如，`en_US`是美国英语，`fr_FR`是法语，`zh_CN`是中文。您可以在[这里](http://www.iana.org/assignments/language-subtag-registry)找到合法地区和语言的列表。

类似地，将所有翻译的`.md`文件添加到OpenSesame的分支。

最后，提交一个拉取请求，将您的翻译包含在OpenSesame中。

## 更新现有翻译

更新现有翻译的过程与创建新翻译的过程类似。关键的区别在于，您不是从`resources/ts/translatables.ts`开始，而是从一个非空白的翻译文件开始，例如`resources/ts/fr_FR.ts`。