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

def convert_panjang():
    # --- Pindahkan semua PRINT dan INPUT ke sini ---
    print("=== KONVERSI SATUAN PANJANG ===")

    #tampilkan daftar satuan
    print("\nSatuan yang tersedia: ")
    for unit in satuan_panjang:
        print("-", unit)

    #input user (Sekarang ada di dalam fungsi, jadi aman)
    satuan_awal = input("\nDari satuan: ").lower()
    satuan_akhir = input("Ke satuan: ").lower()
    value = float(input("Nilai yang ingin dikonversi: "))

    # --- Logika asli temanmu (tidak diubah) ---
    
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

