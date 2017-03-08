<div class="ClassDoc YAMLDoc" id="pool" markdown="1">

# class __pool__

The `pool` object provides dict-like access to the file pool. When
checking whether a file is in the file pool, several folders are
searched. For more details, see [folders].

In addition to the functions listed below, the following semantics are
supported:

__Example 1__:

~~~ .python
# Get the full path to a file in the file pool
print(u'The full path to img.png is %s' %  pool[u'img.png'])
# Check if a file is in the file pool
if u'img.png' in pool:
        print(u'img.png is in the file pool')
# Delete a file from the file pool
del pool[u'img.png']
# Walk through all files in the file pool. This retrieves the full
# paths.
for path in pool:
        print(path)
# Check the number of files in the file pool
print(u'There are %d files in the file pool' % len(pool))
~~~

__Example 2__:

~~~ .python
# Get the full path to an image from the file pool and show it
if u'img.png' in pool:
        print(u'img.png could not be found!')
else:
        image_path = pool[u'img.png']
        my_canvas = canvas()
        my_canvas.image(image_path)
        my_canvas.show()
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="pool-add" markdown="1">

## function __pool\.add__\(path, new\_name=None\)

Copies a file to the file pool.

__Example:__

~~~ .python
pool.add(u'/home/username/Pictures/my_ing.png')
~~~

__Arguments:__

- `path` -- The full path to the file on disk.
	- Type: str, unicode

__Keywords:__

- `new_name` -- A new name for the file in the pool, or None to use the file's original name.
	- Type: str, NoneType
	- Default: None

</div>

[pool.add]: #pool-add
[add]: #pool-add

<div class="FunctionDoc YAMLDoc" id="pool-fallback_folder" markdown="1">

## function __pool\.fallback\_folder__\(\)

No description specified.

__Example:__

~~~ .python
if pool.fallback_folder() is not None:
        print(u'There is a fallback pool folder!')
~~~

__Returns:__

The full path to the fallback pool folder, which is the `__pool__` subfolder of the current experiment folder, or `None` if this folder does not exist. The fallback pool folder is mostly useful in combination with a [versioning system](/miscellaneous/git/).

- Type: unicode, NoneType

</div>

[pool.fallback_folder]: #pool-fallback_folder
[fallback_folder]: #pool-fallback_folder

<div class="FunctionDoc YAMLDoc" id="pool-files" markdown="1">

## function __pool\.files__\(\)

Returns all files in the file pool.

__Example:__

~~~ .python
for path in pool.files():
        print(path)
# Equivalent to:
for path in pool:
        print(path)
~~~

__Returns:__

A list of full paths.

- Type: list

</div>

[pool.files]: #pool-files
[files]: #pool-files

<div class="FunctionDoc YAMLDoc" id="pool-folder" markdown="1">

## function __pool\.folder__\(\)

No description specified.

__Example:__

~~~ .python
print(u'The pool folder is here: ' % pool.folder())
~~~

__Returns:__

The full path to the (main) pool folder. This is typically a temporary folder that is deleted when the experiment is finished.

- Type: unicode

</div>

[pool.folder]: #pool-folder
[folder]: #pool-folder

<div class="FunctionDoc YAMLDoc" id="pool-folders" markdown="1">

## function __pool\.folders__\(include\_fallback\_folder=True, include\_experiment\_path=False\)

Gives a list of all folders that are searched when retrieving the
full path to a file. These are (in order):

1. The file pool folder itself, as returned by [folder].
2. The folder of the current experiment (if it exists)
3. The fallback pool folder, as returned by [fallback_folder]
   (if it exists)

__Example:__

~~~ .python
print(u'The following folders are searched for files:')
for folder in pool.folders():
        print(folder)
~~~

__Keywords:__

- `include_fallback_folder` -- Indicates whether the fallback pool folder should be included if it exists.
	- Type: bool
	- Default: True
- `include_experiment_path` -- Indicates whether the experiment folder should be included if it exists.
	- Type: bool
	- Default: False

__Returns:__

A list of all folders.

- Type: list

</div>

[pool.folders]: #pool-folders
[folders]: #pool-folders

<div class="FunctionDoc YAMLDoc" id="pool-in_folder" markdown="1">

## function __pool\.in\_folder__\(path\)

Checks whether path is in the pool folder. This is different from the `path in pool` syntax in that it only checks the main pool folder, and not the fallback pool folder and experiment folder.

__Arguments:__

- `path` -- A file basename to check.
	- Type: str

__Returns:__

No description

- Type: bool

</div>

[pool.in_folder]: #pool-in_folder
[in_folder]: #pool-in_folder

<div class="FunctionDoc YAMLDoc" id="pool-rename" markdown="1">

## function __pool\.rename__\(old\_path, new\_path\)

Renames a file in the pool folder.

__Example:__

~~~ .python
pool.rename(u'my_old_img.png', u'my_new_img.png')
~~~

__Arguments:__

- `old_path` -- The old file name.
	- Type: str, unicode
- `new_path` -- The new file name.
	- Type: str, unicode

</div>

[pool.rename]: #pool-rename
[rename]: #pool-rename

<div class="FunctionDoc YAMLDoc" id="pool-size" markdown="1">

## function __pool\.size__\(\)

No description specified.

__Example:__

~~~ .python
print(u'The size of the file pool is %d bytes' % pool.size())
~~~

__Returns:__

The combined size in bytes of all files in the file pool.

- Type: int

</div>

[pool.size]: #pool-size
[size]: #pool-size

</div>

[pool]: #pool

