# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def getCheks():
    import pickle
    import datetime
    import json
    import requests
    AuthToken = 'b8da24fd7f1b4bf880ba0d736ddc583f'
    params = {'FNSerialNumber': '7281440701491259',
              'KKTSerialNumber': '00105703726631',
              'KKTRegNumber': '0002842895012548',
              'AuthToken': AuthToken}
    INN = '2130133051'
    resp = requests.get('https://ofd.ru/api/integration/v2/inn/' + INN + '/kkts', params=params)

    if (resp.json()['Status'] == "Success"):
        print('ok')

        dateFrom = datetime.date(2022, 9, 30)

        # pickle.dump(dateFrom, open("date.json", 'wb'))
        dateFrom = pickle.load(open("date.json", 'rb'))
        dateTo = dateFrom + datetime.timedelta(30)

        print(dateFrom)
        print(dateTo)

        param_cheks = {'dateFrom': dateFrom, 'dateTo': dateTo, 'AuthToken': AuthToken}
        cheks = []
        err_cheks = requests.get(
            'https://ofd.ru/api/integration/v2/kkt/' + params['KKTRegNumber'] + '/receipts/errors?DateFrom=' + str(
                dateFrom) + '&DateTo=' + str(dateFrom) + '&AuthToken=' + params['AuthToken'])
        cheks_table = err_cheks.json()['Data']
        cheks_body = requests.get('https://ofd.ru/api/integration/v2/inn/' + INN + '/kkt/' + params[
            'KKTRegNumber'] + '/receipts-with-fpd-short?dateFrom=' + str(dateFrom) + '&dateTo=' + str(
            dateTo) + '&AuthToken=' + params['AuthToken'])
        for i in range(len(cheks_body.json()['Data'])):
            print(i, end=' ')
            cheks_with_moneyOperator = requests.get(
                'https://ofd.ru/api/integration/v2/inn/' + INN + '/kkt/' + params[
                    'KKTRegNumber'] + '/receipt/' + cheks_body.json()['Data'][i]['Id'] + '?AuthToken=' + params[
                    'AuthToken'])
            # print(cheks_with_moneyOperator.json()['Data'])
            cheks.append(cheks_with_moneyOperator.json()['Data'])

        cheks.sort(key=lambda x: x.get('Document_Number'))
        # print (cheks)
        filename = str(dateFrom) + '.json'
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(cheks, file)
        file.close
        # chekst = []
        # with open(filename, 'r', encoding="utf-8") as file:
        #     chekst = json.load(file)
        # file.close
        dateTo = dateTo + datetime.timedelta(1)
        pickle.dump(dateTo, open("date.json", 'wb'))
        print('end__')


if __name__ == '__main__':
    import pickle
    import datetime
    import json
    import requests
    from libfptr10 import IFptr

    fptr = IFptr("")
    # fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    # fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    # fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM7")
    # fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    # version = fptr.version()

    # with open("settings.set", "r" , encoding="utf-8") as file:
    #     json.load( file , setting)
    # file.close
    # if (fptr.showProperties(IFptr.LIBFPTR_GUI_PARENT_NATIVE, 0)==0):

    setting = json
    print(fptr.getSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE))
    setting = fptr.getSettings();
    with open("settings.set", 'w', encoding="utf-8") as file:
        json.dump(setting, file)
    file.close
    fptr.applySingleSettings()
    fptr.open()

    fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SERIAL_NUMBER)
    fptr.queryData()
    serialNumber = fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER)
    print(serialNumber)

    import jss
    filename = "2022-09-30.json"
    with open(filename, "rb") as file:
        ju = json.load(file)
    ss = ju[1]
    ss["type"] = "sellReturn"
    del ss["Tag"]
    del ss["UserInn"]
    del ss["ShiftNumber"]
    del ss["DateTime"]
    del ss["Number"]
    del ss["OperationType"]
    del ss["KKT_RegNumber"]
    del ss["FN_FactoryNumber"]
    del ss["Format_Version"]

    ss["operator"] = {}
    ss["operator"]["name"] = ss["Operator"];
    del ss["Operator"]
    ss["payments"] = {}
    ss["operator"]["type"] = "cash";
    ss["operator"]["sum"] = ss["Amount_Cash"];
    del ss["Amount_Cash"]
    ss["total"] = ss["Amount_Total"]
    del ss["Amount_Total"]

    ss["supplierInfo"] = {}
    ss["supplierInfo"]["phones"] = ss["MoneyOperator_Phone"][0]
    ss["supplierInfo"]["name"] = ss["MoneyOperator_Name"]
    ss["supplierInfo"]["vatin"] = ss["MoneyOperator_INN"]

    # del ss[""]
    # del ss[""]
    # del ss[""]

    for i in range(len(ss["Items"])):
        ssi = ss["Items"][i]
        ssi["type"] = "position"
        ssi["price"] = ssi["Price"] *0.01
        del ssi["Price"]
        ssi["amount"] = ssi["Total"] *0.01
        del ssi["Total"]
        ssi["quantity"] = ssi["Quantity"]
        del ssi["Quantity"]
        ssi["name"] = ssi["Name"]
        del ssi["Name"]
        ssi["tax"] = {}
        ssi["tax"]["type"] = "vat0"
        ssi["department"] = 1
        ssi["paymentMethod"] ="fullPayment"
        del ssi["CalculationMethod"]
        ssi["paymentObject"]= "commodity"

    print()

    # fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, jss.j())
    # fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, ss)
    # print(fptr.validateJson())

    jssj = json.loads(jss.j())
    jssj["type"] = "sellReturn"

    fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA,  json.dumps(jssj))
    # fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, json.dumps(ss))
    fptr.processJson()


    fptr.close()

    # result = fptr.getParamString(IFptr.LIBFPTR_PARAM_JSON_DATA)
    # import getCheks
    # getCheks.getChek()



