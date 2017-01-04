# WebObjCaption.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ObjectID_
``` python
return 'object/id/'+getValue("ObjectID")
```

#### _ClassificationURI_
From column: _URI_
``` python
return getValue("URI")+'/classification'
```

#### _ClassificationTypeURI_
From column: _ClassificationURI_
``` python
return getValue("URI")+'/classification/type'
```

#### _CreationURI_
From column: _ClassificationTypeURI_
``` python
return getValue("URI")+'/creation'
```

#### _CreationTimeURI_
From column: _CreationURI_
``` python
return getValue("URI")+'/creation/time'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Classification_ | `rdfs:label` | `crm:E55_Type1`|
| _ClassificationTypeURI_ | `uri` | `crm:E55_Type1`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _CreationTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreationURI_ | `uri` | `crm:E12_Production1`|
| _URI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _datebegin_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _dateend_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
