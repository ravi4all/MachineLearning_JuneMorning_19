import cv2

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread('bahubali.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img, (x,y), (width, height), (color in bgr), border_thickness
cv2.rectangle(img,(40,40), (150,150),(255,0,0),4)

#img, 'text',(x,y), fontface, scale(font size), (color in bgr), thickness
cv2.putText(img,"Bahubali",(20,20),font,1,(255,0,0),2)

while True:
    cv2.imshow('image',img)
    #1 millisecond of delay for window switching
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
