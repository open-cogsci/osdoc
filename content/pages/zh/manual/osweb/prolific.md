title: Prolific
hash: ae0240db997107f3570b2cbf0d4576f801d25a57fbdd0a043e7f8be1bb82d715
locale: zh
language: Chinese

[TOC]

## 关于Prolific

[Prolific](https://prolific.co/)是一种用于招募研究参与者的商业工具。要在Prolific上运行OSWeb实验，您需要按照以下步骤操作。

另请参阅：

- <http://www.jatos.org/Use-Prolific.html>

## 在JATOS上创建研究

首先，将您的实验导入到JATOS中，如上所述。接下来，进入Worker & Batch Manager，激活General Multiple Worker，点击Get Link获取URL，并将其复制（%FigJatosURL）。

%--
图：
 id: FigJatosURL
 source: jatos-url.png
 caption: 从JATOS获取研究URL。
--%

## 在Prolific上创建研究

接下来，在Prolific上创建一个研究。在Study Details（%FigProlific）下，将JATOS研究URL插入到标有“What is the URL of your study?”的字段中。这将告诉Prolific如何启动实验。重要的是，在URL末尾添加以下内容（这将从Prolific传递重要信息到您的实验中）：

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

当实验完成时，Prolific需要知道这一点。为此，Prolific使用一个End Redirect URL，在标有"To prove that participants have completed your study …"的字段中列出。复制此End Redirect URL。还要勾选上标有"I've set up my study to redirect to this url at the end"的框。

%--
图：
 id: FigProlific
 source: prolific.png
 caption: Prolific上的研究详细信息。
--%

## 在JATOS中设置End Redirect URL

现在回到JATOS，打开您的研究的属性（%FigJatosProperties）。在那里，将您从Prolific复制的End Redirect URL粘贴到标有"End Redirect URL"的字段中。这将告诉JATOS在实验完成时，参与者应该被重定向回Prolific，以便Prolific知道参与者完成了实验。

%--
图：
 id: FigJatosProperties
 source: jatos-properties.png
 caption: 在JATOS中设置End Redirect URL。
--%

## 在您的实验中注册Prolific信息

每个来自Prolific的参与者都有一个唯一的ID。记录这个ID很重要，因为这可以让您知道哪个Prolific参与者对应JATOS结果中的哪个条目。您可以通过将以下脚本添加到您实验开始时的`inline_javascript`项的Prepare阶段来实现这一点。

当通过Prolific运行实验时，这将使Prolific ID作为实验变量`prolific_participant_id`可用。当以其他方式运行实验（例如在测试过程中），变量`prolific_participant_id`将设置为-1。这个逻辑同样适用于Prolific Study ID（`prolific_study_id`）和Prolific Session ID（`prolific_session_id`）。


```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific information is available')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific information is not available (setting values to -1)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```

## 测试研究

返回Prolific上的研究详细信息页面。页面底部有一个预览按钮。这允许您通过自己充当参与者来测试实验。别忘了检查JATOS结果，以确保实验已成功完成，并且已记录所有必要信息（包括Prolific信息）！