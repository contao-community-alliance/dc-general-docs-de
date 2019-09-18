.. _manual_edit-override-all:

Mehrfachbearbeitung (edit/overrideAll)
======================================

Der DCG bringt ein eigenes Tool für die Mehrfachbearbeitung mit,
welches einen erweiterten Funktionsumfang gegenüber der Standardmethode
von Contao hat.

Die Vorteile sind:

* Vor-, Zurück- und Beenden-Button
* es werden nur die Properties für die Bearbeitungsauswahl angezeigt,
  die für das Widget relevant sind; werden verschiedenartige Widgets
  ausgewählt, ist nur noch die gemeinsame Schnittmenge an Properties
  sichtbar
* es stehen zwei weitere `eval`-Parameter für das DCA zur Verfügung
  als `doNotEditMultiple` und `doNotOverrideMultiple`

Die zusätzlichen DCA-Parameter für die Mehrfachbearbeitung haben folgende
Einsatzmöglichkeit:

* `doNotEditMultiple` - verhindert für ein Feld das Editieren in der
  Mehrfachberabeitung
* `doNotOverrideMultiple` - verhindert für ein Feld das Überschreiben
  in der Mehrfachberabeitung; z.B. Feldern, die Unique bleiben müssen
  wie Spaltennamen für Tabellen.

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

