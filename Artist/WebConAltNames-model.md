# WebConAltNames.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404845`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404662`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


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

#### _AltGivenNameURI_
From column: _AltNameTypeURI_
``` python
return getValue("URI")+'/altname/givenname'
```

#### _AltFamilyNameURI_
From column: _AltGivenNameURI_
``` python
return getValue("URI")+'/altname/familyname'
```

#### _AltPrefixURI_
From column: _AltFamilyNameURI_
``` python
return getValue("URI")+'/altname/prefix'
```

#### _AltSuffixURI_
From column: _AltPrefixURI_
``` python
return getValue("URI")+'/altname/suffix'
```

#### _AltGivenNameTypeURI_
From column: _AltGivenNameURI_
``` python
return getValue("URI")+'/altname/givenname/type'
```

#### _AltFamilyNameTypeURI_
From column: _AltFamilyNameURI_
``` python
return getValue("URI")+'/altname/familyname/type'
```

#### _AltPrefixTypeURI_
From column: _AltPrefixURI_
``` python
return getValue("URI")+'/altname/prefix/type'
```

#### _AltSuffixTypeURI_
From column: _AltSuffixURI_
``` python
return getValue("URI")+'/altname/suffix/type'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AltFamilyNameTypeURI_ | `uri` | `crm:E55_Type3`|
| _AltFamilyNameURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _AltGivenNameTypeURI_ | `uri` | `crm:E55_Type2`|
| _AltGivenNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _AltName_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _AltNameTypeURI_ | `uri` | `crm:E55_Type1`|
| _AltNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _AltPrefixTypeURI_ | `uri` | `crm:E55_Type4`|
| _AltPrefixURI_ | `uri` | `crm:E82_Actor_Appellation4`|
| _AltSuffixTypeURI_ | `uri` | `crm:E55_Type5`|
| _AltSuffixURI_ | `uri` | `crm:E82_Actor_Appellation5`|
| _FirstName_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _LastName_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _NameTitle_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _NameType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _Suffix_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _URI_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E55_Type2` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type3` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404845`|
| `crm:E55_Type5` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404662`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type4`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type5`|
