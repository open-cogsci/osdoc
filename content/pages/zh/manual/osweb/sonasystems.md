title: Sona系统
hash: d944a35b3e0c80d34ad14fc5152e628c6249312a06e28b86e5e6da4470fa60a2
locale: zh
language: Chinese

[TOC]


## 关于 Sona Systems

Sona Systems 是许多大学用于招募参与者、给学生参与者授予课程学分等的在线工具。

参见:

- <https://www.sona-systems.com/help/integration_test.aspx>


## 在 JATOS 上创建研究

首先，将你的实验导入到 JATOS，如上所述。然后，进入 Worker & Batch 管理器，激活 General Multiple Worker，点击 Get Link 获取 URL，然后复制它。


## 在 Sona Systems 上创建研究

接下来，在 Sona Systems 上创建研究。将 JATOS 研究 URL 插入到标记为 “Study URL” 的字段中。这将告诉 Sona Systems 如何启动实验。重要的是，要将以下内容添加到URL的末尾（这将会将参与者的 Sona ID 传递给你的实验）:

```bash
&SONA_ID=%SURVEY_CODE% 
```

Sona Systems 不使用重定向 URL。这意味着 Sona Systems 不会自动知道参与者是否完成了研究。


## 在你的实验中注册 Sona ID

Sona 的每一个参与者都有一个独特的 ID。在你的实验中记录这个 ID 是很重要的，因为这样你可以知道哪一个来自 Sona 的参与者对应 JATOS 结果中的哪一个条目。你可以通过在实验开始时的 `inline_javascript` 项目的准备阶段添加下面的脚本来实现这一点。

当通过 Sona 运行实验时，这将使 Sona ID 作为实验变量 `sona_participant_id` 可用。当以任何其他方式运行实验（例如，在测试期间），变量 `sona_participant_id` 将设为 -1 。


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Sona 信息可用')
    var sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Sona 信息不可用（设置值为 -1）')
    var sona_participant_id = -1
}
console.log('sona_participant_id = ' + sona_participant_id)
```


## 自动在研究完成后授予学分

Sona Systems 提供了一个完成 URL (客户端)，当研究成功完成时应当被调用，以便 Sona Systems 可以给参与者授予学分（见%FigCompletionURL）。

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: Sona Systems 研究信息中的完成 URL。
--%

完成 URL（客户端）里有三个参数：

- `experiment_id`，它识别研究，并对所有参与者相同
- `credit_token`，它（显然）在你更改研究信息时会更改，但否则对所有参与者相同
- `survey_code`，它对应于 Sona 参与者 ID，因此对每个参与者来说都是不同的

复制完成 URL，并将 `XXX` 替换为 `[SONA_ID]`。转到 JATOS 的 Study Properties，并将得到的 URL 插入到 End Redirect URL 字段中。

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: JATOS 研究属性中的结束重定向 URL。
--%