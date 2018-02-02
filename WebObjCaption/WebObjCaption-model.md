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

#### Literal Node: `http://vocab.getty.edu/aat/300404621`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan/500311465`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _URI_
From column: _ObjectID_
``` python
return "object/id/"+getValue("objectnumber")
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
return getValue("URI")+'/production'
```

#### _CreationTimeURI_
From column: _CreationURI_
``` python
if getValue("DateBeginClean"):
    return getValue("CreationURI")+'/time'
else:
    return ""
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

#### _OwnerURI_
From column: _objectnumber_
``` python
return "http://data.americanart.si.edu"
```

#### _OwnerLabel_
From column: _OwnerURI_
``` python
return "Smithsonian American Art Museum"
```

#### _Pref_Id_Label_
From column: _objectnumber_
``` python
return getValue("objectnumber")
```

#### _PrefIdURI_
From column: _objectnumber_
``` python
return getValue("URI")+"/pref_id"
```

#### _ObjNoURI_
From column: _ObjectID_
``` python
if getValue("ObjectID"):
    return getValue("URI")+"/obj_no"
else:
    return ""
```

#### _DateBeginClean_
From column: _datebegin_
``` python
if getValue("datebegin"):
    return getValue("datebegin") + "-01-01"
else:
    return ""
```

#### _DateEndClean_
From column: _dateend_
``` python
if getValue("dateend"):
    return getValue("dateend") + "-12-31"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Classification_ | `rdfs:label` | `crm:E55_Type1`|
| _ClassificationTypeURI_ | `uri` | `crm:E55_Type1`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _CreationTimeURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreationURI_ | `uri` | `crm:E12_Production1`|
| _Creditline_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _CreditlineURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _DateBeginClean_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _DateEndClean_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _DimensionURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _Dimensions_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _Medium_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _MediumURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _ObjNoURI_ | `uri` | `crm:E42_Identifier2`|
| _ObjectID_ | `rdf:value` | `crm:E42_Identifier2`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _PrefIdURI_ | `uri` | `crm:E42_Identifier1`|
| _Pref_Id_Label_ | `rdfs:label` | `crm:E42_Identifier1`|
| _PrimaryTitle_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _Title_ | `rdf:value` | `crm:E35_Title1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _URI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _dated_clean_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _objectDetailsWebPage_ | `rdfs:label` | `foaf:Document1`|
| _objectnumber_ | `rdf:value` | `crm:E42_Identifier1`|
| _website_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier2`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300264237`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300026687`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500311465`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E42_Identifier2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404621`|
