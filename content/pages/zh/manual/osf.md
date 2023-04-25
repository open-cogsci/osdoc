title: 与开放科学框架的整合
hash: b86c05caa254209c5f4d161cd5c5a9daffef60ec5e5d5fca41a7aec00643d1f7
locale: zh
language: Chinese

[TOC]

## 关于

OpenScienceFramework 扩展将 OpenSesame 与 [Open Science Framework](https://osf.io) (OSF) 连接起来，OSF 是一个用于共享、连接和简化科学工作流程的网络平台。要使用此扩展，[您需要一个 OSF 账户](https://osf.io/login/?sign_up=True)。

使用 OpenScienceFramework 扩展，您可以：

- 自动将您的实验保存到 OSF
- 自动将数据上传到 OSF
- 从 OSF 打开实验
- 通过 OSF 向其他研究人员共享您的实验和数据

## 登录 OSF

要登录 OSF：

- 在 <https://osf.io> 上创建一个帐户。（您不能从 OpenSesame 内创建帐户。）
- 在 OpenSesame 中，点击主工具栏上的登录按钮，并输入您的凭据。
- 登录后，您可以通过点击登录按钮所在处的您的名字，然后选择 *显示资源管理器* 来打开 OSF 资源管理器。资源管理器将显示您的所有 OSF 项目，以及与您的项目关联的所有存储库/云服务。

## 将实验链接到 OSF

如果您将实验链接到 OSF，则每次在 OpenSesame 中保存实验时，新版本也将上传到 OSF。

要链接实验：

- 在您的计算机上保存实验。
- 打开 OSF 资源管理器，选择您希望在 OSF 上存储实验的文件夹或存储库。右键单击此文件夹，然后选择 *将实验同步到此文件夹*。实验链接的 OSF 节点将显示在资源管理器顶部。
- 实验随后将上传到选定的位置。
- 如果您勾选 *始终在保存时上传实验*，每次保存时将自动将新版本保存到 OSF；如果您不启用此选项，每次都会询问您是否要执行此操作。

要取消链接实验：

- 打开 OSF 资源管理器，然后点击 *实验链接到* 链接旁边的 *取消链接* 按钮。

## 将数据链接到 OSF

如果您将数据链接到 OSF，则每次收集数据后（通常在每个实验会话之后），这些数据也将上传到 OSF。

要将数据链接到 OSF：

- 在您的计算机上保存实验。
- 打开 OSF 资源管理器，右键单击您希望将数据上传到的文件夹，然后选择 *将数据同步到此文件夹*。数据链接的 OSF 节点将显示在资源管理器顶部。
- 如果您勾选 *始终上传收集到的数据*，在收集后，数据文件将自动保存到 OSF；如果您不启用此选项，每次都会询问您是否要执行此操作。

要从 OSF 取消链接数据：

- 打开 OSF 资源管理器，然后点击 *数据存储到* 链接旁边的 *取消链接* 按钮。

## 打开存储在 OSF 上的实验

要从 OSF 打开实验：

- 打开 OSF 资源管理器，找到实验。
- 在实验上右键单击并选择 *打开实验*。
- 在您的计算机上保存实验。

## 处理版本不匹配的问题

如果您在计算机上打开与 OSF 上的版本不同的链接到 OSF 的实验，系统会询问您要执行什么操作：

- 使用您计算机上的版本；或
- 使用 OSF 上的版本。如果您选择使用 OSF 上的版本，它将被下载并覆盖您计算机上的实验。

## 安装 OpenScienceFramework 扩展

OpenScienceFramework 扩展在 OpenSesame 的 Windows 软件包中默认已安装。如果扩展未安装，您可以按照以下方法安装：

从 PyPi 安装：

~~~
pip install opensesame-extension-osf
~~~

在 Anaconda 环境中安装

~~~
conda install -c cogsci opensesame-extension-osf
~~~

扩展的源代码可在 GitHub 上找到：

- <https://github.com/dschreij/opensesame-extension-osf>

以及扩展使用的 `python-qosf` 模块：

- <https://github.com/dschreij/python-qosf>