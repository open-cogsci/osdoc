title: 调试
hash: 183510524112a0f1a17d60669acd2273f06aa15f0b358eb9d3fdaac1002810c0
locale: zh
language: Chinese

在设计新实验时，你将不可避免地遇到bug。Bug可能表现为伴随错误消息的崩溃，或者没有任何明确的错误消息但表现出意料之外的行为。

调试，即诊断和纠正这些错误及未预期行为的技术和技巧，是实验设计过程中的关键部分。

[TOC]

## 用户界面中的调试

### 使用变量检查器

OpenSesame的变量检查器提供了你的实验中所有当前活动的变量的概览，包括：

- 在用户界面中明确定义的变量，通常在LOOP项目中。
- 响应变量，由各种响应项目设定，如KEYBOARD_RESPONSE项目。
- 使用Python INLINE_SCRIPT项目定义的变量。

实验运行时，变量检查器动态更新，提供变量和其值的实时概览。这个功能允许你实时监控实验的行为，帮助你识别出任何可能的问题或bug。

例如，考虑一个你定义了一个变量`left_letter`来决定哪个字母应该出现在SKETCHPAD的左边的情况。然而，在执行过程中，你在变量检查器中注意到一个不符：`left_letter`实际上显示在你的显示器的右边。这就意味着一个bug，也就是你在SKETCHPAD上放错了左边和右边的字母。

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: 您可以使用变量检查器来检查您的实验是否按照预期执行。在这个例子中，存在一个bug，那就是通过变量`left_letter`定义的字母实际上出现在右边，反之亦然。
--%

定期使用变量检查器来监控变量有助于确保你的实验按预期进行，并及早发现问题。

### 输出调试信息至IPython / Jupyter控制台

Python `print()`函数用于INLINE_SCRIPT项目中时，是一个简单而强大的调试工具，与变量检查器的用途类似。例如，在每个试验开始时的INLINE_SCRIPT的准备阶段，你可以打印变量`left_letter`和`right_letter`的值。

要查看这些调试消息，打开Jupyter / IPython控制台，并在运行实验时监视输出。这样，你可以验证控制台中显示的输出是否与实验的实际行为一致。

%--
figure:
 id: FigPrintingOutput
 source: printing-output.png
 caption: Python `print()`函数可用来向控制台输出调试消息。
--%

在上述示例中，显然，分配给`left_letter`变量的字母（因此预计会出现在左边）实际上出现在右边，反之亦然。

### 解读用户界面错误消息

当你的实验中的一个bug导致崩溃时，OpenSesame会显示一个错误消息，也称为'异常'。错误消息通常包括以下组件：

- **错误类型：** 表示错误的一般类别。在下面的例子中，这是一个 `FStringError`。
- **描述：** 提供了更具体的解释，说明触发了什么错误。在这种情况下，"无法评估..."。
- **源：** 指定触发错误的项目，以及它是在运行阶段还是准备阶段发生的。
- **追溯：** 详细的Python错误信息。只有在评估自定义Python代码时才会显示此信息，包括INLINE_SCRIPT项目，但也包括条件表达式(例如，如果运行表达式)，以及带有嵌入式变量引用的文本。
- **了解更多关于这个错误的信息：**您可以点击以获取有关错误消息的更详细信息的交互式按钮。

让我们看一个例子，以更好地理解这些组件，并了解如何修复一个常见的错误：

%--
figure:
 id: FigFStringError
 source: fstring-error.png
 caption: An `FStringError` indicates an issue when trying to evaluate a text string containing a Python expression.
--%

这是一个`FStringError`的错误，意思是在解析包含Python表达式的文本字符串时遇到了问题。在这个例子中，问题文本是`{right_leter}`。任何被大括号包围的内容，都被解析为Python表达式，因此在这种情况下，Python表达式就是`right_leter`，它只是一个变量名。试图评估Python表达式`right_leter`触发了`NameError`，因为`right_leter`没有被定义。

