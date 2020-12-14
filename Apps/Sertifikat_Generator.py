'''
AUTHOR    : MCHEVRO
PYTHON    : 3.8
Github    : https://github.com/mchevro
'''
from PIL import Image, ImageFont, ImageDraw
import random

print("SERTIFIKAT GENERATOR\n\n")

try:
    while True:
        try:
            input_nama = input('Input File Nama Peserta : ') #Input File Berisi Nama Peserta
            baca_nama = open(input_nama, "r").readlines()    #Baca File Yang Telah Dimasukan
            break
        except:
            print('Nama File Tidak Ada!')
            continue

    list_nama = []
    for x in baca_nama:
        list_nama.append(x.strip())

    for nama in list_nama:
        sertifikat = Image.open('assets/template.jpg') #Template Sertifikat 

        #CETAK NAMA PESERTA
        font_type = ImageFont.truetype('assets/Raleway-Light.ttf',150) #Jenis Font Sertifikat
        draw = ImageDraw.Draw(sertifikat)
        draw.text(xy=(190,850),text=nama,fill=(66, 66, 66), font=font_type) #Koordinate Dan Warna Font

        #CETAK ID
        ID = random.randint(1,100)
        draw2 = ImageDraw.Draw(sertifikat)
        draw2.text(xy=(190,550),text=f'#12132020{ID}',fill=(66, 66, 66), font=font_type) #Koordinate Dan Warna Font

        #SAVE ID
        file = open('validasi_sertifikat.txt','a')
        file.write(f'{nama};12132020{ID}\n')
        file.close
        
        sertifikat.save(f'assets/SERTIFIKAT_PESERTA/{nama}.pdf')  #Tempat File Disimpan
        print(f'Selesai {nama}')

except KeyboardInterrupt:
    print('\n\nAnda Keluar Program!')