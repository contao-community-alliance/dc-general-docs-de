.. _manual_edit-override-all:

Mehrfachbearbeitung (edit/overrideAll)
======================================

Der DCG bringt eine eigene Mehrfachbearbeitung mit, welche einen
erweiterten Funktionsumfang gegenüber der Standardmethode von
Contao hat. Die Mehrfachbearbeitung wird automatisch mit der
Definition `general`im DCA aktiviert (siehe :ref:`manual_data-container`).

Die Vorteile sind:

* Vor-, Zurück- und Beenden-Button
* es werden nur die Properties für die Bearbeitungsauswahl angezeigt,
  die für die Bearbeitung relevant sind; werden verschiedenartige Widgets
  ausgewählt, ist nur noch die gemeinsame Schnittmenge an Properties
  sichtbar
* es stehen zwei weitere `eval`-Parameter für das DCA zur Verfügung
  als `doNotEditMultiple` und `doNotOverrideMultiple` für Ansteuerung
  der Sichtbarkeit für den jeweiligen Bearbeitungstyp.

Die zusätzlichen DCA-Parameter für die Mehrfachbearbeitung haben folgende
Einsatzmöglichkeit:

* `doNotEditMultiple` - verhindert für ein Property das Editieren in der
  Mehrfachberabeitung
* `doNotOverrideMultiple` - verhindert für ein Property das Überschreiben
  in der Mehrfachberabeitung; z.B. Properties, die Unique bleiben müssen
  wie Spaltennamen für Tabellen von MetaModels.

Ein Beispiel für einen DCA-Eintrag:

.. code-block:: php

   $GLOBALS['TL_DCA']['tl_my_table'] = array
   (
      ...
       'fields' => array
       (
           'my_field' => array
           (
               ...
               'eval' => array(
                   'doNotEditMultiple'     => true, // Hide at editAll.
                   'doNotOverrideMultiple' => true, // Hide at overrideAll.
              ...

