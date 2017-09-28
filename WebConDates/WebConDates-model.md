# WebConDates.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ConstituentURI_
From column: _ConstituentID_
``` python
return "constituent/id/"+getValue("ConstituentID")
```

#### _BirthURI_
From column: _DateDescription_
``` python
if getValue("DateDescription") == "Birth Date":
    return getValue("ConstituentURI") + "/birth"
else:
    return ""
```

#### _BirthYearURI_
From column: _DateDescription_
``` python
if getValue("DateDescription") == "Birth Date":
    return getValue("ConstituentURI") + "/birth_year"
else:
    return ""
```

#### _BirthDateBegin_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Birth Date":
    return getValue("DateBegSearch") + "-01-01"
else:
    return ""
```

#### _BirthDateEnd_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Birth Date":
    return getValue("DateBegSearch") + "-12-31"
else:
    return ""
```

#### _DateLabel_
From column: _DateBegSearch_
``` python
if getValue("DateDescription") == "Birth Date":
    return getValue("DateBegSearch")
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthDateBegin_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _BirthYearURI_ | `uri` | `crm:E52_Time-Span1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DateLabel_ | `rdfs:label` | `crm:E52_Time-Span1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
