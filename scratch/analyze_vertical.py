from PIL import Image

def find_vertical_limits():
    img_path = 'C:/Users/mark/.gemini/antigravity/brain/415b7b97-d415-43ae-b834-8baa3ee87328/media__1779739655833.png'
    img = Image.open(img_path)
    width, height = img.size
    
    # We will trace vertical color changes down the center of Card 2 (x = 625)
    # Card 2 has a bright background in the middle but let's see where the purple starts/ends.
    # Purple background is around R=55, G=41, B=94 (at the top, or maybe it changes slightly).
    # Let's print out pixel values for every 5 rows at x = 625.
    x_test = 625
    print("Vertical profile at x=625:")
    for y in range(0, height, 5):
        p = img.getpixel((x_test, y))
        print(f"y={y:03d}: {p}")

if __name__ == '__main__':
    find_vertical_limits()
