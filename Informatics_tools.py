def konversi_basis():
    print("\n=== KONVERSI BASIS BILANGAN ===")
    try:
        angka = int(input("Masukkan angka desimal: "))
        print(f"Biner: {bin(angka)}")
        print(f"Oktal: {oct(angka)}")
        print(f"Heksadesimal: {hex(angka).upper()}")
    except ValueError:
        print("Error ⚠️ Masukkan angka bulat!")

def hitung_statistika():
    print("\n=== STATISTIKA DASAR (MEAN) ===")
    try:
        data_input = input("Masukkan angka (pisahkan dengan koma, misal: 1,2,3): ")
        angka_list = [float(x.strip()) for x in data_input.split(",")]
        
        if not angka_list:
            return "Data kosong!"
            
        mean = sum(angka_list) / len(angka_list)
        print(f"Jumlah data: {len(angka_list)}")
        print(f"Rata-rata (Mean): {mean:.2f}")
    except ValueError:
        print("Error ⚠️ Pastikan format input benar (angka dipisah koma)!")

def menu_informatika():
    while True:
        print("\n=== MENU INFORMATIKA ===")
        print("1. Konversi Desimal ke Biner/Oktal/Hex")
        print("2. Hitung Rata-rata (Statistika)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            konversi_basis()
        elif pilihan == "2":
            hitung_statistika()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")