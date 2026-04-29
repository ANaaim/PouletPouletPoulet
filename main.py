import requests
import pytesseract
from PIL import Image

from io import BytesIO

def main():
    response = requests.get("https://apio.univ-gustave-eiffel.fr/fileadmin/contributeurs/APIO/ARA/Menu.png")
    img = Image.open(BytesIO(response.content))
    x0, y0 = (32, 522)
    w0, h0 = (418, 80)
    s0 = 76
    for i in range(5):
        x, y = (x0+(w0+s0)*i, y0)
        img_dish = img.crop((x, y, x+w0, y+h0))
        dish_name = pytesseract.image_to_string(img_dish, lang='fra')
        if 'poulet' in dish_name.lower():
            print("Poulet cette semaine !!!")
            break
    else:
        print("Pas de poulet cette semaine :'(")

if __name__ == '__main__':
    main()
