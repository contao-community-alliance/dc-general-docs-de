Willkommen zu DC_General!
=========================

Dies ist die offizielle Dokumentation des `DC_General <https://github.com/contao-community-alliance/dc-general>`_,
eine Erweiterung für das `Contao CMS <https://contao.org>`_.

Mit der Erweiterung DC_General ist eine Alternative für den im Contao-Core enthaltenen DC_Table. Der
`DC_Table <https://github.com/contao/core-bundle/blob/master/src/Resources/contao/drivers/DC_Table.php>`_
ist als "Driver" in erster Linie für die Datenmanipulation wie z.B. Datensatz speichern, kopieren und
löschen zuständig - zudem ist im DC_Table auch das Mehrfachbearbeiten implementiert. Weiterhin kümmert
sich der DC_Table um die Anzeige der Daten im Backend z.B. für die Listenansichten oder die Eingabemasken.

Der aktuelle DC_Table ist im Verlauf seiner Entwicklung zu einem
recht "monolithischem Gebilde" herangewachsen, so dass die Erweiterung und Modernisierung sehr schwierig 
bis unmöglich ist. Zudem ist es nicht möglich, den Code per `Unittest <https://phpunit.de/>`_ zu prüfen.

Aufgrund dieser Schwierigkeiten wurde der `DC_General <https://github.com/contao-community-alliance/dc-general>`_
als moderner "Data container" entwickelt und nutzt die Möglichkeiten, die sich aus einer modernen OOP
sowie dem Einsatz von Symfony ergeben, bestens aus. Der DC_General ist gegenüber dem DC_Table `"Event driven"
<https://easysolutionsit.de/artikel/ck2018-event-driven-development.html>`_, hat eine Abstraktion der Datenquelle
sowie eine verbesserte Konfiguration der Abhängigkeiten zwischen Datacontainers.

Wird der DC_General in eigene Erweiterungen implementiert stehen vielfältige Manipulationsmöglichkeiten
für die Daten und das Contao-Backend über Events zur Verfügung. Mehr zu den zu den Funktionen unter...

Der DC_General ist in einigen großen Erweiterungen wie `MetaModels <https://github.com/MetaModels>`_,
`Avisota <https://github.com/avisota>`_, `syncCto <http://www.contao-synccto.de>`_ oder `Language2File <http://menatwork.github.io/language-doku>`_
implementiert.

Die gängige Abkürzung für den DC_General ist 'DCG'.

Diese Dokumentation gliedert sich in drei Bereiche:

    :ref:`index_manual` - Hier werden generelle Sachen des DCG dokumentiert.

    :ref:`index_cookbook` - Workflows und 'Best practice'-Beispiele um mit dem DCG zu arbeiten.

    :ref:`index_reference` - Dokumentation über Events, Schnittstellen und vielem mehr.


Unterstützung und Spenden
-------------------------
Die Erweiterung DC_General ist eine kostenfreie Erweiterung auf der Basis von OpenSource und benötigt 
für eine kontinuierliche Weiterentwicklung die Unterstützung einer aktiven Community. Mitarbeit in 
Form von Programmierungen oder die Meldung von Fehlern sowie eigenen Workflows werden gern angenommen.

.. _index_manual:

Handbuch
--------

    .. toctree::
        :glob:
        :maxdepth: 1

        manual/introduction
        manual/install
        manual/data-container
        manual/edit-override-all

.. _index_cookbook:

Kochbuch
--------

    .. toctree::
        :glob:
        :maxdepth: 1

        cookbook/*

.. _index_reference:

Referenz
--------

    .. toctree::
        :glob:
        :maxdepth: 1

        reference/index
        imprint/index

