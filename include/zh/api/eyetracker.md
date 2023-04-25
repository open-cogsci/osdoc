<div class="ClassDoc YAMLDoc" id="eyetracker" markdown="1">

# 类 __eyetracker__

一个通用的Python库，用于眼动追踪。

<div class="FunctionDoc YAMLDoc" id="eyetracker-calibrate" markdown="1">

## 函数 __eyetracker\.calibrate__\(\)

校准眼动追踪系统。此函数的实际行为取决于眼动追踪器的类型，并在下面进行了描述。

__EyeLink:__

此功能将激活摄像机设置屏幕，允许您调整摄像机并执行校准/验证程序。按下'q'将退出设置程序。按下'escape'，将首先触发确认对话框，然后在确认后引发异常。

__EyeTribe:__

激活一个简单的校准程序。

__返回值：__

如果校准成功，则返回True；如果校准失败，则返回False；此外，校准日志将添加到日志文件中，还将更新一些属性（例如检测算法的阈值）。

- 类型：布尔值

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-close" markdown="1">

## 函数 __eyetracker\.close__\(\)

整净地关闭到追踪器的连接。保存数据并将`self.connected`设置为False。

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-connected" markdown="1">

## 函数 __eyetracker\.connected__\(\)

检查跟踪器是否已连接。

__返回值：__

如果已建立连接，则返回True；如果未建立连接，则返回False；将`self.connected`设置为相同的值。

- 类型：布尔值

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_calibration_target" markdown="1">

## 函数 __eyetracker\.draw\_calibration\_target__\(x, y\)

绘制一个校准目标。

__参数：__

- `x` -- X坐标
	- 类型：整数
- `y` -- Y坐标
	- 类型：整数

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_drift_correction_target" markdown="1">

## 函数 __eyetracker\.draw\_drift\_correction\_target__\(x, y\)

绘制一个漂移校正目标。

__参数：__

- `x` -- X坐标
	- 类型：整数
- `y` -- Y坐标
	- 类型：整数

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-drift_correction" markdown="1">

## 函数 __eyetracker\.drift\_correction__\(pos=None, fix\_triggered=False\)

执行漂移校正程序。此函数在眼动追踪器类型上的具体行为在下面进行了描述。因为漂移校正可能会失败，所以您通常会在循环中调用此函数。

__EyeLink:__

在漂移校正过程中按'q'将激活摄像机设置屏幕。从那里，再次按下'q'将立即导致漂移校正失败。按下'escape'将有选择中断实验的选项，在这种情况下会引发异常。

__关键字参数:__

- `pos` -- 固定点的(x, y)位置，或者为None表示中心固定。
	- 类型：元组，NoneType
	- 默认值：None
- `fix_triggered` -- 布尔值，表示漂移检查是否应根据凝视位置（True）或空格（False）执行。
	- 类型：布尔值
	- 默认值：False

__返回值：__

布尔值，表示漂移检查是否正常（True）或异常（False）。

- 类型：布尔值

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-fix_triggered_drift_correction" markdown="1">

## 函数 __eyetracker\.fix\_triggered\_drift\_correction__\(pos=None, min\_samples=30, max\_dev=60, reset\_threshold=10\)

通过收集一定数量的样本并计算与固定位置的平均距离，执行固定位置触发的漂移校正。

__关键字参数：__

- `pos` -- 固定点的(x, y)位置，或者为None表示中心固定。
	- 类型：元组，NoneType
	- 默认值：None
- `min_samples` -- 计算平均偏差所需的最小样本数量。
	- 类型：整数
	- 默认值：30
- `max_dev` -- 固定的最大像素偏差。
	- 类型：整数
	- 默认值：60
- `reset_threshold` -- 如果两个连续样本之间的水平或垂直像素距离大于此阈值，则重置样本收集。
	- 类型：整数
	- 默认值：10

__返回：__

表示漂移检查是否正常（True）或不正常（False）的布尔值。

- 类型：bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-get_eyetracker_clock_async" markdown="1">

## 函数 __eyetracker\.get\_eyetracker\_clock\_async__\(\)

返回跟踪器时间和PyGaze时间之间的差值，可以用于同步时间

__返回：__

眼动跟踪器时间和PyGaze时间之间的差值。

