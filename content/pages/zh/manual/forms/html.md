title: 自定义HTML表单
hash: 7ce4d5848c0a4e0e32e903dbfb423bd42fbcf30dea52cc43cde013192eeab9dd
locale: zh
language: Chinese

INLINE_HTML 项目允许您使用自定义 HTML 实现表单。

- `input` 标签的 `name` 属性对应于实验变量。因此，将文本输入到示例 1 的文本输入框中，将其存储为实验变量 `text_response`。
- 对于 `checkbox` 和 `radio` 元素，您可以使用 `id` 属性为关联的实验变量指定一个特定值。
- 您可以使用 `required` 属性指示在填写字段之前，表单不能提交。
- 当参与者点击提交类型的输入时，表单关闭。
- 要在自定义 HTML 表单中包含文件池中的图像，首先检索文件的 URL，将其分配给实验变量，然后将此变量用作 `<img>` 标签的来源（请参阅示例 3）。

示例 1：

一个非常基本的文本输入表单：

```html
<input type='text' name='text_response'>
<input type='submit' value='点击此处继续'>
```

示例 2：

带有多个单选按钮的表单：

```html
<p>请选择您的年龄：</p>
<input type="radio" id="age1" name="age" value="30" required>
<label for="age1">0 - 30</label><br>
<input type="radio" id="age2" name="age" value="60">
<label for="age2">31 - 60</label><br>  
<input type="radio" id="age3" name="age" value="100">
<label for="age3">61 - 100</label><br><br>
<input type="submit" value="提交">
```

示例 3：

您可以包含变量引用（除了在 `<script>` 标签中，其中花括号仅被解释为 JavaScript 代码的一部分）：

```html
<p>您的年龄组是 {age}</p>
<input type='submit' value='ok'>
```

示例 4：

您可以通过 `<script>` 标签使用 JavaScript。例如，您可以从文件池获取图像并将其分配给最初为空的 `<img>` 标签，如下所示：

```html
<img id='capybara'>
<input type='submit' value='ok'>

<script>
document.getElementById('capybara').src = pool['capybara.png'].data.src
</script>
```