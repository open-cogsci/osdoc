title: 关于JavaScript
hash: b35489df1d7af79c088585c5b57e0661050203bbe5a62da2cd5449da48a08da6
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

您可以通过 `pool` 对象访问文件池中的'文件'。最明显的用途是使用 `csv-parse` 库（下面详细介绍）从文件池中解析 CSV 文件，例如实验条件。

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

您还可以直接从文件池播放音频文件。假如文件池中有一个名为 `bark.ogg` 的文件，你可以这样播放它：

```js
pool['bark.ogg'].data.play()
```


### `Canvas` 类：呈现视觉刺激

`Canvas` 类用于呈现视觉刺激。例如，您可以像这样显示一个注视点：

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

关于 `Canvas` 类的完整概述可以在这里找到：

- %link:manual/javascript/canvas%


## 可用的 JavaScript 库

OSWeb 随附了几个方便的 JavaScript 库。


### random-ext：高级随机化

`random-ext` 类库以 `random` 的形式提供。此库为随机化提供了许多便捷的高级功能。

__示例：__

在五行五列的网格中，绘制八个随机颜色的圆，位置从五行五列的网格中随机采样：

```js
let positions = xy_grid(5, 50)
positions = random.subArray(positions, 8)
const cnv = Canvas()
cnv.fixdot()
for (const [x, y] of positions) {
    cnv.circle({x: x, y: y, r: 20, fill: true, color: random.color()})
}
cnv.show()
```

概述如下：

- <https://www.npmjs.com/package/random-ext>


### pythonic：用于遍历数组的 Python 类似函数

`pythonic` 库提供了类似 Python 的遍历数组的函数。提供的功能有：`range()`, `enumerate()`, `items()`, `zip()`, 和 `zipLongest()`。

__示例：__

绘制一个五行五列的递增数字网格：

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

概述如下：

- <https://www.npmjs.com/package/pythonic>


### color-convert：颜色转换工具

`color-convert` 类库以 `convert` 的形式提供。它提供了方便的高级功能，将一种颜色规范转换为另一种颜色规范。

__示例：__

```js
console.log('The RGB values for blue are ' + convert.keyword.rgb('blue'))
```

概述如下：

- <https://www.npmjs.com/package/color-convert>


###csv-parse: 将 CSV 格式的文本解析为对象

`csv-parse` 库提供了同步的 `parse()` 函数。这使您可以将 CSV 格式的文本解析为对象，例如从文件池中的 CSV 文件。

__示例：__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

概述如下：

- <https://csv.js.org/parse/api/sync/#sync-api>


## 调试

现代浏览器大多数，尤其是 Chrome 和 Firefox, 都内置了强大的调试器。您可以通过在脚本中添加一个简单的 `debugger` 行来激活调试器（%FigDebuggerInlineJavaScript）。

%--
figure:
 id: FigDebuggerInlineJavaScript
 source: debugger-inline-javascript.png
 caption: 从 INLINE_JAVASCRIPT 项目中激活调试器。
--%

然后启动实验并在 OSWeb 欢迎屏幕出现后显示调试器（或者：在 Chrome 中打开开发者工具，或者：在 Firefox 中打开 Web 开发者工具）。当调试器遇到 `debugger` 语句时，将暂停实验。在这一点上，您可以使用控制台与 JavaScript 工作区进行交互，或者使用 Scope 工具检查变量 (%FigDebuggerChrome)。

%--
figure:
 id: FigDebuggerChrome
 source: debugger-chrome.png
 caption: Inspecting the variable scope in Chrome.
--%

另请参阅：

- %link:manual/osweb/osweb%