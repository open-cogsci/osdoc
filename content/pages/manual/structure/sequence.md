title: Doing things in sequence

The SEQUENCE item has two important functions:

- It runs multiple other items one after another.
- It determines which items should, and which shouldn't, be run.

SEQUENCEs are run from top to bottom; that is, the item at the top is run first. The order of a SEQUENCE is always sequential.

## Run-if expressions

You can use run-if expressions to determine whether or not a particular item should be run. For example, if you want a display to be presented only if a participant has made an incorrect response, you can set the run-if expressions for that item to:

```python
{correct} == 0
```

If you leave the run-if expressions empty or enter `True`, the item will always be run. Run-if expressions use the same syntax as other conditional expressions. For more information, see:

- %link:manual/variables%

Run-if expressions only affect which items are run, not which items are prepared. Phrased differently, the Prepare phase of all items in a SEQUENCE is always executed, regardless of the run-if expressions. See also:

- %link:prepare-run%


## Disabling items

To completely disable an item in a SEQUENCE, right-click on it and select 'Disable'. This is mostly useful during development of your experiment, for example to temporarily bypass the instructions.
