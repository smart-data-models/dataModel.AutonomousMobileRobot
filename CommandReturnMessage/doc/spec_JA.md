<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティコマンドリターンメッセージ    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**コマンドリターンメッセージ    
バージョン: 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `commandTime[date-time]`: ロボットに時間を送信  - `errors[array]`: ロボットで発生したエラーについて説明する。  - `receivedCommand[string]`: ロボットが受信したコマンド  - `receivedTime[date-time]`: ロボットへのコマンド受信時間  - `receivedWaypoints[array]`: ロボットが受信したウェイポイント  - `result[string]`: Enum:'ack, error, ignore'.ロボットがコマンドを受信した結果  - `type[string]`: NGSI エンティティタイプ。これは CommandReturnMessage でなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `commandTime`  - `errors`  - `id`  - `receivedCommand`  - `receivedTime`  - `receivedWaypoints`  - `result`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### CommandReturnMessage NGSI-v2 キー値の例    
以下は、JSON-LD形式のCommandReturnMessageのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
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
#### CommandReturnMessage NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のCommandReturnMessageの例である。これは、NGSI-v2と互換性があり、オプションを使用せず、個々のエンティティのコンテキストデータを返す。    
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
#### CommandReturnMessage NGSI-LD キー値の例    
JSON-LD形式のCommandReturnMessageのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
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
#### CommandReturnMessage NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のCommandReturnMessageの例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
