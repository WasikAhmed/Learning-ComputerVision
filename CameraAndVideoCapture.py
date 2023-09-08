import numpy as np
import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Display the resulting frame
#     cv2.imshow('frame', frame)

#     # Press q to exit
#     if cv2.waitKey(1) == ord('q'): # ord('q') returns the unicode of 'q'
#         break


# Mirroring the video multiple times
while True:
    ret, frame = cap.read(0)
    width = int(cap.get(3)) # 3 is the property id for width
    height = int(cap.get(4)) # 4 is the property id for height

    image = np.zeros(frame.shape, np.uint8) 
    # np.uint8 is the datatype of the image and it is unsigned integer of 8 bits. frame.shape returns the shape of the frame

    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # resizing the frame to half of its size in both x and y direction
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # rotating the frame by 180 degrees and placing it in the top left corner of the image
    image[height//2:, :width//2] = smaller_frame # placing the frame in the bottom left corner of the image
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # rotating the frame by 180 degrees and placing it in the top right corner of the image
    image[height//2:, width//2:] = smaller_frame # placing the frame in the bottom right corner of the image

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