- 类型：int、float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log" markdown="1">

## 函数 __eyetracker\.log__\(msg\)

将消息写入日志文件。

__参数：__

- `msg` -- 一个消息。
	- 类型：str、unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log_var" markdown="1">

## 函数 __eyetracker\.log\_var__\(var, val\)

将变量的名称和值写入日志文件

__参数：__

- `var` -- 变量名。
	- 类型：str、unicode
- `val` -- 变量值

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-pupil_size" markdown="1">

## 函数 __eyetracker\.pupil\_size__\(\)

返回最新的瞳孔大小样本；大小可能是以瞳孔直径或瞳孔面积来衡量的，这取决于您的设置（请注意，瞳孔大小大多以任意单位给出）。

__返回：__

返回当前正在跟踪的眼睛（由self.eye_used指定）的瞳孔大小，如果无法获取数据，则返回-1。

- 类型：int、float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-sample" markdown="1">

## 函数 __eyetracker\.sample__\(\)

返回最新可用的凝视位置。

__返回：__

一个（x，y）元组，错误时返回（-1，-1）。

- 类型：元组

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-send_command" markdown="1">

## 函数 __eyetracker\.send\_command__\(cmd\)

直接向眼动追踪器发送命令（并非所有品牌都支持；如果您的设置不支持直接命令，可能会产生警告消息）。

__参数：__

- `cmd` -- 要发送到眼动追踪器的命令。
	- 类型：str、unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_detection_type" markdown="1">

## 函数 __eyetracker\.set\_detection\_type__\(eventdetection\)

将事件检测类型设置为PyGaze算法或原生算法（仅在可用的情况下：如果没有提供本地函数，检测类型将默认为PyGaze）

__参数：__

- `eventdetection` -- 一个字符串，表示应该采用哪种检测类型：'pygaze'表示PyGaze事件检测算法，'native'表示制造商算法（仅在可用的情况下；如果没有本地事件检测可用，将默认为'pygaze'）
	- 类型：str、unicode

__返回：__

间跃、固定和眨眼的检测类型的元组，例如：('pygaze','native','native')，当传递的是'native'，原生检测对于间跃检测不可用。

- 类型：元组

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_calibration_target_func" markdown="1">

## 函数 __eyetracker\.set\_draw\_calibration\_target\_func__\(func\)

指定一个自定义函数来绘制校准目标。这将覆盖默认的[draw_calibration_target]。

__参数：__

- `func` -- 用于绘制校准目标的函数。此函数应接受两个参数，用于目标的x和y坐标。
	- 类型：函数

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_drift_correction_target_func" markdown="1">

## 函数 __eyetracker\.set\_draw\_drift\_correction\_target\_func__\(func\)

指定一个自定义函数来绘制漂移校正目标。这将覆盖默认的[draw_drift_correction_target]。

__参数：__

- `func` -- 用于绘制漂移校正目标的函数。此函数应接受两个参数，用于目标的x和y坐标。
	- 类型：函数

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_eye_used" markdown="1">

## 函数 __eyetracker.set_eye_used__()

记录`eye_used`变量，基于指定的眼睛（如果两只眼睛都被追踪，使用左眼）。不返回任何内容。

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-start_recording" markdown="1">

## 函数 __eyetracker.start_recording__()

开始记录。当记录成功开始时，将`self.recording`设置为`True`。

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-status_msg" markdown="1">

## 函数 __eyetracker.status_msg__(msg)

将状态消息发送到眼动仪，该消息将显示在跟踪器的GUI中（仅适用于EyeLink设置）。

__参数：__

- `msg` -- 一个要在实验者PC上显示的字符串，
例如："current trial: %d" % trialnr.
	- 类型：str，unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-stop_recording" markdown="1">

## 函数 __eyetracker.stop_recording__()

停止记录。当记录成功停止时，将`self.recording`设置为`False`。

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_end" markdown="1">

## 函数 __eyetracker.wait_for_blink_end__()

等待眨眼结束并返回眨眼结束时间。
如果EVENTDETECTION设置为'pygaze'，则根据Dalmaijer等人（2013）进行检测；如果EVENTDETECTION设置为'native'，则使用本地检测功能（注意：并非每个系统都具有本地功能；如果没有可用的'native'，则退回到'pygaze'！）

