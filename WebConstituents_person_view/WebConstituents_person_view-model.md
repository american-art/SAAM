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


## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return "artist/id/"+getValue("ConstituentID")
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
return getValue("BeginDate")
```

#### _LatestDeathDate_
From column: _EndDate_
``` python
return getValue("EndDate")
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
return getValue("URI")+"/name/givenname"
```

#### _SortNameURI_
From column: _GivenNameURI_
``` python
return getValue("URI")+"/name/sortname"
```

#### _FamilyNameURI_
From column: _GivenNameURI_
``` python
return getValue("URI")+"/name/familyname"
```

#### _PrefixURI_
From column: _NameURI_
``` python
return getValue("URI")+"/name/prefix"
```

#### _SuffixURI_
From column: _FamilyNameURI_
``` python
return getValue("URI")+"/name/suffix"
```

#### _PrefixTypeURI_
From column: _PrefixURI_
``` python
return getValue("URI")+"/name/prefix/type"
```

#### _GivenNameTypeURI_
From column: _GivenNameURI_
``` python
return getValue("URI")+"/name/givenname/type"
```

#### _FamilyNameTypeURI_
From column: _FamilyNameURI_
``` python
return getValue("URI")+"/name/familyname/type"
```

#### _SuffixTypeURI_
From column: _SuffixURI_
``` python
return getValue("URI")+"/name/suffix/type"
```

#### _SortNameTypeURI_
From column: _SortNameURI_
``` python
return getValue("URI")+"/name/sortname/type"
```

#### _NationalityURI_
From column: _Code_
``` python
return getValue("URI")+"/nationality"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlphaSort_ | `rdf:value` | `crm:E82_Actor_Appellation6`|
| _BeginDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DisplayBirthDate_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DisplayDeathDate_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _DisplayName_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _EndDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
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
| `crm:E55_Type1` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404845`|
| `crm:E55_Type2` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type3` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404662`|
| `crm:E55_Type5` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404672`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation6`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type4`|
| `crm:E82_Actor_Appellation6` | `crm:P2_has_type` | `crm:E55_Type5`|
