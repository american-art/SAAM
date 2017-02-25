# WebConDates.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _DeathLatest_
From column: _DateBegSearch_
``` python
return getValue("DateBegSearch")
```

#### _DeathURI_
From column: _URI_
``` python
return getValue("URI")+'/death'
```

#### _DeathTimeURI_
From column: _DeathURI_
``` python
return getValue("URI")+'/death/time'
```


## Selections
#### _DEFAULT_TEST_
From column: _DateDescription_
<br>Operation: `Union`
``` python
return getValue("DateDescription") != "Death Date"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _DateBegSearch_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DeathLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _DeathTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
