import cv2
import face_recognition

input_movie = cv2.VideoCapture("C:\\temp\\5.mp4")

length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter("C:\\temp\\output2.avi", fourcc, 23.98, (360, 640))

faces = []

face_locations = []
face_encodings = []
frame_number = 0
while True:
    ret, frame = input_movie.read()

    frame_number += 1

    if not ret:
        break

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(faces, face_encoding, tolerance=0.60)
        Flag = True
        for i in range(len(match)):
            if match[i]:
                Flag = False
        if Flag:
            faces.append(face_encoding)
            cv2.imwrite("C:/temp/"+str(len(faces))+".jpg", frame)
            
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

    cv2.imshow('gay party', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


input_movie.release()
output_movie.release()
cv2.destroyAllWindows()
