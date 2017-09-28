# WebArtistBio.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300080102`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _BioURI_
From column: _URI_
``` python
if getValue("PrimaryBio") == "Primary":
    return getValue("URI")+'/bio'+'/primary'
else:
    return getValue("URI")+'/bio'+'/non-primary'
```

#### _BioDspValue_
From column: _BioDsp_
``` python
return getValue("BioDsp")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BioDspValue_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _BioURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300080102`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E39_Actor1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
