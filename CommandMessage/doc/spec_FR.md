<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : CommandMessage    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/CommandMessage/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Message de commande**    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `command[string]`: Commande envoyée au robot  - `commandTime[date-time]`: Envoi de l'heure au robot  - `type[string]`: Type d'entité NGSI. Il doit s'agir de CommandMessage  - `waypoints[array]`: Liste des points de passage  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `command`  - `commandTime`  - `id`  - `type`  - `waypoints`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
CommandMessage:      
  description: Command message      
  properties:      
    command:      
      description: Command sent to the robot      
      type: string      
      x-ngsi:      
        type: Property      
    commandTime:      
      description: Sent time to the robot      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be CommandMessage      
      enum:      
        - CommandMessage      
      type: string      
      x-ngsi:      
        type: Property      
    waypoints:      
      description: List of waypoints      
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
  required:      
    - id      
    - type      
    - commandTime      
    - command      
    - waypoints      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/CommandMessage/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/datamodel.AutonomousMobileRobot/CommandMessage/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### CommandMessage Valeurs clés NGSI-v2 Exemple    
Voici un exemple de message de commande au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### CommandMessage NGSI-v2 normalisé Exemple    
Voici un exemple de message de commande au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "CommandMessage",  
  "commandTime": {  
    "type": "DateTime",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "command": {  
    "type": "Text",  
    "value": "navi"  
  },  
  "waypoints": {  
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
  }  
}  
```  
</details>    
#### CommandMessage Valeurs clés NGSI-LD Exemple    
Voici un exemple de message de commande au format JSON-LD en tant que valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### CommandMessage NGSI-LD normalisé Exemple    
Voici un exemple de message de commande au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
