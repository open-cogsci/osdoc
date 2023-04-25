title: 变量
hash: 87f8069d56f529c53b29b95555f8d096d7d742f9b355ff6689a0d6e7cb2b8654
locale: zh
language: Chinese

[TOC]

## OpenSesame中的实验变量是什么？

OpenSesame中的实验变量是指这些变量：

- 您可以在用户界面中使用' {variable_name}'语法引用。
- 在Python INLINE_SCRIPT中作为全局变量可用。
- 在JavaScript INLINE_JAVASCRIPT中作为全局变量可用。
- 包含以下内容：
	- 您在LOOP项目中定义的变量。
	- 您收集的响应。
	- 实验的各种属性。
	- 等

## 变量检查器

变量检查器（`Ctrl+I`）提供了可用变量的概述（％FigVariableInspector）。实验未运行时，此概述基于对实验过程中将提供哪些变量的最佳猜测。但是，实验运行时，变量检查器显示变量及其值的实时概述。这对于调试您的实验非常有用。

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: 变量检查器提供了OpenSesame已知的所有变量的概述。
--%

## 定义变量

定义变量的最简单方法是通过LOOP项目。例如，％FigLoop展示了如何定义名为`gaze_cue`的变量。在此示例中，当`gaze_cue`为'left'时，调用*trial_sequence*项目四次，当'gaze_cue'为'right'时，再调用四次。

%--
figure:
 id: FigLoop
 source: defining-variables-in-a-loop.png
 caption: 使用LOOP表定义自变量的最常见方法。
--%

## 内置变量

以下变量始终可用：

### 实验变量

|变量名           |说明|
|-----------------|-----------|
| `title`         |实验的标题|
| `description`     |实验的描述|
| `foreground`    |默认前景色。例如，'white' 或 '#FFFFFF'.|
| `background`    |默认背景色。例如，'black' 或 '#000000'.|
| `height`        |显示分辨率的高度部分。例如，' 768'|
| `width`         |显示分辨率的宽度部分。例如，' 1024'|
| `subject_nr`    |实验开始时询问的受试编号。|
| `subject_parity`|如果`subject_nr`为奇数，则为'odd'；如果`subject_nr`为偶数，则为'even'。适用于计数平衡。|
| `experiment_path`|当前实验的文件夹，不包括实验文件名本身。如果实验未保存，则值为`None`。|
| `pool_folder`   |文件池内容已解压到的文件夹。通常是临时文件夹。|
| `logfile`       |日志文件路径。|

### 项目变量

还有一些变量可用于跟踪实验中的所有项目。

|变量名           |说明|
|-----------------|-----------|
| `time_[item_name]`|包含上次执行该项目的时间戳。对于SKETCHPAD项目，可用于验证显示呈现的时序。|
| `count_[item_name]`|等于minus一次（换句话说，从0开始）调用项目的次数。这可以用作试验或块计数器。|

### 响应变量

当您使用标准响应项目，例如KEYBOARD_RESPONSE和MOUSE_RESPONSE时，系统会根据参与者的响应设置一些变量。

|变量名                      |描述|
|---------------------------|----|
|`response`                  | 包含已给出的最后一个回答。 |
|`response_[item_name]`      | 包含某个特定回答项目的最后一个回答。如果有多个应答回答项目，这就很有用。|
|`response_time`             | 包含从回答间隔开始到最后一个回答之间的毫秒数间隔。|
|`response_time_[item_name]` | 包含特定回答项目的回答时间。|
|`correct`                   | 如果最后的`response`与变量`correct_response`匹配，则设置为“1”，如果不匹配，则设置为“0”，如果未设置变量`correct_response`，则设置为“未定义”。 |
|`correct_[item_name]`       | 与`correct`相同，但用于特定的回答项目。|

### 反馈变量

反馈变量维护准确性和响应时间的移动平均值。

|变量名                      |描述|
|---------------------------|----|
|`average_response_time`     | 平均响应时间。此变量可用于向参与者提供反馈。|
|`avg_rt`                    | `average_response_time`的同义词 |
|`accuracy`                  | 正确回答的平均百分比。此变量可用于向参与者提供反馈。|
|`acc`                       | `accuracy`的同义词|

## 在用户界面中使用变量

在用户界面中看到的任何值都可以使用‘{变量名}’符号替换为变量。例如，如果您在LOOP项目中定义了一个变量`soa`，则可以将此变量用于草图板的持续时间，如%FigSketchpad所示。

%--
figure:
 id: FigSketchpad
 source: variable-duration.png
 caption: 持续时间‘{soa}’表示SKETCHPAD的持续时间取决于变量`soa`。
--%

这在整个用户界面中都有用。 例如，如果您定义了一个变量`my_freq`，则可以将此变量用作SYNTH项目中的频率，如%FigSynth所示。

