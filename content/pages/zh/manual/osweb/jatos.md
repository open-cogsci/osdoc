title: JATOS
hash: b885bbb21d5bc5d8ffa13b6adf7ce306d93ad1253011bddf7529f22af3b5eb59
locale: zh
language: Chinese

[TOC]

## JATOS简介

[JATOS](https://www.jatos.org/) 是一个用于管理在线实验的系统。它允许您创建实验者的账户，上传实验，并生成可以分发给参与者的链接。OpenSesame与JATOS紧密集成。

要访问JATOS服务器，您有三个主要选择：

- 在[MindProbe](https://mindprobe.eu/)（一个由ESCoP和OpenSesame赞助的公开JATOS服务器）上申请一个免费账户。
- 使用您所在机构提供的JATOS服务器。
- 下载JATOS并将其安装到您自己的服务器上。

## 将OpenSesame与JATOS/MindProbe连接起来

OpenSesame需要一个API令牌来访问您在JATOS服务器（如MindProbe）上的账户。按照以下步骤生成API令牌：

1. **登录JATOS。**
2. **打开您的用户资料**，点击位于页面右上角的您的名字。
3. **创建一个API令牌**，点击'API令牌'查看所有当前的令牌，然后点击'新建令牌'。
4. **为您的令牌指定一个名字**。此名字是一个描述符，表明其预定的用途，如'OpenSesame集成'。
5. **为您的令牌设置一个过期时间**。令牌默认在30天后过期，需要您每个月生成一个新的令牌。您可以选择'无过期日期'以方便使用，但请注意这会降低安全性。如果有人获得了一个不会过期的令牌，他们可以无限期地使用它，或者直到您撤销这个令牌。

%--
figure:
 id: FigAPIToken
 source: api-token.png
 caption: API tokens can be generated within your JATOS user profile.
--%

注意：API令牌总是以`jap_`开始，后面跟着一系列的字符和数字。请保管好您的令牌！

一旦您有了API令牌，就打开OpenSesame中的OSWeb和JATOS控制面板。将您的API令牌输入到相应的字段中，并在必要时调整JATOS服务器的URL。

%--
figure:
 id: FigJATOSControlPanel
 source: jatos-control-panel.png
 caption: Specify the JATOS server and your API token in the OSWeb and JATOS control panel.
--%



## 发布和下载实验到JATOS/MindProbe

成功将OpenSesame连接到JATOS后，如上所述，您就可以将实验发布到JATOS。要做到这一点，从文件菜单中选择'发布到JATOS/MindProbe'选项。在初次发布时，您的实验将被分配一个唯一标识符(UUID)，该UUID将其链接到JATOS上的一个研究中。

然后，您可以访问您的JATOS服务器，并注意到新发布的实验已经被添加到您的研究列表中。

从那时开始，每次发布实验，现有的JATOS研究都会根据新版本进行更新。如果您希望将实验作为一个完全新的研究发布到JATOS，您需要通过OSWeb和JATOS控制面板重置JATOS的UUID。

要从JATOS下载实验，请从文件菜单中选择'从JATOS/MindProbe打开'选项。请注意，这个功能只有在相应的JATOS研究与OSWeb 2兼容时才适用。