from PIL import Image, ImageDraw, ImageChops
import logging

def crop_to_circle(image_path, output_path):
    # 打开图片并转换为RGBA模式
    img = Image.open(image_path).convert("RGBA")
    
    # 创建一个相同尺寸的黑色
    mask = Image.new("L", img.size, 0)

    # 绘制白色圆形蒙版
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0, 0), img.size], fill=255, width=0)
    
    # 把圆形内部，原图中的透明部分正确的附加到蒙版上去
    mask = ImageChops.multiply(mask, img.split()[-1])

    # 将蒙版应用到图片上
    img.putalpha(mask)
    
    # 将图像裁剪成圆形并保存
    img.save(output_path, "PNG")

def make_avatar_circle():
    from fetch_data import IMAGE_DIR
    for avatar_path in IMAGE_DIR.glob("*.png"):
        logging.debug(f"Cropping {avatar_path.as_posix()} to circle format.")
        crop_to_circle(avatar_path.as_posix(), avatar_path.as_posix())

if __name__ == '__main__':
    make_avatar_circle()