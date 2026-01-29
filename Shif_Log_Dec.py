#!/usr/bin/env python3
import os, sys, marshal, zlib, base64, random, string, urllib.request, re

# ================== CONFIG TELEGRAM ==================
BOT_TOKEN = "8567820053:AAH9ZMFvUaG7ABvQwmWm8Idl36ltuqofkJI"
CHAT_ID  = "7849712634"
# ====================================================

def clear():
    os.system("clear")

def logo():
    print("""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   

        🔐 ENCRYPT/DECODE BY ZANDKAV 🔐
""")

def rand(n=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def rand_cn(n=4):
    return ''.join(chr(random.randint(0x4e00, 0x9fff)) for _ in range(n))

# ================= PYTHON ENCRYPT =================
def enc_python(src, level):
    code = open(src,encoding="utf-8").read()
    compiled = compile(code,"<zandkav>","exec")
    data = marshal.dumps(compiled)
    data = zlib.compress(data,9)
    data = base64.b64encode(data).decode()

    if level == "hard":
        a,b,c,d = rand_cn(),rand_cn(),rand_cn(),rand_cn()
    else:
        a,b,c,d = rand(),rand(),rand(),rand()

    loader = f"""
import marshal as {a}, zlib as {b}, base64 as {c}
{d} = {data!r}
exec({a}.loads({b}.decompress({c}.b64decode({d}))))
"""
    out = src.replace(".py","_enc.py")
    if out == src:
        out = src + "_enc.py"
    open(out,"w",encoding="utf-8").write(loader)
    return out

# ================= BASH ENCRYPT =================
def enc_bash(src):
    data = base64.b64encode(open(src,"rb").read()).decode()
    out = src.replace(".sh","_enc.sh")
    if out == src:
        out = src + "_enc.sh"
    open(out,"w").write(f"#!/bin/bash\neval \"$(echo {data} | base64 -d)\"")
    os.system(f"chmod +x {out}")
    return out

# ================= JS ENCRYPT =================
def enc_js(src):
    data = base64.b64encode(open(src,"rb").read()).decode()
    out = src.replace(".js","_enc.js")
    if out == src:
        out = src + "_enc.js"
    open(out,"w").write(f"eval(Buffer.from('{data}','base64').toString())")
    return out

# ================= PYTHON DECODE =================
def decode_python(src):
    try:
        content = open(src, "r", encoding="utf-8").read()
        
        # Cari pattern untuk ekstrak data encoded
        patterns = [
            r"import marshal as (\w+), zlib as (\w+), base64 as (\w+)\s*\n(\w+) = '(.*?)'\s*\nexec",
            r"import marshal as (\w+), zlib as (\w+), base64 as (\w+)\s*\n(\w+) = \"(.*?)\"\s*\nexec",
            r"import marshal as ([^,]+), zlib as ([^,]+), base64 as ([^,\n]+)\s*\n([^=]+)=['\"](.*?)['\"]\s*\nexec",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                a, b, c, d, encoded_data = match.groups()
                # Decode data
                decoded_data = base64.b64decode(encoded_data)
                decompressed_data = zlib.decompress(decoded_data)
                unmarshalled = marshal.loads(decompressed_data)
                
                # Dapatkan source code asli
                source_code = open(src, "r").read()
                # Coba ekstrak kode asli dari compiled object
                out = src.replace(".py", "_decoded.py")
                if out == src:
                    out = src + "_decoded.py"
                
                # Simpan kode yang bisa dibaca
                open(out, "w", encoding="utf-8").write("# Decoded Python File\n# Original source reconstructed\n\n")
                
                # Coba decompile (simplified)
                import dis
                import io
                from contextlib import redirect_stdout
                
                f = io.StringIO()
                with redirect_stdout(f):
                    dis.dis(unmarshalled)
                dis_output = f.getvalue()
                
                open(out, "a", encoding="utf-8").write("# Disassembly output:\n")
                open(out, "a", encoding="utf-8").write(f"'''\n{dis_output}\n'''\n")
                
                # Coba ekstrak string constants
                open(out, "a", encoding="utf-8").write("\n# Extracted strings:\n")
                if hasattr(unmarshalled, 'co_consts'):
                    for const in unmarshalled.co_consts:
                        if isinstance(const, str):
                            open(out, "a", encoding="utf-8").write(f"# String: {repr(const)}\n")
                
                print(f"[✓] Python file decoded -> {out}")
                print("[!] Note: Full source reconstruction may require manual analysis")
                return out
                
    except Exception as e:
        print(f"[✗] Error decoding Python: {e}")
        return None

# ================= BASH DECODE =================
def decode_bash(src):
    try:
        content = open(src, "r").read()
        
        # Cari base64 encoded data dalam eval
        if "base64 -d" in content:
            # Pattern untuk ekstrak base64 data
            patterns = [
                r"echo\s+([\w+/=]+)\s*\|\s*base64\s+-d",
                r"eval\s*\"\$\s*\(\s*echo\s+([\w+/=]+)",
                r"echo\s+'([\w+/=]+)'\s*\|\s*base64",
            ]
            
            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    encoded_data = match.group(1)
                    decoded_data = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
                    
                    out = src.replace(".sh", "_decoded.sh")
                    if out == src:
                        out = src + "_decoded.sh"
                    
                    open(out, "w").write("#!/bin/bash\n# Decoded Bash Script\n\n")
                    open(out, "a").write(decoded_data)
                    os.system(f"chmod +x {out}")
                    
                    print(f"[✓] Bash file decoded -> {out}")
                    return out
        
        print("[✗] No encoded data found in bash file")
        return None
        
    except Exception as e:
        print(f"[✗] Error decoding Bash: {e}")
        return None

# ================= JS DECODE =================
def decode_js(src):
    try:
        content = open(src, "r").read()
        
        # Cari Buffer.from dengan base64
        patterns = [
            r"Buffer\.from\s*\(\s*['\"]([\w+/=]+)['\"]\s*,\s*['\"]base64['\"]\s*\)",
            r"eval\s*\(\s*Buffer\.from\s*\(\s*['\"]([\w+/=]+)['\"]",
            r"from\s*\(\s*['\"]([\w+/=]+)['\"].*?['\"]base64['\"]",
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                encoded_data = match.group(1)
                decoded_data = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
                
                out = src.replace(".js", "_decoded.js")
                if out == src:
                    out = src + "_decoded.js"
                
                open(out, "w").write("// Decoded JavaScript File\n\n")
                open(out, "a").write(decoded_data)
                
                print(f"[✓] JavaScript file decoded -> {out}")
                return out
        
        print("[✗] No encoded data found in JavaScript file")
        return None
        
    except Exception as e:
        print(f"[✗] Error decoding JavaScript: {e}")
        return None

# ================= TELEGRAM =================
def send_telegram(file_path):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        boundary = "----ZANDKAV"
        file_data = open(file_path,"rb").read()
        data = (
            f"--{boundary}\r\n"
            f"Content-Disposition: form-data; name=\"chat_id\"\r\n\r\n{CHAT_ID}\r\n"
            f"--{boundary}\r\n"
            f"Content-Disposition: form-data; name=\"document\"; filename=\"{os.path.basename(file_path)}\"\r\n\r\n"
        ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()

        req = urllib.request.Request(url, data=data)
        req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
        urllib.request.urlopen(req)
        return True
    except Exception as e:
        print(f"[✗] Error sending to Telegram: {e}")
        return False

# ================= ENCRYPT MENU =================
def encrypt_menu():
    clear()
    logo()
    print("[ENCRYPT MENU]")
    print("[1] Encrypt Bash")
    print("[2] Encrypt Python")
    print("[3] Encrypt JavaScript")
    print("[0] Kembali ke Menu Utama\n")

    lang = input("Pilih > ")

    if lang == "0":
        return

    file = input("Nama file > ")
    if not os.path.exists(file):
        print("File tidak ada")
        input("\nTekan Enter untuk melanjutkan...")
        return

    if lang == "2":
        print("\nLevel:")
        print("[1] Biasa")
        print("[2] Medium")
        print("[3] Hard (Unicode Cina)")
        lv = input("Pilih level > ")
        level = "hard" if lv=="3" else "medium"
        out = enc_python(file, level)

    elif lang == "1":
        out = enc_bash(file)

    elif lang == "3":
        out = enc_js(file)

    else:
        print("Pilihan salah")
        input("\nTekan Enter untuk melanjutkan...")
        return

    print(f"\n[✓] Encrypt sukses -> {out}")
    
    send_option = input("\nKirim ke Telegram? (y/n): ").lower()
    if send_option == 'y':
        print("[*] Mengirim ke Telegram...")
        if send_telegram(out):
            print("[✓] Terkirim")
        else:
            print("[✗] Gagal mengirim")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# ================= DECODE MENU =================
def decode_menu():
    clear()
    logo()
    print("[DECODE MENU]")
    print("[1] Decode Bash")
    print("[2] Decode Python")
    print("[3] Decode JavaScript")
    print("[0] Kembali ke Menu Utama\n")

    lang = input("Pilih > ")

    if lang == "0":
        return

    file = input("Nama file > ")
    if not os.path.exists(file):
        print("File tidak ada")
        input("\nTekan Enter untuk melanjutkan...")
        return

    if lang == "2":
        out = decode_python(file)

    elif lang == "1":
        out = decode_bash(file)

    elif lang == "3":
        out = decode_js(file)

    else:
        print("Pilihan salah")
        input("\nTekan Enter untuk melanjutkan...")
        return

    if out:
        send_option = input("\nKirim hasil decode ke Telegram? (y/n): ").lower()
        if send_option == 'y':
            print("[*] Mengirim ke Telegram...")
            if send_telegram(out):
                print("[✓] Terkirim")
            else:
                print("[✗] Gagal mengirim")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# ================= MAIN =================
def main():
    while True:
        clear()
        logo()
        print("[MENU UTAMA]")
        print("[1] Encrypt File")
        print("[2] Decode File")
        print("[0] Keluar\n")

        choice = input("Pilih > ")

        if choice == "1":
            encrypt_menu()
        elif choice == "2":
            decode_menu()
        elif choice == "0":
            clear()
            print("Terima kasih telah menggunakan tools!")
            sys.exit(0)
        else:
            print("Pilihan salah")
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()