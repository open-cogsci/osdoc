title: 使用 OSWeb 在线运行实验
hash: d164c11575309f8213f7683999953e7c4d0eb5adf6c728cb34d716947a673fbf
locale: zh
language: Chinese

[TOC]

## 工作流程

有关工作流程的介绍，请参见:

Mathôt, S., & March, J. (2022). 使用OpenSesame和OSWeb在线进行语言实验。 *Language Learning*. doi:10.1111/lang.12509
<br /><small>[相关预印本（与已发表稿件不完全相同）](https://doi.org/10.31234/osf.io/wnryc)</small>

### 开发实验

首先，像通常使用OpenSesame桌面应用程序一样来开发你的实验。在线实验中并非所有功能都可用。尤其是，你不能使用Python INLINE_SCRIPT 项目，而是必须使用JavaScript INLINE_JAVASCRIPT项目。在实验开发过程中，检查你的实验是否与OSWeb兼容非常重要。

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%
- %link:manual/osweb/questionnaires%

### 将实验上传至JATOS

一旦开发完实验，你可以从OpenSesame导出实验并上传至JATOS。JATOS是一个管理实验的Web服务器：它允许你生成可以向参与者分发的链接，并储存已收集的数据。

并没有一个唯一的JATOS服务器。相反，许多机构维护着自己的JATOS服务器。此外，由ESCoP和OpenSesame赞助的<https://mindprobe.eu>是一个免费的JATOS服务器。

- %link:jatos%

### 收集数据

将实验上传至JATOS后，你可以开始收集数据。你可以通过向参与者手动发送链接的方式进行数据收集，例如通过电子邮件。或者你可以使用参与者招募平台，如Prolific、Mechanical Turk或Sona Systems。

- %link:prolific%
- %link:mturk%
- %link:sonasystems%

## 教程

- %link:tutorials/intermediate-javascript%
- %link:wcst%