<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __responses__

`responses` 对象包含在实验期间收集的所有响应历史记录。

实验开始时，将自动创建一个 `responses` 对象。

除了下面列出的功能外，还支持以下语义：

__示例__

~~~ .python
# 遍历所有响应，最后给出的响应排在前面
# 每个响应都有正确的响应、response_time、item 和 feedback
# 属性。
for response in responses:
    print(response.correct)
# 打印两个最后给出的响应
print('最后两个响应：')
print(responses[:2])
~~~

[TOC]

## add(response=None, correct=None, response_time=None, item=None, feedback=True)

添加一个响应。


__参数__

- **response**：响应值，例如，'space' 代表空格键，0 代表游戏杆按钮 0 等。
- **correct**：响应的正确性。
- **response_time**：响应时间。
- **item**：收集响应的项目。
- **feedback**：表示响应是否应包含在准确性和平均响应时间的反馈中。

__示例__

~~~ .python
responses.add(response_time=500, correct=1, response='left')
~~~



## clear(self)

清除所有响应。



__示例__

~~~ .python
responses.clear()
~~~



## reset_feedback(self)

将所有响应的反馈状态设置为 False，以便只有
新的响应将包含在反馈中。



__示例__

~~~ .python
responses.reset_feedback()
~~~



</div>