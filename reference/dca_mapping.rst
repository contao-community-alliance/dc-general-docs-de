.. _reference_dca_mapping:

DCA Mapping
==========

In der folgenden Auflistung sind alle bekannten Angaben zum DCA aufgeführt:


+----------------------------------------------------------------------------------------+---------------------------------------------+
| .. code-block:: php                                                                    | .. parsed-literal::                         |
|                                                                                        |                                             |
|     $GLOBALS['TL_DCA']['tl_example'] = array                                           |    -> `Data provider mapping`_              |
|     (                                                                                  |                                             |
|         // Config                                                                      |                                             |
|         'config' => array                                                              |                                             |
|         (                                                                              |                                             |
|             'label'              => &$GLOBALS['TL_LANG']['tl_example']['headline'],    |    -> `Listing mapping`_                    |
|             'dataContainer'      => 'General',                                         |    -> :ref:`*ignored* <dataContainer>`      |
|             'ptable'             => 'tl_parent',                                       |    -> `Data provider mapping`_              |
|             'dynamicPtable'      => true, // require 'ptable'=>''                      |    -> :ref:`*ignored* <dynamicPtable>`      |
|             'ctable'             => array('tl_child1', 'tl_child2'),                   |    -> :ref:`*ignored* <ctable>`             |
|             'validFileTypes'     => 'jpg,png,gif',                                     |    -> :ref:`*ignored* <validFileTypes>`     |
|             'uploadScript'       => '',                                                |    -> :ref:`*ignored* <uploadScript>`       |
|             'closed'             => true,                                              |    ->                                       |
|             'notEditable'        => true,                                              |    ->                                       |
|             'notDeletable'       => true,                                              |    ->                                       |
|             'switchToEdit'       => true,                                              |    ->                                       |
|             'enableVersioning'   => true,                                              |    ->                                       |
|             'doNotCopyRecords'   => true,                                              |    ->                                       |
|             'doNotDeleteRecords' => true,                                              |    -> :ref:`*ignored* <doNotDeleteRecords>` |
|             'onload_callback'    => array                                              |    ->                                       |
|             (                                                                          |       ^                                     |
|                 array('<class name>', '<method name>')                                 |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'onsubmit_callback'  => array                                              |    ->                                       |
|             (                                                                          |       ^                                     |
|                 array('<class name>', '<method name>')                                 |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'ondelete_callback'  => array                                              |    ->                                       |
|             (                                                                          |       ^                                     |
|                 array('<class name>', '<method name>')                                 |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'oncut_callback'     => array                                              |    ->                                       |
|             (                                                                          |       ^                                     |
|                 array('<class name>', '<method name>')                                 |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'oncopy_callback'    => array                                              |    ->                                       |
|             (                                                                          |       ^                                     |
|                 array('<class name>', '<method name>')                                 |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'sql'                => array                                              |    -> :ref:`*ignored* <sql>`                |
|             (                                                                          |       ^                                     |
|                 'keys' => array                                                        |       ^                                     |
|                 (                                                                      |       ^                                     |
|                     'id'    => 'primary',                                              |       ^                                     |
|                     'pid'   => 'index',                                                |       ^                                     |
|                     'alias' => 'index'                                                 |       ^                                     |
|                 )                                                                      |       ^                                     |
|             )                                                                          |       ^                                     |
|         ),                                                                             |                                             |
|                                                                                        |                                             |
|         // DcGeneral config                                                            |                                             |
|         'dca_config' => array                                                          |    ->                                       |
|         (                                                                              |                                             |
|             'callback'       => 'DcGeneral\Callbacks\ContaoStyleCallbacks',            |    -> `Deprecated DcGeneral config`_        |
|             'controller'     => 'DcGeneral\Controller\DefaultController',              |    -> `Deprecated DcGeneral config`_        |
|             'view'           => 'DcGeneral\View\DefaultView',                          |    -> `Deprecated DcGeneral config`_        |
|             'data_provider'  => array                                                  |    -> `Data provider mapping`_              |
|             (                                                                          |       ^                                     |
|                     'default' => array                                                 |       ^                                     |
|                     (                                                                  |       ^                                     |
|                             'type'    => '...\ContaoDataProviderInformation',          |       ^                                     |
|                             'factory' => '...\ContaoDataProviderInformationFactory',   |       ^                                     |
|                             'class'   => 'DcGeneral\Data\DefaultDriver',               |       ^                                     |
|                             'source'  => 'tl_example'                                  |       ^                                     |
|                     ),                                                                 |       ^                                     |
|                     'parent'  => array                                                 |       ^                                     |
|                     (                                                                  |       ^                                     |
|                             'type'    => '...\ContaoDataProviderInformation',          |       ^                                     |
|                             'factory' => '...\ContaoDataProviderInformationFactory',   |       ^                                     |
|                             'class'  => 'DcGeneral\Data\DefaultDriver',                |       ^                                     |
|                             'source' => 'tl_parent'                                    |       ^                                     |
|                     )                                                                  |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'rootEntries' => array(                                                    |    -> `Root entries mapping`_               |
|                 'tl_example' => array(                                                 |       ^                                     |
|                     'setOn'  => array                                                  |       ^                                     |
|                     (                                                                  |       ^                                     |
|                         array(                                                         |       ^                                     |
|                             'property' => 'id',                                        |       ^                                     |
|                             'value'    => 0                                            |       ^                                     |
|                         ),                                                             |       ^                                     |
|                     ),                                                                 |       ^                                     |
|                     'filter' => array                                                  |       ^                                     |
|                     (                                                                  |       ^                                     |
|                         array                                                          |       ^                                     |
|                         (                                                              |       ^                                     |
|                             'property'  => 'id',                                       |       ^                                     |
|                             'value'     => 0,                                          |       ^                                     |
|                             'operation' => '='                                         |       ^                                     |
|                         )                                                              |       ^                                     |
|                     )                                                                  |       ^                                     |
|                 )                                                                      |       ^                                     |
|             ),                                                                         |       ^                                     |
|             'childCondition' => array(                                                 |    -> `Parent-child condition mapping`_     |
|                 array(                                                                 |       ^                                     |
|                     'from'   => 'tl_parent',                                           |       ^                                     |
|                     'to'     => 'tl_example',                                          |       ^                                     |
|                     'setOn'  => array                                                  |       ^                                     |
|                     (                                                                  |       ^                                     |
|                         array(                                                         |       ^                                     |
|                             'from_field' => 'id',                                      |       ^                                     |
|                             'to_field'   => 'pid'                                      |       ^                                     |
|                         ),                                                             |       ^                                     |
|                     ),                                                                 |       ^                                     |
|                     'filter' => array                                                  |       ^                                     |
|                     (                                                                  |       ^                                     |
|                         array                                                          |       ^                                     |
|                         (                                                              |       ^                                     |
|                             'remote'    => 'id',                                       |       ^                                     |
|                             'local'     => 'pid',                                      |       ^                                     |
|                             'operation' => '='                                         |       ^                                     |
|                         )                                                              |       ^                                     |
|                     ),                                                                 |       ^                                     |
|                     'inverse' => array                                                 |       ^                                     |
|                     (                                                                  |       ^                                     |
|                         array                                                          |       ^                                     |
|                         (                                                              |       ^                                     |
|                             'local'    => 'pid',                                       |       ^                                     |
|                             'remote'     => 'id',                                      |       ^                                     |
|                             'operation' => '='                                         |       ^                                     |
|                         )                                                              |       ^                                     |
|                     )                                                                  |       ^                                     |
|                 )                                                                      |       ^                                     |
|             )                                                                          |       ^                                     |
|         ),                                                                             |                                             |
|                                                                                        |                                             |
|         // List                                                                        |                                             |
|         'list' => array                                                                |    -> `Backend view mapping`_               |
|         (                                                                              |                                             |
|             'sorting' => array                                                         |                                             |
|             (                                                                          |                                             |
|                 'mode'                  => 6,                                          |    -> `Basic config mapping`_               |
|                 'flag'                  => 6,                                          |    -> `Listing mapping`_                    |
|                 'panelLayout'           => 'filter;search,limit',                      |    -> `Panel layout mapping`_               |
|                 'fields'                => array('published DESC', 'title', 'author'), |    -> `Listing mapping`_                    |
|                 'headerFields'          => array('title', 'headline', 'author'),       |       ^                                     |
|                 'header_callback'       => array('<class name>', '<method name>'),     |       ^                                     |
|                 'icon'                  => 'path/to/icon.png',                         |       ^                                     |
|                 'root'                  => 6,                                          |    ->                                       |
|                 'filter'                => array(array('status=?', 'active')),         |    ->                                       |
|                 'disableGrouping'       => true,                                       |    -> `Listing mapping`_                    |
|                 'paste_button_callback' => array('<class name>', '<method name>'),     |    ->                                       |
|                 'child_record_callback' => array('<class name>', '<method name>'),     |    -> `Listing mapping`_                    |
|                 'child_record_class'    => 'css_class_name'                            |       ^                                     |
|             ),                                                                         |                                             |
|             'label' => array                                                           |    -> `Listing mapping`_                    |
|             (                                                                          |       ^                                     |
|                 'fields'         => array('title', 'inColumn'),                        |       ^                                     |
|                 'format'         => '%s <span style="color:#b3b3b3">[%s]</span>',      |       ^                                     |
|                 'maxCharacters'  => 255,                                               |       ^                                     |
|                 'group_callback' => array('<class name>', '<method name>'),            |       ^                                     |
|                 'label_callback' => array('<class name>', '<method name>')             |       ^                                     |
|             ),                                                                         |                                             |
|             'global_operations' => array                                               |    -> `Global operations mapping`_          |
|             (                                                                          |                                             |
|                 'all' => array                                                         |    -> `Operation mapping`_                  |
|                 (                                                                      |       ^                                     |
|                     'label'           => &$GLOBALS['TL_LANG']['MSC']['all'],           |       ^                                     |
|                     'href'            => 'act=select',                                 |       ^                                     |
|                     'class'           => 'header_edit_all',                            |       ^                                     |
|                     'attributes'      => 'onclick="Backend.getScrollOffset()"',        |       ^                                     |
|                     'button_callback' => array('<class name>', '<method name>')        |       ^                                     |
|                 )                                                                      |       ^                                     |
|             ),                                                                         |                                             |
|             'operations' => array                                                      |    -> `Model operations mapping`_           |
|             (                                                                          |                                             |
|                 'delete' => array                                                      |    -> `Operation mapping`_                  |
|                 (                                                                      |       ^                                     |
|                     'label'           => &$GLOBALS['TL_LANG']['tl_example']['delete'], |       ^                                     |
|                     'href'            => 'act=delete',                                 |       ^                                     |
|                     'icon'            => 'delete.gif',                                 |       ^                                     |
|                     'attributes'      => 'onclick="Backend.getScrollOffset()"',        |       ^                                     |
|                     'button_callback' => array('<class name>', '<method name>')        |       ^                                     |
|                 ),                                                                     |       ^                                     |
|             )                                                                          |                                             |
|         ),                                                                             |                                             |
|                                                                                        |                                             |
|         // Palettes                                                                    |                                             |
|         'palettes' => array                                                            |    -> `Palettes mapping`_                   |
|         (                                                                              |       ^                                     |
|             '__selector__' => array('protected'),                                      |       ^                                     |
|             'default'      => '{title_legend},title,alias,author;...'                  |       ^                                     |
|         ),                                                                             |       ^                                     |
|                                                                                        |       ^                                     |
|         // Subpalettes                                                                 |       ^                                     |
|         'subpalettes' => array                                                         |       ^                                     |
|         (                                                                              |       ^                                     |
|             'protected' => 'groups'                                                    |       ^                                     |
|         ),                                                                             |       ^                                     |
|                                                                                        |                                             |
|         // Fields                                                                      |                                             |
|         'fields' => array                                                              |    -> `Properties (fka fields) mapping`_    |
|         (                                                                              |       ^                                     |
|             'title' => array                                                           |       ^                                     |
|             (                                                                          |       ^                                     |
|                 'label'                => &$GLOBALS['TL_LANG']['tl_example']['title'], |       ^                                     |
|                 'default'              => 'default value',                             |       ^                                     |
|                 'exclude'              => true,                                        |       ^                                     |
|                 'search'               => true,                                        |       ^                                     |
|                 'sorting'              => true,                                        |       ^                                     |
|                 'filter'               => true,                                        |       ^                                     |
|                 'flag'                 => 12,                                          |       ^                                     |
|                 'length'               => 3,                                           |       ^                                     |
|                 'inputType'            => 'text',                                      |       ^                                     |
|                 'options'              => array('a', 'b', 'c'),                        |       ^                                     |
|                 'options_callback'     => array('<class name>', '<method name>'),      |       ^                                     |
|                 'foreignKey'           => 'tl_other_table.name',                       |       ^                                     |
|                 'reference'            => &$GLOBALS['TL_LANG']['tl_example']['title'], |       ^                                     |
|                 'explanation'          => &$GLOBALS['TL_LANG']['tl_example']['title'], |       ^                                     |
|                 'input_field_callback' => array('<class name>', '<method name>'),      |       ^                                     |
|                 'wizard'               => array('<class name>', '<method name>'),      |       ^                                     |
|                 'relation'             => array('type'=>'hasOne', 'load'=>'eager'),    |       ^                                     |
|                 'load_callback'        => array                                        |       ^                                     |
|                 (                                                                      |       ^                                     |
|                     array('<class name>', '<method name>')                             |       ^                                     |
|                 ),                                                                     |       ^                                     |
|                 'save_callback'        => array                                        |       ^                                     |
|                 (                                                                      |       ^                                     |
|                     array('<class name>', '<method name>')                             |       ^                                     |
|                 ),                                                                     |       ^                                     |
|                 'eval'                 => array(                                       |       ^                                     |
|                     'helpwizard'            => true,                                   |       ^                                     |
|                     'mandatory'             => true,                                   |       ^                                     |
|                     'maxlength'             => 255,                                    |       ^                                     |
|                     'minlength'             => 255,                                    |       ^                                     |
|                     'fallback'              => true,                                   |       ^                                     |
|                     'rgxp'                  => 'friendly',                             |       ^                                     |
|                     'cols'                  => 12,                                     |       ^                                     |
|                     'rows'                  => 6,                                      |       ^                                     |
|                     'wrap'                  => 'hard',                                 |       ^                                     |
|                     'multiple'              => true,                                   |       ^                                     |
|                     'size'                  => 6,                                      |       ^                                     |
|                     'style'                 => 'border:2px',                           |       ^                                     |
|                     'rte'                   => 'tinyFlash',                            |       ^                                     |
|                     'submitOnChange'        => true,                                   |       ^                                     |
|                     'nospace'               => true,                                   |       ^                                     |
|                     'allowHtml'             => true,                                   |       ^                                     |
|                     'preserveTags'          => true,                                   |       ^                                     |
|                     'decodeEntities'        => true,                                   |       ^                                     |
|                     'doNotSaveEmpty'        => true,                                   |       ^                                     |
|                     'alwaysSave'            => true,                                   |       ^                                     |
|                     'spaceToUnderscore'     => true,                                   |       ^                                     |
|                     'unique'                => true,                                   |       ^                                     |
|                     'encrypt'               => true,                                   |       ^                                     |
|                     'trailingSlash'         => true,                                   |       ^                                     |
|                     'files'                 => true,                                   |       ^                                     |
|                     'filesOnly'             => true,                                   |       ^                                     |
|                     'extensions'            => 'jpg,png,gif',                          |       ^                                     |
|                     'path'                  => 'path/inside/of/contao',                |       ^                                     |
|                     'fieldType'             => 'checkbox',                             |       ^                                     |
|                     'includeBlankOption'    => true,                                   |       ^                                     |
|                     'blankOptionLabel'      => '- none selected -',                    |       ^                                     |
|                     'chosen'                => true,                                   |       ^                                     |
|                     'findInSet'             => true,                                   |       ^                                     |
|                     'datepicker'            => true,                                   |       ^                                     |
|                     'colorpicker'           => true,                                   |       ^                                     |
|                     'feEditable'            => true,                                   |       ^                                     |
|                     'feGroup'               => 'contact',                              |       ^                                     |
|                     'feViewable'            => true,                                   |       ^                                     |
|                     'doNotCopy'             => true,                                   |       ^                                     |
|                     'hideInput'             => true,                                   |       ^                                     |
|                     'doNotShow'             => true,                                   |       ^                                     |
|                     'isBoolean'             => true,                                   |       ^                                     |
|                     'disabled'              => true,                                   |       ^                                     |
|                     'readonly'              => true,                                   |       ^                                     |
|                     'doNotEditMultiple'     => true,                                   |    Hide at editAll.                         |
|                     'doNotOverrideMultiple' => true,                                   |    Hide at overrideAll.                     |
|                 ),                                                                     |    |nl|                                     |
|                 'sql' => 'varchar(255) NOT NULL default '''                            |    -> :ref:`*ignored* <sql>`                |
|             )                                                                          |    |nl|                                     |
|         )                                                                              |    |nl|                                     |
|     );                                                                                 |    |nl|                                     |
+----------------------------------------------------------------------------------------+---------------------------------------------+



.. |nbsp| unicode:: 0xA0
   :trim:

.. |nl| unicode:: 0xA0