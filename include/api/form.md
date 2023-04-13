<div class="ClassDoc YAMLDoc" markdown="1">

# class __Form__

The `Form` is a container for widgets, such as labels, etc. If you use
the FORM_BASE plug-in in combination with OpenSesame script, you do not
need to explicitly create a `Form` object. However, if you use Python
inline code, you do.

__Example__:

~~~ .python
form = Form()
label =
Label(text='label)
form.set_widget(label, (0,0))
form._exec()
~~~

[TOC]

## cell_index(pos)

Converts a position to a cell index. A cell index corresponds to
the number of the cell in the form, from left-to-right, top-to-bottom.


__Parameters__

- **pos**: A position in the form, which can be an index (int) or a (column,
row) tuple.

__Returns__

- A cell index.


## get_cell(index)

Returns the position of a widget

Arguments:
index -- the index of the widget

Returns:
A (column, row, column_span, row_span) tuple



## get_rect(index)

Returns the boundary area for a given cell

Arguments:
index -- a cell index

Returns:
A (left, top, width, height) tuple



## render(self)

Shows the form canvas without any user interaction.




## set_widget(widget, pos, colspan=1, rowspan=1)

Adds a widget to the form.


__Parameters__

- **widget**: The widget to add.
- **pos**: The position to add the widget, which can be an index or a (column,
row) tuple.
- **colspan**: The number of columns that the widget should span.
- **rowspan**: The number of rows that the widget should span.


## timed_out(self)

visible: False

returns:
        desc:   True if a timeout occurred, False otherwise.
        type:   bool



## xy_to_index(xy)

Converts a coordinate in pixels to a cell index. This allows you to
determine on which widget a user has clicked.


__Parameters__

- **xy**: An (x,y) coordinates tuple.

__Returns__

- A cell index.


</div>

