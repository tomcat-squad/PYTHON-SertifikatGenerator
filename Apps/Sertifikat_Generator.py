'''
AUTHOR    : MCHEVRO
PYTHON    : 3.8
Github    : https://github.com/mchevro
'''
from PIL import Image, ImageFont, ImageDraw

print("SERTIFIKAT GENERATOR\n\n")

try:
    while True:
        try:
            input_nama = input("Masukan Nama File Peserta : ") #Input File Berisi Nama Peserta
            baca_nama = open(input_nama, "r").readlines()      #Baca File Yang Telah Dimasukan
            break
        except:
            print('Nama File Tidak Ada!')
            continue

    list_nama = []
    for x in baca_nama:
        list_nama.append(x.strip())

    for nama in list_nama:
        sertifikat = Image.open('/assets/template.jpg') #Template Sertifikat 
        font_type = ImageFont.truetype('/assets/Raytone.ttf',200) #Jenis Font Sertifikat
        draw = ImageDraw.Draw(sertifikat)
        draw.text(xy=(950,1420),text=nama,fill=(30, 30, 31), font=font_type) #Koordinate Dan Warna Font
        sertifikat.save(f'/SERTIFIKAT_PESERTA/{nama}.pdf')  #Tempat File Disimpan

except KeyboardInterrupt:
    print('\n\nAnda Keluar Program!')