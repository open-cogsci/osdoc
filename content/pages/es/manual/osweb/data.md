title: Descargando y convirtiendo datos
hash: 107ebe6aa385be243fb6fa5d9117a4cbe10925553e29d4cbf251a8ba7a3b0ef9
locale: es
language: Spanish

Una vez que haya recolectado datos con OSWeb a través de JATOS, puede descargar estos datos en JATOS navegando a su experimento, haciendo clic en Resultados y luego seleccionando Exportar resultados → Todos (ver %FigJatosExportResults).

%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Exportando resultados recolectados con OSWeb a través de JATOS.
--%

Luego, descargará un archivo que tiene un nombre similar a `jatos_results_20190429113807.txt`. Este archivo contiene principalmente datos JSON, pero también puede contener fragmentos de datos que hacen que el archivo no sea válido como una cadena JSON regular. Sin embargo, puede convertir fácilmente los datos a un archivo `.csv` o `.xlsx` con la opción 'Convertir resultados de JATOS a csv / xlsx' en la extensión OSWeb.