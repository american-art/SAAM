# WebConstituents_institution_view.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404672`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: _ConstituentID_
``` python
return "constituent/id/"+getValue("ConstituentID")
```

#### _PrimaryNameURI_
From column: _AlphaSort_
``` python
return getValue("ConstituentURI")+"/primary_name"
```

#### _NameLabel_
From column: _DisplayName_
``` python
return getValue("DisplayName")
```

#### _SortNameURI_
From column: _ConstituentURI_
``` python
return getValue("ConstituentURI")+"/sort_name"
```

#### _NationalityURI_
From column: _Code_
``` python
return UM.uri_from_fields("thesauri/nationality/",getValue("Nationality"))
```

#### _LatestBeginDate_
From column: _BeginDate_
``` python
return getValue("BeginDate")
```

#### _LatestEndDate_
From column: _EndDate_
``` python
return getValue("EndDate")
```

#### _BirthURI_
From column: _NameLabel_
``` python
return getValue("ConstituentURI")+"/birth"
```

#### _BirthTimeURI_
From column: _BirthURI_
``` python
return getValue("BirthURI")+"/time"
```

#### _DeathURI_
From column: _LatestBeginDate_
``` python
return getValue("ConstituentURI")+"/death"
```

#### _DeathTimeURI_
From column: _DeathURI_
``` python
return getValue("DeathURI")+"/time"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _BeginDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DeathTimeURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DisplayName_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _EndDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _LatestBeginDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _LatestEndDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _PrimaryNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _SortNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404672`|
