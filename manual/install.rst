.. _manual_install:

DCG installieren und aktualisieren
==================================

Der DCG wird üblicher Weise in einem eigenen Projekt über die Angabe
"require" in der composer.json eingebunden:

.. code-block:: yaml

    ...
    "require": {
        "php": "^7.1",
        "contao-community-alliance/dc-general": "^2.1",
        ...
    }
    ...

Es ist aber auch möglich, den DCG manuell über den Contao Manager oder
über die Konsole zu installieren. Für die Konsole erfolgt die Installation
mit

``php web/contao-manager.phar.php composer require contao-community-alliance/dc-general``

Über den Contao Manager bzw. "composer update" wird der DCG aktuell gehalten.