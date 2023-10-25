<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `accuracy[object]`: 로봇의 위치 정확도  
- `battery[object]`: 로봇이 장착한 배터리 상태  
	- `remainingPercentage[number]`: 배터리 잔량    
	- `remainingTime[time]`: 배터리 예상 수명  . Model: [ https:/schema.org/DateTime]( https:/schema.org/DateTime)  
	- `voltage[number]`: 모바일 요소의 전압  . Model: [ https:/schema.org/Number]( https:/schema.org/Number)  
- `commandTime[date-time]`: 로봇에 시간 보내기  
	- `mapId[string]`: 지도 ID    
	- `orientation2D[object]`: 요소의 2D 각도    
	- `orientation3D[object]`: 요소의 3D 각도    
	- `point2D[object]`: 2D에서 두 개의 간단한 좌표 x와 y로 포인트를 지정합니다.    
	- `point3D[object]`: 3D에서 세 개의 간단한 좌표 x, y, z로 포인트를 지정합니다.    
- `errors[array]`: 로봇에서 발생한 오류를 설명합니다.  
	- `mapId[string]`: 지도 ID    
	- `orientation2D[object]`: 요소의 2D 각도    
	- `orientation3D[object]`: 요소의 3D 각도    
	- `point2D[object]`: 2D에서 두 개의 간단한 좌표 x와 y로 포인트를 지정합니다.    
	- `point3D[object]`: 3D에서 세 개의 간단한 좌표 x, y, z로 포인트를 지정합니다.    
- `type[string]`: NGSI 엔티티 유형입니다. StateMessage여야 합니다.  
<!-- 35-RequiredProperties -->

- `accuracy`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

StateMessage:    
  description: State message    
  properties:    
    accuracy:    
      additionalProperties: false    
      description: Position accuracy of the robot    
      properties:    
        covariance:    
          description: Error covariance matrix of estimated position    
          items:    
            type: number    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    battery:    
      additionalProperties: false    
      description: The states of the battery the robot mounted    
      oneOf:    
        - required:    
            - voltage    
        - required:    
            - remainingTime    
        - required:    
            - remainingPercentage    
      properties:    
        current:    
          description: Current of the mobile element    
          type: number    
          x-ngsi:    
            model: ' https:/schema.org/Number'    
            type: Property    
            units: Ampere    
        remainingPercentage:    
          description: Remaining battery charge    
          maximum: 100    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        remainingTime:    
          description: Expected lifespan of a battery    
          format: time    
          type: string    
          x-ngsi:    
            model: ' https:/schema.org/DateTime'    
            type: Property    
        voltage:    
          description: Voltage of the mobile element    
          type: number    
          x-ngsi:    
            model: ' https:/schema.org/Number'    
            type: Property    
            units: Volt    
      type: object    
      x-ngsi:    
        type: Property    
    commandTime:    
      description: Sent time to the robot    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    destination:    
      additionalProperties: false    
      description: 'Current destination of the robot. Basically, it is the same as one of the waypoints'    
      maxProperties: 3    
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
      type: object    
      x-ngsi:    
        type: Property    
    errors:    
      description: Describes the errors that occurred in the robot    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    mode:    
      description: 'Enum:''error, navi, standby''. Navigational status of the robot'    
      enum:    
        - error    
        - navi    
        - standby    
      type: string    
      x-ngsi:    
        type: Property    
    pose:    
      additionalProperties: false    
      description: Current position of the robot.    
      maxProperties: 3    
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
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be StateMessage    
      enum:    
        - StateMessage    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - accuracy    
    - battery    
    - commandTime    
    - destination    
    - errors    
    - id    
    - mode    
    - pose    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/StateMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AutonomousMobileRobot/StateMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "Robot:Mega_rover:01",  
  "type": "StateMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "mode": "navi",  
  "errors": [],  
  "pose": {  
    "point2D": {  
      "x": 3.402,  
      "y": 1.015  
    },  
    "orientation2D": {  
      "theta": 0.0  
    }  
  },  
  "destination": {  
    "point2D": {  
      "x": 3.411,  
      "y": 2.81  
    },  
    "orientation2D": {  
      "theta": 0.0  
    },  
    "mapId": "2345:ae43"  
  },  
  "accuracy": {  
    "covariance": [  
      0.1,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.1,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.05  
    ]  
  },  
  "battery": {  
    "remainingPercentage": 75.4  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "Robot:Mega_rover:01",  
  "type": "StateMessage",  
  "commandTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "mode": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "errors": {  
    "type": "array",  
    "value": []  
  },  
  "pose": {  
    "type": "StructuredValue",  
    "value": {  
      "point2D": {  
        "x": 3.402,  
        "y": 1.015  
      },  
      "orientation2D": {  
        "theta": 0.0  
      }  
    }  
  },  
  "destination": {  
    "type": "StructuredValue",  
    "value": {  
      "point2D": {  
        "x": 3.411,  
        "y": 2.81  
      },  
      "orientation2D": {  
        "theta": 0.0  
      },  
      "mapId": "2345:ae43"  
    }  
  },  
  "accuracy": {  
    "type": "StructuredValue",  
    "value": {  
      "covariance": [  
        0.1,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.1,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.05  
      ]  
    }  
  },  
  "battery": {  
    "type": "StructuredValue",  
    "value": {  
      "remainingPercentage": 75.4  
    }  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StateMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "mode": "navi",  
  "errors": [],  
  "pose": {  
    "point2D": {  
      "x": 3.402,  
      "y": 1.015  
    },  
    "orientation2D": {  
      "theta": 0.0  
    }  
  },  
  "destination": {  
    "point2D": {  
      "x": 3.411,  
      "y": 2.81  
    },  
    "orientation2D": {  
      "theta": 0.0  
    },  
    "mapId": "2345:ae43"  
  },  
  "accuracy": {  
    "covariance": [  
      0.1,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.1,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      1.7976931348623157e308,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.0,  
      0.05  
    ]  
  },  
  "battery": {  
    "remainingPercentage": 75.4  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StateMessage",  
  "commandTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2019-06-07T08:39:40.064+09:00"  
    }  
  },  
  "mode": {  
    "type": "Property",  
    "value": "navi"  
  },  
  "errors": {  
    "type": "Property",  
    "value": []  
  },  
  "pose": {  
    "type": "Property",  
    "value": {  
      "point2D": {  
        "x": 3.402,  
        "y": 1.015  
      },  
      "orientation2D": {  
        "theta": 0.0  
      }  
    }  
  },  
  "destination": {  
    "type": "Property",  
    "value": {  
      "point2D": {  
        "x": 3.411,  
        "y": 2.81  
      },  
      "orientation2D": {  
        "theta": 0.0  
      },  
      "mapId": "2345:ae43"  
    }  
  },  
  "accuracy": {  
    "type": "Property",  
    "value": {  
      "covariance": [  
        0.1,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.1,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        1.7976931348623157e+308,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.0,  
        0.05  
      ]  
    }  
  },  
  "battery": {  
    "type": "Property",  
    "value": {  
      "remainingPercentage": 75.4  
    }  
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
