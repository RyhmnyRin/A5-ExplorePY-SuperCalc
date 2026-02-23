def hitung_aritmatika():
    print("=== Kalkulator Aritmatika ===")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Modulus (%)")
    print("6. Pangkat (**)")
    
    pilihan = input("Pilih operasi (1-6): ")
    
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
    except ValueError:
        return "Error ⚠️ Input harus angka!"
    
    if pilihan == "1":
        return f"Hasil: {a} + {b} = {a+b}"
    elif pilihan == "2":
        return f"Hasil: {a} - {b} = {a-b}"
    elif pilihan == "3":
        return f"Hasil: {a} * {b} = {a*b}"
    elif pilihan == "4":
        if b == 0:
            return "Error ⚠️ Tidak bisa membagi dengan 0!"
        return f"Hasil: {a} / {b} = {a/b}"
    elif pilihan == "5":
        if b == 0:
            return "Error ⚠️ Tidak bisa modulus dengan 0!"
        return f"Hasil: {a} % {b} = {a%b}"
    elif pilihan == "6":
        return f"Hasil: {a} ** {b} = {a**b}"
    else:
        return "Error ⚠️ Pilihan tidak valid!"