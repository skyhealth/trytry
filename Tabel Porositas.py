import csv
import pandas as pd

def make():
    with open ('Porositas.csv','w+') as file:
        myFile = csv.writer(file)
        myFile.writerow(["No","Sample ID", "Diameter", "Height", "Weight","P1", "P2", "P1/P2", "Sample Bulk Volume", "Grain Volume", "Pore Volume", "Porosity", "Grain Density", "Keterangan" ])
        i=1
        n = int(input("Masukkan jumlah data sampel yang dimiliki: "))
        while i <= n:
            no = i
            sampleID =input("Masukkan Sample ID: ")
            diameter = float(input(f"Masukkan diameter dari Sampel {sampleID} (cm): "))
            height = float(input(f"Masukkan tinggi dari Sampel {sampleID} (cm): "))
            weight = float(input(f"Masukkan berat dari Sampel {sampleID} (g): "))
            p1 = float(input(f"Masukkan P1 saat melakukan percobaan dengan Sampel {sampleID} (psig): "))
            p2 = float(input(f"Masukkan P2 saat melakukan percobaan dengan Sampel {sampleID} (psig): "))
            volume = float(input(f"Masukkan volume dari Sampel {sampleID} (cc): "))
            p1_2=p1/p2
            g_volume = (-0.0158*(p1_2**3))+(0.2597*(p1_2**2))+(-7.5585*(p1_2**1))+(57.104)
            p_volume = volume-g_volume
            porosity = (p_volume/volume) * 100
            density = weight/g_volume
            if 0 < porosity < 5:
                ket = 'Sangat buruk'
            elif 5 <= porosity < 10:
                ket = 'Buruk'
            elif 10 <= porosity < 15:
                ket = 'Cukup'
            elif 15 <= porosity < 20:
                ket = 'Baik'
            elif 20 <= porosity <= 25:
                ket = 'Sangat baik'
            elif porosity > 25:
                ket = 'Batu belum kokoh'
            elif porosity == 0 :
                ket = 'Batu tidak memiliki pori'
            elif 100 < porosity < 0:
                ket = 'Input salah'
            myFile.writerow([no,sampleID, diameter, height, weight, p1, p2, round(p1_2,2), volume, round(g_volume,2), round(p_volume,2), round(porosity,2), round(density,2), ket])
            i+=1
    por = pd.read_csv('Porositas.csv', index_col='No')
    return por[:n]

