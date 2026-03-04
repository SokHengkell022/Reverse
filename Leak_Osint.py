import requests
import json
import os
import sys
import time
import platform
import re
from pypasser import reCaptchaV3
from bs4 import BeautifulSoup as parser
from datetime import datetime

def get_user_id():
    system = platform.system()
    if system == 'Linux':
        if os.path.exists('/data/data/com.termux/files/home'):
            try:
                user_id = os.getlogin()
            except OSError:
                pass  # postinserted
            else:  # inserted
                return user_id
        else:  # inserted
            user_id = os.getenv('USER') or os.getenv('LOGNAME') or 'Tidak tersedia'
            return user_id
    else:  # inserted
        if system == 'Darwin':
            user_id = os.getenv('USER') or os.getenv('LOGNAME')
            return user_id
        if system == 'Windows':
            user_id = os.getlogin()
            return user_id
        if system == 'iOS':
            user_id = 'Tidak tersedia'
            return user_id
        user_id = 'Sistem operasi tidak dikenali'
        return user_id
        user_id = os.getenv('USER') or os.getenv('LOGNAME') or 'Pengguna Termux'

def check_id_status(user_id):
    url = 'https://api.ryochinel.my.id/users/data/get'
    response = requests.get(url).json()
    for user in response['id']:
        if user_id in user.values():
            expired_date_str = user['expired_date']
            expired_date = datetime.strptime(expired_date_str, '%d-%m-%y').date()
            current_date = datetime.now().date()
            if expired_date < current_date:
                return ('expired', expired_date_str, user['name'], user.get('phone', None))
            return ('active', expired_date_str, user['name'], user.get('phone', None))
    else:  # inserted
        return ('not_registered', None, None, None)

def censor_phone(phone):
    if phone and len(phone) > 6:
        return phone[:5] + '******' + phone[(-2):]
    return 'No phone'
user_id = get_user_id()
status, expired_date, user_name, phone = check_id_status(user_id)

def format_phone(phone):
    if phone and phone.startswith('+62'):
        return phone.replace('+62', '0', 1)
    return phone
censored_phone = censor_phone(phone)
formatted_phone = format_phone(phone)
reCaptcha_response = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcs6gYaAAAAAFgluYoQBea_lCpiT9MkKH-jzhDH&co=aHR0cHM6Ly9jZWtkcHRvbmxpbmUua3B1LmdvLmlkOjQ0Mw..&hl=id&v=WV-mUKO4xoWKy9M4ZzRyNrP_&size=invisible&cb=g4jdr7vvyjlj')

