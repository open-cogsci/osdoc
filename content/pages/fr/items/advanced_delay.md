title: Advanced_delay
hash: 54879490fe7472c89ac95be6dc21911ffcdddabbe58ec3de0baf4b660ad5dc89
locale: fr
language: French

Le plug-in `advanced_delay` retarde l'expérience pendant une durée moyenne spécifiée à l'avance, plus une marge aléatoire.

- *Durée* est la durée moyenne du retard en millisecondes.
- *Jitter* est l'ampleur de la variation du retard en millisecondes.
- *Mode Jitter* est la façon dont le jitter est défini :
  - *Écart type* tirera les valeurs d'une distribution gaussienne avec Jitter comme écart type.
  - *Uniforme* tirera les valeurs d'une distribution uniforme centrée sur la Durée, avec Jitter comme amplitude.