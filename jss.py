def j():
    return  """{
       "type": "sell",
       "taxationType": "osn",
       "ignoreNonFiscalPrintErrors": false,
    
       "operator": {
           "name": "Иванов",
           "vatin": "123654789507"
       },
    
       "items": [
           {
               "type": "position",
               "name": "Бананы",
               "price": 73.15,
               "quantity": 1.0,
               "amount": 73.15,
               "infoDiscountAmount": 0.0,
               "department": 1,
               "measurementUnit": "кг",
               "paymentMethod": "advance",
               "paymentObject": "commodity",
               "nomenclatureCode": "RE0ELx+WgXhKZ1hKNS5UMTEyMDAw",
               "tax": {
                   "type": "vat20"
               },
               "agentInfo": {
                   "agents": ["payingAgent", "bankPayingAgent"],
                   "payingAgent": {
                       "operation": "Оплата",
                       "phones": ["+79161112233"]
                   },
                   "receivePaymentsOperator": {
                        "phones": ["+79163331122"]
                   },
                   "moneyTransferOperator": {
                        "phones": ["+79162223311"],
                        "name": "Оператор перевода",
                        "address": "Улица Оператора Перевода, д.1",
                        "vatin": "321456987121"
                   }
               },
               "supplierInfo": {
                   "phones": ["+79175555555"],
                   "name": "Поставщик",
                   "vatin": "956839506500"
               }
               {
                   "phones": ["+79175555555"],
                   "name": "Поставщик",
                   "vatin": "956839506500",
                   "supplierPrint": true,
                   "supplierVatinPrint": true
                }
           },
           {
               "type": "text",
               "text": "--------------------------------",
               "alignment": "left",
               "font": 0,
               "doubleWidth": false,
               "doubleHeight": false
           },
           {
               "type": "position",
               "name": "Шуба",
               "price": 51.25,
               "quantity": 2.0,
               "amount": 102.50,
               "department": 1,
               "paymentMethod": "fullPayment",
               "paymentObject": "commodity",
               "nomenclatureCode": {
                  "type": "furs",
                  "gtin": "98765432101234",
                  "serial": "RU-430302-ABC1234567"
               },
               "tax": {
                   "type": "vat10"
               }
           },
           {
               "type": "text",
               "text": "--------------------------------",
               "alignment": "left",
               "font": 0,
               "doubleWidth": false,
               "doubleHeight": false
           },
           {
               "type": "position",
               "name": "Кефир",
               "price": 48.45,
               "quantity": 1.0,
               "amount": 48.45,
               "department": 1,
               "measurementUnit": "шт.",
               "paymentMethod": "fullPrepayment",
               "paymentObject": "excise",
               "additionalAttribute": "ID:iASDv3w45",
               "tax": {
                   "type": "vat0"
               }
           },
           {
               "type": "barcode",
               "barcode": "123456789012",
               "barcodeType": "EAN13",
               "scale": 2
           }
       ],
       "payments": [
           {
               "type": "cash",
               "sum": 2000.00
           }
       ],
       "total": 224.00
    }"""