def GetCode(passport, formatted_phone):
    url = 'https://cekdptonline.kpu.go.id/v2'
    headers = {'Host': 'cekdptonline.kpu.go.id', 'Connection': 'keep-alive', 'Content-Length': '2059', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://cekdptonline.kpu.go.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://cekdptonline.kpu.go.id/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie': '_ga=GA1.3.898975063.1723632644; aliyungf_tc=f5298cbe2a7209647b3b4a631ce40a48a666a2ba1bfe21ac2d474f295fa35d7a; acw_tc=ac11000117257210620496016e8bd8776c0c4d4f8ce19c9d41eaa1c0becf7d; _gid=GA1.3.1584439243.1725721063'}
    data = {'query': '\n      {\n        findNikPilkada (\n            nik: \"%s\",\n            wilayah_id:0,\n            hp: \"%s\"\n            token:\"qs1byəL03AFcWeAxJP5ʍ_Lu3ɴ3WugztD9HVT7fMʌaMilfL6iOɢRpw2CgOlXJZCDZk32jCR-yc8Xu39lz0ZFtZhUg9O5DYrVkSdyDWIbWK2gkqnUk4NrYNQdvDr79vt0wU1Q2if866Crr5Lj4hmgvVSLiuopX3Hu7BGrJ3gqhIQHsrJpzzBxndtu-NlQhD1_Rm0iWyooVuqVXHJEsKNxNwiDPMMR1EjnXYgg6IYa3hnDMpBYQjIoMkhOkihPnFcD_80pupLcF9-uqKMiZLVkI76PqxRelZiVzpIf1tx4Tz_9KRESf4DKQvj24ixzNO3iiv6nVEV3lCfLKyjaj5LYO6XnqaRMgObDGfhtTD4C9zHgf60q3dBW8dafiOf7nqeQ0MUa8V4i-oJlkaPOwr9jalZf1-7I0B00vOmB4pUHRobGgCwsF1w_U7fAFkge3pDWPdNP1DPX29xR7BvYo0b9baNPA_b2JTBUHUGM9UjgQY0DtOlEkG-hapUnJW2icmpE4kw6ikpkOn8Ye4syT-slKJSrx4nJL4F6KTj9rlrBaMa_ItbJknHDUiQLbjamOWSSstZYLTs8VVJsUE9RnO40X2Qei9n0ttFKAgh_9r-WLpXfLdM0CqR9VQ1fH5RkFSRqQxYV8lOVRmh3Ek5jiXfHpSTuCZcD-F0g51zPqP4KGcjUtCGLdllW18xtoehdPnrccD9sCuSmIs5wXL0F39Ai9p9XmcjI3ZuRjnU-MD64t7d4X2UVZDJatKSTFnkU5Yy5qX9_HNyx1fhC0BowKVCN_Bo9RBwnt6mu3yJ0rb0ySUCiQD-mq7nf_-0GoOPSsMiv2FdcPnog8pSVjgq___CMTk1qOPwRH3ZuAEsy0uOsJf1JODaCB14QoG7j5qoMLvHTFskuoCb6i4DMvLfLh4\",\n        ) {\n          nama,\n          nik,\n          nkk,\n          provinsi,\n          kabupaten,\n          kecamatan,\n          kelurahan,\n          tps,\n          alamat,\n          lat,\n          lon,\n          metode,\n          lhp {\n                nama,\n                nik,\n                nkk,\n                kecamatan,\n                kelurahan,\n                tps,\n                id,\n                flag,\n                source,\n                alamat,\n                lat,\n                lon,\n                metode\n          }\n        }\n      }\n      ' % (passport, formatted_phone)}
    return requests.post(url, headers=headers, json=data).json()['errors'][0]['message']

def GetData(formatted_phone, hash, code):
    url = 'https://cekdptonline.kpu.go.id/v2'
    headers = {'Host': 'cekdptonline.kpu.go.id', 'Connection': 'keep-alive', 'Content-Length': '1983', 'Accept': 'application/json, text/plain, */*', 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://cekdptonline.kpu.go.id', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://cekdptonline.kpu.go.id/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'Cookie': '_ga=GA1.3.898975063.1723632644; aliyungf_tc=f5298cbe2a7209647b3b4a631ce40a48a666a2ba1bfe21ac2d474f295fa35d7a; acw_tc=ac11000117257210620496016e8bd8776c0c4d4f8ce19c9d41eaa1c0becf7d; _gid=GA1.3.1584439243.1725721063'}
    data = {'query': '\n      {\n        getMyResult (\n            hp: \"%s\",\n            seq: \"%s\",\n            otp: \"%s\",\n            token: \"_f!2-əQ%s\"\n        ) {\n          nama,\n          nik,\n          nkk,\n          provinsi,\n          kabupaten,\n          kecamatan,\n          kelurahan,\n          tps,\n          alamat,\n          lat,\n          lon,\n          metode,\n          lhp {\n                nama,\n                nik,\n                nkk,\n                kecamatan,\n                kelurahan,\n                tps,\n                id,\n                flag,\n                source,\n                alamat,\n                lat,\n                lon,\n                metode\n          }\n        }\n      }\n      ' % (formatted_phone, hash, code, reCaptcha_response)}
    resp = requests.post(url, headers=headers, json=data)
    try:
        nama = resp.json()['data']['getMyResult']['nama']
        provinsi = resp.json()['data']['getMyResult']['provinsi']
        kabupaten = resp.json()['data']['getMyResult']['kabupaten']
        kecamatan = resp.json()['data']['getMyResult']['kecamatan']
        kelurahan = resp.json()['data']['getMyResult']['kelurahan']
        alamat = resp.json()['data']['getMyResult']['alamat']
        lat = resp.json()['data']['getMyResult']['lat']
        lon = resp.json()['data']['getMyResult']['lon']
        kordinat = f'https://www.google.com/maps?q={lat},{lon}'
        print('   [ DATA DITEMUKAN ]')
        print(f'\n   [!] Nama     : {nama}\n   [!] Provinsi : {provinsi}\n   [!] Kabupaten: {kabupaten}\n   [!] Kecamatan: {kecamatan}\n   [!] Kelurahan: {kelurahan}\n   [!] Alamat   : {alamat}\n   [!] Maps     : {kordinat}\n    ')
    except:
        print('   [!] Gagal mendapatkan Data')

def clear_screen():
    os_system = os.name
    if os_system == 'nt':
        os.system('cls')
    else:  # inserted
        os.system('clear')
url_token = 'https://raw.githubusercontent.com/Hoshiyuki-Api/Swagger-Api/refs/heads/main/database/token.json'
response = requests.get(url_token)
data = json.loads(response.text)
token = data.get('token')

def main():
    banner = f'\n    __               __   ____       _       __\n   / /   ___  ____ _/ /__/ __ \\_____(_)___  / /_\n  / /   / _ \\/ __ `/ //_/ / / / ___/ / __ \\/ __/\n / /___/  __/ /_/ / ,< / /_/ (__  ) / / / / /_\n/_____/\\___/\\__,_/_/|_|\\____/____/_/_/ /_/\\__/\n------------------------------------------------\n{\"name\": \"{user_name}\", \"id\": \"{user_id}\", \n\"expired\": \"{expired_date}\", \"phone\": \"{censored_phone}\"}\n------------------------------------------------\nDisclaimer: script ini mengambil dari data data\n            yang telah bocor, Jika result tidak\n            muncul, berarti input anda tidak masuk\n            atau ikut dalam data bocor (safe)\n------------------------------------------------'
    menu = '   [1] Osint Phone\n   [2] Osint Image\n   [3] Osint Name\n   [4] Track Nik\n   [5] Osint vehicle plate\n'
    try:
        clear_screen()
        print(banner)
        print(menu)
        select_ = int(input('   [•] Select Menu ›⟩ '))
        if select_ == 1:
            clear_screen()
            print(banner + '\n')
            phone = input('   [•] Input Phone (+628xxx) ›⟩ ')
            data = {'token': token, 'request': phone, 'limit': 100, 'lang': 'id'}
            url = 'https://server.leakosint.com/'
            response = requests.post(url, json=data).json()
            formatted_response = json.dumps(response, indent=2, ensure_ascii=False)
            print(formatted_response)
    except KeyboardInterrupt:
        else:  # inserted
            try:
                passport = response['List']['KomInfo Indonesia']['Data'][0]['Passport']
                hash = GetCode(passport, formatted_phone)
                code = input('   [•] Input OTP ›⟩ ')
                GetData(formatted_phone, hash, code)
                resp = requests.get(f'http://simrs.belitung.go.id:3000/api/wsvclaim/pesertaNik?nik={passport}').json()
                formatted_response2 = json.dumps(resp, indent=2, ensure_ascii=False)
                print(formatted_response2)
                url = 'https://tools.revesery.com/nik/'
                headers = {'authority': 'tools.revesery.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'cookie': '_ga=GA1.1.1992994149.1723390762; _ga_G8KSZGHJ0D=GS1.1.1723390761.1.1.1723390872.0.0.0', 'origin': 'https://tools.revesery.com', 'referer': 'https://tools.revesery.com/nik/', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
                data2 = {'nik': passport}
                resp2 = requests.post(url, headers=headers, data=data2)
                par = parser(resp2.text, 'html.parser').find('table', {'class': 'table'})
                nik = {}
                for i in par.find_all('tr'):
                    nm = re.findall('<td>(.*?)</td>', str(i))
                    if len(nm) > 0:
                        nmd = nm[0]
                    datn = re.findall('<td><input disabled=\"\" value=\"(.*?)\"/></td>', str(i))
                    if len(datn) > 0:
                        datnk = datn[0]
                    if nmd!= 'Tanggal Lahir':
                        nik.update({str(nmd): str(datnk)})
                print(json.dumps(nik, indent=4, ensure_ascii=False))
            except (KeyError, IndexError) as e:
                pass  # postinserted
            else:  # inserted
                try:
                    response_data = []
                    ewallets = requests.get('https://api-rekening.lfourr.com/listEwallet').json()['data']
                    for ewallet in ewallets:
                        wallet_check = requests.get(f"https://api-rekening.lfourr.com/getEwalletAccount?bankCode={ewallet['kodeBank']}&accountNumber={phone}")
                        if wallet_check.json()['status']:
                            account_info = wallet_check.json()['data']
                            response_data.append({'Type Wallet': account_info['bankcode'], 'Name': account_info['accountname']})
                    print(json.dumps(response_data, indent=4, ensure_ascii=False))
            except requests.exceptions.ConnectionError:
                pass  # postinserted
        else:  # inserted
            if select_ == 2:
                clear_screen()
                print(banner + '\n')
                image = input('   [•] Input Image/Url ›⟩ ')
                reCaptcha_response = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Ldogl4pAAAAACC465AmPrvJtX1--Eu_o1cOiZhV&co=aHR0cHM6Ly9nZW9zcHkuYWk6NDQz&hl=id&v=aR-zv8WjtWx4lAw-tRCA-zca&size=invisible&cb=dix3q5la9yal')
                url = 'https://us-central1-phaseoneai.cloudfunctions.net/locate_image_DEV'
                headers = {'authority': 'us-central1-phaseoneai.cloudfunctions.net', 'accept': '*/*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'origin': 'https://geospy.ai', 'referer': 'https://geospy.ai/', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
                if image.startswith('http://') or image.startswith('https://'):
                    response = requests.get(image)
                    if response.status_code == 200:
                        files = {'image': ('image.jpg', response.content, 'image/jpeg')}
                    else:  # inserted
                        print('Failed to retrieve the image from the URL.')
                        os._exit(0)
                else:  # inserted
                    if os.path.isfile(image):
                        files = {'image': (image, open(image, 'rb'), 'image/jpeg')}
                    else:  # inserted
                        print('The specified file does not exist.')
                        os._exit(0)
                data = {'recaptcha_token': reCaptcha_response}
                response = requests.post(url, headers=headers, files=files, data=data)
                response_json = response.json()
                formatted_response = json.dumps(response_json, indent=2)
                print(formatted_response)
            else:  # inserted
                if select_ == 3:
                    clear_screen()
                    print(banner + '\n')
                    name = input('   [•] Input Name ›⟩ ')
                    data = {'token': token, 'request': name, 'limit': 100, 'lang': 'id'}
                    url = 'https://server.leakosint.com/'
                    response = requests.post(url, json=data).json()
                    output = json.dumps(response, indent=2, ensure_ascii=False)
                    directory = 'result'
                    os.makedirs(directory, exist_ok=True)
                    current_time = datetime.now().strftime('%d%m%Y-%H%M%S')
                    file_name = f'result-{current_time}.txt'
                    file_path = os.path.join(directory, file_name)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(output)
                            time.sleep(2)
                            print(f'   [•] Hasil Osint Telah Disimpan ke {file_path}')
                else:  # inserted
                    if select_ == 4:
                        clear_screen()
                        print(banner + '\n')
                        nik = input('   [•] Input Nik ›⟩ ')
                        data = {'token': token, 'request': nik, 'limit': 100, 'lang': 'id'}
                        url = 'https://server.leakosint.com/'
                        response = requests.post(url, json=data).json()
                        phone = response.get('List', {}).get('KomInfo Indonesia', {}).get('Data', [])[0].get('Phone', 'Phone not found')
                        resp = requests.get(f'http://simrs.belitung.go.id:3000/api/wsvclaim/pesertaNik?nik={nik}').json()
                        formatted_response2 = json.dumps(resp, indent=2, ensure_ascii=False)
                        print(formatted_response2)
                        url = 'https://tools.revesery.com/nik/'
                        headers = {'authority': 'tools.revesery.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'cookie': '_ga=GA1.1.1992994149.1723390762; _ga_G8KSZGHJ0D=GS1.1.1723390761.1.1.1723390872.0.0.0', 'origin': 'https://tools.revesery.com', 'referer': 'https://tools.revesery.com/nik/', 'sec-ch-ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
                        data2 = {'nik': nik}
                        resp2 = requests.post(url, headers=headers, data=data2)
                        par = parser(resp2.text, 'html.parser').find('table', {'class': 'table'})
                        nik = {}
                        for i in par.find_all('tr'):
                            nm = re.findall('<td>(.*?)</td>', str(i))
                            if len(nm) > 0:
                                nmd = nm[0]
                            datn = re.findall('<td><input disabled=\"\" value=\"(.*?)\"/></td>', str(i))
                            if len(datn) > 0:
                                datnk = datn[0]
                            if nmd!= 'Tanggal Lahir':
                                pass  # postinserted
                            else:  # inserted
                                nik.update({str(nmd): str(datnk)})
                        else:  # inserted
                            print(f'\n   [-] Phone: +{phone}')
                            print(json.dumps(nik, indent=4, ensure_ascii=False))
                    else:  # inserted
                        if select_ == 5:
                            clear_screen()
                            print(banner + '\n')
                            plate = input('   [•] Input Plate (H6145AHE) ›⟩ ')
                            data = {'token': token, 'request': plate, 'limit': 100, 'lang': 'id'}
                            url = 'https://server.leakosint.com/'
                            response = requests.post(url, json=data).json()
                            formatted_response = json.dumps(response, indent=2, ensure_ascii=False)
                            print(formatted_response)
            print('[!] Data paspor tidak ditemukan.')
            pass
            print('[!] Gagal Mengambil Data Ewallet')
            return
            print('   [!] System Stopped!!')
            os._exit(0)
        except ValueError:
            print('   [!] Input dengan benar!!')
            os._exit(0)
if status == 'not_registered':
    print('ID tidak terdaftar, silakan daftar premium terlebih dahulu.')
    demo = input('Apakah Anda ingin menggunakan demo access (y/n): ')
    if demo.lower() == 'y':
        response = requests.get('https://api.ryochinel.my.id/exec/ryochi/app/hidden/demo')
        if response.status_code == 200:
            data = response.json()
            demo_key = data.get('x_ryochi_demo-key')
            key_demo = input('Masukkan Key Demo Acc: ')
            if key_demo == demo_key:
                print('[✓] Akses demo diterima!')
                time.sleep(2)
                main()
            else:  # inserted
                print('Key Demo salah, akses ditolak.')
                os._exit(0)
        else:  # inserted
            print('[!] Saat ini tidak ada Access Demo')
            os._exit(0)
    else:  # inserted
        os._exit(0)
else:  # inserted
    if status == 'expired':
        print(f'ID Anda telah expired pada {expired_date}, upgrade masa aktif terlebih dahulu.')
        os._exit(0)
main()