这种说法很技术，但是这里到底出了什么问题呢？问题源自引用了一个不存在的变量：`right_leter`。看看变量名称，似乎很可能有一个拼写错误，预期的变量应该是`right_letter`，带有两个“t”。

我们应该在哪里纠正这个错误呢？错误消息表明错误的源头是一项叫做 *target* 的项目，它是一个SKETCHPAD。要解决这个错误，我们需要打开 *target*，将文本从'{right_leter}'修改为'{right_letter}'。


### 解读Python错误消息

在Python中，错误分为两种类别：语法错误和异常（或运行时错误）。


#### Python语法错误

当Python解释器不能解析代码，因为它违反了Python的语法规则时，就会发生语法错误。这可能是由于括号不匹配、缺少逗号、缩进不正确等等。在OpenSesame中，这会导致`PythonSyntaxError`。

%--
figure:
 id: FigPythonSyntaxError
 source: python-syntax-error.png
 caption: A `PythonSyntaxError` is triggered when the code violates Python's syntax rules and cannot be parsed.
--%

上面的错误消息表明，在准备阶段的第16行，名称为*constants*的项目发生了语法错误。这是有问题的一行：

```python
target_orientations = [('z', 0), ('/', 90]
```

消息也暗示括号不匹配可能是错误的源头。考虑到这一点，我们可以通过在关闭括号`]`前添加一个丢失的圆括号`)`来解决问题：

```python
target_orientations = [('z', 0), ('/', 90)]
```


#### Python异常

当Python代码在语法上正确但在执行过程中遇到问题时，会引发异常。在OpenSesame中，这种异常会导致`PythonError`。

%--
figure:
 id: FigPythonError
 source: python-error.png
 caption: A `PythonError` is triggered when an exception is raised during the execution of syntactically correct Python code.
--%

上面的错误消息表明，在运行阶段的第2行，名称为*trial_script*的项目引发了一个`NameError`。具体来说，标识符'clock_sleep'不能被识别。看看引发错误的这一行，很明显，我们错误地使用了下划线(`_`)而不是点(`.`)，错误地暗示了`clock_sleep()`是一个功能。

```python
clock_sleep(495)
```

要解决这个问题，我们应该正确地将 `sleep()` 函数作为 `clock` 对象的一部分进行引用：

```python
clock.sleep(495)
```

## 在网络浏览器中调试（OSWeb）

### 将输出打印到浏览器控制台

在INLINE_JAVASCRIPT项目中使用JavaScript的 `console.log()` 函数是一种简单而强大的调试工具。它起到类似于Python的 `print()` 函数和变量查看器的作用，这两者在OSWeb中都不可用。例如，你可以在每个试验开始时的INLINE_SCRIPT的准备阶段打印变量 `left_letter` 和 `right_letter` 的值。

要查看这些调试消息，你需要打开浏览器控制台。下面是在Chrome、Firefox和Edge中如何做的方法：

- **Google Chrome：**按Ctrl + Shift + J（Windows / Linux）或Cmd + Option + J（Mac）。
- **Mozilla Firefox：**按Ctrl + Shift + K（Windows / Linux）或Cmd + Option + K（Mac）。
- **Microsoft Edge：**按F12打开开发人员工具，然后选择“控制台”标签。

一旦控制台打开，你就可以在运行实验时监控输出，这样你就可以检查控制台显示的输出是否与实验的实际行为一致。

%--
figure：
 id：FigPrintingOutputOSWeb
 source：printing-output-osweb.png
 caption：JavaScript 的 `console.log()` 函数可以用来向浏览器控制台输出调试消息。
--%

在上面的例子中，显然，应该出现在左边的 `left_letter` 变量所赋予的字母实际上出现在右边，反之亦然。


### 理解错误消息

当你的基于浏览器的实验崩溃时，OSWeb将在浏览器中显示一个错误消息。错误消息通常包括以下组件：

