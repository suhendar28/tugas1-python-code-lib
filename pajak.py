harga = float(input("masukan harga pembelian: "))
pajak = 0.11 * harga
total_pembayaran = harga + pajak
print(f"total yang harus di bayar (pajak 11%): {total_pembayaran:.0f}")