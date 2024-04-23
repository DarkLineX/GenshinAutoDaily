from PIL import Image

# UtilsImage.split_image(test_pic,'snap_pic_split.png',1004,64,1112,90)
## 区域截图
def split_image(image_path, out_path, left, upper, right, lower):
    img = Image.open(image_path)
    cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower) 左上，右下
    cropped.save(out_path)
