title: Sona系统
hash: b16a73f1e8a3fb7fd7efb983a26825940c0de47ec814bf27280a22d31c398657
locale: zh
language: Chinese

[TOC]

## 关于Sona Systems

Sona Systems 是许多大学用于招募参与者、为学生参与者授予课程学分等的在线工具。

另请参阅：

- <https://www.sona-systems.com/help/integration_test.aspx>

## 在 JATOS 上创建研究

首先，将您的实验导入 JATOS，如上所述。接下来，进入 Worker & Batch Manager，激活 General Multiple Worker，点击 Get Link 获取一个 URL，并复制它。

## 在 Sona Systems 上创建研究

接下来，在 Sona Systems 上创建一个研究。在标记为 "Study URL" 的字段中插入 JATOS 研究 URL。这将告诉 Sona Systems 如何启动实验。重要的是，在URL的末尾添加以下内容（这将将参与者的 Sona ID 传递给您的实验）：

```bash
&SONA_ID=%SURVEY_CODE%
```

Sona Systems 不使用重定向 URL。这意味着 Sona Systems 不会自动知道参与者是否完成了研究。

## 在实验中注册 Sona ID

每个来自 Sona 的参与者都由唯一的 ID 标识。将此 ID 记录在您的实验中非常重要，因为这允许您确定来自 Sona 的哪个参与者对应于 JATOS 结果中的哪个条目。您可以通过在实验开始时的 `inline_javascript` 项目的 Prepare 阶段添加以下脚本来实现这一点。

当通过 Sona 运行实验时，这将使 Sona ID 作为实验变量 `sona_participant_id` 可用。当以其他方式运行实验（例如在测试期间），变量 `sona_participant_id` 将设置为 -1。

```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Sona information is available')
    vars.sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Sona information is not available (setting value to -1)')
    vars.sona_participant_id = -1
}
console.log('sona_participant_id = ' + vars.sona_participant_id)
```

## 在研究完成后自动授予学分

Sona Systems 提供了一个完成 URL（客户端），在研究成功完成时应调用该 URL，以便 Sona Systems 可以为参与者授予学分（参见 %FigCompletionURL）。

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: Sona Systems 研究信息中的完成 URL。
--%

完成 URL（客户端）包含三个参数：

- `experiment_id`，用于识别研究，对所有参与者都相同
- `credit_token`，当您更改研究信息时会更改，但对所有参与者都相同
- `survey_code`，对应 Sona 参与者 ID，因此对每个参与者都不同

复制完成 URL，并将 `XXX` 替换为 `[SONA_ID]`。转到 JATOS 的 Study Properties，并将结果 URL 插入 End Redirect URL 字段。

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: JATOS 研究属性中的结束重定向 URL。
--%