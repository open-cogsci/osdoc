title: 关于JavaScript
hash: a7f9ce07f8ba8ef35658430e6e490db256a6c6c1681e7b791f85a4d8f288ae44
locale: zh
language: Chinese

在OpenSesame中，您可以仅通过图形用户界面(GUI)创建复杂的实验。但是，您有时会遇到GUI提供的功能不足的情况。在这些情况下，您可以向您的实验中添加JavaScript代码。

JavaScript适用于在带有OSWeb的浏览器中运行的实验。如果你需要在桌面上运行你的实验，你需要用[Python](%url:manual/python/about%)代替JavaScript。

__版本说明：__在OpeSesame 4.0中删除了对桌面JavaScript的支持。这是因为桌面对JavaScript的支持不完整，用户认为该功能并未带来太多帮助的同时却感到混乱。
{: .page-notification}

[TOC]


## 学习JavaScript

在线上有许多JavaScript教程可供参考。一个不错的资源是Code Academy：

- <https://www.codecademy.com/learn/introduction-to-javascript>


## 在OpenSesame GUI中的JavaScript


### Inline_javascript 项目

要使用JavaScript代码，您需要在您的实验中添加一个INLINE_JAVASCRIPT项目。完成此操作后，您会看到像%FigInlineJavaScript这样的内容。

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: 这就是INLINE_JAVASCRIPT项目.
--%

如你所见，INLINE_JAVASCRIPT项目由两个选项卡组成：一个用于Prepare阶段，一个用于Run阶段。Prepare阶段先被执行，以便项目准备有关任务的关键运行阶段。在Prepare阶段 创建`Canvas`对象是一个好的习惯，这样他们就可以在Run阶段毫无延迟地被呈现。但这只是个习惯，你可以在这两个阶段执行任意的JavaScript代码。

有关 prepare-run 策略的更多信息，请见：

- %link:prepare-run%


### 命令控制台中的输出

您可以使用 `console.log()` 命令打印到命令控制台：

```js
console.log('This will appear in the console!')
```

在桌面上运行时，输出将出现在OpenSesame 控制台（或：debug 窗口）。在浏览器中运行时，输出将出现在浏览器的命令控制台。


## 应当知道的内容

### 常用函数

许多常用函数可以直接在INLINE_JAVASCRIPT项目中使用。例如：

```js
// `Canvas()`是返回`Canvas`对象的工厂函数
let fixdotCanvas = Canvas()
if (sometimes()) {  // 有时候小圆点是绿色的
    fixdotCanvas.fixdot({color: 'green'})
} else {  // 有时候小圆点是红色的
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

有关常用函数的列表，请参阅：

- %link:manual/javascript/common%


### `persistent`对象：在不同的脚本中保留对象

__版本注__从OSWeb 2.0开始，所有的JavaScript代码都在相同的工作空间中执行，对象因此可以在脚本之间保留。这意味着您不再需要 `persistent` 对象。
{:.page-notification}

每个INLINE_JAVASCRIPT项目都在其自己的工作空间中执行。这意味着（这与Python INLINE_SCRIPT项目不同！）您无法在另一个脚本中使用在一个脚本中声明的变量或函数。作为解决方法，您可以将变量或函数作为属性附加到`persistent`对象上，该对象充当您希望在各个脚本中保留的东西的容器。

以这种方式，你可以在一个INLINE_JAVASCRIPT中构建一个`Canvas`...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

...然后在另一个INLINE_JAVASCRIPT中展示它：

```js
persistent.myCanvas.show()
```


### `vars`对象：实验变量的访问

__版本注__从OSWeb 2.0开始，所有的实验变量都作为全局变量可以使用。这意味着你不再需要`vars`对象。
{:.page-notification}

你可以通过`vars`对象访问实验变量：

```js
// OSWeb <= 1.4 (带有 vars 对象)
// 获取实验变量
console.log('my_variable是：' + vars.my_variable)
// 设置实验变量
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (无vars 对象)
// 获取实验变量
console.log('my_variable是：' + my_variable)
// 设置实验变量
var my_variable = 'my_value'
```


### `pool` 对象：访问文件池

您可以通过 `pool` 对象从文件池中访问'files'。其最明显的用途是使用 `csv-parse` 库（下面将更详细地描述）解析来自文件池的 CSV 文件，例如带有实验条件的文件。

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

您还可以直接从文件池播放声音文件。假设文件池中有一个名为 `bark.ogg` 的文件，您可以这样播放它：

```js
pool['bark.ogg'].data.play()
```


### `Canvas` 类：呈现视觉刺激

`Canvas` 类用于呈现视觉刺激。例如，您可以按以下方式显示固定小点：

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

`Canvas` 类的完整概述可以在这里找到：

- %link:manual/javascript/canvas%

## 可用的 JavaScript 库

以下 JavaScript 库默认包含在内：

- [random functions （`random-ext`）](%url:manual/javascript/random%)
- [颜色转换函数（`color-convert`）](%url:manual/javascript/color-convert%)
- [CSV 函数（`csv-parse`）](%url:manual/javascript/csv%)
- [Python style 迭代器（`pythonic`）](%url:manual/javascript/pythonic%)

您可以在 OSWeb 控制面板的'外部 JavaScript'库字段中通过 URL 添加更多 JavaScript 库。


## 调试

参见：

- %link:debugging%