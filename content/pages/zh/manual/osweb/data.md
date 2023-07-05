title: 下载并转换数据
hash: 3ab535f2cc44ff0565b2183aa31768623aacd998a849e1cf6667e3b4ec5425da
locale: zh
language: Chinese

使用OSWeb通过JATOS收集数据后，您可以下载并处理这些数据进行分析。要下载，请导航到JATOS中的您的研究，点击“结果”，选择所有的结果条目，然后选择“导出结果 → JATOS结果存档”（见％FigJatosExportResults）。

%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Procedure for exporting results collected with OSWeb through JATOS.
--%

下载的文件，通常以`jatos_results_<timestamp>.jzip`的格式命名，包含着对应于元数据和参与者数据的各种文件夹和文件。这种格式直接用于数据分析可能会比较困难。

为了简化数据分析，您可以将此文件转换为更易访问的格式，如`.csv`或`.xlsx`。通过使用OSWeb扩展中的'转换OSWeb结果为csv/xlsx'选项，可以轻松实现这种转换。