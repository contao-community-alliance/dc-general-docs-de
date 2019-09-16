.. _manual_data-container:

Data-Container erstellen
========================

Der Data-Container mit dem DCG wird analog wie mit dem DC_Table über die
Konfiguration des DCA erstellt.

Als erster Punkt wird im Knoten ``config`` der Data-Container auf den 
DCG per ``General`` umgestellt.

.. code-block:: yaml

   $GLOBALS['TL_DCA']['tl_my_table'] = array
   (
       // Config
       'config' => array
       (
           // Replace the data container Table with General.
           'dataContainer'    => 'General'
           'notCopyable'      => true, // wird erst ab DCG 2.2 untertützt
           'enableVersioning' => true, // wird erst ab DCG 2.2 untertützt
           'sql' => array
           (
               'keys' => array
               (
                   'id' => 'primary'
               )
           )
           // *_callback per Event
       ),
       ...

Die übrigen, möglichen Parameter bei ``config`` können wie bei DC_Table eingesetzt werden.
Der Knoten ``ctable`` für Kindtabellen ist nicht notwendig und wird dafür im Knoten
``data_provider`` behandelt (s.u.).

Die Callbacks könnten wie gehabt in ``config`` eingetragen werden und werden von dem
DCG-Legacy-Builder mit in die Abarbeitung übernommen - besser ist es,
die Aufgaben einen entsprechenden Event-Listener zu übergeben.

Der Standard-Datenprovider (Datentabelle) wird Knoten ``data_provider``
in ``data_provider`` angegeben.

.. code-block:: yaml

   $GLOBALS['TL_DCA']['tl_my_table'] = array
   (
       ...
       // Add the data container configuration.
       'dca_config' => array
       (
           // Configure the data provider and all child data provider.
           'data_provider' => array
           (
               // The default data provider, for this data container.
               'default' => array
               (
                   'source' => 'tl_my_table'
               ),


Gibt es Kindtabellen, werden ebenfalls diese im Knoten ``data_provider`` angegeben -
beim DC_Table würde das in ``ctable`` erfolgen.

.. code-block:: yaml

   $GLOBALS['TL_DCA']['tl_my_table'] = array
   (
       ...
       // Add the data container configuration.
       'dca_config' => array
       (
           // Configure the data provider and all child data provider.
           'data_provider' => array
           (
               ...
               // The child data provider for all children are has related to this and has their child relation.
               // This must configure so when you delete this theme are all relations deletes too. (deep delete)
               'tl_my_child' => array
               (
                   'source' => 'tl_my_child'
               ),
               ...

Mit der Konfiguration der Kindtabelle(n) wird automatisch ein `deep delete`
konfiguriert, d.h. wenn der Elterndatensatz gelöscht wird, werden automatisch
auch alle Kind-Datensätze gelöscht.

Die Beziehung zwischen einer Kind- zur Eltern-Tabelle wird in den ``childCondition``
definiert.

.. code-block:: yaml

   $GLOBALS['TL_DCA']['tl_my_table'] = array
   (
       ...
       // Add the data container configuration.
       'dca_config' => array
       (
       ...
        // Add the child condition. This will announce the relations.
        'childCondition' => array
        (
           array
           (
               'from'    => 'tl_my_table',
               'to'      => 'tl_my_child',
               'setOn'   => array
               (
                   array
                   (
                       'to_field'   => 'pid',
                       'from_field' => 'id',
                   ),
               ),
               'filter'  => array
               (
                   array
                   (
                       'local'     => 'pid',
                       'remote'    => 'id',
                       'operation' => '=',
                   ),
               ),
               'inverse' => array
               (
                   array
                   (
                       'local'     => 'pid',
                       'remote'    => 'id',
                       'operation' => '=',
                   ),
               )
           ),
           ...

Der Knoten ``inverse`` ist optional, aber beschleunigt
die Datenbankabfrage für eine Abfrage vom Kind- zur Elterntabelle.

Die Konfiguration für eine Kindtabelle ist analog der Elterntabelle.
Beim ``data_provider`` wird statt ``default`` die Tabelle für ``parent``
angegeben.

.. code-block:: yaml

   $GLOBALS['TL_DCA']['tl_my_child'] = array
   (
       // Config
       'config' => array
       (
           'dataContainer'               => 'General',
       ),
       // Add the data container configuration.
       'dca_config' => array
       (
           // Configure the data provider and all child data provider.
           'data_provider' => array
           (
               // The default data provider, for this data container.
               'parent' => array
               (
                   'source' => 'tl_my_table'
               )
           ),
           // Add the child condition. This will announce the relations.
           'childCondition' => array
           (
               array
               (
                   'from'    => 'tl_my_table',
                   'to'      => 'tl_my_child',
                   'setOn'   => array
                   (
                       array
                       (
                           'to_field'   => 'pid',
                           'from_field' => 'id',
                       ),
                   ),
                   'filter'  => array
                   (
                       array
                       (
                           'local'     => 'pid',
                           'remote'    => 'id',
                           'operation' => '=',
                       ),
                   ),
                   'inverse' => array
                   (
                       array
                       (
                           'local'     => 'pid',
                           'remote'    => 'id',
                           'operation' => '=',
                       ),
                   )
               )
           )
       ),

Die übrigen Parameter im DCA werden analog dem üblichen Vorgehen
wie bei einem "DC_Table-Projekt" vorgenommen. Die Einstellungen
können an einer `Beispielkonfiguration für tl_theme
<https://github.com/contao-community-alliance/dc-general-example/blob/master/example/example-1/example-1.md>`_
nachvollzogen werden.