### change_experiment

Fired in: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'change_experiment')
```

### change_item

Fired in: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

Fired in: [loop.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/loop.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

### close

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'close')
```

### delete_item

Fired in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'delete_item', name=name)
```

### heartbeat

Fired in: [multiprocess_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/multiprocess_runner.py)

```python
extension_manager.fire(u'heartbeat')
```

### ide_jump_to_line

Fired in: [SymbolSelector.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/SymbolSelector/SymbolSelector.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=lineno)
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=line_number)
```

### ide_new_file

Fired in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'ide_new_file', source=code, ext=ext)
```

### ide_save_current_file

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_save_current_file')
```

### image_annotations_detect

Fired in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'image_annotations_detect', code=code)
```

### jupyter_exception_occurred

Fired in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_exception_occurred')
```

### jupyter_execute_finished

Fired in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_finished')
```

### jupyter_execute_result_text

Fired in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_result_text', text=text)
```

### jupyter_execute_start

Fired in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_start')
```

### jupyter_interrupt

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_interrupt')
```

### jupyter_restart

Fired in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_restart')
```

### jupyter_run_code

Fired in: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('jupyter_run_code',
                                                     code=command)
```

### jupyter_run_system_command

Fired in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire('jupyter_run_system_command', cmd=cmd)
```

### jupyter_show_prompt

Fired in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_show_prompt')
```

### jupyter_write

Fired in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_write', msg=s)
```

### new_item

Fired in: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire(u'new_item', name=item.name,
				_type=item.item_type)
```

### new_linked_copy

Fired in: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire('new_linked_copy', name=item_name)
```

### notify

Fired in: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'notify',
					message=_(u'Sequence contains non-existing item: %s')
```

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is set to a variable or '
						u'unknown value and can only be edited through '
						u'the script.')
```

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						'variables and can only be edited through the '
						'script.')
```

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						u'variables or has an invalid value, and can only be '
						u'edited through the script.')
```

Fired in: [logger.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/logger.py)

```python
extension_manager.fire(u'notify',
					message=_(u'You have multiple unlinked loggers. This can lead to messy log files.')
```

Fired in: [sketchpad_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/sketchpad_widget.py)

```python
extension_manager.fire(u'notify', message=notification,
				category=u'info')
```

### open_experiment

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'open_experiment', path=path)
```

### open_item

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'open_item', name=self.name)
```

### pause_experiment

Fired in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'pause_experiment')
```

### prepare_change_experiment

Fired in: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'prepare_change_experiment')
```

### prepare_delete_item

Fired in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_delete_item', name=name)
```

### prepare_open_item

Fired in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'prepare_open_item', name=self.name)
```

### prepare_purge_unused_items

Fired in: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'prepare_purge_unused_items')
```

### prepare_regenerate

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'prepare_regenerate')
```

### prepare_rename_item

Fired in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_rename_item', from_name=from_name,
			to_name=to_name)
```

### purge_unused_items

Fired in: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'purge_unused_items')
```

### pyqode_clear_breakpoints

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_clear_breakpoints')
```

### pyqode_resume_auto_backend_restart

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

### pyqode_select_indentation_mode

Fired in: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('pyqode_select_indentation_mode')
```

### pyqode_suspend_auto_backend_restart

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

### regenerate

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

### register_editor

Fired in: [qtplugin.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtplugin.py)

```python
extension_manager.fire(u'register_editor', editor=editor)
```

### rename_item

Fired in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'rename_item', from_name=from_name,
			to_name=to_name)
```

### resume_experiment

Fired in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'resume_experiment')
```

### run_experiment_canceled

Fired in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire('run_experiment_canceled')
```

### save_experiment

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'save_experiment', path=self.current_path)
```

### startup

Fired in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'startup')
```

### unregister_editor

Fired in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('unregister_editor', editor=editor)
```

