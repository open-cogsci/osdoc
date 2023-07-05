title: Prolific
hash: fd3ba787ea541676148e558d0e902641c2b9f9eb848745aff73e95c443e9fc56
locale: zh
language: Chinese

[TOC]


## 关于Prolific

[Prolific](https://prolific.co/) 是一个用于招募研究参与者的商业工具。要在Prolific 上运行 OSWeb 实验，需要按照下面的步骤进行。

请参考：

- <http://www.jatos.org/Use-Prolific.html>


## 在 JATOS 上创建研究

首先，将实验导入到 JATOS 中，如上所述。接下来，进入 Worker & Batch Manager，激活 General Multiple Worker，点击 Get Link 获取一个 URL 并复制它（%FigJatosURL）。

%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: 从 JATOS 获取研究的URL。
--%


## 在 Prolific 创建研究

接下来，在 Prolific 上创建研究。在“研究详情”（%FigProlific）下，将 JATOS 的研究 URL 插入标有 "What is the URL of your study?" 的字段中。这将告诉 Prolific 如何启动实验。重要的是，将下面的内容添加到 URL 的末尾（这将把 Prolific 的重要信息传递给您的实验）：

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

实验完成后，Prolific 需要了解此情况。为此，Prolific 使用了一个 End Redirect URL，该 URL 列在标有 "To prove that participants have completed your study …" 的字段中。复制这个 End Redirect URL。另外，勾选标有 "I've set up my study to redirect to this url at the end" 的方框。

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Prolific 中的研究详情。
--%



## 在 JATOS 中设置 End Redirect URL

现在返回到 JATOS，并打开您的研究的属性（%FigJatosProperties）。在这里，将您从 Prolific 复制的 End Redirect URL 粘贴到标有 "End Redirect URL" 的字段中。这将告诉 JATOS，实验结束时，参与者应该被重定向回 Prolific，以便 Prolific 知道参与者已经完成了实验。

%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: 在 JATOS 设置 End Redirect URL。
--%


## 在您的实验中注册 Prolific 信息

Prolific 的每个参与者都由一个唯一的 ID 标识。在您的实验中记录此 ID 很重要，因为这可以让您知道哪个来自 Prolific 的参与者对应 JATOS 结果中的哪一项。您可以通过在实验开始时的 `inline_javascript` 项目的准备阶段添加下面的脚本来实现这一点。

当通过 Prolific 运行实验时，将使 Prolific ID 作为试验变量 `prolific_participant_id` 可用。当以任何其他方式运行实验时（例如在测试中），变量 `prolific_participant_id` 将被设置为 -1。同样的逻辑适用于 Prolific 研究 ID（`prolific_study_id`）和 Prolific 会话 ID （`prolific_session_id`）。

```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific 信息可用')
    var prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    var prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    var prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific 信息不可用（设置值为 -1）')
    var prolific_participant_id = -1
    var prolific_study_id = -1
    var prolific_session_id = -1
}
console.log('prolific_participant_id = ' + prolific_participant_id)
console.log('prolific_study_id = ' + prolific_study_id)
console.log('prolific_session_id = ' + prolific_session_id)
```

## 测试研究

返回Prolific上的研究详细信息页面。页面底部有一个预览按钮。这允许您通过自己充当参与者来测试实验。别忘了检查JATOS结果，以确保实验已成功完成，并且已记录所有必要信息（包括Prolific信息）！