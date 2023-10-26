title: 并口 (EEG 触发器)
reviewed: false
hash: 173d67c1a3fbe4fb17b8a936fe30584d71443f518bf86bd65c9ad6da21c4e229
locale: zh
language: Chinese

在EEG / ERP研究中，通常会发送触发信号来标记重要事件（例如，试验的开始，特定刺激的呈现等）的时间戳。触发器通常是通过并行端口发送到EEG设备的字节。

[TOC]

## 使用 `parallel_port_trigger` 插件

Parallel_port_trigger 是一个第三方插件，不由 OpenSesame 团队维护。
{: .page-notification}

这是一个 OpenSesame 插件，用于通过并行端口向数据采集系统发送刺激同步触发信号。

- <https://github.com/dev-jam/opensesame-plugin-parallel_port_trigger/>

您可以从 PyPi 安装 `parallel_port_trigger` 插件：

```
pip install pip install opensesame-plugin-parallel-port-trigger
```


## 在Python 内联脚本中使用 `dportio.dll`（仅限Windows）

除了使用 `parallel_port_trigger` 插件，还可以通过在Python内联脚本中使用 `dlportio.dll` 来发送触发器。这种方法仅适用于Windows。为此，首先在实验的开始处添加一个INLINE_SCRIPT，并在准备阶段运行以下代码：

~~~ .python
try:
	from ctypes import windll
	global io
	io = windll.dlportio # 需要 dlportio.dll ！！！
except:
	print('并行端口无法打开')
~~~

这将加载 `dlportio.dll` 为一种名为 `io` 的全局对象。请注意，失败并不会导致实验崩溃，因此确保检查调试窗口以查看错误消息！

现在，在实验的任何地方使用以下代码在 INLINE_SCRIPT 中发送一个触发信号：

~~~ .python
global io
trigger = 1
port = 0x378
try:
	io.DlPortWritePortUchar(port, trigger)
except:
	print('发送触发信号失败！')
~~~

请注意，这将触发器1发送到端口0x378（=888）。根据您的设置更改这些值。

## 获取并行端口的访问权限

### Linux

在 Linux 中，我们使用 `parport_pc` 模块（在 Debian Wheezy 中测试过），我们需要提供相应的权限。我们可以通过执行以下命令来实现：

	sudo rmmod lp
	sudo rmmod parport_pc
	sudo modprobe parport_pc
	sudo adduser [user] lp

这里的 `[user]` 应替换为您的用户名。然后，注销并重新登录，您就可以开始了！

### Windows XP 和 Windows Vista（32 位）

1. 从[此处][win32-dll]下载32位的 DLPortIO 驱动程序，并解压缩zip存档。
2. 转到 `DriverLINX/drivers` 文件夹，并复制 `dlportio.dll` 和 `dlportio.sys` 到 `install` 文件夹。这是包含 `install.exe` 的文件夹。然后运行 `install.exe`
3. 您需要将 `dlportio.dll` 复制到 OpenSesame 文件夹（也就是包含 `opensesame.exe` 的文件夹）。

### Windows 7（32位和64位）

1. 下载32位或64位的DLPortIO驱动程序[这里][win7-dll]，并解压缩zip存档。
2. 由于Windows 7具有加强的安全系统（至少与XP相比），因此无法简单地安装DLPortIO驱动程序。这不起作用，因为Windows 7将阻止安装未经正式签名（由Microsoft签名）的驱动程序的所有尝试。对于普通用户的安全性很好，但对我们来说不好。要绕过此限制，必须使用一个名为“数字签名强制执行覆盖器”（DSEO）的小助手程序，可以在[这里][dseo]下载（当然还有其他可能的方法可以执行此操作， 但是这个程序在DLPortIO的`readme.txt`中被提及，不需要深入了解MS Windows 7体系结构专用功能）。
3. 以管理员权限启动DSEO（右键单击`dseo13b.exe`，选择“以管理员身份运行”）。现在会弹出DSEO窗口。 它仅列出了要运行的选项列表。
4. 选择“签名驱动程序/ sys文件”选项，然后按确定。 现在将出现另一个窗口，您需要在其中输入`DLPortIO.sys`文件的绝对路径（仅此文件，而非dll！）。 如果存在路径中的空格，请记住转义空格（别问我这花了多长时间），否则将找不到您的文件。 按确定将对sys文件进行签名。
5. 回到DSEO列表中，选择“启用测试模式”并按确定。然后选择“退出”并重新启动计算机。 Windows 7错误地抱怨DSEO可能未正确安装-只需点击“是，软件已正确安装”。
6. 启动完成后，你会看到“Windows 7测试模式build ＃number＃”字样显示在开始栏时钟上方的桌面上。这是必要的。您必须处于测试模式才能运行这个非官方签名的驱动程序。
7. 用管理员权限运行`DLPortIO_install.bat`（在Windows资源管理器中，右键单击该文件，...）。 如果Windows警告您更改注册表，请选择“是”。
8. 重新启动。
9. 将`DLPortIO.dll`复制到Opensesame文件夹，即包含`opensesame.exe`的文件夹中。

来源：[Absurd 发表的论坛帖子][post-3]

## 建议

- 从“零”触发开始实验，以确保所有引脚都设置为零。
- 建议使用[psycho]或[xpyriment]后端而不是[legacy]后端（使用PyGame）进行时间关键的实验。这是因为[psycho]和[xpyriment]在返回时间戳时会考虑显示器的刷新速率，而[legacy]则不会。有关更多信息，请参阅[miscellaneous/timing]。
- 在呈现刺激物之后（而不是之前）立即发送触发代码（假设您要标记的是刺激物的开始）。这样做可确保时间戳尽可能准确，且不会因显示器刷新率而受到随机抖动。 [来源：lvanderlinden][post-2]

## 故障排除

论坛中有很多相关主题讨论了触发相关问题（并且大多数都已解决！）。

- 关于幽灵触发的帖子，即EEG设备神秘地记录到的不需要的触发：[链接][post-2]
- 关于DLPortIO在Windows 7上详细安装说明的帖子（[来源：absurd][post-3]）。

请随时在论坛上发布问题，或告知我们您的经验（无论好坏）。

[win32-dll]: http://files.cogsci.nl/misc/dlportio.zip
[win7-dll]: http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE
[dseo]: http://www.ngohq.com/home.php?page=dseo
[post-2]: http://forum.cogsci.nl/index.php?p=/discussion/comment/780#Comment_780
[post-3]: http://forum.cogsci.nl/index.php?p=/discussion/comment/745#Comment_745
[miscellaneous/timing]: /miscellaneous/timing
[legacy]: /backends/legacy
[xpyriment]: /backends/xpyriment
[psycho]: /backends/psycho