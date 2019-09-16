.. _reference_callbacks:

Callbacks als Event
===================

Die Callbacks aus DC_Table werden über den Legacy-Builder abgefangen
und im DCG verarbeitet. Es ist aber zu Empfehlen, statt des Callback-
Aufrufes den entsprechenden Event direkt zu verwenden.

Die Events werden als Service angesprochen und können damit auch mit
einer Priorität der Verarbeitungsreihenfolge versehen werden.

Folgend eine Auflistung, welcher Callback mit welchem Event seine
Ersetzung hat:

Callback in ``config``
----------------------

+-------------------+--------------------------------------+
| Callback          | Event                                |
+===================+======================================+
| onload_callback   | dc-general.factory.create-dc-general |
+-------------------+--------------------------------------+
| onsubmit_callback | dc-general.model.post-persist        |
+-------------------+--------------------------------------+
| ondelete_callback | dc-general.model.post-delete         |
+-------------------+--------------------------------------+
| oncut_callback    | dc-general.model.post-paste          |
+-------------------+--------------------------------------+
| oncopy_callback   | dc-general.model.post-duplicate      |
+-------------------+--------------------------------------+


Callback in ``list/sorting``
----------------------------

| Callback | Event |
| -------- | ----- |
| header_callback | dc-general.view.contao2backend.get-parent-header  |
| paste_button_callback | dc-general.view.contao2backend.get-paste-root-button  |
| paste_button_callback | dc-general.view.contao2backend.get-paste-button  |
| child_record_callback | dc-general.view.contao2backend.parent-view-child-record  |


Callback in ``list/label``
--------------------------

| Callback | Event |
| -------- | ----- |
| group_callback | dc-general.view.contao2backend.get-group-header  |
| label_callback | dc-general.view.contao2backend.model-to-label  |


Callback in ``list/global_operations``
--------------------------------------

| Callback | Event |
| -------- | ----- |
| button_callback | dc-general.view.contao2backend.get-global-button  |


Callback in ``list/operations``
-------------------------------

| Callback | Event |
| -------- | ----- |
| button_callback | dc-general.view.contao2backend.get-global-button  |


Callback in ``fields``
----------------------

| Callback | Event |
| -------- | ----- |
| load_callback | dc-general.view.contao2backend.decode-property-value-for-widget  |
| save_callback | dc-general.view.contao2backend.encode-property-value-from-widget  |
| options_callback | dc-general.view.contao2backend.get-property-options  |
| input_field_callback | dc-general.view.contao2backend.build-widget  |
| wizard | dc-general.view.contao2backend.manipulate-widget  |

