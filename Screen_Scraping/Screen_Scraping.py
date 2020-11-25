from PIL import ImageGrab
import cv2
import numpy as np


class Process:
    def __init__(self):
        self.currentHealth = 100
        self.ocrErr = False

    def processImg(self, greyImg):
        # self.currentHealth
        txt = pytesseract.image_to_string(greyImg)
        print(txt)
        if txt == '' or txt == '|1oo':
            return True
        try:
            health = int(txt)
            self.ocrErr = False
        except:
            health = self.currentHealth
            if not self.ocrErr:
                health = self.currentHealth - 1
                self.ocrErr = True

        if health < self.currentHealth:
            self.currentHealth = health
            return True
        return False


def main():
    process = Process()
    while True:
        x = 50
        y = 13

        offX = 40
        offY = 20
        img = ImageGrab.grab(bbox=(x, y, x + offX, y + offY)).convert('L')

        img = np.array(img)
        cv2.imshow('window', img)

        process.processImg(img)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()

