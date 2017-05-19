# WebObjDimensionsSplit_view.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _ObjectID_
``` python
return "object/id/"+getValue("objectnumber").replace(".","_").replace(",","_")
```

#### _DimensionType_
From column: _type_
``` python
return getValue("type")[:-2]
```

#### _DimensionUnit_
From column: _DimensionType_
``` python
return getValue("type")[-2:]
```

#### _TypeURI_
From column: _type_
``` python
return UM.uri_from_fields("thesauri/dimension_type/", getValue("type")[:-2])
```

#### _DimensionURI_
From column: _value_
``` python
return getValue("ObjectURI")+"/"+getValue("Element")+"/dimension/"+getValue("DimensionType").lower()
```

#### _PartURI_
From column: _Element_
``` python
return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("Element"))
```

#### _DimUnitURI_
From column: _DimensionUnit_
``` python
return UM.uri_from_fields("thesauri/dimension_unit/",getValue("type")[-2:])
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _DimUnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|
| _DimensionType_ | `skos:prefLabel` | `crm:E55_Type1`|
| _DimensionURI_ | `uri` | `crm:E54_Dimension1`|
| _DimensionUnit_ | `skos:prefLabel` | `crm:E58_Measurement_Unit1`|
| _Element_ | `rdfs:label` | `crm:E18_Physical_Thing1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _PartURI_ | `uri` | `crm:E18_Physical_Thing1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _value_ | `rdf:value` | `crm:E54_Dimension1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E22_Man-Made_Object1` | `crm:P46_is_composed_of` | `crm:E18_Physical_Thing1`|
| `crm:E54_Dimension1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E54_Dimension1` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
