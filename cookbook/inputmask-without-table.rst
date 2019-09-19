.. _cookbook_inputmask-without-table:

Eingabemaske ohne Tabelle
=========================

Wir erstellen eine Eingabemaske, die direkt durch einen Navigationslink
im Backend aufgerufen wird und die Daten aber in keiner Tabelle gespeichert
werden.

In unserem Beispiel nutzen wir das für eine eigene Importmöglichkeit z.B. von
CSV-Dateien.

Als erstes benötigen wir einen Navigationslink in der Backend-Navigation in der
`config.php`. Anschließen manipulieren wir den Link, so dass wir direkt in einer
Eingabemaske landen. Die Manipulation erfolgt über einen Hook von Contao
`getUserNavigation` und binden den Hook als Service über die `service.yml`ein.

Im letzten Schritt erstellen wir die Widgets für die Eingabemaske per DCA-Definition
in einer `dcaconfig.php` und verarbeiten den Aufruf in einem EventListener. Das
Besondere an der DCA ist, dass hier der `NoOpDataProvider` zum Einsatz kommt, der die
übliche Speicherung in einer zugehörigen Tabelle unterbindet.

Die Dateien sind in einem `Beispiel <https://github.com/contao-community-alliance/dc-general-example/blob/master/example/example-3/example-3.md>`_
zusammengefasst.