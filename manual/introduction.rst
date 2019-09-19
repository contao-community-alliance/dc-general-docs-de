.. _introdution_dcg:

Vorstellung des DCG
===================

Das Handbuch richtet sich an Entwickler, die Erweiterungen für `Contao <https://contao.org>`_
programmieren oder bestehende Erweiterungen auf Basis des DC_General anpassen möchten.

Die Erweiterung DC_General ist eine Alternative für den im Contao-Core enthaltenen DC_Table. Der
`DC_Table <https://github.com/contao/core-bundle/blob/master/src/Resources/contao/drivers/DC_Table.php>`_
ist als "Datencontainer-Treiber" in erster Linie für die Datenmanipulation wie z.B. Datensatz
speichern, kopieren und löschen zuständig - zudem ist im DC_Table auch das Mehrfachbearbeiten
eigenständig implementiert. Weiterhin kümmert sich der DC_Table um die Anzeige der Daten
im Backend z.B. für die Listenansichten oder die Eingabemasken.

.. _introdution_vergleich_dcg_dct:

Der DCG im Vergleich zum DC_Table
---------------------------------

Der DCG hat im Vergleich zum DC_Table folgende Vorteile:

* Event Driven
* Objektbasierte Abstraktion der Definitionen
* Abstraktion der Datenquelle
* Verbesserte Konfiguration der Abhängigkeiten zwischen Datacontainers
* modularer Aufbau
* Prüfung der Daten vor Speicherung - nur wenn Daten konsistent sind, wird gespeichert
* Deep-Delete ohne anladen der referenzierten Datacontainer, mehr Variabilität
  da nicht abhängig von ptable-Bezug

Der DCG unterstützt alle :ref:`Callback-Aufrufe <reference_callbacks>` von Contao und
leitet diese in die eigenen Events um.


Ressourcen
----------

* `DCG auf Github <https://github.com/contao-community-alliance/dc-general>`_
* `DCG Handbuch auf Github <https://github.com/contao-community-alliance/dc-general-docs-de>`_
