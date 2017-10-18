# WebConDates.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ConstituentURI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _DeathURI_
From column: _DateDescription_
``` python
if getValue("DateDescription") == "Death Date":
    return getValue("ConstituentURI")+'/death'
else:
    return ""
```

#### _DeathYearURI_
From column: _DateDescription_
``` python
if getValue("DateDescription") == "Death Date":
    return getValue("ConstituentURI")+'/death_year'
else:
    return ""
```

#### _DeathDateBegin_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Death Date":
    return getValue("DateBegSearch") + "-01-01"
else:
    return ""
```

#### _DeathDateEnd_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Death Date":
    return getValue("DateBegSearch") + "-12-31"
else:
    return ""
```

#### _DateLabel_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Death Date":
    return getValue("DateBegSearch")
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DateLabel_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DeathDateBegin_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DeathDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DeathYearURI_ | `uri` | `crm:E52_Time-Span1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
