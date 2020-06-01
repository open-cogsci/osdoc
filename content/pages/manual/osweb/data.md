title: Downloading and converting data

Once you have collected data with OSWeb through JATOS, you can download this data in JATOS by navigating to your experiment, clicking on Results, and then selecting Export Results → All (see %FigJatosExportResults).


%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Exporting results collecting with OSWeb through JATOS.
--%


You will then download a file that has a name similar to `jatos_results_20190429113807.txt`. This file contains mostly JSON data, but may also contain fragments of data that render the file invalid as a regular JSON string. However, you can easily convert the data to a `.csv` or `.xlsx` file with 'Convert JATOS results to csv/ xlsx' option in the OSWeb extension.
