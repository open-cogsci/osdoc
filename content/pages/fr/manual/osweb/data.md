title: Téléchargement et conversion des données
hash: 107ebe6aa385be243fb6fa5d9117a4cbe10925553e29d4cbf251a8ba7a3b0ef9
locale: fr
language: French

Une fois que vous avez collecté des données avec OSWeb via JATOS, vous pouvez télécharger ces données dans JATOS en accédant à votre expérimentation, en cliquant sur Résultats, puis en sélectionnant Exporter Résultats → Tout (voir %FigJatosExportResults).

%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Exportation des résultats collectés avec OSWeb via JATOS.
--%

Vous téléchargerez alors un fichier dont le nom ressemble à `jatos_results_20190429113807.txt`. Ce fichier contient principalement des données JSON, mais peut également contenir des fragments de données qui rendent le fichier invalide en tant que chaîne JSON régulière. Cependant, vous pouvez facilement convertir les données en un fichier `.csv` ou `.xlsx` avec l'option 'Convert JATOS results to csv/ xlsx' dans l'extension OSWeb.