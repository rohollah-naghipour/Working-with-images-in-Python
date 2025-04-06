import cv2

image_path = 'input2.jpg' 
image = cv2.imread(image_path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
    
    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
    
    image[y:y+h, x:x+w] = blurred_face

cv2.imshow('Blurred Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('blurred_faces_output.jpg', image)