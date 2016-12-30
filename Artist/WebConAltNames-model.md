# WebConAltNames.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _AltName_
From column: _FirstName_
``` python
return getValue("NameTitle")+' '+getValue("FirstName")+' '+getValue("LastName")+' '+getValue("Suffix")
```

#### _URI_
From column: _ConstituentID_
``` python
return 'actor/id/'+getValue("ConstituentID")
```

#### _AltNameURI_
From column: _URI_
``` python
return getValue("URI")+'/altname'
```

#### _AltNameTypeURI_
From column: _AltNameURI_
``` python
return getValue("URI")+'/altname/type'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AltName_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _AltNameTypeURI_ | `uri` | `crm:E55_Type1`|
| _AltNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _NameType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `crm:E55_Type1`|
