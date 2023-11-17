<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: StateMessage    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StateMessage/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **상태 메시지**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `accuracy[object]`: 로봇의 위치 정확도  	- `covariance[array]`: 추정 위치의 오차 공분산 행렬      
- `battery[object]`: 로봇이 장착한 배터리 상태  	- `current[number]`: 모바일 요소의 전류  . Model: [ https:/schema.org/Number]( https:/schema.org/Number)    
	- `remainingPercentage[number]`: 배터리 잔량      
	- `remainingTime[time]`: 배터리 예상 수명  . Model: [ https:/schema.org/DateTime]( https:/schema.org/DateTime)    
	- `voltage[number]`: 모바일 요소의 전압  . Model: [ https:/schema.org/Number]( https:/schema.org/Number)    
- `commandTime[date-time]`: 로봇에 시간 보내기  - `destination[object]`: 로봇의 현재 목적지입니다. 기본적으로 웨이포인트 중 하나와 동일합니다.  	- `geographicPoint[object]`: 지리적 좌표의 포인트      
	- `mapId[string]`: 지도 ID      
	- `orientation2D[object]`: 요소의 2D 각도      
	- `orientation3D[object]`: 요소의 3D 각도      
	- `point2D[object]`: 2D에서 두 개의 간단한 좌표 x와 y로 포인트를 지정합니다.      
	- `point3D[object]`: 3D에서 세 개의 간단한 좌표 x, y, z로 포인트를 지정합니다.      
- `errors[array]`: 로봇에서 발생한 오류를 설명합니다.  - `mode[string]`: Enum:'오류, 내비, 대기'. 로봇의 내비게이션 상태  - `pose[object]`: 로봇의 현재 위치입니다.  	- `geographicPoint[object]`: 지리적 좌표의 포인트      
	- `mapId[string]`: 지도 ID      
	- `orientation2D[object]`: 요소의 2D 각도      
	- `orientation3D[object]`: 요소의 3D 각도      
	- `point2D[object]`: 2D에서 두 개의 간단한 좌표 x와 y로 포인트를 지정합니다.      
	- `point3D[object]`: 3D에서 세 개의 간단한 좌표 x, y, z로 포인트를 지정합니다.      
- `type[string]`: NGSI 엔티티 유형입니다. StateMessage여야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `accuracy`  - `battery`  - `commandTime`  - `destination`  - `errors`  - `id`  - `mode`  - `pose`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
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
## 페이로드 예시    
#### StateMessage NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 StateMessage의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
  },  
  "battery": {  
    "remainingPercentage": 75.4  
  }  
}  
```  
</details>    
#### StateMessage NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 StateMessage의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StateMessage",  
  "commandTime": {  
    "type": "DateTime",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "mode": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "errors": {  
    "type": "StructuredValue",  
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
#### StateMessage NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 StateMessage의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
#### StateMessage NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 StateMessage의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
