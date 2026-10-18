import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ok, f = cap.read()
    if not ok: break
    cv2.imshow("test", f)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cap.release(); cv2.destroyAllWindows()