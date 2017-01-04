# books_master2.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ID_
``` python
return 'book/id/'+getValue("ID")
```

#### _TitleURI_
From column: _URI_
``` python
return getValue("URI")+'/title'
```

#### _TitleValue_
From column: _InternalTitle_
``` python
return getValue("InternalTitle")
```

#### _DisplayTitleURI_
From column: _TitleURI_
``` python
return getValue("URI")+'/displaytitle'
```

#### _YearLatest_
From column: _YearPublished_
``` python
return getValue("YearPublished")
```

#### _CreationURI_
From column: _DisplayTitleURI_
``` python
return getValue("URI")+'/creation'
```

#### _CreationTImeURI_
From column: _CreationURI_
``` python
return getValue("URI")+'/creation/time'
```

#### _DimensionURI_
From column: _CreationTImeURI_
``` python
return getValue("URI")+'/dimension'
```

#### _SubjectURI_
From column: _DimensionURI_
``` python
return getValue("URI")+'/subject'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BookTitleDisplay_ | `rdf:value` | `crm:E35_Title2`|
| _CreationTImeURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreationURI_ | `uri` | `crm:E12_Production1`|
| _DimensionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DisplayTitleURI_ | `uri` | `crm:E35_Title2`|
| _InternalTitle_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _SubjectURI_ | `uri` | `owl:Thing1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _TitleValue_ | `rdf:value` | `crm:E35_Title1`|
| _URI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _YearLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _YearPublished_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _dimensions_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _subjectType_ | `rdfs:label` | `owl:Thing1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title2`|
| `crm:E22_Man-Made_Object1` | `crm:P62_depicts` | `owl:Thing1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300266036`|
| `crm:E35_Title1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
