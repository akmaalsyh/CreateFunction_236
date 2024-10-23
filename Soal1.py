# Fungsi untuk mengonversi suhu antara Celsius dan Fahrenheit
def konversi_suhu(nilai, satuan):
    if satuan == 'C':
        # Mengonversi Celsius ke Fahrenheit
        return (nilai * 9/5) + 32
    elif satuan == 'F':
        # Mengonversi Fahrenheit ke Celsius
        return (nilai - 32) * 5/9
    else:
        return "Satuan tidak valid! Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Contoh penggunaan
if __name__ == "__main__":
    # Input suhu dari pengguna
    suhu = float(input("Masukkan nilai suhu: "))
    satuan = input("Masukkan satuan suhu ('C' untuk Celsius atau 'F' untuk Fahrenheit): ").strip().upper()
    
    # Konversi suhu
    suhu_terkonversi = konversi_suhu(suhu, satuan)
    if isinstance(suhu_terkonversi, str):
        print(suhu_terkonversi)  # Jika ada pesan kesalahan
    else:
        if satuan == 'C':
            print(f"{suhu}°C adalah {suhu_terkonversi:.2f}°F")
        else:
            print(f"{suhu}°F adalah {suhu_terkonversi:.2f}°C")
