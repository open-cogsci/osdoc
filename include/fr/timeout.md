## Délai d'attente

Le champ *Timeout* indique une valeur de délai d'attente en millisecondes, ou 'infini' pour aucun délai d'attente. Lorsqu'un délai d'attente se produit, les actions suivantes se produisent :

- `response_time` est défini sur la valeur du délai d'attente, ou plutôt sur le temps qu'il faut pour qu'un délai d'attente soit enregistré, ce qui peut varier légèrement par rapport à la valeur du délai d'attente.
- `response` est défini sur 'None'. Cela signifie que vous pouvez spécifier 'None' comme réponse correcte lorsqu'un délai d'attente doit se produire; cela peut être utile, par exemple, dans une tâche de type go/no-go, lorsque le participant doit retenir une réponse lors des essais de type no-go.