<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: StopCommandReturnMessage  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AutonomousMobileRobot/blob/master/StopCommandReturnMessage/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전역 설명: **명령 반환 메시지 중지**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `commandTime[date-time]`: 로봇에 시간 보내기  - `errors[array]`: 로봇에서 발생한 오류를 설명합니다.  - `receivedStopCommand[string]`: 로봇이 수신한 중지 명령입니다.  - `receivedTime[date-time]`: 명령이 로봇에 수신된 시간  - `resultsOfStopCommand[string]`: Enum:'에러'. 로봇이 중지 명령을 받은 결과입니다.  - `type[string]`: NGSI 엔티티 유형. StopCommandReturnMessage여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `commandTime`  - `errors`  - `id`  - `receivedStopCommand`  - `receivedTime`  - `result`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StopCommandReturnMessage:    
  description: Stop Command Return Message    
  properties:    
    commandTime:    
      description: Sent time to the robot    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    errors:    
      description: Describes the errors that occurred in the robot    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    receivedStopCommand:    
      description: The stop command which the robot received.    
      enum:    
        - stop    
      type: string    
      x-ngsi:    
        type: Property    
    receivedTime:    
      description: Command received time to the robot    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    resultsOfStopCommand:    
      description: 'Enum:''ack, error''. The result of the robot received the stop command'    
      enum:    
        - ack    
        - error    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be StopCommandReturnMessage    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AutonomousMobileRobot/blob/master/StopCommandReturnMessage/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/datamodel.AutonomousMobileRobot/StopCommandReturnMessage/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### StopCommandReturnMessage NGSI-v2 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 StopCommandReturnMessage의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StopCommandReturnMessage NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StopCommandReturnMessage의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StopCommandReturnMessage NGSI-LD 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 StopCommandReturnMessage의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StopCommandReturnMessage NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StopCommandReturnMessage의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
