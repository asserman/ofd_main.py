# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pickle


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # from PyQT4 import Qt
    import datetime
    import json
    import requests

    from libfptr10 import IFptr
    fptr = IFptr(r"")
    print(fptr.version())
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, "COM16")
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_BAUDRATE, str(IFptr.LIBFPTR_PORT_BR_115200))
    fptr.applySingleSettings()
    print(fptr.LIBFPTR_SETTING_COM_FILE)
    if (fptr.showProperties(IFptr.LIBFPTR_GUI_PARENT_NATIVE, 0)):
        print('kkm ok')

    AuthToken = 'b8da24fd7f1b4bf880ba0d736ddc583f'
    params = {'FNSerialNumber':'7281440701491259',
              'KKTSerialNumber':'00105703726631',
              'KKTRegNumber':'0002842895012548',
              'AuthToken': AuthToken}
    INN = '2130133051'
    resp = requests.get('https://ofd.ru/api/integration/v2/inn/'+INN+'/kkts', params=params )

    if (resp.json()['Status'] == "Success"):
        print ('ok')

        dateFrom = datetime.date(2022, 9, 30)

        # pickle.dump(dateFrom, open("date.json", 'wb'))
        dateFrom = pickle.load(open("date.json", 'rb'))
        dateTo = dateFrom + datetime.timedelta(30)

        print(dateFrom)
        print(dateTo)

        param_cheks = {'dateFrom' : dateFrom , 'dateTo' : dateTo, 'AuthToken': AuthToken}
        cheks =[]
        err_cheks = requests.get('https://ofd.ru/api/integration/v2/kkt/'+params['KKTRegNumber']+'/receipts/errors?DateFrom='+str(dateFrom)+'&DateTo='+str(dateFrom)+'&AuthToken='+params['AuthToken'])
        cheks_table = err_cheks.json()['Data']
        cheks_body = requests.get('https://ofd.ru/api/integration/v2/inn/'+INN+'/kkt/'+params['KKTRegNumber']+'/receipts-with-fpd-short?dateFrom='+str(dateFrom)+'&dateTo='+str(dateTo)+'&AuthToken='+params['AuthToken'])
        for i in range(len(cheks_body.json()['Data'])):
            print(i, end=' ')
            cheks_with_moneyOperator = requests.get('https://ofd.ru/api/integration/v2/inn/'+INN+'/kkt/'+params[
                'KKTRegNumber']+'/receipt/'+cheks_body.json()['Data'][i]['Id'] + '?AuthToken=' + params['AuthToken'])
            # print(cheks_with_moneyOperator.json()['Data'])
            cheks.append(cheks_with_moneyOperator.json()['Data'])

        cheks.sort(key= lambda x: x.get('Document_Number'))
        # print (cheks)
        filename = str(dateFrom) + '.json'
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(cheks, file)
        file.close
        # chekst = []
        # with open(filename, 'r', encoding="utf-8") as file:
        #     chekst = json.load(file)
        # file.close
        dateTo = dateTo  + datetime.timedelta(1)
        pickle.dump(dateTo, open("date.json", 'wb'))
        print('end__')



