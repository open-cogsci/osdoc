title: 关于JavaScript
hash: 1a7fe7974b0f26b2ee7c29211c43267ef47dff0d720592d5fd82996550c56b07
locale: zh
language: Chinese

在 OpenSesame 中，您可以使用图形用户界面 (GUI) 创建复杂的实验。但有时您会遇到 GUI 提供的功能不足的情况。在这些情况下，您可以向实验中添加 JavaScript 代码。

JavaScript 用于在浏览器中通过 OSWeb 运行的实验。如果您需要在桌面上运行实验，您需要使用 [Python](%url:manual/python/about%) 而不是 JavaScript。

__版本说明：__ 在 OpenSesame 4.0 中移除了对桌面的 JavaScript 支持。这是因为桌面上的 JavaScript 支持不完整，并且在没有增加太多便利的情况下让用户感到困惑。
{: .page-notification}

[TOC]

## 学习 JavaScript

在线上有许多 JavaScript 教程可供学习。一个好的资源是 Code Academy：

- <https://www.codecademy.com/learn/introduction-to-javascript>

## OpenSesame 的 GUI 中的 JavaScript

### Inline_javascript 项目

为了使用 JavaScript 代码，您需要向实验中添加一个 INLINE_JAVASCRIPT 项目。完成此操作后，您将看到如 %FigInlineJavaScript 所示的内容。

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: INLINE_JAVASCRIPT 项目。
--%

如您所见，INLINE_JAVASCRIPT 项目包括两个标签页：一个是准备阶段，另一个是运行阶段。准备阶段首先执行，以便项目为对时间敏感的运行阶段做好准备。通常，在准备阶段构建 `Canvas` 对象是一个良好的实践，这样它们可以在运行阶段无延迟地呈现。不过这只是一个惯例；您可以在这两个阶段执行任意 JavaScript 代码。

有关准备-运行策略的更多信息，请参见：

- %link:prepare-run%

### 打印输出到控制台

您可以使用 `console.log()` 命令打印到控制台：

```js
console.log('这将出现在控制台中！')
```

在桌面上运行时，输出将出现在 OpenSesame 控制台（或者说：调试窗口）中。在浏览器中运行时，输出将出现在浏览器控制台中。

## 需知事项

### 常用函数

许多常用函数可以直接在 INLINE_JAVASCRIPT 项目中使用。例如：

```js
// `Canvas()` 是一个工厂函数，返回一个 `Canvas` 对象
let fixdotCanvas = Canvas()
if (sometimes()) {  // 有时候固定点是绿色的
    fixdotCanvas.fixdot({color: 'green'})
} else {  // 有时候它是红色的
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

有关常用函数的列表，请参见：

- %link:manual/javascript/common%

### 声明变量 (let 和 var)

INLINE_JAVASCRIPT 项目以非严格（或者说：宽松）模式执行。这意味着您可以为未显式声明的变量赋值。当您这样做时，如果变量尚未被声明，将隐式地使用 `var` 来声明该变量。

```js
my_variable = '我的值'  // 使用 var 隐式声明
```

隐式或显式使用 `var` 声明的变量是全局的，这主要意味着它们可能被 LOGGER 记录。使用 `let` 声明的变量不是全局的，这主要意味着它们不会被 LOGGER 记录。

```js
this_is_a_global_variable = '我的值'
var this_is_also_a_global_variable = '我的值'
let this_is_not_a_global_variable = '我的值'
```

### `persistent` 对象：跨脚本保持对象

__版本说明__ 从 OSWeb 2.0 开始，所有 JavaScript 代码都在同一个工作空间中执行，因此对象在脚本之间得以保持。这意味着您不再需要 `persistent` 对象。
{:.page-notification}

每个 `INLINE_JAVASCRIPT` 项都在其自己的工作区中执行。这意味着——同 `Python INLINE_SCRIPT` 项不同！——您不能在一个脚本中声明的变量或函数在另一个脚本中使用。作为解决办法，您可以将变量或函数作为属性附加到 `persistent` 对象上，`persistent` 对象用作跨脚本保留事物的容器。

这样您就可以在一个 `INLINE_JAVASCRIPT` 中构造一个 `Canvas` ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. 并在另一个 `INLINE_JAVASCRIPT` 中显示它:

```js
persistent.myCanvas.show()
```


### `vars` 对象：访问实验变量

__版本说明__ 从 OSWeb 2.0 开始，所有实验变量都可作为全局变量使用。这意味着您不再需要 `vars` 对象。
{:.page-notification}

您可以通过 `vars` 对象访问实验变量：

```js
// OSWeb <= 1.4（使用 vars 对象）
// 获取一个实验变量
console.log('my_variable is: ' + vars.my_variable)
// 设置一个实验变量
vars.my_variable = 'my_value'

// OSWeb >= 2.0（不使用 vars 对象）
// 获取一个实验变量
console.log('my_variable is: ' + my_variable)
// 设置一个实验变量
my_variable = 'my_value'
```


### `pool` 对象：访问文件池

您可以通过 `pool` 对象从文件池中访问“文件”。最明显的用法是使用 `csv-parse` 库（下面将更详细地描述）解析文件池中的 CSV 文件，例如包含实验条件的文件。

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

您也可以直接从文件池播放声音文件。假设文件池中有一个叫做 `bark.ogg` 的文件，您可以这样播放它：

```js
pool['bark.ogg'].data.play()
```


### `Canvas` 类：呈现视觉刺激

`Canvas` 类用于呈现视觉刺激。例如，您可以以下述方式显示一个注视点：

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

`Canvas` 类的完整概述可以在这里找到：

- %link:manual/javascript/canvas%

## 可用的 JavaScript 库

以下 JavaScript 库默认包含在内：

- [随机函数 (`random-ext`)](%url:manual/javascript/random%)
- [颜色转换函数 (`color-convert`)](%url:manual/javascript/color-convert%)
- [CSV 函数 (`csv-parse`)](%url:manual/javascript/csv%)
- [类 Python 迭代器 (`pythonic`)](%url:manual/javascript/pythonic%)

您可以通过在 OSWeb 控制面板的“外部 JavaScript 库”字段中添加库的 URL 来包含其他 JavaScript 库。


## 调试

见：

- %link:debugging%