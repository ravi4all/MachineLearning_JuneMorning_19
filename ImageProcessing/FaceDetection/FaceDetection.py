import cv2

dataset = cv2.CascadeClassifier('data.xml')

image = cv2.imread('image_1.jpg')
faces = dataset.detectMultiScale(image,1.2)
# print(faces)
for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),2)

cv2.imwrite('result_1.jpg', image)