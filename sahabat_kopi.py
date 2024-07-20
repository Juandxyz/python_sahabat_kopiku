import os
import platform
import webbrowser
import urllib.parse

def bersihkan_tampilan():
    sistem = platform.system()
    if sistem == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def tampilkan_logo(logo):
    print("=" * 20)
    print(logo)
    print("=" * 20)

def tampilkan_menu(menu):
    print("Menu Minuman:")
    lebar_jarak = max(len(minuman) for minuman, _ in menu)
    format_string = f"{{:<{lebar_jarak}}}   Rp{{:>6}}"
    for i, (minuman, harga) in enumerate(menu, start=1):
        print(f"{i}. {format_string.format(minuman, harga)}")

def pilih_minuman(menu):
    while True:
        try:
            pilihan = int(input(f"Silahkan pilih nomor (1-{len(menu)}): "))
            if 1 <= pilihan <= len(menu):
                return menu[pilihan - 1]
            else:
                print(f"Nomor harus antara 1 dan {len(menu)}. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

def pilih_jumlah():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah cups: "))
            if jumlah > 0:
                return jumlah
            else:
                print("Jumlah cups harus lebih dari 0. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")

def tampilkan_hasil_pesanan(minuman, jumlah, harga, total):
    tampilkan_logo(logo)
    print(f"Menu minuman: {minuman}")
    print(f"Jumlah Cups: {jumlah}")
    print(f"Harga per cup: Rp {harga}")
    print(f"Total belanja: Rp {total}")
    print("=" * 20)

def minta_kode_dan_nomor():
    kode_negara = input("Masukkan kode negara (misalnya +62 untuk Indonesia): ")
    nomor_hp = input("Masukkan nomor HP tujuan (tanpa kode negara): ")
    return kode_negara, nomor_hp

def kirim_pesan(nomor_hp, kode_negara, pesan):
    # Encode pesan untuk URL
    pesan_encoded = urllib.parse.quote(pesan)
    nomor_penuh = f"{kode_negara}{nomor_hp}"
    url = f"https://wa.me/{nomor_penuh}?text={pesan_encoded}"
    webbrowser.open(url)  # Buka URL di browser default

# Logo
logo = "𝐒𝐀𝐇𝐀𝐁𝐀𝐓 𝐊𝐎𝐏𝐈𝐊𝐔"

# Daftar minuman
menu_minuman = [
    ("Kopi Espresso", 15000),
    ("Kopi Americano", 16000),
    ("Kopi Cappuccino", 18000),
    ("Kopi Latte", 15000),
    ("Kopi Mocha", 15000),
    ("Kopi Macchiato", 25000),
    ("Kopi Flat White", 25000),
    ("Kopi Affogato", 50000)
]

# Menampilkan menu
tampilkan_menu(menu_minuman)

# Minta user untuk memilih
minuman_dipilih, harga_minuman = pilih_minuman(menu_minuman)
jumlah_cups = pilih_jumlah()

# Bersihkan tampilan
bersihkan_tampilan()

# Menghitung total belanja
total_belanja = harga_minuman * jumlah_cups

# Menampilkan hasil pesanan user
tampilkan_hasil_pesanan(minuman_dipilih, jumlah_cups, harga_minuman, total_belanja)

# Tanya apakah ingin mengirim hasil pesanan
while True:
    pilihan = input("Apakah Anda ingin mengirim hasil pesanan ke teman? (iya/tidak): ").strip().lower()
    if pilihan == 'tidak':
        print("Terima kasih telah berbelanja. Sampai jumpa lagi!")
        break
    elif pilihan == 'iya':
        kode_negara, nomor_hp = minta_kode_dan_nomor()
        pesan = (f"Hallo! Saya ingin memesan:\n\n"
                "====================\n"
                f"{logo}\n"
                "====================\n"
                f"Menu minuman: {minuman_dipilih}\n"
                f"Jumlah Cups: {jumlah_cups}\n"
                f"Harga per cup: Rp {harga_minuman}\n"
                "===================="
                f"Total belanja: Rp {total_belanja}")
        kirim_pesan(nomor_hp, kode_negara, pesan)
        break
    else:
        print("Pilihan tidak valid. Silakan ketik 'iya' atau 'tidak'.")
