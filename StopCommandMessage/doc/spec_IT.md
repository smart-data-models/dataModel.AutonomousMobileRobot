[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: StopCommandMessage  
==========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StopCommandMessage/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Messaggio di comando di arresto**  
versione: 0.0.1  

## Elenco delle proprietà  

- `commandTime`: Tempo inviato al robot  - `stopCommand`: Enum:'stop'. Il comando di arresto del robot.  - `type`: Tipo di entità NGSI. Deve essere StopCommandMessage    
Proprietà richieste  
- `commandTime`  - `id`  - `stopCommand`  - `type`  ## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StopCommandMessage:    
  description: 'Stop Command message'    
  properties:    
    commandTime:    
      description: 'Sent time to the robot'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    stopCommand:    
      description: 'Enum:''stop''. The stop command to the robot.'    
      enum:    
        - stop    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StopCommandMessage'    
      enum:    
        - StopCommandMessage    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - commandTime    
    - stopCommand    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/StopCommandMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AutonomousMobileRobot/StopCommandMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempi di payload  
#### StopCommandMessage Valori chiave NGSI-v2 Esempio  
Ecco un esempio di StopCommandMessage in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "stopCommand": "stop"  
}  
```  
#### StopCommandMessage NGSI-v2 normalizzato Esempio  
Ecco un esempio di StopCommandMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "stopCommand": {  
    "type": "Text",  
    "value": "stop"  
  }  
}  
```  
#### StopCommandMessage Valori chiave NGSI-LD Esempio  
Ecco un esempio di StopCommandMessage in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "stopCommand": "stop",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
#### StopCommandMessage Esempio normalizzato NGSI-LD  
Ecco un esempio di StopCommandMessage in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Date-Time",  
      "@value": "2019-06-07T08:39:40.064+09:00"  
    }  
  },  
  "stopCommand": {  
    "type": "Property",  
    "value": "stop"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
