# OSDOC Organizer

The osdoc organizer is a simple GUI to restructure the documentation site. You can select an item and press `+` to move the item down, and `-` to move the item up. Press `r` to refresh the overview. The content folder should be passed as the final command line argument:
	
	python qtorganizer /path/to/content
	
To perform a dry run, without any changes to disk, you can pass the `--dry` arguments:
	
	python qtorganizer --dry /path/to/content