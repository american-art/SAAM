# WebConDates.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _BirthURI_
From column: _URI_
``` python
return getValue("URI")+'/birth'
```

#### _BirthTimeURI_
From column: _URI_
``` python
return getValue("URI")+'/birth/time'
```

#### _BirthLatest_
From column: _DateBegSearch_
``` python
return getValue("DateBegSearch")
```


## Selections
#### _DEFAULT_TEST_
From column: _DateDescription_
<br>Operation: `Union`
``` python
return getValue("DateDescription") != "Birth Date"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DateBegSearch_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
