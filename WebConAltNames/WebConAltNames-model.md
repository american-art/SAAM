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
return getValue("FirstName") + " " + getValue("LastName")
```

#### _AltNameURI_
From column: _LastName_
``` python
return getValue("ConstituentURI")+"/alt_name"
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
