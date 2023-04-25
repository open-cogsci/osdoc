title: 计数平衡
hash: f746c6dcc8ded61b700e84340fafff7a9ab6a1c217365d1ff9b97ab344438cd2
locale: zh
language: Chinese

反平衡是通过为不同的参与者组设置略有不同的任务，从实验中消除混杂因素的一种方法。这听起来很抽象，所以我们来看两个例子。

[TOC]

### 示例1：反平衡响应规则

考虑一个词汇决策实验，参与者通过用左手按'z'来将单词分类为动词，或用右手按'm'将单词分类为名词。这个设计有一个问题：如果发现参与者对名词的反应速度比对动词的反应速度快，这可能是因为名词比动词处理速度更快，或是因为参与者用右手比用左手反应更快。您可以通过反平衡响应规则来解决这个问题。

对于偶数参与者编号：

- 动词 → z
- 名词 → m

对于奇数参与者编号：

- 动词 → m
- 名词 → z

### 示例2：旋转刺激条件

考虑一个掩模启动实验，参与者大声朗读目标词。在每个试验中，目标词前有三种类型的启动词之一：

- 不相关的引导词，例如用'berry'(浆果)来引导目标词 'house'(房子)。
- 正字法相关的引导词，例如用‘mouse’(鼠标)来引导目标词‘house’（房子）
- 语义相关的引导词，例如用'garden'(花园)来引导目标词'house'(房子)

为了避免重复效应，您只希望每个参与者目标词只出现一次。因此，您为每种引导词类型创建三个不同的目标词集。这是一个单词间设计，其统计效力低于单词内设计，即每个目标词在每个条件下都出现。（原因是单词间设计的效力低于单词内设计。）

您可以通过在参与者之间“旋转”每个词出现的条件来使用反平衡使这个实验成为一个单词内设计。我们有三个条件，因此我们有三组参与者：

- 参与者1、4、7等
    - 词A在条件1
    - 词B在条件2
    - 词C在条件3
- 参与者2、5、8等
    - 词A在条件2
    - 词B在条件3
    - 词C在条件1
- 参与者3、6、9等
    - 词A在条件3
    - 词B在条件1
    - 词C在条件2

## 实施反平衡

### 使用受试者编号

当您在桌面上运行OpenSesame实验时，会要求您输入一个受试者编号。当您在线运行实验时，系统会从您在[OSWeb扩展](%url:osweb)中指定的可能受试者编号列表中随机选择一个。（这意味着对于在线实验，您无法确保各个想要进行反平衡的条件的参与者数量完全相等，至少不能依靠受试者编号。）

此受试者编号可作为实验变量`subject_nr`获得。此外，实验变量`subject_parity`根据受试者编号的奇偶性取值为'odd'(奇数)或'even'(偶数)。现在假设您想要像示例1中那样反平衡响应规则，您可以在实验开始时添加以下INLINE_SCRIPT。

```python
if subject_parity == 'odd':
    verb_response = 'z'
    noun_response = 'm'
else:
    verb_response = 'm'
    noun_response = 'z'
```

或者，在创建OSWeb实验时，在实验开始时添加以下INLINE_JAVASCRIPT：

```javascript
if (subject_parity === 'odd') {
    verb_response = 'z'
    noun_response = 'm'
} else {
    verb_response = 'm'
    noun_response = 'z'
}
```

现在，在*block_loop*中，您将`correct_response`设置为一个变量，而不是固定值：`{verb_response}`或`{noun_response}`。您可以查看*词位决策任务*示例，了解这是如何工作的（菜单->工具->示例实验）。

### 使用批量会话数据 (仅限JATOS和OSWeb)

在 JATOS 上托管的 OSWeb 实验中运行时，您可以使用[批处理会话数据](https://www.jatos.org/jatos.js-Reference.html#functions-to-access-the-batch-session)。这是在同一工作批次中的所有实验会话之间共享的数据。因此，您可以使用此数据定义一个应该在参与者之间分发的条件列表。在每个实验会话开始时，从此列表中删除一个条件并用于当前会话。这是针对 JATOS 上托管的 OSWeb 实验实现计数平衡的最复杂方法。

您可以在此处下载模板实验：

- %static:attachments/counterbalancing-osweb-jatos.osexp%

当从 JATOS 运行时，实验从批处理会话数据（见下文）中检索单个条件，并将此注册为实验变量 `condition`。进行测试运行时，`condition` 的默认值设置为 *init_condition* 结尾处指定的值。

实验本身应该在 *experiment* SEQUENCE 中实现，在模板中只包含 *show_condition* SKETCHPAD（见%FigCounterbalancingOSWebJATOS）。

%--
figure:
    source: counterbalancing-osweb-jatos.png
    id: FigCounterbalancingOSWebJATOS
    caption: |
        使用 JATOS 批处理会话数据实现计数平衡的模板实验的概览区。
--%

将实验导入 JATOS 时，所有条件都应在批处理会话数据的 `pending` 列表中指定（请参阅 Worker & Batch Manager; 见 %FigBatchSessionData）。来自 `pending` 的每个条件对应一个实验会话；因此，如果条件`a`应该用于两个实验会话，那么`a`需要在 `pending` 列表中出现两次。条件将按照定义的顺序使用。

%--
figure:
    source: batch-session-data.png
    id: FigBatchSessionData
    caption: |
        应在 JATOS 的批处理会话数据中指定条件。
--%

在实验会话开始时，一个条件从 `pending` 移动到 `started`。 （当 `pending` 列表为空时，参与者将被告知他/她不能再参加实验。）实验会话结束时，条件附加到 `finished` 列表中。

为了使这更具体，假设您已经将批处理会话数据定义为显示在 %FigBatchSessionData 中。然后，启动四个实验会话，但第二个实验会话（条件 `a`）从未完成，例如，因为参与者在实验进行到一半时关闭了浏览器。然后，批处理会话数据将显示在 %FigBatchSessionAfter 中：

%--
figure:
    source: batch-session-data-after.png
    id: FigBatchSessionAfter
    caption: |
        所有条件都已耗尽后的批处理会话数据。一个条件为 `a` 的会话从未结束。
--%

您可以从批处理会话数据中看到，一个实验会话以条件 `a` 开始，但从未完成。为了仍然收集具有此条件的实验会话，您必须手动向 `pending` 列表中添加一个新的 `a` 并收集新的会话。