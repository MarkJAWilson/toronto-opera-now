import os
from PIL import Image

def crop_posters():
    img_path = 'C:/Users/mark/.gemini/antigravity/brain/415b7b97-d415-43ae-b834-8baa3ee87328/media__1779740380787.png'
    dest_dir = 'assets/images'
    os.makedirs(dest_dir, exist_ok=True)
    
    img = Image.open(img_path)
    
    crops = {
        'the_medium.png': (250, 30, 499, 480),
        'earnest.png': (499, 30, 748, 480),
        'katya_kabanova.png': (748, 30, 997, 480)
    }
    
    for filename, box in crops.items():
        cropped = img.crop(box)
        dest_path = os.path.join(dest_dir, filename)
        cropped.save(dest_path)
        print(f"Saved cropped image to {dest_path} with size {cropped.size}")

if __name__ == '__main__':
    crop_posters()
