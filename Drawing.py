import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)
    width = int(cap.get(3)) # 3 is the property id for width
    height = int(cap.get(4)) # 4 is the property id for height

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # drawing a blue line from the top left corner to the bottom right corner of the frame
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10) # drawing a green line from the bottom left corner to the top right corner of the frame
    img = cv2.rectangle(img, (600, 335), (680, 380), (128, 128, 128), 5) # drawing a gray rectangle with a thickness of 5 pixels
    img = cv2.circle(img, (640, 357), 50, (0, 0, 255), 5) # drawing a red circle with a thickness of 5 pixels and a radius of 50 pixels
    # need to use -1 as the thickness to fill the shape

    # Drawing text
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Hello, there!"
    img = cv2.putText(img, text, (500, 50), font, 1, (0, 0, 0), 4, cv2.LINE_AA) # drawing the text with a font size of 1 and a thickness of 2 pixels


    


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()