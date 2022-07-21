[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティStopCommandReturnMessage  
==============================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StopCommandReturnMessage/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**ストップコマンドリターンメッセージ  
バージョン: 0.0.1  

## プロパティ一覧  

- `commandTime`: ロボットへの送信時間  - `errors`: ロボットで発生したエラーについて説明します。  - `receivedStopCommand`: ロボットが受信した停止コマンド。  - `receivedTime`: ロボットへのコマンド受信時間  - `resultsOfStopCommand`: Enum:'ack, error'.ロボットが停止コマンドを受信した結果です。  - `type`: NGSI エンティティタイプ。StopCommandReturnMessageでなければならない。    
必要なプロパティ  
- `commandTime`  - `errors`  - `id`  - `receivedStopCommand`  - `receivedTime`  - `result`  - `type`  ## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### StopCommandReturnMessage NGSI-v2 key-value Example  
以下は、StopCommandReturnMessage を JSON-LD フォーマットで key-value にした例です。これは、`options=keyValues` を使用したときに NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StopCommandReturnMessage NGSI-v2 正規化例  
以下は、StopCommandReturnMessage を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StopCommandReturnMessage NGSI-LD キー値例  
以下は、StopCommandReturnMessageをJSON-LD形式でkey-valuesとして記述した例です。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
#### StopCommandReturnMessage NGSI-LD 正規化例  
以下は、StopCommandReturnMessage を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
