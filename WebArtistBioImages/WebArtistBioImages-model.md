# WebArtistBioImages.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _URI_
From column: _ConstituentID_
``` python
return 'constituent/id/'+getValue("ConstituentID")
```

#### _ImageURI_
From column: _URI_
``` python
return getValue("URI")+'/image'
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _PublicCaption_ | `rdfs:label` | `crm:E38_Image1`|
| _URI_ | `uri` | `crm:E39_Actor1`|
| _imageUrl_ | `uri` | `crm:E38_Image1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
