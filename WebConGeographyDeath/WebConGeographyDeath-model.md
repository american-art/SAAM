# WebConGeography.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _DeathPlace_
From column: _City_
``` python
c = str(getValue("City"))
s = str(getValue("State"))
co = str(getValue("Country"))
place = ""
if c!="":
    place += c
if s != "":
    if place!="":
        place += ", "+s
    else:
        place = s
if co != "":
    if place!="":
        place += ", "+co
    else:
        place = co
return place
```

#### _URI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _DeathURI_
From column: _URI_
``` python
return getValue("URI")+'/death'
```

#### _DeathLocationURI_
From column: _DeathURI_
``` python
return UM.uri_from_fields("thesauri/place/",getValue("City"))
```


## Selections
#### _DEFAULT_TEST_
From column: _City_
<br>Operation: `Union`
``` python
return getValue("ConGeoCode") != "Place of Death"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _DeathLocationURI_ | `uri` | `crm:E53_Place1`|
| _DeathPlace_ | `rdfs:label` | `crm:E53_Place1`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
