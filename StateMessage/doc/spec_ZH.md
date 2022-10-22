<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。状态信息  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StateMessage/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**状态信息**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `accuracy[object]`: 机器人的位置精度。  - `battery[object]`: 机器人安装的电池的状态。  - `commandTime[string]`: 发送给机器人的时间  - `destination[object]`: 机器人的当前目的地。基本上，它与其中一个航点相同  - `errors[array]`: 描述机器人中发生的错误。  - `mode[string]`: Enum:'error, navi, standby'.机器人的导航状态。  - `pose[object]`: 机器人的当前位置。  - `type[string]`: NGSI实体类型。它必须是StateMessage  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `accuracy`  - `battery`  - `commandTime`  - `destination`  - `errors`  - `id`  - `mode`  - `pose`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StateMessage:    
  description: 'State message'    
  properties:    
    accuracy:    
      additionalProperties: false    
      description: 'Position accuracy of the robot.'    
      properties:    
        covariance:    
          description: 'Property. Error covariance matrix of estimated position'    
          items:    
            type: number    
          type: array    
      type: object    
      x-ngsi:    
        type: Property    
    battery:    
      additionalProperties: false    
      description: 'The states of the battery the robot mounted.'    
      oneOf:    
        - required:    
            - voltage    
        - required:    
            - remainingTime    
        - required:    
            - remainingPercentage    
      properties:    
        current:    
          description: 'Property. Current of the mobile element. Units:''Ampere''. Model: ''https:/schema.org/Number'''    
          type: number    
        remainingPercentage:    
          description: 'Property. Remaining battery charge'    
          maximum: 100    
          minimum: 0    
          type: number    
        remainingTime:    
          description: 'Property. Expected lifespan of a battery. Model: ''https:/schema.org/DateTime'''    
          format: time    
          type: string    
        voltage:    
          description: 'Property. Voltage of the mobile element. Units:''Volt''. Model: ''https:/schema.org/Number'''    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    commandTime:    
      description: 'Sent time to the robot'    
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
          description: 'Property. Point in geographic coordinates'    
          properties: &statemessage_-_properties_-_pose_-_properties_-_geographicpoint_-_properties    
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
          required: &statemessage_-_properties_-_pose_-_properties_-_geographicpoint_-_required    
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
          properties: &statemessage_-_properties_-_pose_-_properties_-_orientation2d_-_properties    
            theta:    
              default: 0.0    
              description: 'Property. Simple measurement of an angle'    
              type: number    
          required: &statemessage_-_properties_-_pose_-_properties_-_orientation2d_-_required    
            - theta    
          type: object    
        orientation3D:    
          additionalProperties: true    
          description: 'Property. 3D Angles of an element'    
          properties: &statemessage_-_properties_-_pose_-_properties_-_orientation3d_-_properties    
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
          required: &statemessage_-_properties_-_pose_-_properties_-_orientation3d_-_required    
            - roll    
            - pitch    
            - yaw    
          type: object    
        point2D:    
          additionalProperties: true    
          description: 'Property. Point in 2D as a two simple coordinates x and y'    
          properties: &statemessage_-_properties_-_pose_-_properties_-_point2d_-_properties    
            x:    
              default: 0.0    
              description: 'Property. Simple coordinate of a point'    
              type: number    
            y:    
              default: 0.0    
              description: 'Property. Simple coordinate of a point'    
              type: number    
          required: &statemessage_-_properties_-_pose_-_properties_-_point2d_-_required    
            - x    
            - y    
          type: object    
        point3D:    
          additionalProperties: true    
          description: 'Property. Point in 3D as a three simple coordinates x, y and z'    
          properties: &statemessage_-_properties_-_pose_-_properties_-_point3d_-_properties    
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
          required: &statemessage_-_properties_-_pose_-_properties_-_point3d_-_required    
            - x    
            - y    
            - z    
          type: object    
      type: object    
      x-ngsi:    
        type: Property    
    errors:    
      description: 'Describes the errors that occurred in the robot.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    mode:    
      description: 'Enum:''error, navi, standby''. Navigational status of the robot.'    
      enum:    
        - error    
        - navi    
        - standby    
      type: string    
      x-ngsi:    
        type: Property    
    pose:    
      additionalProperties: false    
      description: 'Current position of the robot.'    
      maxProperties: 3    
      properties:    
        geographicPoint:    
          additionalProperties: true    
          description: 'Property. Point in geographic coordinates'    
          properties: *statemessage_-_properties_-_pose_-_properties_-_geographicpoint_-_properties    
          required: *statemessage_-_properties_-_pose_-_properties_-_geographicpoint_-_required    
          type: object    
        mapId:    
          description: 'Property. Map ID'    
          type: string    
        orientation2D:    
          additionalProperties: true    
          description: 'Property. 2D Angle of an element'    
          properties: *statemessage_-_properties_-_pose_-_properties_-_orientation2d_-_properties    
          required: *statemessage_-_properties_-_pose_-_properties_-_orientation2d_-_required    
          type: object    
        orientation3D:    
          additionalProperties: true    
          description: 'Property. 3D Angles of an element'    
          properties: *statemessage_-_properties_-_pose_-_properties_-_orientation3d_-_properties    
          required: *statemessage_-_properties_-_pose_-_properties_-_orientation3d_-_required    
          type: object    
        point2D:    
          additionalProperties: true    
          description: 'Property. Point in 2D as a two simple coordinates x and y'    
          properties: *statemessage_-_properties_-_pose_-_properties_-_point2d_-_properties    
          required: *statemessage_-_properties_-_pose_-_properties_-_point2d_-_required    
          type: object    
        point3D:    
          additionalProperties: true    
          description: 'Property. Point in 3D as a three simple coordinates x, y and z'    
          properties: *statemessage_-_properties_-_pose_-_properties_-_point3d_-_properties    
          required: *statemessage_-_properties_-_pose_-_properties_-_point3d_-_required    
          type: object    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StateMessage'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ＃＃＃＃有效载荷的例子  
#### StateMessage NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的StateMessage的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### StateMessage NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的StateMessage的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### StateMessage NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的StateMessage的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### StateMessage NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的StateMessage的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
