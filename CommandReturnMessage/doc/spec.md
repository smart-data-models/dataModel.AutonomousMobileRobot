<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: CommandReturnMessage    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Command return message**    
version: 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `commandTime[date-time]`: Sent time to the robot  - `errors[array]`: Describes the errors that occurred in the robot  - `receivedCommand[string]`: The command which the robot received  - `receivedTime[date-time]`: Command received time to the robot  - `receivedWaypoints[array]`: The waypoints which the robot received  - `result[string]`: Enum:'ack, error, ignore'. The result of the robot received the command  - `type[string]`: NGSI Entity type. It has to be CommandReturnMessage  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `commandTime`  - `errors`  - `id`  - `receivedCommand`  - `receivedTime`  - `receivedWaypoints`  - `result`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
CommandReturnMessage:      
  description: Command return message      
  properties:      
    commandTime:      
      description: Sent time to the robot      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    errors:      
      description: Describes the errors that occurred in the robot      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    receivedCommand:      
      description: The command which the robot received      
      type: string      
      x-ngsi:      
        type: Property      
    receivedTime:      
      description: Command received time to the robot      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    receivedWaypoints:      
      description: The waypoints which the robot received      
      items:      
        additionalProperties: false      
        properties:      
          geographicPoint:      
            additionalProperties: true      
            description: Point in geographic coordinates      
            properties:      
              altitude:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
              latitude:      
                allOf:      
                  - default: 0.0      
                    description: Simple coordinate of a point      
                    type: number      
                    x-ngsi:      
                      type: Property      
                  - maximum: 90      
                    minimum: -90      
              longitude:      
                allOf:      
                  - default: 0.0      
                    description: Simple coordinate of a point      
                    type: number      
                    x-ngsi:      
                      type: Property      
                  - maximum: 180      
                    minimum: -180      
            required:      
              - latitude      
              - longitude      
              - altitude      
            type: object      
            x-ngsi:      
              type: Property      
          mapId:      
            description: Map ID      
            type: string      
            x-ngsi:      
              type: Property      
          orientation2D:      
            additionalProperties: true      
            description: 2D Angle of an element      
            properties:      
              theta:      
                default: 0.0      
                description: Simple measurement of an angle      
                type: number      
                x-ngsi:      
                  type: Property      
            required:      
              - theta      
            type: object      
            x-ngsi:      
              type: Property      
          orientation3D:      
            additionalProperties: true      
            description: 3D Angles of an element      
            properties:      
              pitch:      
                default: 0.0      
                description: Simple measurement of an angle      
                type: number      
                x-ngsi:      
                  type: Property      
              roll:      
                default: 0.0      
                description: Simple measurement of an angle      
                type: number      
                x-ngsi:      
                  type: Property      
              yaw:      
                default: 0.0      
                description: Simple measurement of an angle      
                type: number      
                x-ngsi:      
                  type: Property      
            required:      
              - roll      
              - pitch      
              - yaw      
            type: object      
            x-ngsi:      
              type: Property      
          point2D:      
            additionalProperties: true      
            description: Point in 2D as a two simple coordinates x and y      
            properties:      
              x:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
              y:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
            required:      
              - x      
              - y      
            type: object      
            x-ngsi:      
              type: Property      
          point3D:      
            additionalProperties: true      
            description: 'Point in 3D as a three simple coordinates x, y and z'      
            properties:      
              x:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
              y:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
              z:      
                default: 0.0      
                description: Simple coordinate of a point      
                type: number      
                x-ngsi:      
                  type: Property      
            required:      
              - x      
              - y      
              - z      
            type: object      
            x-ngsi:      
              type: Property      
          speed:      
            description: 'Robot speed between coordinates of waypoints[m/s]'      
            type: number      
            x-ngsi:      
              type: Property      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    result:      
      description: 'Enum:''ack, error, ignore''. The result of the robot received the command'      
      enum:      
        - ack      
        - ignore      
        - error      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be CommandReturnMessage      
      enum:      
        - CommandReturnMessage      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - commandTime      
    - receivedTime      
    - receivedCommand      
    - receivedWaypoints      
    - result      
    - errors      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.AutonomousMobileRobot/CommandReturnMessage/schema.json      
  x-model-tags: ""      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### CommandReturnMessage NGSI-v2 key-values Example      
