<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=========================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `commandTime[date-time]`: 로봇에 시간 보내기  
<!-- 35-RequiredProperties -->

- `commandTime`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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
  "errors": [""]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "Robot:Mega_rover:01",  
  "type": "CommandReturnMessage",  
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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
