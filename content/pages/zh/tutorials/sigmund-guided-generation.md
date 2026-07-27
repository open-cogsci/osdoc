title: 使用 guided generation 用 SigmundAI 创建任意实验
hash: 9fd2992708f865ec29c9a7080a645de89d5d0a9619c8e543101fe468cd89d355
locale: zh
language: Chinese

[TOC]


## 关于本教程

在本教程中，你将学习如何使用 SigmundAI 构建任何实验。这不是一个专注于某个特定实验的分步教程。相反，它概述了一种通用工作流程，你可以根据自己的需要进行调整。

不要期待奇迹！如果你的实验很复杂，那么当完全让 Sigmund 自行处理时，它很可能会遇到困难。你通常需要积极地与 Sigmund 协作来实现一个实验。

我将此称为 *引导式生成*，因为你是在引导 Sigmund 完成整个过程。

如果你还没有使用过 Sigmund，我建议你先完成[SigmundAI 初学者教程](%url:beginner-sigmund%)。


## 你将学到什么

完成本教程后，你将知道如何：

- 💡 向 Sigmund 提供清晰且有效的指令
- 💡 将从零开始构建完整实验的过程拆分为可管理的步骤
- 💡 修复 Sigmund 在构建实验时可能出现的错误。


## 我应该使用哪个模型？

大多数步骤并不需要特别强大的模型。我主要使用 Z.ai GLM 5.2，在撰写本文时，它在智能程度和成本之间提供了良好的平衡。不过，最终的实现步骤正在逼近大多数 AI 模型能力的极限。因此，在这一阶段，你可以切换到更强大的模型，例如 Claude Sonnet 5。不过请考虑，更强大的模型通常也（要）贵得多。

在实践中，尝试不同的模型，看看哪一种能为你的特定实验带来最佳结果。


## 工作流程

以下是我们将要做的事情：

1. 用清晰的语言描述你想要构建的实验。
2. 请 Sigmund 将你的描述扩展为一份全面的叙述性说明，以完整详细地规定该实验。
3. 审查这份全面说明。如有必要，进行讨论并调整。
4. 请 Sigmund 制定一个 JSON 规范（一种人类可读的技术格式），用于描述实验结构。
5. 审查 JSON 规范。如有必要，进行讨论并调整。
6. 请 Sigmund 一次性构建整个实验。
7. 测试并润色实验。

本教程的重点是与 Sigmund 进行有效沟通。我们将帮助 Sigmund 把构建实验这一复杂任务细分为可管理的子任务，并在适当的时候提供具体操作指示。

__重要：__ 你需要通过 OpenSesame 内部的聊天面板与 Sigmund 交谈。如果你使用网页界面，Sigmund 将无法控制 OpenSesame。


## 制定实验的全面叙述性说明

以下是我们在这个示例中将使用的实验描述：

💬 **描述：**

```text
一个典型的视觉工作记忆任务，需要记住不同颜色的圆圈。通过在原始圆圈位置呈现一个颜色相同或不同的圆圈来探测其中一个圆圈。参与者作出相同/不同判断。集合大小会变化。
```

我们首先要求 Sigmund 根据这段描述补充出一份详细的实验说明。在你的实验描述中，尽可能提供更多细节，因为这有助于 Sigmund 提出符合你设想的设计。例如，如果你认为试次逻辑应通过 `inline_script` 实现，请说明这一点。

我们将这段描述包含在一个为 Sigmund 提供清晰指令的 prompt 中：

💬 **Prompt：**

```text
我有一个富有挑战性的任务要交给你！我们将从零开始实现一个 OpenSesame 实验。为了便于处理，我们会把这个过程拆分成几个步骤。在当前这一步中，你的任务是扩展实验任务的描述，使其包含我们实现它所需的全部细节。

以下是一些关于试次结构需要考虑的事项：

- 参与者作出反应的方式
- 刺激呈现的时序
- 刺激的外观
- 刺激的布局
- 是否提供参与者反馈，以及如果提供，是如何提供的
- 任何未被明确提及但应当包含的刺激
- 刺激之间的空白或注视显示（如果有注视点，通常会在整个试次中持续显示）

以下是一些关于实验结构需要考虑的事项：

- 自变量和因变量
- 是否有练习阶段
- 试次是否被划分为若干区组
- 试次数量以及（如果适用）区组数量
- 任何欢迎、说明和结束界面

另外，也请包含你认为相关的任何附加信息。

<experimental_task_description>
一个典型的视觉工作记忆任务，其中需要记住不同颜色的圆圈。通过在原始圆圈位置呈现一个颜色相同或不同的圆圈来探测其中一个圆圈。参与者作出“相同/不同”的判断。集合大小会变化。
</experimental_task_description>

请回复一个全面的描述。先不要将其保存为笔记，因为我们首先要进行审核。
```

