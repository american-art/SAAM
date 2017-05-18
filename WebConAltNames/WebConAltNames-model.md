# WebConAltNames.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ConstituentURI_
From column: _ConstituentID_
``` python
return "constituent/id/"+getValue("ConstituentID")
```

#### _Name_
From column: _LastName_
``` python
name = getValue("FirstName") + " " + getValue("LastName")
if getValue("NameTitle"):
    name = getValue("NameTitle") + " " + name
if getValue("Suffix"):
    name = name + " " + getValue("Suffix")
return name
```

#### _AltNameURI_
From column: _LastName_
``` python
return UM.uri_from_fields(getValue("ConstituentURI")+"/",getValue("NameType"))
```

#### _NameTypeURI_
From column: _NameType_
``` python
return UM.uri_from_fields("thesauri/name_type/",getValue("NameType"))
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AltNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _Name_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _NameType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _NameTypeURI_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `crm:E55_Type1`|
