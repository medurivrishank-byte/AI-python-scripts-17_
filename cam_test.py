import cv2

for index in (0, 1, 2):
    for name, backend in (("DSHOW", cv2.CAP_DSHOW), ("MSMF", cv2.CAP_MSMF), ("DEFAULT", cv2.CAP_ANY)):
        cap = cv2.VideoCapture(index, backend)
        ok, frame = (cap.read() if cap.isOpened() else (False, None))
        print(f"index={index} backend={name} opened={cap.isOpened()} frame={ok}")
        cap.release()