- **错误类型：** 表示一般类别的错误。在下面这个例子中，这是一个 `ReferenceError`。
- **描述：** 提供了触发错误的更具体的解释。在这个情况下，'right_leter is not defined'。
- **来源：** 指定触发错误的项目以及它是在运行阶段还是准备阶段发生的。
- **来源脚本：** 导致错误的JavaScript代码。只有在评估自定义JavaScript时才会显示这些信息，其中包括INLINE_JAVASCRIPT项目，还有条件表达式（例如，运行-如果表达式），以及带有嵌入变量引用的文本。

让我们看一个例子，更好地理解这些组成部分，并学习如何解决一个常见的错误：

%--
figure：
 id：FigOSWebError
 source：osweb-error.png
 caption：一个 `ReferenceError` 表示对不存在的变量或其他不存在的对象的引用。
--%

这是一个 `ReferenceError`，表明实验引用了一个不存在的变量或其他不存在的对象。在这个例子中，错误源于文本`${right_leter}`。任何被大括号包围并且有`$`前缀的东西都被解释为JavaScript表达式，在这种情况下，JavaScript表达式是 `right_leter`——这只是一个变量名。试图评估JavaScript表达式 `right_leter` 触发了一个 `ReferenceError`， 因为 `right_leter` 没有定义。

这太技术了，但用简单的术语来说，这里到底出了什么问题呢？问题出在引用一个不存在的变量： `right_leter`。看看变量名，可能有一个拼写错误：应该是 `right_letter`，后面有两个 't'。

我们应该在哪里纠正这个错误呢？ 错误消息指出错误的来源是名为 *target* 的项目， 这是一个 SKETCHPAD。要解决这个错误，我们需要打开 *target* 并将文本从 '{right_leter}' 修改为 '{right_letter}'。


### 在 INLINE_JAVASCRIPT 项目中使用 `debugger` 语句

JavaScript `debugger`语句是一个强大的调试 OpenSesame/OSWeb实验中的 `INLINE_JAVASCRIPT` 项目的工具。它允许您在代码中插入断点，使浏览器的JavaScript执行在那个点暂停。这使您能检查JavaScript工作区的当前状态。

使用 `debugger` 语句很简单。只需在希望暂停执行的行插入 `debugger` 语句。例如：

```javascript
console.log(`left_letter = ${left_letter}`)
console.log(`right_letter = ${right_letter}`)
debugger // 执行在此处暂停
```

一旦你已经在你的代码中插入了 `debugger` 语句，你需要打开浏览器控制台，如上所述。打开浏览器控制台后，运行你的实验。当JavaScript解释器到达 `debugger` 语句时，它将暂停执行，并且开发者工具将切换到"Sources" (Chrome/Edge) 或 "Debugger" (Firefox) 选项卡，高亮显示断点行。

%--
figure:
 id: FigJavaScriptDebugger
 source: javascript-debugger.png
 caption: 当JavaScript解释器到达 `debugger` 语句时，它将暂停执行，并允许您检查JavaScript工作区。`debugger` 语句只在打开浏览器控制台时才有效。
--%

当执行暂停时，您可以查看变量值，逐行查看代码，并查看调用堆栈以更好地理解程序在断点处的状态。

记得在调试完成后删除或注释掉 `debugger` 语句，因为它们会干扰实验的正常运行。

##处理实验进程已死亡错误

偶尔，您可能在实验中遇到`ExperimentProcessDied`错误。

%--
figure:
 id: FigExperimentProcessDied
 source: experiment-process-died.png
 caption: 一般来说，`ExperimentProcessDied`错误表示的是底层 Python进程或相关库的问题，而非你的实验代码的问题。
--%

此错误意味着运行实验的Python进程意外终止。它通常不表示您的实验中存在错误，而是暗示OpenSesame使用的底层库中存在问题，甚至可能是Python本身的错误。

确定此错误的确切原因可能具有挑战性，修复它可能更为困难。然而，有几种可以尝试的解决办法来减少这个问题：

- **更改后端：**在 'Run Experiment' 的实验属性下选择不同的后端。这可能解决问题，因为不同的后端使用不同的底层库集。
- **更新 OpenSesame 和相关包：**定期更新 OpenSesame 和所有相关的包可以潜在的解决此问题，因为新版本经常修复错误。