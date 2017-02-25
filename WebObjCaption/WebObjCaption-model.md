# WebObjCaption.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300264237`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300026687`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055547`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ObjectID_
``` python
return 'object/id/'+getValue("ObjectID")
```

#### _ClassificationURI_
From column: _URI_
``` python
return getValue("URI")+'/classification'
```

#### _NotInUse_
From column: _ClassificationURI_
``` python
return getValue("URI")+'/classification/type'
```

#### _CreationURI_
From column: _NotInUse_
``` python
return getValue("URI")+'/creation'
```

#### _CreationTimeURI_
From column: _CreationURI_
``` python
return getValue("URI")+'/creation/time'
```

#### _PrimaryTitle_
From column: _Title_
``` python
return getValue("Title")
```

#### _TitleURI_
From column: _CreationTimeURI_
``` python
return getValue("URI")+'/title'
```

#### _MediumURI_
From column: _TitleURI_
``` python
return getValue("URI")+'/medium'
```

#### _DimensionURI_
From column: _MediumURI_
``` python
return getValue("URI")+'/dimension'
```

#### _CreditlineURI_
From column: _DimensionURI_
``` python
return getValue("URI")+'/creditline'
```

#### _ImageURI_
From column: _CreditlineURI_
``` python
return getValue("URI")+'/image'
```

#### _ImageRightsURI_
From column: _ImageURI_
``` python
return getValue("URI")+'/image/rights'
```

#### _website_
From column: _ImageRightsURI_
``` python
return getValue("objectDetailsWebPage")
```

#### _AlternateWebsiteURI_
From column: _website_
``` python
return getValue("linkedDataLink")
```

#### _ClassificationTypeURI_
From column: _NotInUse_
``` python
s = getValue("Classification")
if getValue("SubClassification"):
    s += "--"+getValue("SubClassification")
return AATTerm.get_aat_uri("saam",s)
```

#### _dated_clean_
From column: _dated_
``` python
if getValue("dated")!="n.d.":
    return getValue("dated")
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AlternateWebsiteURI_ | `uri` | `foaf:Document2`|
| _Classification_ | `rdfs:label` | `crm:E55_Type1`|
| _ClassificationTypeURI_ | `uri` | `crm:E55_Type1`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _CreationTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreationURI_ | `uri` | `crm:E12_Production1`|
| _Creditline_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _CreditlineURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _DimensionURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _Dimensions_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _Medium_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _MediumURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _PrimaryTitle_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _URI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _datebegin_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _dated_clean_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _dateend_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _linkedDataLink_ | `rdfs:label` | `foaf:Document2`|
| _objectDetailsWebPage_ | `rdfs:label` | `foaf:Document1`|
| _website_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object4`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P62_depicts` | `crm:E39_Actor2`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document2`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300264237`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300266036`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300026687`|
| `crm:E33_Linguistic_Object4` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300055547`|
| `crm:E35_Title1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E39_Actor2` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E39_Actor2` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E39_Actor2` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
