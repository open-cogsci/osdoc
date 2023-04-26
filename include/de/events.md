### change_experiment

Ausgelöst in: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'change_experiment')
```

### change_item

Ausgelöst in: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

Ausgelöst in: [loop.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/loop.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

### close

Ausgelöst in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'close')
```

### delete_item

Ausgelöst in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'delete_item', name=name)
```

### heartbeat

Ausgelöst in: [multiprocess_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/multiprocess_runner.py)

```python
extension_manager.fire(u'heartbeat')
```

### ide_jump_to_line

Ausgelöst in: [SymbolSelector.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/SymbolSelector/SymbolSelector.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=lineno)
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=line_number)
```

### ide_new_file

Ausgelöst in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'ide_new_file', source=code, ext=ext)
```

### ide_save_current_file

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_save_current_file')
```

### image_annotations_detect

Ausgelöst in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'image_annotations_detect', code=code)
```

### jupyter_exception_occurred

Ausgelöst in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_exception_occurred')
```

### jupyter_execute_finished

Ausgelöst in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_finished')
```

### jupyter_execute_result_text

Ausgelöst in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_result_text', text=text)
```

### jupyter_execute_start

Ausgelöst in: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_start')
```

### jupyter_interrupt

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_interrupt')
```

### jupyter_restart

Ausgelöst in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_restart')
```

### jupyter_run_code

Ausgelöst in: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('jupyter_run_code',
                                                     code=command)
```

### jupyter_run_system_command

Ausgelöst in: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire('jupyter_run_system_command', cmd=cmd)
```

### jupyter_show_prompt

Ausgelöst in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_show_prompt')
```

### jupyter_write

Ausgelöst in: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_write', msg=s)
```

### new_item

Ausgelöst in: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire(u'new_item', name=item.name,
				_type=item.item_type)
```

### new_linked_copy

Ausgelöst in: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire('new_linked_copy', name=item_name)
```

### notify

Ausgelöst in: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'notify',
					message=_(u'Sequence contains non-existing item: %s')
```

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is set to a variable or '
						u'unknown value and can only be edited through '
						u'the script.')
```

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						'variables and can only be edited through the '
						'script.')
```

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						u'variables or has an invalid value, and can only be '
						u'edited through the script.')
```

Ausgelöst in: [logger.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/logger.py)

```python
extension_manager.fire(u'notify',
					message=_(u'You have multiple unlinked loggers. This can lead to messy log files.')
```

Ausgelöst in: [sketchpad_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/sketchpad_widget.py)

```python
extension_manager.fire(u'notify', message=notification,
				category=u'info')
```

### open_experiment

Ausgelöst in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'open_experiment', path=path)
```

### open_item

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'open_item', name=self.name)
```

### pause_experiment

Ausgelöst in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'pause_experiment')
```

### prepare_change_experiment

Ausgelöst in: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'prepare_change_experiment')
```

### prepare_delete_item

Ausgelöst in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_delete_item', name=name)
```

### prepare_open_item

Ausgelöst in: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'prepare_open_item', name=self.name)
```

### prepare_purge_unused_items

Ausgelöst in: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'prepare_purge_unused_items')
```

### prepare_regenerate

Ausgelöst in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'prepare_regenerate')
```

### prepare_rename_item

Ausgelöst in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_rename_item', from_name=from_name,
			to_name=to_name)
```

### purge_unused_items

Ausgelöst in: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'purge_unused_items')
```

### pyqode_clear_breakpoints

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_clear_breakpoints')
```

### pyqode_resume_auto_backend_restart

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

### pyqode_select_indentation_mode

Ausgelöst in: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('pyqode_select_indentation_mode')
```

### pyqode_suspend_auto_backend_restart

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Ausgelöst in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

### regenerate

Ausgelöst in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

Ausgeführt in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'neu_generieren')
```

### register_editor

Ausgeführt in: [qtplugin.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtplugin.py)

```python
extension_manager.fire(u'register_editor', editor=editor)
```

### rename_item

Ausgeführt in: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'benenne_item_um', from_name=from_name,
			to_name=to_name)
```

### resume_experiment

Ausgeführt in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'fortsetzen_experiment')
```

### run_experiment_canceled

Ausgeführt in: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire('lauf_experiment_abgebrochen')
```

### save_experiment

Ausgeführt in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'speichern_experiment', path=self.current_path)
```

### startup

Ausgeführt in: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'startup')
```

### unregister_editor

Ausgeführt in: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('editor_abmelden', editor=editor)
```