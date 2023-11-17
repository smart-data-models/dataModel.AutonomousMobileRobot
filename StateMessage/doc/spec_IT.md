<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: StatoMessaggio    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StateMessage/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Messaggio di stato**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `accuracy[object]`: Precisione di posizione del robot  	    
- `battery[object]`: Gli stati della batteria montata dal robot  	- `current[number]`: Corrente dell'elemento mobile  . Model: [ https:/schema.org/Number]( https:/schema.org/Number)    
	- `remainingPercentage[number]`: Carica residua della batteria      
	- `remainingTime[time]`: Durata di vita prevista di una batteria  . Model: [ https:/schema.org/DateTime]( https:/schema.org/DateTime)    
- `commandTime[date-time]`: Tempo inviato al robot  - `destination[object]`: Destinazione attuale del robot. Fondamentalmente, è la stessa di uno dei waypoint  	- `geographicPoint[object]`: Punto in coordinate geografiche      
	- `mapId[string]`: ID mappa      
	- `orientation2D[object]`: Angolo 2D di un elemento      
	- `orientation3D[object]`: Angoli 3D di un elemento      
	- `point2D[object]`: Punto in 2D come due semplici coordinate x e y      
- `errors[array]`: Descrive gli errori che si sono verificati nel robot.  - `mode[string]`: Enum:'error, navi, standby'. Stato di navigazione del robot  - `pose[object]`: Posizione attuale del robot.  	- `geographicPoint[object]`: Punto in coordinate geografiche      
	- `mapId[string]`: ID mappa      
	- `orientation2D[object]`: Angolo 2D di un elemento      
	- `orientation3D[object]`: Angoli 3D di un elemento      
	- `point2D[object]`: Punto in 2D come due semplici coordinate x e y      
- `type[string]`: Tipo di entità NGSI. Deve essere StateMessage  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `accuracy`  - `battery`  - `commandTime`  - `destination`  - `errors`  - `id`  - `mode`  - `pose`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### StatoMessaggio Valori chiave NGSI-v2 Esempio    
Ecco un esempio di StateMessage in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### StatoMessaggio NGSI-v2 normalizzato Esempio    
Ecco un esempio di StateMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### StatoMessaggio Valori chiave NGSI-LD Esempio    
Ecco un esempio di StateMessage in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### StatoMessaggio NGSI-LD normalizzato Esempio    
Ecco un esempio di StateMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
