<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：命令返回信息    
=========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**命令返回信息**    
版本： 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `commandTime[date-time]`: 向机器人发送时间  - `errors[array]`: 描述机器人发生的错误  - `receivedCommand[string]`: 机器人接收到的指令  - `receivedTime[date-time]`: 接收到机器人指令的时间  - `receivedWaypoints[array]`: 机器人接收到的航点  - `result[string]`: 枚举："接受、错误、忽略"。机器人接收命令的结果  - `type[string]`: NGSI 实体类型。必须是 CommandReturnMessage  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `commandTime`  - `errors`  - `id`  - `receivedCommand`  - `receivedTime`  - `receivedWaypoints`  - `result`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### CommandReturnMessage NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 CommandReturnMessage 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### 命令返回信息 NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的命令返回信息（CommandReturnMessage）示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### CommandReturnMessage NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 CommandReturnMessage 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### 命令返回信息 NGSI-LD 正常化示例    
下面是一个规范化 JSON-LD 格式的 CommandReturnMessage 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
