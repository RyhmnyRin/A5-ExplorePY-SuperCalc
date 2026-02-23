print("=================================")
print("======= KALKULATOR SUPER ========")
print("=================================")

print("Pilih operasi yang ingin dilakukan:")
print("1. Aritmatika")
print("2. Termodinamika")
print("3. Pengukuran")
print("4. Keluar")
operasi = input("Masukkan nomor operasi (1-4): ")

if operasi == "1":
    aritmatika.hitung()
    
elif operasi == "2":
    termodinamika.hitung()
    
elif operasi == "3":
    pengukuran.hitung()
    
elif operasi == "4":
    print("Terima kasih telah menggunakan Kalkulator Super!")