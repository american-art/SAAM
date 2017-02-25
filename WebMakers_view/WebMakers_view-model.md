# WebMakers_view.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _ObjectID_
``` python
return "object/id/"+getValue("ObjectID")
```

#### _ArtistURI_
From column: _ConstituentID_
``` python
if getValue("Role") in ["Artist","Author","Designer"]:
    return "constituent/id/"+getValue("ConstituentID")
else:
    return ""
```

#### _CreatorURI_
From column: _URI_
``` python
return getValue("URI")+"/creator"
```

#### _ProductionURI_
From column: _URI_
``` python
return getValue("URI")+"/production"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ArtistURI_ | `uri` | `crm:E39_Actor1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _URI_ | `uri` | `crm:E22_Man-Made_Object1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
