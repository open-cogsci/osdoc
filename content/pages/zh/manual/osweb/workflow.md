title: 使用 OSWeb 在线运行实验
hash: f0cc1f57958c34a65409a874ee511e03fee4f8ee35bc0bef55d0af11ac74f56e
locale: zh
language: Chinese

[TOC]


## 工作流程

有关工作流程的介绍，请参见:

Mathôt, S., & March, J. (2022). 使用OpenSesame和OSWeb在线进行语言实验。*Language Learning*. doi:10.1111/lang.12509
<br /><small>[相关预备印刷版 (与已出版的手稿不完全相同)](https://doi.org/10.31234/osf.io/wnryc)</small>


### 开发你的实验

首先，你会像平常一样使用OpenSesame桌面应用程序来开发你的实验。在线实验并不具备所有的功能。值得注意的是，你不能使用Python的INLINE_SCRIPT项目，而必须使用JavaScript的INLINE_JAVASCRIPT项目。因此，在开发实验过程中，检查你的实验是否与OSWeb兼容是非常重要的。

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%


### 将你的实验上传到JATOS

一旦你开发好你的实验，你可以将其发布到JATOS。JATOS是一个管理实验的web服务器：它允许你生成可以分发给参与者的链接，它存储已收集的数据。

并不存在单一的JATOS服务器，相反，许多机构都维护着他们自己的JATOS服务器。此外，<https://mindprobe.eu> 是一个由ESCoP和OpenSesame赞助的免费JATOS服务器。

- %link:jatos%


### 收集数据

在你的实验发布到JATOS后，你可以开始收集数据。你可以通过手动向参与者发送链接，比如通过电子邮件来做这一点。或者，你可以使用一种参与者招募平台，如Prolific, Mechanical Turk, 或者 Sona Systems。

- %link:prolific%
- %link:mturk%
- %link:sonasystems%


### 分析数据

一旦数据收集完成，你可以从JATOS下载数据并将其转换成`.xlsx`或`.csv`格式进行进一步分析:

- %link:manual/osweb/data%


## 教程

- %link:tutorials/intermediate-javascript%
- %link:wcst%