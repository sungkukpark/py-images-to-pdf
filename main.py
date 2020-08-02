import os
from PIL import Image

rawImagePaths = []
sortedImagePaths = []

for root, dirs, files in os.walk("./source"):
    for filename in files:
        rawImagePaths.append(f"source/{filename}")

sortedImagePaths = sorted(rawImagePaths)
print(sortedImagePaths)

convertedImages = [Image.open(i).convert('RGB') for i in sortedImagePaths]
convertedImages[0].save(r'export/target.pdf', save_all=True, append_images=convertedImages)
