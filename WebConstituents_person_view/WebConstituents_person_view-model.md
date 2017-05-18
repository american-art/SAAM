# WebConstituents_person_view.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404662`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404845`
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

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return "constituent/id/"+getValue("ConstituentID")
```

#### _DisplayBirthDate_
From column: _DisplayDate_
``` python
d = getValue("DisplayDate")
if '-' in d:
    return d[:d.index('-')]
else:
    if "born" in d:
        return d
    else:
        return ""

```

#### _DisplayDeathDate_
From column: _DisplayDate_
``` python
d = getValue("DisplayDate")
if '-' in d:
    return d[d.index('-')+1:]
else:
    if "died" in d:
        return d
    else:
        return ""

```

#### _LatestBirthDate_
From column: _BeginDate_
``` python
return getValue("BeginDate")+"-12-31"
```

#### _LatestDeathDate_
From column: _EndDate_
``` python
return getValue("EndDate")+"-12-31"
```

#### _BirthURI_
From column: _URI_
``` python
return getValue("URI")+"/birth"
```

#### _DeathURI_
From column: _BirthURI_
``` python
return getValue("URI")+"/death"
```

#### _BirthDateURI_
From column: _BirthURI_
``` python
return getValue("URI")+"/birth/time"
```

#### _DeathDateURI_
From column: _DeathURI_
``` python
return getValue("URI")+"/death/time"
```

#### _PrimaryName_
From column: _DisplayName_
``` python
return getValue("DisplayName")
```

#### _NameURI_
From column: _DeathDateURI_
``` python
return getValue("URI")+"/name"
```

#### _GivenNameURI_
From column: _NameURI_
``` python
if getValue("FirstName"):
    return getValue("URI")+"/first_name"
else:
    return ""
```

#### _SortNameURI_
From column: _GivenNameURI_
``` python
return getValue("URI")+"/sortname"
```

#### _FamilyNameURI_
From column: _GivenNameURI_
``` python
if getValue("LastName"):
    return getValue("URI")+"/last_name"
else:
    return ""
```

#### _PrefixURI_
From column: _NameURI_
``` python
if getValue("NameTitle"):
    return getValue("URI")+"/prefix"
else:
    return ""
```

#### _SuffixURI_
From column: _FamilyNameURI_
``` python
if getValue("Suffix"):
    return getValue("URI")+"/suffix"
else:
    return ""
```

#### _PrefixTypeURI_
From column: _PrefixURI_
``` python
return "thesauri/name_type/prefix"
```

#### _GivenNameTypeURI_
From column: _GivenNameURI_
``` python
return "thesauri/name_type/first_name"
```

#### _FamilyNameTypeURI_
From column: _FamilyNameURI_
``` python
return "thesauri/name_type/last_name"
```

#### _SuffixTypeURI_
From column: _SuffixURI_
``` python
return "thesauri/name_type/suffix"
```

#### _SortNameTypeURI_
From column: _SortNameURI_
``` python
return "thesauri/name_type/sort_name"
```

#### _NationalityURI_
From column: _Code_
``` python
return getValue("URI")+"/nationality"
```

#### _PrimaryNameURI_
From column: _FirstName_
``` python
return getValue("URI")+"/name"
```

#### _EarliestBeginDate_
From column: _BeginDate_
``` python
if getValue("BeginDate"):
    return getValue("BeginDate")+"-01-01"
else:
    return ""
```

#### _EarliestEndDate_
From column: _EndDate_
``` python
return getValue("EndDate")+"-01-01"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation6`|
| _BeginDate_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DisplayName_ | `rdf:value` | `crm:E82_Actor_Appellation7`|
| _EarliestBeginDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _EarliestEndDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _EndDate_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _FamilyNameTypeURI_ | `uri` | `crm:E55_Type3`|
| _FamilyNameURI_ | `uri` | `crm:E82_Actor_Appellation4`|
| _FirstName_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _GivenNameTypeURI_ | `uri` | `crm:E55_Type2`|
| _GivenNameURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _LastName_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _LatestBirthDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _LatestDeathDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _NameTitle_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _Nationality_ | `rdfs:label` | `crm:E74_Group1`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _PrefixTypeURI_ | `uri` | `crm:E55_Type1`|
| _PrefixURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _PrimaryName_ | `rdfs:label` | `crm:E39_Actor1`|
| _PrimaryNameURI_ | `uri` | `crm:E82_Actor_Appellation7`|
| _SortNameTypeURI_ | `uri` | `crm:E55_Type5`|
| _SortNameURI_ | `uri` | `crm:E82_Actor_Appellation6`|
| _Suffix_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _SuffixTypeURI_ | `uri` | `crm:E55_Type4`|
| _SuffixURI_ | `uri` | `crm:E82_Actor_Appellation5`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation6`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation7`|
| `crm:E55_Type1` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404845`|
| `crm:E55_Type2` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type3` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404662`|
| `crm:E55_Type5` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404672`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type4`|
| `crm:E82_Actor_Appellation6` | `crm:P2_has_type` | `crm:E55_Type5`|
| `crm:E82_Actor_Appellation7` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