def modify():
    por = pd.read_csv('Porositas.csv', index_col='No')
    n=input('Masukkan jumlah data yang dimiliki: ')
    indeks = int(input(f'Masukkan No baris yang ingin diganti: (1-{n}) '))
    nama_kolom = input('Masukkan nama kolom yang ingin diganti: ')
    newID = por.loc[indeks,'Sample ID']
    di_new = por.loc[indeks,'Diameter']
    he_new =por.loc[indeks,'Height']
    w_new =por.loc[indeks,'Weight']
    p1_new=por.loc[indeks,'P1']
    p2_new=por.loc[indeks,'P2']
    p1_2_new=por.loc[indeks,'P1/P2']
    v_new=por.loc[indeks,'Sample Bulk Volume']
    gv_new=por.loc[indeks,'Grain Volume']
    pv_new=por.loc[indeks,'Pore Volume']
    p_new=por.loc[indeks,'Porosity']
    d_new=por.loc[indeks,'Grain Density']
    k_new=por.loc[indeks,'Keterangan']
    if nama_kolom == 'Sample ID':
        nilai_baru = input('Masukkan ID yang baru: ')
        newID = nilai_baru
    elif nama_kolom == 'Diameter':
        nilai_baru=float(input('Masukkan nilai baru: '))
        di_new=nilai_baru
    elif nama_kolom == 'Height':
        nilai_baru=float(input('Masukkan nilai baru: '))
        he_new=nilai_baru
    elif nama_kolom == 'Weight':
        nilai_baru=float(input('Masukkan nilai baru: '))
        d_new = nilai_baru/gv_new
        w_new=nilai_baru
    elif nama_kolom == 'P1':
        nilai_baru=float(input('Masukkan nilai baru: '))
        p1_2_new = nilai_baru/p2_new
        p1_new=nilai_baru
        gv_new=(-0.0158*(p1_2_new**3))+(0.2597*(p1_2_new**2))+(-7.5585*(p1_2_new**1))+(57.104)
        pv_new= v_new - gv_new
        p_new= (pv_new/v_new) * 100
        d_new=(w_new/gv_new)
        if 0 < p_new < 5:
            k_new = 'Porositas Sangat Buruk'
        elif 5 <= p_new < 10:
            k_new = 'Porositas Buruk'
        elif 10 <= p_new < 15:
            k_new = 'Porositas Cukup'
        elif 15 <= p_new < 20:
            k_new = 'Porositas Baik'
        elif 20 <= p_new <= 25:
            k_new = 'Porositas Sangat Baik'
        elif p_new > 25:
            k_new = 'Batu belum kokoh'
        elif p_new == 0 :
            k_new = 'Batu tidak memiliki pori'
        elif 100 < p_new < 0:
            k_new = 'Input salah'
    elif nama_kolom == 'P2':
        nilai_baru=float(input('Masukkan nilai baru: '))
        p1_2_new = p1_new/nilai_baru
        p2_new=nilai_baru
        gv_new=(-0.0158*(p1_2_new**3))+(0.2597*(p1_2_new**2))+(-7.5585*(p1_2_new**1))+(57.104)
        pv_new= v_new - gv_new
        p_new= (pv_new/v_new) * 100
        d_new=(w_new/gv_new)
        if 0 < p_new < 5:
            k_new = 'Sangat buruk'
        elif 5 <= p_new < 10:
            k_new = 'Buruk'
        elif 10 <= p_new < 15:
            k_new = 'Cukup'
        elif 15 <= p_new < 20:
            k_new = 'Baik'
        elif 20 <= p_new <= 25:
            k_new = 'Sangat baik'
        elif p_new > 25:
            k_new = 'Batu belum kokoh'
        elif p_new == 0 :
            k_new = 'Batu tidak memiliki pori'
        elif 100 < p_new < 0:
            k_new = 'Input salah'
    elif nama_kolom == 'Sample Bulk Volume':
        nilai_baru=float(input('Masukkan nilai baru: '))
        v_new=nilai_baru
        pv_new= v_new - gv_new
        p_new= (pv_new/v_new) * 100
        d_new=(w_new/gv_new)
        if 0 < p_new < 5:
            k_new = 'Sangat buruk'
        elif 5 <= p_new < 10:
            k_new = 'Buruk'
        elif 10 <= p_new < 15:
            k_new = 'Cukup'
        elif 15 <= p_new < 20:
            k_new = 'Baik'
        elif 20 <= p_new <= 25:
            k_new = 'Sangat baik'
        elif p_new > 25:
            k_new = 'Batu belum kokoh'
        elif p_new == 0 :
            k_new = 'Batu tidak memiliki pori'
        elif 100 < p_new < 0:
            k_new = 'Input salah'
    elif nama_kolom == 'P1/P2' or nama_kolom == 'No' or nama_kolom == 'Grain Volume' or nama_kolom == 'Pore Volume' or nama_kolom == 'Porosity' or nama_kolom == 'Keterangan' or nama_kolom == 'Grain Density':
        return(Kolom ini tidak bisa diganti)
    por.loc[indeks,'Diameter']= di_new
    por.loc[indeks,'Sample ID']= newID
    por.loc[indeks,'Height']= he_new
    por.loc[indeks,'Weight']= round(w_new,2)
    por.loc[indeks,'P1']=round(p1_new,2)
    por.loc[indeks,'P2']=p2_new
    por.loc[indeks,'P1/P2']=round(p1_2_new,2)
    por.loc[indeks,'Sample Bulk Volume']=v_new
    por.loc[indeks,'Grain Volume']=round(gv_new,2)
    por.loc[indeks,'Pore Volume']=round(pv_new,2)
    por.loc[indeks,'Porosity']=round(p_new,2)
    por.loc[indeks,'Grain Density']=round(d_new,2)
    por.loc[indeks,'Keterangan']=k_new
    poe.head
