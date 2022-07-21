[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: CommandReturnMessage  
============================  
[Open License](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Command return message**  
version: 0.1.0  

## List of properties  

- `commandTime`: Sent time to the robot  - `errors`: Describes the errors that occurred in the robot.  - `receivedCommand`: The command which the robot received  - `receivedTime`: Command received time to the robot  - `receivedWaypoints`: The waypoints which the robot received.  - `result`: Enum:'ack, error, ignore'. The result of the robot received the command.  - `type`: NGSI Entity type. It has to be CommandReturnMessage    
Required properties  
- `commandTime`  - `errors`  - `id`  - `receivedCommand`  - `receivedTime`  - `receivedWaypoints`  - `result`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CommandReturnMessage:    
  description: 'Command return message'    
  properties:    
    commandTime:    
      description: 'Sent time to the robot'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    errors:    
      description: 'Describes the errors that occurred in the robot.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    receivedCommand:    
      description: 'The command which the robot received'    
      type: string    
      x-ngsi:    
        type: Property    
    receivedTime:    
      description: 'Command received time to the robot'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    receivedWaypoints:    
      description: 'The waypoints which the robot received.'    
      items:    
        additionalProperties: false    
        properties:    
          geographicPoint:    
            additionalProperties: true    
            description: 'Property. Point in geographic coordinates'    
            properties:    
              altitude:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
              latitude:    
                allOf:    
                  - default: 0.0    
                    description: 'Property. Simple coordinate of a point'    
                    type: number    
                  - maximum: 90    
                    minimum: -90    
              longitude:    
                allOf:    
                  - default: 0.0    
                    description: 'Property. Simple coordinate of a point'    
                    type: number    
                  - maximum: 180    
                    minimum: -180    
            required:    
              - latitude    
              - longitude    
              - altitude    
            type: object    
          mapId:    
            description: 'Property. Map ID'    
            type: string    
          orientation2D:    
            additionalProperties: true    
            description: 'Property. 2D Angle of an element'    
            properties:    
              theta:    
                default: 0.0    
                description: 'Property. Simple measurement of an angle'    
                type: number    
            required:    
              - theta    
            type: object    
          orientation3D:    
            additionalProperties: true    
            description: 'Property. 3D Angles of an element'    
            properties:    
              pitch:    
                default: 0.0    
                description: 'Property. Simple measurement of an angle'    
                type: number    
              roll:    
                default: 0.0    
                description: 'Property. Simple measurement of an angle'    
                type: number    
              yaw:    
                default: 0.0    
                description: 'Property. Simple measurement of an angle'    
                type: number    
            required:    
              - roll    
              - pitch    
              - yaw    
            type: object    
          point2D:    
            additionalProperties: true    
            description: 'Property. Point in 2D as a two simple coordinates x and y'    
            properties:    
              x:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
              y:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
            required:    
              - x    
              - y    
            type: object    
          point3D:    
            additionalProperties: true    
            description: 'Property. Point in 3D as a three simple coordinates x, y and z'    
            properties:    
              x:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
              y:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
              z:    
                default: 0.0    
                description: 'Property. Simple coordinate of a point'    
                type: number    
            required:    
              - x    
              - y    
              - z    
            type: object    
          speed:    
            description: 'Property. Robot speed between coordinates of waypoints[m/s]'    
            type: number    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    result:    
      description: 'Enum:''ack, error, ignore''. The result of the robot received the command.'    
      enum:    
        - ack    
        - ignore    
        - error    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be CommandReturnMessage'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AutonomousMobileRobot/CommandReturnMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## Example payloads    
#### CommandReturnMessage NGSI-v2 key-values Example    
Here is an example of a CommandReturnMessage in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandMessageReturn",  
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
  "errors": [""]  
}  
```  
#### CommandReturnMessage NGSI-v2 normalized Example    
Here is an example of a CommandReturnMessage in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandMessageReturn",  
  "commandTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:42.921+09:00"  
  },  
  "receivedTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "receivedCommand": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "receivedWaypoints": {  
    "type": "array",  
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
    "type": "array",  
    "value": [  
      ""  
    ]  
  }  
}  
```  
#### CommandReturnMessage NGSI-LD key-values Example    
Here is an example of a CommandReturnMessage in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandMessageReturn",  
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
#### CommandReturnMessage NGSI-LD normalized Example    
Here is an example of a CommandReturnMessage in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandMessageReturn",  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