Here is an example of a CommandReturnMessage in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandReturnMessage",  
  "commandTime": "2019-06-07T08:39:42.921+09:00",  
  "receivedTime": "2019-06-07T08:39:40.064+09:00",  
  "receivedCommand": "navi",  
  "receivedWaypoints": [  
    {  
      "point2D": {  
        "x": 0.503,  
        "y": 0.0  
      }  
    },  
    {  
      "point2D": {  
        "x": 3.411,  
        "y": 0.0  
      }  
    },  
    {  
      "point2D": {  
        "x": 3.411,  
        "y": 2.81  
      },  
      "orientation2D": {  
        "theta": 0.0  
      }  
    }  
  ],  
  "result": "ack",  
  "errors": [  
    ""  
  ]  
}  
```  
</details>    
#### CommandReturnMessage NGSI-v2 normalized Example      
Here is an example of a CommandReturnMessage in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandReturnMessage",  
  "commandTime": {  
    "type": "DateTime",  
    "value": "2019-06-07T08:39:42.921+09:00"  
  },  
  "receivedTime": {  
    "type": "DateTime",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "receivedCommand": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "receivedWaypoints": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "point2D": {  
          "x": 0.503,  
          "y": 0.0  
        }  
      },  
      {  
        "point2D": {  
          "x": 3.411,  
          "y": 0.0  
        }  
      },  
      {  
        "point2D": {  
          "x": 3.411,  
          "y": 2.81  
        },  
        "orientation2D": {  
          "theta": 0.0  
        }  
      }  
    ]  
  },  
  "result": {  
    "type": "Text",  
    "value": "ack"  
  },  
  "errors": {  
    "type": "StructuredValue",  
    "value": [  
      ""  
    ]  
  }  
}  
```  
</details>    
#### CommandReturnMessage NGSI-LD key-values Example      
Here is an example of a CommandReturnMessage in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandReturnMessage",  
  "commandTime": "2019-06-07T08:39:42.921+09:00",  
  "receivedTime": "2019-06-07T08:39:40.064+09:00",  
  "receivedCommand": "navi",  
  "receivedWaypoints": [  
    {  
      "point2D": {  
        "x": 0.503,  
        "y": 0.0  
      }  
    },  
    {  
      "point2D": {  
        "x": 3.411,  
        "y": 0.0  
      }  
    },  
    {  
      "point2D": {  
        "x": 3.411,  
        "y": 2.81  
      },  
      "orientation2D": {  
        "theta": 0.0  
      }  
    }  
  ],  
  "result": "ack",  
  "errors": [  
    ""  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### CommandReturnMessage NGSI-LD normalized Example      
Here is an example of a CommandReturnMessage in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandReturnMessage",  
  "commandTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2019-06-07T08:39:42.921+09:00"  
    }  
  },  
  "receivedTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2019-06-07T08:39:40.064+09:00"  
    }  
  },  
  "receivedCommand": {  
    "type": "Property",  
    "value": "navi"  
  },  
  "receivedWaypoints": {  
    "type": "Property",  
    "value": [  
      {  
        "point2D": {  
          "x": 0.503,  
          "y": 0.0  
        }  
      },  
      {  
        "point2D": {  
          "x": 3.411,  
          "y": 0.0  
        }  
      },  
      {  
        "point2D": {  
          "x": 3.411,  
          "y": 2.81  
        },  
        "orientation2D": {  
          "theta": 0.0  
        }  
      }  
    ]  
  },  
  "result": {  
    "type": "Property",  
    "value": "ack"  
  },  
  "errors": {  
    "type": "Property",  
    "value": [  
      ""  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
