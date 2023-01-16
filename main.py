import cv2
import time
from send_mail import mail_send
video = cv2.VideoCapture(0)

time.sleep(1)
first_frame = None
status_list = []
detected_image = None
while True:
    status = 0
    check1, frame1 = video.read()

    gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    gray_frame_gau =cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]

    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow("Video one", dilate_frame)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 4000:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame1, (x, y), (x+width, y+height), (0, 0, 255), 3)
        if rectangle.any():
            status = 1


    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        mail_send()
        print("Email!")
        detected_image = frame1
    cv2.imshow("Video_true", frame1)



    key= cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()

