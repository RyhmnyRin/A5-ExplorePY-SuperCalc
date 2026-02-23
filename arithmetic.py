#YANG BARUUU
def hitung_aritmatika():
    while True:
        print("\n=== Kalkulator Aritmatika ===")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Modulus (%)")
        print("6. Pangkat (**)")
        print("7. Kembali ke Menu Utama")

        pilihan = input("Pilih operasi (1-7): ").strip()

        if pilihan == "7":
            break

        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Error ⚠️ Input harus angka!")
            continue

        if pilihan == "1":
            print(f"Hasil: {a} + {b} = {a+b}")
        elif pilihan == "2":
            print(f"Hasil: {a} - {b} = {a-b}")
        elif pilihan == "3":
            print(f"Hasil: {a} * {b} = {a*b}")
        elif pilihan == "4":
            if b == 0:
                print("Error ⚠️ Tidak bisa membagi dengan 0!")
            else:
                print(f"Hasil: {a} / {b} = {a/b}")
        elif pilihan == "5":
            if b == 0:
                print("Error ⚠️ Tidak bisa modulus dengan 0!")
            else:
                print(f"Hasil: {a} % {b} = {a%b}")
        elif pilihan == "6":
            print(f"Hasil: {a} ** {b} = {a**b}")
        else:
            print("Pilihan tidak valid!")
            continue

        ulang = input("\nMau hitung lagi? (y/n): ").lower()
        if ulang != "y":
            break