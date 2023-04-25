title: 下载并转换数据
hash: 107ebe6aa385be243fb6fa5d9117a4cbe10925553e29d4cbf251a8ba7a3b0ef9
locale: zh
language: Chinese

当你通过JATOS使用OSWeb收集到数据后，你可以在JATOS中下载这些数据。方法是导航到你的实验，点击结果，然后选择导出结果→全部（参见％FigJatosExportResults）。

%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: 通过 JATOS 导出使用 OSWeb 收集的结果。
--%

然后，您将下载一个名为`jatos_results_20190429113807.txt`的文件。这个文件主要包含 JSON 数据，但也可能包含使文件作为常规 JSON 字符串无效的数据片段。然而，您可以轻松地使用 OSWeb 扩展中的'将 JATOS 结果转换为 csv/ xlsx'选项将数据转换为`.csv`或`.xlsx`文件。