title: 使用界面
hash: 76f98fb7d0797037375f61ab159fef066c3fe407e469e0f97494e76d38e6177e
locale: zh
language: Chinese

OpenSesame 的图形界面非常强大，由多个组件组成（%FigInterface）。

%--
figure:
 id: FigInterface
 source: interface.png
 caption: OpenSesame 用户界面。
--%


[TOC]

## 工具栏和菜单栏

### 菜单栏

菜单栏（%FigMenubar）位于窗口的顶部，或者在某些操作系统中与窗口边框集成。菜单栏包含一般功能，如保存和打开实验、运行实验等。

%--
figure:
 id: FigMenubar
 source: menubar.png
 caption: 菜单栏。
--%

### 主工具栏

主工具栏（%FigMainToolbar）（默认情况下）位于窗口顶部，正下方为菜单栏。主工具栏包含菜单栏中最相关的功能。

%--
figure:
 id: FigMainToolbar
 source: main-toolbar.png
 caption: 主工具栏。
--%

### 项目工具栏

项目工具栏（%FigItemToolbar）（默认情况下）位于窗口左侧。项目工具栏包含所有项目，即所有实验的构建模块。您可以通过将项目从项目工具栏拖动到概览区域，将项目添加到您的实验中。

%--
figure:
 id: FigItemToolbar
 source: item-toolbar.png
 caption: 项目工具栏。
--%

## 标签页区域

标签页区域是窗口的中心部分（%FigTabArea）。标签页区域中显示项目控件、文档、重要消息等。标签页区域可以包含多个标签页，其功能类似于带标签的网络浏览器。

%--
figure:
 id: FigTabArea
 source: tab-area.png
 caption: 标签页区域。
</notranslated>

## 概览区域

概览区域（%FigOverviewArea）（默认情况下）位于窗口左侧，项目工具栏右侧。概览区域以树形结构显示实验的结构。您可以通过在概览区域内将项目从一个位置拖动到另一个位置来重新排序实验中的项目。

- 隐藏/显示的快捷方式：`Ctrl+\`

%--
figure:
 id: FigOverviewArea
 source: overview-area.png
 caption: 概览区域。
</notranslated>

## 文件池

文件池（%FigFilePool）（默认情况下）位于窗口右侧。它提供了与实验捆绑的所有文件的概览。

- 隐藏/显示的快捷方式：`Ctrl+P`

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: 文件池。
--%

## 调试窗口

调试窗口（%FigDebugWindow）（默认情况下）位于窗口底部。它提供了一个 [IPython 解释器](https://ipython.org/)，并在实验运行时用作标准输出。也就是说，如果您使用 Python 的 `print()` 函数，结果将显示在调试窗口中。

- 隐藏/显示的快捷方式：`Ctrl+D`

%--
figure:
 id: FigDebugWindow
 source: debug-window.png
 caption: 调试窗口。
--%

## 变量检查器

变量检查器（%FigVariableInspector）（默认情况下）位于窗口右侧。它提供了您在实验中检测到的所有变量的列表。当您运行实验时，变量检查器还提供了变量及其值的实时概览。

- 隐藏/显示的快捷方式：`Ctrl+I`

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: 变量检查器。
--%

## 键盘快捷键

以下列出的键盘快捷键均为默认值。你可以通过 *菜单 → 工具 → 偏好设置* 来修改许多快捷键。

### 通用快捷键

以下键盘快捷键可在所有地方使用：

- 快速切换器：`Ctrl+Space`
- 命令面板：`Ctrl+Shift+P`
- 新建实验：`Ctrl+N`
- 打开实验：`Ctrl+O`
- 保存实验：`Ctrl+S`
- 另存实验为：`Ctrl+Shift+S`
- 撤销：`Ctrl+Alt+Z`
- 重做：`Ctrl+Alt+Shift+Z`
- 全屏运行实验：`Ctrl+R`
- 窗口模式运行实验：`Ctrl+W`
- 快速运行实验：`Ctrl+Shift+W `
- 在浏览器中测试实验：`Alt+Ctrl+W`
- 显示/隐藏概览区：`Ctrl+\`
- 显示/隐藏调试窗口：`Ctrl+D`
- 显示/隐藏文件池：`Ctrl+P`
- 显示/隐藏变量检查器：`Ctrl+I`
- 聚焦概览区：`Ctrl+1`
- 聚焦标签区：`Ctrl+2`
- 聚焦调试窗口：`Ctrl+3`
- 聚焦文件池：`Ctrl+4`
- 聚焦变量检查器：`Ctrl+5`

### 编辑器快捷键

以下键盘快捷键可在编辑器组件（如INLINE_SCRIPT）中使用：

- （取消）注释选定行：`Ctrl+/`
- 查找文本：`Ctrl+F`
- 替换文本：`Ctrl+H`
- 隐藏查找/替换对话框：`Escape`
- 复制行：`Ctrl+Shift+D `
- 撤销：`Ctrl+Z`
- 重做：`Ctrl+Shift+Z`
- 复制：`Ctrl+C`
- 剪切：`Ctrl+X`
- 粘贴：`Ctrl+V`

### 标签区快捷键

标签区域内可用以下键盘快捷键：

- 下一个标签：`Ctrl+Tab`
- 上一个标签：`Ctrl+Shift+Tab`
- 关闭其他标签：`Ctrl+T`
- 关闭所有标签：`Ctrl+Alt+T`
- 关闭当前标签：`Alt+T`

### 概览区和序列快捷键

概览区域及SEQUENCE项目中可用以下键盘快捷键：

- 上下文菜单：`+`
- 复制项目（未链接）：`Ctrl+C`
- 复制项目（已链接）：`Ctrl+Shift+C`
- 粘贴项目：`Ctrl+V`
- 删除项目：`Del`
- 永久删除项目：`Shift+Del`
- 重命名：`F2`
- 更改run-if语句（如果适用）：`F3`