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
#### _ObjectID_
From column: _ConstituentID_
``` python
return 'webartist/'+getValue("ConstituentID")
```

#### _BioURI_
From column: _ObjectID_
``` python
return 'webartist/'+getValue("ConstituentID")+'/bio'
```

#### _BioDescVal_
From column: _BioDsp_
``` python
return getValue("BioDsp")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BioDescVal_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _BioDsp_ | `dc:description` | `crm:E39_Actor1`|
| _BioURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _ObjectID_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300080102`|
| `crm:E39_Actor1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
