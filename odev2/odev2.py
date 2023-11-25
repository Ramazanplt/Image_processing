import cv2
import numpy as np

#Kamera bağlantısını başlatalım. (0, bilgisayara bağlı olan kamerayı ifade ediyor)
cap = cv2.VideoCapture(0)

while True:
    #Kameradan bir çerçeve okuyalım.
    #cap.read() fonksiyonu, bir çerçeve okur ve frame değişkenine atar. ret değeri, çerçeve başarıyla okunduysa True, aksi takdirde False olacaktır.
    ret, frame = cap.read()

    #Giriş görüntüsünü HSV formatına dönüştürelim.(Çerçeve, RGB formatından HSV formatına dönüştürülür.)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Kırmızı renk aralığını belirle. (HSV formatında)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    #Belirtilen renk aralığındaki pikselleri beyaz yap, diğerlerini siyah yap.
    mask = cv2.inRange(hsv, lower_red, upper_red)

    #Giriş görüntüsü ile maskeyi birleştir.
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #Görüntüyü ekrana göster.
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    #Çıkış için 'q' tuşuna basılmasını kontrol et.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Kamera bağlantısını kapat.
cap.release()
cv2.destroyAllWindows()