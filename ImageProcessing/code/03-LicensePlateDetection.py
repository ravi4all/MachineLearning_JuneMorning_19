import cv2

dataset = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# img = cv2.imread('car_1.jpg', cv2.COLOR_BGR2GRAY)
img = cv2.imread('car_3.jpg', cv2.COLOR_BGR2GRAY)
plates = dataset.detectMultiScale(img)
# print(plates)
for x,y,w,h in plates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 4)

cv2.imwrite('car_result_3.jpg', img)