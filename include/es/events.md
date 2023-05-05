### cambio_experimento

Disparado en: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'cambio_experimento')
```

### cambio_elemento

Disparado en: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'cambio_elemento', nombre=self.name)
```

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'cambio_elemento', nombre=self.name)
```

Disparado en: [loop.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/loop.py)

```python
extension_manager.fire(u'cambio_elemento', nombre=self.name)
```

### cerrar

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'cerrar')
```

### eliminar_elemento

Disparado en: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'eliminar_elemento', nombre=nombre)
```

### latido_corazon

Disparado en: [multiprocess_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/multiprocess_runner.py)

```python
extension_manager.fire(u'latido_corazon')
```

### ide_saltar_a_linea

Disparado en: [SymbolSelector.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/SymbolSelector/SymbolSelector.py)

```python
extension_manager.fire('ide_saltar_a_linea', lineno=lineno)
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_saltar_a_linea', lineno=line_number)
```

### ide_nuevo_archivo

Disparado en: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'ide_nuevo_archivo', fuente=code, ext=ext)
```

### ide_guardar_archivo_actual

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('ide_guardar_archivo_actual')
```

### deteccion_anotaciones_imagen

Disparado en: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire(u'deteccion_anotaciones_imagen', code=code)
```

### excepcion_jupyter_ocurrida

Disparado en: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('excepcion_jupyter_ocurrida')
```

### finalizacion_ejecucion_jupyter

Disparado en: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('finalizacion_ejecucion_jupyter')
```

### resultado_texto_ejecucion_jupyter

Disparado en: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('resultado_texto_ejecucion_jupyter', texto=texto)
```

### inicio_ejecucion_jupyter

Disparado en: [transparent_jupyter_widget.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterConsole/jupyter_tabwidget/transparent_jupyter_widget.py)

```python
extension_manager.fire('inicio_ejecucion_jupyter')
```

### interrupcion_jupyter

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'interrupcion_jupyter')
```

### reiniciar_jupyter

Disparado en: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire(u'jupyter_restart')
```

### jupyter_run_code

Disparado en: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('jupyter_run_code',
                                                     code=command)
```

### jupyter_run_system_command

Disparado en: [JupyterNotebook.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/JupyterNotebook/JupyterNotebook.py)

```python
extension_manager.fire('jupyter_run_system_command', cmd=cmd)
```

### jupyter_show_prompt

Disparado en: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_show_prompt')
```

### jupyter_write

Disparado en: [console_bridge.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/console_bridge.py)

```python
extension_manager.fire(u'jupyter_write', msg=s)
```

### new_item

Disparado en: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire(u'new_item', name=item.name,
				_type=item.item_type)
```

### new_linked_copy

Disparado en: [tree_overview.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/tree_overview.py)

```python
extension_manager.fire('new_linked_copy', name=item_name)
```

### notify

Disparado en: [sequence.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/sequence.py)

```python
extension_manager.fire(u'notify',
					message=_(u'Sequence contains non-existing item: %s')
```

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is set to a variable or '
						u'unknown value and can only be edited through '
						u'the script.')
```

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						'variables and can only be edited through the '
						'script.')
```

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'notify',
						message=_(u'"%s" is defined using '
						u'variables or has an invalid value, and can only be '
						u'edited through the script.')
```

Disparado en: [logger.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/logger.py)

```python
extension_manager.fire(u'notify',
					message=_(u'You have multiple unlinked loggers. This can lead to messy log files.')
```

Disparado en: [sketchpad_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/sketchpad_widget.py)

```python
extension_manager.fire(u'notify', message=notification,
				category=u'info')
```

### open_experiment

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'open_experiment', path=path)
```

### open_item

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'open_item', name=self.name)
```

### pause_experiment

Disparado en: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'pause_experiment')
```

### prepare_change_experiment

Disparado en: [general_properties.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/general_properties.py)

```python
extension_manager.fire(u'prepare_change_experiment')
```

### prepare_delete_item

Disparado en: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_delete_item', name=name)
```

### prepare_open_item

Disparado en: [qtitem.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtitem.py)

```python
extension_manager.fire(u'prepare_open_item', name=self.name)
```

### prepare_purge_unused_items

Disparado en: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'prepare_purge_unused_items')
```

### prepare_regenerate

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'prepare_regenerate')
```

### prepare_rename_item

Disparado en: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'prepare_rename_item', from_name=from_name,
			to_name=to_name)
```

### purge_unused_items

Disparado en: [unused_widget.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/widgets/unused_widget.py)

```python
extension_manager.fire(u'purge_unused_items')
```

### pyqode_clear_breakpoints

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_clear_breakpoints')
```

### pyqode_resume_auto_backend_restart

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_resume_auto_backend_restart')
```

### pyqode_select_indentation_mode

Disparado en: [menubar.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/opensesame_ide/menubar.py)

```python
extension_manager.fire('pyqode_select_indentation_mode')
```

### pyqode_suspend_auto_backend_restart

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('pyqode_suspend_auto_backend_restart')
```

### regenerate

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'regenerate')
```

### register_editor

Disparado en: [qtplugin.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/items/qtplugin.py)

```python
extension_manager.fire(u'register_editor', editor=editor)
```

### rename_item

Disparado en: [qtitem_store.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/misc/qtitem_store.py)

```python
extension_manager.fire(u'rename_item', from_name=from_name,
			to_name=to_name)
```

### resume_experiment

Disparado en: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire(u'resume_experiment')
```

### run_experiment_canceled

Disparado en: [base_runner.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/runners/base_runner.py)

```python
extension_manager.fire('run_experiment_canceled')
```

### save_experiment

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'save_experiment', path=self.current_path)
```

### startup

Disparado en: [qtopensesame.py](https://github.com/open-cogsci/OpenSesame/blob/master/libqtopensesame/qtopensesame.py)

```python
extension_manager.fire(u'startup')
```

### unregister_editor

Disparado en: [OpenSesameIDE.py](https://github.com/open-cogsci/rapunzel/blob/master/opensesame_extensions/OpenSesameIDE/OpenSesameIDE.py)

```python
extension_manager.fire('unregister_editor', editor=editor)
```