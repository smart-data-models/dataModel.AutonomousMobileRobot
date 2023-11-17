<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティStopCommandMessage    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StopCommandMessage/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**コマンド停止メッセージ    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `commandTime[date-time]`: ロボットに時間を送信  - `stopCommand[string]`: Enum:'stop'.ロボットへの停止命令  - `type[string]`: NGSI エンティティタイプ。これは StopCommandMessage でなければなりません。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `commandTime`  - `id`  - `stopCommand`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
StopCommandMessage:      
  description: Stop Command message      
  properties:      
    commandTime:      
      description: Sent time to the robot      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    stopCommand:      
      description: 'Enum:''stop''. The stop command to the robot'      
      enum:      
        - stop      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be StopCommandMessage      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/StopCommandMessage/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.AutonomousMobileRobot/StopCommandMessage/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### StopCommandMessage NGSI-v2 キー値の例    
以下はStopCommandMessageをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": "2019-06-07T08:39:40.064+09:00",  
  "stopCommand": "stop"  
}  
```  
</details>    
#### 停止コマンドメッセージ NGSI-v2 正規化例    
以下は、正規化されたJSON-LDフォーマットのStopCommandMessageの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "Robot:Mega_rover:01",  
  "type": "StopCommandMessage",  
  "commandTime": {  
    "type": "DateTime",  
    "value": "2019-06-07T08:39:40.064+09:00"  
  },  
  "stopCommand": {  
    "type": "Text",  
    "value": "stop"  
  }  
}  
```  
</details>    
#### StopCommandMessage NGSI-LD キー値の例    
以下はStopCommandMessageをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### StopCommandMessage NGSI-LD 正規化例    
以下は、正規化されたJSON-LDフォーマットのStopCommandMessageの例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
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
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
