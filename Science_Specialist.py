
def celsius_to_fahrenheit(c):
    hasil = (9/5 * c) + 32
    return f"{hasil :.2f} °F"

def celsius_to_kelvin(c):
    hasil = c + 273.15
    return f"{hasil :.2f} °k"

def celsius_to_reamur(c):
    hasil = 4/5 * c
    return f"{hasil :.2f} °R"

#menghitung masa jenis dari massa dan volume
def hitung_massa_jenis(massa, volume):
    if volume == 0:
        return "Volume tidak boleh nol!"
    
    hasil = massa / volume
    return f"{hasil:.2f} kg/m³"

def hitung_kecepatan(jarak, waktu):
    if waktu == 0:
        return "Waktu tidak boleh nol!"
    
    hasil = jarak / waktu
    return f"{hasil:.2f} m/s"

def menu_science():
    while True:
        print("\n=== MENU SCIENCE ===")
        print("1. Konversi Celsius ke Fahrenheit")
        print("2. Konversi Celsius ke Kelvin")
        print("3. Konversi Celsius ke Reamur")
        print("4. Hitung Massa Jenis")
        print("5. Hitung Kecepatan")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            c = float(input("Masukkan suhu Celsius: "))
            print("Hasil:", celsius_to_fahrenheit(c))
            
        elif pilihan == "2":
            c = float(input("Masukkan suhu Celsius: "))
            print("Hasil:", celsius_to_kelvin(c))
            
        elif pilihan == "3":
            c = float(input("Masukkan suhu Celsius: "))
            print("Hasil:", celsius_to_reamur(c))
            
        elif pilihan == "4":
            massa = float(input("Masukkan massa (kg): "))
            volume = float(input("Masukkan volume (m³): "))
            print("Hasil:", hitung_massa_jenis(massa, volume))
            
        elif pilihan == "5":
            jarak = float(input("Masukkan jarak (m): "))
            waktu = float(input("Masukkan waktu (s): "))
            print("Hasil:", hitung_kecepatan(jarak, waktu))
            
        elif pilihan == "0":
            break
        
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_science()
