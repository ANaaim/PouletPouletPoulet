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
    poulet_in_dish = False
    andouillette_in_dish = False
    for i in range(5):
        x, y = (x0+(w0+s0)*i, y0)
        img_dish = img.crop((x, y, x+w0, y+h0))
        dish_name = pytesseract.image_to_string(img_dish, lang='fra')
        if 'pou
        if 'poulet' in dish_name.lower():
            poulet_in_dish = True
        if 'andouillette' in dish_name.lower():
            andouillette_in_dish = True
    
    if poulet_in_dish:
        print("Poulet au menu cette semaine !")
    else:
        print("Pas de poulet cette semaine.")

    if andouillette_in_dish:
        print("Andouillette au menu cette semaine !")
    else:
        print("Pas d’andouillette cette semaine.")


if __name__ == '__main__':
    main()
