import math

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda jari_jari: math.pi * (jari_jari ** 2)

# Contoh penggunaan
if __name__ == "__main__":
    # Input jari-jari dari pengguna
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    
    # Menghitung luas lingkaran
    luas = luas_lingkaran(jari_jari)
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
