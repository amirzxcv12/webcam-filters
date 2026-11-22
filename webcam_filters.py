import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise SystemExit("Could not open the webcam.")

# Each key selects a different image effect.
mode = "normal"
help_text = "1: Normal  2: Gray  3: Blur  4: Sketch  Q: Quit"

while True:
    success, frame = camera.read()
    if not success:
        print("Could not read a frame.")
        break

    frame = cv2.flip(frame, 1)

    if mode == "gray":
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == "blur":
        output = cv2.GaussianBlur(frame, (25, 25), 0)
    elif mode == "sketch":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        inverted = 255 - gray
        smooth = cv2.GaussianBlur(inverted, (21, 21), 0)
        output = cv2.divide(gray, 255 - smooth, scale=256)
    else:
        output = frame.copy()

    # Add a small label so the current effect is easy to identify.
    label = f"Mode: {mode.upper()}"
    if len(output.shape) == 2:
        cv2.putText(output, label, (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    else:
        cv2.putText(output, label, (15, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Webcam Filters", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        mode = "normal"
    elif key == ord("2"):
        mode = "gray"
    elif key == ord("3"):
        mode = "blur"
    elif key == ord("4"):
        mode = "sketch"
    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
