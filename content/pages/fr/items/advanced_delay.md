title: Advanced_delay
hash: 05d5215072bc5c76e2fd177cc099d6281a44d87cde42c43e79a945b2ac83b98f
locale: fr
language: French

Le plug-in `advanced_delay` retarde l'expérience pendant une durée moyenne pré-spécifiée plus une marge aléatoire.

- *Durée* est la durée moyenne du retard en millisecondes.
- *Jitter* est la taille de la variation du retard en millisecondes.
																								
- *Mode Jitter* est la façon dont le jitter est calculé :
	- *Écart type* prélèvera la variation à partir d'une distribution gaussienne avec Jitter comme écart type.
	- *Uniforme* prélèvera la variation de durée à partir d'une distribution uniforme.