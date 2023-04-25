title: 文本
hash: 1958b3f404645f67ec8c328c22b9b876e1507c616fa82878164f23ac0d364e92
locale: zh
language: Chinese

[TOC]

## 如何呈现文本？

显示文本的最常见方法是使用SKETCHPAD或FEEDBACK项目。这些允许您输入文本和其他视觉刺激。对于类似问卷的文本显示方式，您可以使用[forms](%link:manual/forms/about%)。

## HTML格式

您可以使用HTML标签，只需将其插入您的文本中即可。您可以在任何地方使用这些标签：在SKETCHPAD项目中，在INLINE_SCRIPTs 中（前提是您使用`Canvas`类），在表单中等。

示例：

~~~ .html
OpenSesame支持HTML标签的子集：
- <b>粗体</b>
- <i>斜体</i>
- <u>下划线</u>

此外，您可以将'color'、'size'和'style'作为关键字传递给'span'标签：
- <span style='color:red;'>颜色</span>
- <span style='font-size:32px;'>字体大小</span>
- <span style='font-family:serif;'>字体风格</span>

最后，您可以使用'br' 标签强制换行：
第1行<br>第2行
~~~

## 变量和内联Python

您可以使用 `{...}` 语法在文本中嵌入变量。例如，以下内容：

~~~ .python
主题编号是 {subject_nr}
~~~

... 可能会评估为(针对主题1)：

~~~ .python
主题编号是 1
~~~

您还可以嵌入Python表达式。例如，以下内容：

~~~ .python
主题编号模5是 {subject_nr % 5}
~~~

... 可能会评估为（针对主题7）

~~~ .python
主题编号模5是 2
~~~

## 字体

### 默认字体

您可以从字体选择对话框中选择一个默认字体（％FigFontSelect）。这些字体随OpenSesame一起提供，因此使用它们时您的实验将具有完全的便携性。

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "可以通过字体选择对话框选择一些与OpenSesame捆绑的默认字体。"
--%

这些字体已经为了清晰起见而被重命名，但它们对应于以下开源字体：

|__OpenSesame中的名称__	|__实际字体__		        |
|-------------------------|-------------------------|
|`sans`					|Droid Sans				|
|`serif`				|Droid Serif				|
|`mono`					|Droid Sans Mono		|
|`chinese-japanese-korean`	|WenQuanYi Micro Hei	|
|`arabic`				|Droid Arabic Naskh		|
|`hebrew`				|Droid Sans Hebrew		|
|`hindi`				|Lohit Hindi			|

### 通过字体选择对话框选择自定义字体

如果在字体选择对话框中选择“其他…”，您可以选择操作系统上可用的任何字体。这样做后，您的实验将不再具有完全的便携性，需要在允许实验的系统上安装所选字体。

### 将自定义字体放入文件池

使用自定义字体的另一种方法是将字体文件放入文件池。例如，如果您将字体文件`inconsolata.ttf`放入文件池，您可以在SKETCHPAD项目中使用该字体，如下所示：

	draw textline 0.0 0.0 "This will be inconsolata" font_family="inconsolata"

请注意，字体文件必须是truetype `.ttf` 文件。