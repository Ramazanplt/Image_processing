import cv2
import numpy as np

def main():

    #Görüntüyü yükleyelim
    img = cv2.imread("C:/Users/Ramazan/Desktop/image_processing/odev3/rice3.jpg")

    #Gri seviyeye dönüştürme
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Eşikleme işlemi
    threshold = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

    #Morfolojik işlemler
    kernel = np.ones((3, 3), np.uint8)
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

    #Sayma ve etiketleme fonksiyonları
    cnts, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > 100:
            count += 1

    #Ekran görüntülerini kaydetme(Binary image dediğimiz görüntü kısmı.)
    cv2.imwrite("esiklenmis.jpg", threshold)
    print(f"Pirinc sayisi: {count}")

if __name__ == "__main__":
    main()
