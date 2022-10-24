<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: CommandReturnMessage  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandReturnMessage/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Mensaje de retorno del comando**  
versión: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `commandTime[string]`: Tiempo de envío al robot  - `errors[array]`: Describe los errores ocurridos en el robot.  - `receivedCommand[string]`: La orden que recibió el robot  - `receivedTime[string]`: Tiempo de recepción de la orden al robot  - `receivedWaypoints[array]`: Los puntos de ruta que recibió el robot.  - `result[string]`: Enum:'ack, error, ignorar'. El resultado del robot recibió el comando.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser CommandReturnMessage  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `commandTime`  - `errors`  - `id`  - `receivedCommand`  - `receivedTime`  - `receivedWaypoints`  - `result`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### CommandReturnMessage NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un CommandReturnMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### CommandReturnMessage NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un CommandReturnMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### CommandReturnMessage NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un CommandReturnMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### CommandReturnMessage NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un CommandReturnMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
