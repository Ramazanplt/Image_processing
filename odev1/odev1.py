#HİSTOGRAM HESAPLAMA

#NumPy ve OpenCV Kütüphaneleri İçe Aktarılıyor
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Görüntüyü yükleyelim
image = cv2.imread('flowers2.jpg', cv2.IMREAD_GRAYSCALE)

#Görüntü boyutlarını alalım
height, width = image.shape

#Histogramı sıfırla(Histogram İçin Boş Bir Dizi Oluşturuluyor)
hist = np.zeros(256)

#Histogramı hesapla
#İç içe iki döngü ile görüntünün her pikselinde bulunan gri tonlama değeri alınıyor ve bu değere sahip olan histogram dizisinin ilgili indisindeki değer bir artırılıyor.
for u in range(0, height):
    for v in range(0, width):
        i = image[u, v]
        hist[i] = hist[i] + 1

#Histogramı çizdir
plt.plot(hist)
plt.title('Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()