import cv2
import numpy as np

# Drawing Shapes


def ImageProcessing():
    image = np.zeros((512, 512, 3), np.uint8)

    cv2.line(image, (20, 200), (200, 20), (0, 0, 255), 5)
    cv2.rectangle(image, (200, 60), (20, 200), (255, 0, 0), 3)
    cv2.circle(image, (80, 80), 50, (0, 255, 0), 4)

    mytext = "Hello"

    cv2.putText(image, mytext, (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

    cv2.imshow('Black Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

