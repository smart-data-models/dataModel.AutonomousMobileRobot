[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: StopCommandReturnMessage  
=================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StopCommandReturnMessage/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Mensaje de retorno del comando de parada**  
versión: 0.0.1  

## Lista de propiedades  

- `commandTime`: Tiempo de envío al robot  - `errors`: Describe los errores ocurridos en el robot.  - `receivedStopCommand`: La orden de parada que ha recibido el robot.  - `receivedTime`: Tiempo de recepción de la orden al robot  - `resultsOfStopCommand`: Enum:'ack, error'. El resultado de que el robot haya recibido la orden de parada.  - `type`: Tipo de entidad NGSI. Tiene que ser StopCommandReturnMessage    
Propiedades requeridas  
- `commandTime`  - `errors`  - `id`  - `receivedStopCommand`  - `receivedTime`  - `result`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StopCommandReturnMessage:    
  description: 'Stop Command Return Message'    
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
    receivedStopCommand:    
      description: 'The stop command which the robot received.'    
      enum:    
        - stop    
      type: string    
      x-ngsi:    
        type: Property    
    receivedTime:    
      description: 'Command received time to the robot'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    resultsOfStopCommand:    
      description: 'Enum:''ack, error''. The result of the robot received the stop command.'    
      enum:    
        - ack    
        - error    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StopCommandReturnMessage'    
      enum:    
        - StopCommandReturnMessage    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - commandTime    
    - errors    
    - id    
    - receivedStopCommand    
    - receivedTime    
    - result    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/StopCommandReturnMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/datamodel.AutonomousMobileRobot/StopCommandReturnMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### StopCommandReturnMessage NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un StopCommandReturnMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandReturnMessage",  
  "commandTime": "2019-06-07T08:39:42.921+09:00",  
  "receivedTime": "2019-06-07T08:39:40.064+09:00",  
  "receivedStopCommand": "stop",  
  "result": "ack",  
  "errors": []  
}  
```  
#### StopCommandReturnMessage NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un StopCommandReturnMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandReturnMessage",  
  "commandTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:42.921+09:00"  
  },  
  "receivedTime": {  
    "type": "Date-Time",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "receivedStopCommand": {  
    "type": "Text",  
    "value": "stop"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ack"  
  },  
  "errors": {  
    "type": "array",  
    "value": []  
  }  
}  
```  
#### StopCommandReturnMessage Ejemplo de valores clave NGSI-LD  
Aquí hay un ejemplo de un StopCommandReturnMessage en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StopCommandReturnMessage",  
  "commandTime": "2019-06-07T08:39:42.921+09:00",  
  "receivedTime": "2019-06-07T08:39:40.064+09:00",  
  "receivedStopCommand": "stop",  
  "result": "ack",  
  "errors": [],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
#### StopCommandReturnMessage NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un StopCommandReturnMessage en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:Mega_rover:01",  
  "type": "StopCommandReturnMessage",  
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
  "receivedStopCommand": {  
    "type": "Property",  
    "value": "stop"  
  },  
  "result": {  
    "type": "Property",  
    "value": "ack"  
  },  
  "errors": {  
    "type": "Property",  
    "value": []  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
