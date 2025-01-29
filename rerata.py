angka_list = []
for i in range(10):
    angka = float(input(f"masukan angka ke-{i+1}:"))
    angka_list.append(angka)
rata_rata = sum(angka_list) / len(angka_list)
print("rata rata dari angka yang dimasukan tersebut:",rata_rata)