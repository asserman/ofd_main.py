def getChek():
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