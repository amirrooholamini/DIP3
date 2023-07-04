import cv2

sticker = cv2.imread('face_sticker.png')
glass = cv2.imread("glass.png")
sticker_gray = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
glass_gray = cv2.cvtColor(glass, cv2.COLOR_BGR2GRAY)

R, C = sticker_gray.shape
cap = cv2.VideoCapture(0)

selection = 0

while True:
    _, frame = cap.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if selection == 1:
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        faces = detector.detectMultiScale(image_gray)
        for face in faces:
            x,y,w,h = face
            sticker_resized = cv2.resize(sticker_gray, (w, int(w/C*R)))

        center_c = (x + x + w)//2
        center_r = (y + y + h)//2

        sr_r, sr_c = sticker_resized.shape
        if sr_r %2 == 0:
            start_r = center_r - sr_r//2
        else:
            start_r = center_r - sr_r//2 - 1

        if sr_c %2 == 0:
            start_c = center_c - sr_c//2
        else:
            start_c = center_c - sr_c//2 - 1

        end_r = center_r + sr_r//2
        end_c = center_c + sr_c//2

    # image_gray[start_r:end_r, start_c:end_c] = sticker_resized
        for i in range(start_r, end_r):
            for j in range(start_c, end_c):
                x = i - start_r
                y = j - start_c
                if sticker_resized[x,y] >0:
                    image_gray[i,j] = sticker_resized[x,y]
                    
    elif selection ==2:
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
        parts = detector.detectMultiScale(image_gray)
        if len(parts) == 2:
            x1,y1,w1,h1 = parts[0]
            x2,y2,w2,h2 = parts[1]
            
            center_c1 = (x1 + x1 + w1)//2
            center_c2 = (x2 + x2 + w2)//2
            
            center_r1 = (y1 + y1 + h1)//2
            center_r2 = (y2 + y2 + h2)//2
            
            center_c = (center_c1 + center_c2)//2
            center_r = (center_r1 + center_r2)//2
            w = (w1 + w2 + abs(x2 - x1))
            h = (h1 + h2)//2
            
            R,C = glass_gray.shape
            glass_resized = cv2.resize(glass_gray, (w, int(w/C*R)))
            
            sr_r, sr_c = glass_resized.shape
            if sr_r %2 == 0:
                start_r = center_r - sr_r//2
            else:
                start_r = center_r - sr_r//2 - 1

            if sr_c %2 == 0:
                start_c = center_c - sr_c//2
            else:
                start_c = center_c - sr_c//2 - 1

            end_r = center_r + sr_r//2
            end_c = center_c + sr_c//2
            for i in range(start_r, end_r):
                for j in range(start_c, end_c):
                    x = i - start_r
                    y = j - start_c
                    if glass_resized[x,y] >0:
                        if i < image_gray.shape[0] and j < image_gray.shape[1]:
                            image_gray[i,j] = glass_resized[x,y]

    if selection == 3:
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        faces = detector.detectMultiScale(image_gray)
        for face in faces:
            x,y,w,h = face
            face_img = image_gray[y:y+h, x:x+w]
            R,C = face_img.shape
            
            resized = cv2.resize(face_img, (C//20, R//20), interpolation = cv2.INTER_NEAREST)
            resized = cv2.resize(resized, (C, R))
            image_gray[y:y+h, x:x+w] = resized
            
    elif selection == 4:
        R,C = image_gray.shape
        for c in range(C//2):
            image_gray[:,c] = image_gray[:, C-c-1]     
            

    cv2.imshow("1", image_gray)
    key = cv2.waitKey(10)
    
    if key == ord('q'):
        break

    if key == ord('1'):
        selection = 1
    elif key == ord('2'):
        selection = 2
    elif key == ord('3'):
        selection = 3
    elif key == ord('4'):
        selection = 4
    