Sigmund 将回复一份详细的实验描述。请审核它，并在必要时提供修正意见。如果你满意，请让 Sigmund 将其记录为笔记。


💬 **Prompt:**

```text
太好了！请将这份全面的描述保存为持久笔记，这样你就不会忘记了。不要总结，而是完整保存。
```


## 为实验结构开发 JSON 规范

现在我们将要求 Sigmund 设计实验结构。这将指定哪些项目构成实验，以及它们是如何连接的。

提示中的第二点提到了可以使用哪些项目类型。为了帮助 Sigmund，删除你知道不需要的项目类型。例如，如果参与者不会使用鼠标作答，你可以删除 `mouse_response` 项目类型。


💬 **Prompt:**

```text
继续！这是你的下一个任务：

- 根据你刚刚保存为注释的实验叙述描述，起草一份 JSON 规范。
- JSON 中的每个 dict 都应对应一个单独的 OpenSesame item。你可以使用以下 items：[loop, sequence, sketchpad, feedback, synth, sampler, keyboard_response, mouse_response, logger, inline_script, inline_javascript, form_multiple_choice, form_text_display, form_text_input, reset_feedback]
- sketchpad items 是预先准备好的，因此不能考虑在其 prepare phase 之后定义的变量。因此，要显示包含变量内容的界面时，通常你会想改用 feedback items，但仅限于对时间要求不严格的显示。
- 不要使用多个彼此不关联的 logger items，因为这会导致日志文件混乱。相反，应使用同一个 logger 的 linked copies。
- 不要把 reset_feedback items 放在主实验 sequence 中，因为这与 OSWeb 不兼容。
- 暂时不要包含这些 items 的任何实现细节。我们稍后会处理这些。目前，只需提供 description、name 和 type。对于属于 sequence 的 items，你也可以提供 run-if 表达式。对于在别处出现过的 linked copies，只为第一次出现提供详细信息，后续出现时只提供 name。
- 有子 items 的 items 还应包含一个额外的 `items` 字段。loop 总是有一个单独的 sequence 作为子 item。sequence 通常有多个不同类型的子 items。
- 请尽可能使用 items 的 linked copies。要表明某个 item 是另一个 item 的 linked copy，只需重复使用相同的 name，并添加一个设为 `true` 的 `linked` 字段。
- 下面的 JSON 规范示例展示了大致思路，但做了大量简化。你的 JSON 规范很可能要复杂得多。

<json_example>
{
  "name": "experiment",
  "type": "sequence",
  "description": "任务的一行描述",
  "items": [
    {
      "name": "task_description",
      "type": "notepad",
      "description": "任务的完整叙述描述写在这里。"
    },
    {
      "name": "welcome",
      "type": "sketchpad",
      "description": "简短的欢迎信息"
    },
    {
      "name": "block_loop",
      "type": "loop",
      "description": "一个 trial 区块。这里也定义自变量。",
      "items": [
        {
          "name": "trial_sequence",
          "type": "sequence",
          "description": "单个 trial 的 sequence",
          "items": [
            {
              "name": "fixation",
              "type": "sketchpad",
              "description": "显示黑色注视十字（+）500 ms"
            },
            {
              "name": "target_display",
              "type": "sketchpad",
              "description": "在注视十字保持可见的同时显示目标刺激"
            },
            {
              "name": "keyboard_response",
              "type": "keyboard_response",
              "description": "收集参与者对目标刺激的反应"
            },
            {
              "name": "correct_feedback",
              "type": "sketchpad",
              "description": "正确反应后显示绿色注视点 500 ms",
              "run_if": "correct == 1"
            },
            {
              "name": "fixation",
              "linked": true
            },
            {
              "name": "logger",
              "type": "logger",
              "description": "记录所有 trial 数据"
            }
          ]
        }
      ]
    }
  ]
}
</json_example>

请针对实验叙述描述回复 JSON 规范。暂时不要将 JSON 规范保存为注释，因为我们首先要审查它。
```

