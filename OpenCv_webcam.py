import cv2 # opencv kütüphanesinin yazılıma dahil ediyoruz.

cap = cv2.VideoCapture(0) # dış kamera tanımlaması 
'''
VideoCapture(0) Bilgisayarınızın onboard bağlı olan web kamerasnın tanımlamasıdır.

Harici bir usb kamera kullanılacak ise bu değer VideoCapture(1) yapılmalıdır. 

'''

# kameranın bağlantı sorgulamasının yapıldığı bölümdür..
if not cap.isOpened():
    raise IOError("Usb Web Kamerası Bağlı Değil !!!")

# while döngüsü ile ekran üzerinde yenilenme oluşturuyoruz. 
# bu fonksiyon olmaz ise yazılım bir kez açılır ve kapanır.
    
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 'q':
        break

cap.release()  
cv2.destroyAllWindows()