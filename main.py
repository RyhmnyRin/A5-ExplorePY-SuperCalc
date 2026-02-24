import arithmetic
import konversiPanjang
import Science_Specialist

print("===============================================")
print("============== KALKULATOR SUPER ===============")
print("===============================================")

print("Pilih operasi yang ingin dilakukan:")
print("1. Aritmatika")
print("2. Scienctific")
print("3. Konversi Satuan Panjang")
print("4. Keluar")
pilih = input("Masukkan pilihan (1/2/3/4): ")

if pilih == "1":
    arithmetic.hitung_aritmatika()
elif pilih == "2":
    Science_Specialist.menu_science()
elif pilih == "3":
    konversiPanjang.convert_panjang()
elif pilih == "4":
    print("Terima kasih telah menggunakan Kalkulator Super!")

