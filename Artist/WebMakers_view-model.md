# WebMakers_view.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return 'actor/id/'+getValue("ConstituentID")
```

#### _BirthDisplayDate_
From column: _DisplayDate_
``` python
v = getValue("DisplayDate")
if '-' in v:
    return v[:v.index('-')]
else:
    return v
```

#### _DeathDisplayDate_
From column: _DisplayDate_
``` python
v = getValue("DisplayDate")
if '-' in v:
    return v[v.index('-')+1:]
else:
    return v
```

#### _BirthURI_
From column: _URI_
``` python
return getValue("URI")+'/birth'
```

#### _BirthTimeURI_
From column: _BirthURI_
``` python
return getValue("URI")+'/birth/time'
```

#### _DeathURI_
From column: _BirthURI_
``` python
return getValue("URI")+'/death'
```

#### _DeathTimeURI_
From column: _DeathURI_
``` python
return getValue("URI")+'/death/time'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthDisplayDate_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _BirthTimeURI_ | `uri` | `crm:E52_Time-Span2`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DeathDisplayDate_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DeathTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
