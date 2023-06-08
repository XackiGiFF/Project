import requests

# url для поиска пациэнтов в базе данных больницы
url = 'https://gorzdrav.spb.ru/_api/api/v2/patient/search'
#session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 Safari/537.36',

}

params = {'lpuId': 296,
          'lastName': 'Шарипов',
          'firstName': 'Руслан',
          'middleName': 'Рустемович',
          'birthdate': '1998-07-18T00:00:00',
          'birthdateValue': '18.07.1998'}

resp = requests.get(url, params=params, headers=headers)
print(resp.json())
token = resp.headers['token']
print(token)
# url для для post-запроса
# Вики по запросам: https://github.com/egorantonov/gorzdrav/wiki/SPB-Gorzdrav-API-Documentation
url_1 = 'https://gorzdrav.spb.ru/_api/api/v2/appointment/create' #Это запись на прием

head = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
    'Content-Type': 'application/json',
    'Host': 'gorzdrav.spb.ru',
    'Origin': 'https://gorzdrav.spb.ru',
    'Referer': 'https://gorzdrav.spb.ru/service-free-schedule',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36',
    'Token': token,
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin'

}
data = {
    "esiaId": None,
    "lpuId": "296",
    "patientId": "ШАРИПОВ;РУСЛАН;РУСТЕМОВИЧ;18.07.1998",
    "appointmentId": "16.06.2023;10:06;п76с.229",
    "referralId": None,
    "ipmpiCardId": None,
    "recipientEmail": '',
    "patientLastName": "Шарипов",
    "patientFirstName": "Руслан",
    "patientMiddleName": "Рустемович",
    "patientBirthdate": "1998-07-18T00:00:00",
    "address": "ул. Хлопина, д. 11, к. 1"
}

response = requests.post(url_1, data=data, headers=head)
print(response.json())
