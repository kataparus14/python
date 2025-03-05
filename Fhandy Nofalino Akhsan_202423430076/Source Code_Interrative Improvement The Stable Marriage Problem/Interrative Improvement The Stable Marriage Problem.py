print('Nama  : Fhandy  Nofalino Akhsan')
print('NIM : 23343065 \n')

print('Interrative Improvement The Stable Marriage Problem\n')


def pernikahan_stabil(preferensi_pria, preferensi_wanita):
    """
    Menyelesaikan masalah Pernikahan Stabil menggunakan algoritma Gale-Shapley.
    
    Argumen:
        preferensi_pria (dict): Preferensi pria, format {pria: [wanita1, wanita2, ...]}
        preferensi_wanita (dict): Preferensi wanita, format {wanita: [pria1, pria2, ...]}
    
    Mengembalikan:
        dict: Pasangan stabil, format {wanita: pria}
    """
    # Inisialisasi semua pria sebagai bebas dan dictionary untuk menyimpan pertunangan
    pria_bebas = list(preferensi_pria.keys())
    pertunangan = {}  # Dictionary untuk menyimpan pasangan yang sudah bertunangan

    # Selama masih ada pria yang bebas
    while pria_bebas:
        pria = pria_bebas.pop(0)  # Ambil pria pertama dari daftar pria bebas
        daftar_preferensi = preferensi_pria[pria]  # Daftar preferensi wanita untuk pria tersebut

        # Iterasi melalui daftar preferensi wanita pria tersebut
        for wanita in daftar_preferensi:
            if wanita not in pertunangan:
                # Jika wanita masih bebas, bertunangan dengan pria tersebut
                pertunangan[wanita] = pria
                break
            else:
                # Jika wanita sudah bertunangan, bandingkan preferensinya
                pria_saat_ini = pertunangan[wanita]
                daftar_preferensi_wanita = preferensi_wanita[wanita]
                if daftar_preferensi_wanita.index(pria) < daftar_preferensi_wanita.index(pria_saat_ini):
                    # Jika wanita lebih memilih pria baru, putuskan pertunangan sebelumnya
                    pertunangan[wanita] = pria
                    pria_bebas.append(pria_saat_ini)  # Pria yang ditolak kembali menjadi bebas
                    break
        else:
            # Jika tidak ada wanita yang menerima lamaran, pria tetap menjadi bebas
            pria_bebas.append(pria)

    return pertunangan

# Contoh penggunaan
preferensi_pria = {
    'p1': ['w1', 'w2', 'w3'],
    'p2': ['w2', 'w3', 'w1'],
    'p3': ['w3', 'w1', 'w2']
}

preferensi_wanita = {
    'w1': ['p2', 'p1', 'p3'],
    'w2': ['p3', 'p2', 'p1'],
    'w3': ['p1', 'p3', 'p2']
}

# Menjalankan algoritma
pasangan_stabil = pernikahan_stabil(preferensi_pria, preferensi_wanita)
print("Pasangan Stabil:", pasangan_stabil)