__返回：__

从实验开始时间算起的毫秒数，作为眨眼结束时间。

- 类型：int，float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_start" markdown="1">

## 函数 __eyetracker.wait_for_blink_start__()

等待眨眼开始并返回眨眼开始时间。
如果EVENTDETECTION设置为'pygaze'，则根据Dalmaijer等人（2013）进行检测；如果EVENTDETECTION设置为'native'，则使用本地检测功能（注意：并非每个系统都具有本地功能；如果没有可用的'native'，则退回到'pygaze'！）

__返回：__

从实验开始时间算起的毫秒数，作为眨眼开始时间

- 类型：int，float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_event" markdown="1">

## 函数 __eyetracker.wait_for_event__(event)

等待一个事件。

__参数__:

- `event` -- 一个整数事件代码，以下之一：

- 3 = STARTBLINK
- 4 = ENDBLINK
- 5 = STARTSACC
- 6 = ENDSACC
- 7 = STARTFIX
- 8 = ENDFIX
	- 类型：int

__返回：__

根据指定的事件，调用一个`self.wait_for_*`方法；返回相应方法的返回值。

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_end" markdown="1">

## 函数 __eyetracker.wait_for_fixation_end__()

当注视结束时，返回时间和凝视位置；
函数假设当检测到与初始注视位置的偏离大于自身.pxfixtresh时，“注视”已经结束（self.pxfixtresh在self.calibration中创建，基于self.fixtresh，该属性在self .__init__中定义）。
如果EVENTDETECTION设置为'pygaze'，则根据Dalmaijer等人（2013）进行检测；如果EVENTDETECTION设置为'native'，则使用本地检测功能（注意：并非每个系统都具有本地功能；如果没有可用的'native'，则退回到'pygaze'！）

__返回：__

一个`time, gazepos`元组。时间是毫秒数（从expstart开始），gazepos是一个（x，y）凝视位置元组，表示从该位置开始注视。

- 类型：tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_start" markdown="1">

## 函数 __eyetracker.wait_for_fixation_start__()



返回定位开始的时间和位置；
该函数假设当凝视位置保持相对稳定（即，当最偏离的样本在 self.pxfixtresh 内）连续五个样本时开始“注视”（self.pxfixtresh 在 self.calibration 中创建，基于 self.fixtresh ，在 self.__init__ 中定义的属性）。
如果 EVENTDETECTION 设置为'pygaze'，则基于 Dalmaijer 等人（2013）进行检测，或者如果 EVENTDETECTION 设置为'native'，则使用本机检测功能（注意：并非每个系统都具有本机功能；如果'native' 不可用，将回退到'pygaze'！）

__返回：__

一个`time, gazepos`元组。时间从 expstart 开始以毫秒为单位，gazepos 是从该位置启动定位的（x,y）凝视位置元组。

- 类型：元组

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_end" markdown="1">

## 函数 __eyetracker\.wait\_for\_saccade\_end__\(\)

在眼跳结束时返回结束时间，开始和结束位置；如果 EVENTDETECTION 设置为'pygaze'，则基于 Dalmaijer 等人(2013)在线眼跳检测算法，或者如果 EVENTDETECTION 设置为'native'，则使用本机检测功能（注意：并非每个系统都具有本机功能；如果'native' 不可用，将回退到'pygaze'！）

__返回：__

一个 `endtime, startpos, endpos` 元组。 Endtime 以毫秒为单位（从 expbegintime 开始）； startpos 和 endpos 是（x,y）凝视位置元组。

- 类型：元组

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_start" markdown="1">

## 函数 __eyetracker\.wait\_for\_saccade\_start__\(\)

在眼跳开始时返回开始时间和起始位置；如果 EVENTDETECTION 设置为'pygaze'，则基于 Dalmaijer 等人(2013)在线眼跳检测算法，或者如果 EVENTDETECTION 设置为'native'，则使用本机检测功能（注意：并非每个系统都具有本机功能；如果'native' 不可用，将回退到'pygaze'！）

__返回：__

一个 `endtime, startpos` 元组。 Endtime 以毫秒为单位（从 expbegintime 开始）； startpos 是一个（x,y）凝视位置元组。

- 类型：元组

</div>

</div>