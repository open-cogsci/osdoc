### change_experiment

触发于：[general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'change_experiment')
```

### change_item

触发于：[sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

触发于：[qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

触发于：[loop.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/loop.py)

```python
extension_manager.fire(u'change_item', name=self.name)
```

### close

触发于：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'close')
```

### delete_item

触发于：[qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'delete_item', name=name)
```

### heartbeat

触发于：[multiprocess_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/multiprocess_runner.py)

```python
extension_manager.fire(u'heartbeat')
```

### ide_jump_to_line

触发于：[SymbolSelector.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/SymbolSelector/SymbolSelector.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=lineno)
```

触发于：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_jump_to_line', lineno=line_number)
```

### ide_new_file

触发于：[JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'ide_new_file', source=code, ext=ext)
```

### ide_save_current_file

触发于：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_save_current_file')
```

### image_annotations_detect

触发于：[JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'image_annotations_detect', code=code)
```

### jupyter_exception_occurred

触发于：[transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_exception_occurred')
```

### jupyter_execute_finished

触发于：[transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_finished')
```

### jupyter_execute_result_text

触发于：[transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_result_text', text=text)
```

### jupyter_execute_start

触发于：[transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('jupyter_execute_start')
```

### jupyter_interrupt

触发于：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_interrupt')
```

### jupyter_restart

在 [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py) 中触发：

```python
extension_manager.fire(u'jupyter_restart')
```

在 [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py) 中触发：

```python
extension_manager.fire(u'jupyter_restart')
```

### jupyter_run_code

在 [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py) 中触发：

```python
extension_manager.fire('jupyter_run_code',
                                                     code=command)
```

### jupyter_run_system_command

在 [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py) 中触发：

```python
extension_manager.fire('jupyter_run_system_command', cmd=cmd)
```

### jupyter_show_prompt

在 [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py) 中触发：

```python
extension_manager.fire(u'jupyter_show_prompt')
```

### jupyter_write

在 [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py) 中触发：

```python
extension_manager.fire(u'jupyter_write', msg=s)
```

### new_item

在 [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py) 中触发：

```python
extension_manager.fire(u'new_item', name=item.name,
				_type=item.item_type)
```

### new_linked_copy

在 [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py) 中触发：

```python
extension_manager.fire('new_linked_copy', name=item_name)
```

### notify

在 [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py) 中触发：

```python
extension_manager.fire(u'notify',
					message=_(u'Sequence contains non-existing item: %s')
```

在 [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py) 中触发：

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is set to a variable or '
						u'unknown value and can only be edited through '
						u'the script.')
```

在 [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py) 中触发：

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						'variables and can only be edited through the '
						'script.')
```

在 [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py) 中触发：

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						u'variables or has an invalid value, and can only be '
						u'edited through the script.')
```

在 [logger.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/logger.py) 中触发：

```python
extension_manager.fire(u'notify',
					message=_(u'You have multiple unlinked loggers. This can lead to messy log files.')
```

在 [sketchpad_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/sketchpad_widget.py) 中触发：

```python
extension_manager.fire(u'notify', message=notification,
				category=u'info')
```

### open_experiment

在 [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py) 中触发：

```python
extension_manager.fire(u'open_experiment', path=path)
```

### open_item

在 [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py) 中触发：

```python
extension_manager.fire(u'open_item', name=self.name)
```

### pause_experiment

在 [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py) 中触发：

```python
extension_manager.fire(u'pause_experiment')
```

### prepare_change_experiment

在：[general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'prepare_change_experiment')
```

### prepare_delete_item

在：[qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_delete_item', name=name)
```

### prepare_open_item

在：[qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'prepare_open_item', name=self.name)
```

### prepare_purge_unused_items

在：[unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'prepare_purge_unused_items')
```

### prepare_regenerate

在：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'prepare_regenerate')
```

### prepare_rename_item

在：[qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_rename_item', from_name=from_name,
			to_name=to_name)
```

### purge_unused_items

在：[unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'purge_unused_items')
```

### pyqode_clear_breakpoints

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_clear_breakpoints')
```

### pyqode_resume_auto_backend_restart

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

### pyqode_select_indentation_mode

在：[menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('pyqode_select_indentation_mode')
```

### pyqode_suspend_auto_backend_restart

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

### regenerate

在：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

在：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

### register_editor

在：[qtplugin.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtplugin.py)

```python
extension_manager.fire(u'register_editor', editor=editor)
```

### rename_item

在：[qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'rename_item', from_name=from_name,
			to_name=to_name)
```

### resume_experiment

在：[base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'resume_experiment')
```

### run_experiment_canceled

在：[base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire('run_experiment_canceled')
```

### save_experiment

在：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'save_experiment', path=self.current_path)
```

### startup

在：[qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'startup')
```

### unregister_editor

在：[OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('unregister_editor', editor=editor)
```
