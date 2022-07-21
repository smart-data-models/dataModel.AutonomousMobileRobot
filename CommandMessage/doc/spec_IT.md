[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: CommandMessage  
======================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandMessage/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Messaggio di comando**  
versione: 0.0.1  

## Elenco delle proprietà  

- `command`: Comando inviato al robot  - `commandTime`: Inviato il tempo al robot  - `type`: Tipo di entità NGSI. Deve essere CommandMessage  - `waypoints`: Elenco dei waypoint.    
Proprietà richieste  
- `command`  - `commandTime`  - `id`  - `type`  - `waypoints`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CommandMessage:    
  description: 'Command message'    
  properties:    
    command:    
      description: 'Command sent to the robot'    
      type: string    
      x-ngsi:    
        type: Property    
    commandTime:    
      description: 'Sent time to the robot'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be CommandMessage'    
      enum:    
        - CommandMessage    
      type: string    
      x-ngsi:    
        type: Property    
    waypoints:    
      description: 'List of waypoints.'    
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
  required:    
    - id    
    - type    
    - commandTime    
    - command    
    - waypoints    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/CommandMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/datamodel.AutonomousMobileRobot/CommandMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### CommandMessage Valori chiave NGSI-v2 Esempio  
Ecco un esempio di un CommandMessage in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "command": "navi",  
  "waypoints": [  
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
}  
```  
#### CommandMessage NGSI-v2 normalizzato Esempio  
Ecco un esempio di un CommandMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandMessage",  
  "commandTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "command": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "waypoints": {  
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
  }  
}  
```  
#### CommandMessage Valori chiave NGSI-LD Esempio  
Ecco un esempio di un CommandMessage in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "command": "navi",  
  "waypoints": [  
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
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
#### CommandMessage NGSI-LD normalizzato Esempio  
Ecco un esempio di un CommandMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "CommandMessage",  
  "commandTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2019-06-07T08:39:40.064+09:00"  
    }  
  },  
  "command": {  
    "type": "Property",  
    "value": "navi"  
  },  
  "waypoints": {  
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
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
