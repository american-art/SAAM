# WebConGeography.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _BirthPlace_
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

#### _BirthURI_
From column: _URI_
``` python
return getValue("URI")+'/birth'
```

#### _BirthLocationURI_
From column: _URI_
``` python
return UM.uri_from_fields("thesauri/place/",getValue("BirthPlace"))
```


## Selections
#### _DEFAULT_TEST_
From column: _City_
<br>Operation: `Union`
``` python
return getValue("ConGeoCode") != "Place of Birth"
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthLocationURI_ | `uri` | `crm:E53_Place1`|
| _BirthPlace_ | `rdfs:label` | `crm:E53_Place1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