%--
figure:
 id: FigSynth
 source: variable-frequency.png
 caption: 频率‘{my_freq}’表示SYNTH的频率取决于变量`my_freq`。
--%

有时，用户界面不会让您输入任意文本。例如，SKETCHPAD的元素是以视觉方式显示的，您无法直接将X坐标更改为变量。但是，您可以点击右上角的*选择视图→查看脚本* 按钮，并直接编辑脚本。

例如，您可以将固定点的位置从中心更改为：

```text
draw fixdot x=0 y=0
```

…到由变量`xpos`和`ypos`定义的位置：

```text
draw fixdot x={xpos} y={ypos}
```

## 在用户界面中使用Python表达式

在使用`{my_var}`符号引用变量时，您实际上在使用所谓的[f-string](https://peps.python.org/pep-0498/)，这是一种在文本字符串中嵌入Python代码的方法。 您还可以使用f-strings来评估任意Python代码。 例如，您可以将变量`width`和`height`相乘，并将结果包含在SKETCHPAD中，如下所示：

%--
figure:
 id: FigFString
 source: fstrings.png
 caption: 您可以使用f-strings嵌入Python表达式。
--%

f-strings是Python代码，因此仅在桌面上受支持，但请参阅下面的浏览器实验中的JavaScript替代方案。

## 在用户界面中使用JavaScript表达式

在使用OSWeb时，花括号之间包含的表达式会被解释为[模板文字](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)。 这与Python中的f-strings非常相似，重要的区别在于它使用JavaScript。

在普通的JavaScript中，模板文字内的表达式以 `$` 作为前缀，如下所示：`${expression}`。在OpenSesame中允许但不必使用此前缀：为了提高浏览器和桌面实验之间的兼容性，会自动添加前缀。在大多数情况下，如下图所示，桌面上的Python f-string和浏览器中的JavaScript模板文字可以使用完全相同的表达式。

%--
figure:
 id: FigTempalteLiteral
 source: template-literals.png
 caption: 你可以使用模板文字嵌入JavaScript表达式。
--%

## 在Python中使用变量

在INLINE_SCRIPT中，实验变量作为全局变量可用。例如，如果你在LOOP中定义了 `example_variable`，那么下面的代码将把 `example_variable` 的值打印到调试窗口：

~~~ .python
print(example_variable)
~~~

您可以将实验变量 `example_variable` 设置为值 'some value'，如下所示：

~~~ .python
example_variable = 'some value'
~~~

## 在JavaScript中使用变量

在INLINE_JAVASCRIPT中，实验变量作为全局变量可用。例如，如果你在一个LOOP中定义了 `example_variable`，那么下面的代码将把 `example_variable` 的值打印到浏览器控制台：

```js
console.log(example_variable)
```

您可以将实验变量 `example_variable` 设置为值 'some value'，如下所示：

```js
example_variable = 'some value'
```

## 使用条件（"if"）语句

条件语句，或 "if 语句"，提供了一种方法，用于指示只在特定情况下，如某个变量具有特定值时发生。条件语句是常规的Python表达式。

在OpenSesame中使用最常见的if-语句是SEQUENCE的 run-if 语句，它允许您指定执行特定元素的条件。如果打开一个SEQUENCE项目，会看到序列中的每个项目都有一个 'Run if ...'' 选项。默认值为 'always'，表示项目始终运行；但也可以在此输入条件。例如，如果你想在正确的响应后展示绿色的注视点，错误的响应后展示红色的注视点，可以创建一个如下的SEQUENCE（这利用了KEYBOARD_RESPONSE项目自动设置 `correct` 变量的事实，如上所述），如 %FigRunIf 所示。

*重要提示：* Run-if 语句仅适用于项目的 Run 阶段。Prepare 阶段始终被执行。另请参见[此页面](%link:prepare-run%/)。

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: |
  "Run if" 语句可用于指示SEQUENCE中的某些项目只在特定条件下执行。
--%

您还可以使用更复杂数的条件。让我们看几个例子：

```python
correct == 1 and response_time > 2000
correct != 1 or response_time > max_response_time or response_time < min_response_time
```

同样的原理应用于SKETCHPAD项目中的 'Show if' 字段。例如，如果您只想在变量 `quadrant` 设置为 'upper right' 时绘制指向右上的箭头，只需在 'Show if...' 字段中输入正确的条件并绘制箭头，如 %FigShowIf 所示。请确保在设置条件后绘制箭头。

%--
figure:
 id: FigShowIf
 source: show-if.png
 caption: "'Show if' 语句可用于指示SKETCHPAD或FEEDBACK项目中的某些元素仅在特定条件下显示。"
--%

重要提示：条件语句评估的时刻可能会影响实验的运行方式。这与OpenSesame所采用的 prepare-run 策略有关，详细解释可见：

- %link:prepare-run%