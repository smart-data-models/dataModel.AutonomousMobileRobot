[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: StateMessage  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StateMessage/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Mensaje de estado**  
versión: 0.0.1  

## Lista de propiedades  

- `accuracy`: Precisión de la posición del robot.  - `battery`: Los estados de la batería que montó el robot.  - `commandTime`: Tiempo de envío al robot  - `destination`: Destino actual del robot. Básicamente, es el mismo que uno de los waypoints  - `errors`: Describe los errores ocurridos en el robot.  - `mode`: Enum:'error, navi, standby'. Estado de navegación del robot.  - `pose`: Posición actual del robot.  - `type`: Tipo de entidad NGSI. Tiene que ser StateMessage    
Propiedades requeridas  
- `accuracy`  - `battery`  - `commandTime`  - `destination`  - `errors`  - `id`  - `mode`  - `pose`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### StateMessage NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un StateMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### StateMessage NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un StateMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### StateMessage NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un StateMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### StateMessage NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un StateMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
