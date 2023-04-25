title: 按钮盒
hash: 0bc151c594d9ecc7e386d138f7aa3b43b072aee2019b7106e4c17ae302f91c67
locale: zh
language: Chinese

有许多不同类型的按钮盒，它们的工作方式各不相同。因此，没有单一的OpenSesame项目适用于所有按钮盒。(这与键盘不同，键盘是标准设备，所有键盘都适用于KEYBOARD_RESPONSE项目。)

常见类型的按钮盒：

- 有些按钮盒*模拟按键*。这很简单，因为你可以使用正常的KEYBOARD_RESPONSE项目。
	- %link:manual/response/keyboard%
- 有些按钮盒*模拟一个游戏杆*。这也很简单，因为您可以使用JOYSTICK插件。
	- %link:joystick%
- 有些按钮盒与*串行响应盒*（Serial Response Box，由Psychology Software Tools开发）兼容。这些按钮盒支持SRBOX插件。
	- %link:srbox%
- 有些按钮盒有自己的Python库。在这种情况下，您应该能找到如何在Python中使用按钮盒的示例脚本，即在OpenSesame的INLINE_SCRIPT项目中。