import cv2

image = cv2.imread('cats.jpeg')

print("please wait ... ")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
faces = detector.detectMultiScale(image_gray)

print("Number of cats: ", len(faces))

