print("=== KONVERSI SATUAN PANJANG ===")

#dictionary satuan panjang (berbasis meter)
satuan_panjang = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001,
    "foot": 0.3048,
    "inch": 0.0254,
}

#tampilkan daftar satuan
print("\nSatuan yang tersedia: ")
for unit in satuan_panjang:
    print("-", unit)

#input user
satuan_awal = input("\nDari satuan: ").lower()
satuan_akhir = input("Ke satuan: ").lower()
value = float(input("Nilai yang ingin dikonversi: "))

def convert_panjang(value, satuan_awal, satuan_akhir):
    """
    Mengkonversi satuan yang diinginkan user ke dalam base unit (meter):
    - value dari satuan_awal dikonversi ke meter
    - dari meter dikonversi ke satuan_akhir
    """

    #validasi satuan
    if satuan_awal not in satuan_panjang:
        print("Satuan tidak valid!")
        return
    if satuan_akhir not in satuan_panjang:
        print("Satuan tidak valid!")
        return 
        
    #konversi satuan ke meter terlebih dahulu
    base_value = value * satuan_panjang[satuan_awal]

    #konversi dari meter ke satuan tujuan
    hasil = base_value / satuan_panjang[satuan_akhir]
    print("Hasil: ", hasil)

    #output
    print(f"\n{value} {satuan_awal} = {hasil:.4f} {satuan_akhir}")

convert_panjang(value, satuan_awal, satuan_akhir)


