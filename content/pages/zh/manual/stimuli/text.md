title: 文本
hash: 2c5f78c24fe19088d9f96d120232def3d4ca9bb4bc48409ae868d353c7ebc4ed
locale: zh
language: Chinese

## 如何展示文本？

最常见的展示文本的方式是使用SKETCHPAD或FEEDBACK项目。这些项目允许你输入文本和其他视觉刺激。如果想以问卷式的方式展示文本，你可以使用[表单](%link:manual/forms/about%)。


## HTML格式

你可以在文本中简单插入HTML标签来使用。你可以在任何地方使用这些标签：在SKETCHPAD项目中，在INLINE_SCRIPT中（只要你使用`Canvas`类），在表单中等等。

例子：

~~~ .html
OpenSesame支持一系列HTML标签的子集：
- <b>粗体</b>
- <i>斜体</i>
- <u>下划线</u>

另外，你可以将'color'、'size'和'style'作为关键词传递给'span'标签：
- <span style='color:red;'>颜色</span>
- <span style='font-size:32px;'>字体大小</span>
- <span style='font-family:serif;'>字体风格</span>

最后，你可以使用'br'标签强制换行：
第一行<br>第二行
~~~


## 变量和内嵌Python

你可以使用`{...}`语法在文本中嵌入变量。例如，以下内容：

~~~ .python
被试编号是{subject_nr}
~~~

... 可能会解析为（对于编号为1的被试）：

~~~ .python
被试编号是1
~~~

你也可以嵌入Python表达式。例如，以下内容：

~~~ .python
被试编号模五的结果是{subject_nr % 5}
~~~

... 可能会解析为（对于编号为7的被试）：

~~~ .python
被试编号模五的结果是2
~~~


## 字体

### 默认字体

你可以从字体选择对话框（%FigFontSelect）中选择一个默认字体。这些字体已包含在OpenSesame中，因此当你使用它们时你的实验将完全可移植。

%--
图片：
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "通过字体选择对话框，可以选择随OpenSesame打包的一些默认字体。"
--%

字体名称已经为了清晰而重命名，但对应以下开源字体：

|__在OpenSesame中的名称__		|__实际字体__			|
|---------------------------|-----------------------|
|`sans`						|Droid Sans				|
|`serif`					|Droid Serif			|
|`mono`						|Droid Sans Mono		|
|`chinese-japanese-korean`	|文泉驿微米黑			|
|`arabic`					|Droid Arabic Naskh		|
|`hebrew`					|Droid Sans Hebrew		|
|`hindi`					|Lohit Hindi			|

### 通过字体选择对话框选择自定义字体

如果你在字体选择对话框中选择"其他..."，你可以选择操作系统上可用的任何字体。如果你这样做了，你的实验就不再完全可移植了，它会要求在你运行试验的系统上安装已选字体。

这仅适用于桌面端的OpenSesame，不适用于在线OSWeb实验。


### 将自定义字体放置到文件池中（OpenSesame桌面端）

当你在桌面端运行实验时，使用自定义字体的另一种方法是将字体文件放入文件池。例如，如果你将字体文件`inconsolata.ttf`放到文件池中，你可以在一个SKETCHPAD项目中使用这个字体，像这样：

	draw textline 0.0 0.0 "This will be inconsolata" font_family="inconsolata"

字体文件必须是TrueType `.ttf` 文件。这仅适用于桌面端的OpenSesame，不适用于在线OSWeb实验。


### 在OSWeb中使用谷歌字体（Google Fonts）

当你在浏览器中使用OSWeb运行实验时，你可以使用来自谷歌字体（Google Fonts）的字体。只需编辑文本元素的脚本并在`font_family`下指定字体名称即可：

```
draw textline x=0 y=0 font_family="Jacquard 12 Charted" text="This is shown in a funny font"
```

这仅适用于在线OSWeb实验，不适用于桌面端的OpenSesame。