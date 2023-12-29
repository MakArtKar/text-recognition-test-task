from pathlib import Path

import pytesseract

class OCRModel:
    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        return pytesseract.image_to_string(str(image), lang='chi_sim')[:-1]
