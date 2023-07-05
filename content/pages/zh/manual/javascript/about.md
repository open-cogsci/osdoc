title: 关于JavaScript
hash: c3cfb549c6deb5d2a4f14b8681cb80f556bc41109c145df9574880d7eaa2399b
locale: zh
language: Chinese

在OpenSesame中，您可以仅使用图形用户界面（GUI）来创建复杂的实验。但有时，您会遇到GUI所提供的功能不足的情况。在这些情况下，您可以将JavaScript代码添加到您的实验中。

JavaScript用于在浏览器中运行的带有OSWeb的实验。如果您需要在桌面上运行实验，您需要使用[Python](％url:manual/python/about％)而不是JavaScript。

__版本说明：__OpenSesame 4.0中移除了对桌面的JavaScript支持。这是因为桌面上的JavaScript支持不完全，而且用户认为它令人困惑，且没有带来太多益处。
{：.page-notification}

[TOC]


## 学习JavaScript

网络上有许多JavaScript教程。一个很好的资源是Code Academy：

- <https://www.codecademy.com/learn/introduction-to-javascript>


## OpenSesame GUI中的JavaScript

### Inline_javascript项目

要使用JavaScript代码，您需要在实验中添加一个INLINE_JAVASCRIPT项目。完成此操作后，您将看到类似％FigInlineJavaScript的内容。

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: INLINE_JAVASCRIPT 项目。
--%

如您所见，INLINE_JAVASCRIPT项目包含两个选项卡：一个用于准备阶段，另一个用于运行阶段。首先执行准备阶段，以允许项目为时间关键性的运行阶段做准备。最好在准备阶段构建 `Canvas` 对象，以便在运行阶段无延迟地呈现。但这只是约定。在这两个阶段，您都可以执行任意的JavaScript代码。

有关准备-运行策略的详细信息，请参阅：

- ％link:prepare-run％


### 输出信息到控制台

您可以使用`console.log()`命令将信息打印到控制台：

```js
console.log('这将显示在控制台上!')
```

在桌面上运行时，输出将显示在OpenSesame控制台（或：调试窗口）中。在浏览器中运行时，输出将显示在浏览器控制台中。

## 重要提示

### 常用函数

许多常用功能可以直接在INLINE_JAVASCRIPT项目中使用。例如：

```js
// `Canvas()` 是一个工厂函数，返回一个 `Canvas` 对象
let fixdotCanvas = Canvas()
if (sometimes()) {  // 有时候fixdot是绿色的
    fixdotCanvas.fixdot({color: 'green'})
} else {  // 有时候是红色的
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

有关常用函数列表，请参阅：

- ％link:manual/javascript/common％

### `persistent`对象：在脚本间保留的对象

__版本说明__ 从OSWeb 2.0开始，所有JavaScript代码都在同一个工作空间中执行，因此对象在脚本之间保留。这意味着您不再需要`persistent`对象。
{：.page-notification}

每个INLINE_JAVASCRIPT项目在其自己的工作区中执行。这意味着（与Python INLINE_SCRIPT项目不同！）您无法在一个脚本中使用在另一个脚本中声明的变量或函数。作为解决方法，您可以将变量或函数作为属性附加到`persistent`对象上，该对象将保存在脚本间的对象容器中。

这样，您可以在一个INLINE_JAVASCRIPT中构造一个 `Canvas`...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

..然后在另一个INLINE_JAVASCRIPT中显示它：

```js
persistent.myCanvas.show()
```

### `vars`对象：访问实验变量

__版本说明__ 从OSWeb 2.0开始，所有实验变量都可以作为全局对象。这意味着您不再需要`vars`对象。
{：.page-notification}

您可以通过`vars`对象访问实验变量：

```js
// 获取实验变量
console.log('my_variable 是: ' + vars.my_variable)
// 设置实验变量
vars.my_variable = 'my_value'
```

### `pool` 对象：访问文件池

您可以通过 `pool` 对象从文件池中访问'文件'。最明显的用法是使用 `csv-parse` 库（下面将详细描述）从文件池解析 CSV 文件，例如带有实验条件的文件。

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

您还可以直接从文件池播放声音文件。假设文件池中有一个名为 `bark.ogg` 的文件，您可以像这样播放它：

```js
pool['bark.ogg'].data.play()
```


### `Canvas` 类：展示视觉刺激

`Canvas` 类用于展示视觉刺激。例如，您可以按照以下方式显示一个固定的点：

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

`Canvas` 类的完整概述可以在这里找到：

- %link:manual/javascript/canvas%

## 可用的 JavaScript 库

以下 JavaScript 库默认包含在内：

- [随机函数（`random-ext`）](%url:manual/javascript/random%)
- [颜色转换函数（`color-convert`）](%url:manual/javascript/color-convert%)
- [CSV 函数（`csv-parse`）](%url:manual/javascript/csv%)
- [Python式迭代器（`pythonic`）](%url:manual/javascript/pythonic%)

您可以通过将库的 URL 添加到 OSWeb 控制面板的 '外部 JavaScript' 库字段中，来包含额外的 JavaScript 库。

## 调试

参见：

- %link:debugging%