title: 重置反馈
hash: 1bac08e9d7c690dc8199e762ae4574622cf3faa0486e3ecdcb98823269756ab7
locale: zh
language: Chinese

这个插件具有与呈现0毫秒持续时间的FEEDBACK项目相同的效果
{: .page-notification}

如果您不重置反馈变量，您可能会混淆与任务无关的响应的反馈。例如，在说明阶段进行的按键可能会影响实验第一阶段的反馈。因此，您需要在适当的时刻重置反馈变量。

此插件将将以下变量重置为0：

- `total_response_time`
- `total_response`
- `acc`
- `accuracy`
- `avg_rt`
- `average_response_time`