Sigmund 现在将提供一份详细的 JSON 规范，这本质上是 OpenSesame 中概览区域的技术视图。请审查该规范，并在必要时提供反馈。如果你满意，请要求 Sigmund 记下来。

💬 **Prompt:**

```text
太棒了，做得很好 Sigmund！请把这个保存为另一条持久笔记，以免你忘记。不要总结它，而是完整保存。
```


## 实现实验

现在我们准备就绪了！这最后一步正在逼近大多数 AI 模型能力的极限。如果你发现 Sigmund 持续失败，尝试切换到一个更强大的模型。我曾用 Claude Sonnet 5 成功过。

💬 **Prompt:**

```text
我们现在已经准备好实现实验了。有几点提示：

- 将这些说明保存为持久笔记，以免你忘记。
- *不要* 检查当前实验的项目。它们不相关，因为我们将彻底覆盖当前实验。
- 出于同样的原因，*不要* 检查当前实验的 general script。
- 在编写实验脚本之前，调用 `opensesame_get_syntax_documentation` 并设置 `save_as="note"`，以获取所有相关文档。
- 最后，将新实验写成一个单一的完整 general script，并将其传递给 `opensesame_update_general_script`。

这是一项具有挑战性的任务，但我知道你能做到。开始吧！
```

Sigmund 成功实现了作为示例使用的视觉工作记忆实验。不过，并非所有实验都会顺利进行。

如果 Sigmund 注意到它在生成实验时犯了语法错误，它会尝试修复它。Sigmund 可能会在试图让程序运行时陷入无限循环。发生这种情况时，中止对话。

如果实验成功生成，它仍然可能包含错误或不完善之处。请仔细测试并打磨它！


## 通过引导式生成创建的实验示例

对于下面所有示例，初始步骤都是使用 Z.ai GLM 5.2 完成的，而最终实现步骤使用的是 Claude Sonnet 5。我没有对全面描述或 JSON 规范提供任何反馈。不过，我确实按照下面的说明对最终实验进行了打磨。


### Visual working memory

💬 **Description:**

```text
一个典型的视觉工作记忆任务，需要记住不同颜色的圆。通过在原始圆的位置呈现一个颜色相同或不同的圆来探测其中一个圆。参与者做出相同/不同判断。集合大小会变化。
```

说明：

- Sigmund 在这个实验中使用了已弃用的 `[square_brackets_syntax]` 来在 sketchpad 项目中引用变量。这虽然可用，但我把它改成了推荐的 `{curly_brackets_syntax}`。
- Sigmund 为这个实验使用了 Python INLINE_SCRIPT。因此，它不能在浏览器中运行。

试用该实验：

- %static:attachments/sigmund/sigmund-visual-working-memory.osexp%


### Posner cuing

💬 **Description:**

```text
一个带有中央线索和字母辨别任务的 Posner 线索提示范式。
```

说明：

- Sigmund 使用了 unicode 标记（例如 `\u2190`）作为箭头线索。OpenSesame 不会渲染这些标记，因此需要将其替换为实际字符（例如 “←”）。
- Sigmund 使用了已弃用的 `[square_brackets_syntax]` 来在 sketchpad 项目中引用变量。这虽然可用，但我把它改成了推荐的 `{curly_brackets_syntax}`。

试用该实验：

- %static:attachments/sigmund/sigmund-posner-cuing.osexp%
- [在浏览器中运行](https://jatos.mindprobe.eu/publix/QgymMCSRYzL)


### AX continuous performance

💬 **Description:**

```text
一个 AX continuous performance task。
```

说明：

- Sigmund 忘记设置各个 `sequence` 项目中要运行哪些项目。这需要手动修复。

试用该实验：

- %static:attachments/sigmund/sigmund-axcpt.osexp%
- [在浏览器中运行](https://jatos.mindprobe.eu/publix/5s8TbGLx0bZ)