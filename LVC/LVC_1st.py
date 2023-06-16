from PIL import Image
import numpy as np
import cv2


def text_to_binary(text):
    binary_data = text.encode("utf-8")  # 문자열을 이진 데이터로 인코딩
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)  # 이진 데이터를 이진수 문자열로 변환
    return binary_string


def binary_to_text(binary_string):
    binary_data = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))  # 이진수 문자열을 이진 데이터로 변환
    text = binary_data.decode("utf-8")  # 이진 데이터를 문자열로 디코딩
    return text



def embed_watermark_png(target_image_path, save_image_path, watermark_text):
    img = Image.open(target_image_path)
    img_rgba = img.convert("RGBA")
    image_matrix = np.array(img_rgba)

    code = text_to_binary(watermark_text)

    max_h = len(image_matrix)
    max_w = len(image_matrix[0])
    h = 0
    w = 0

    for i in range(len(code)):
        if max_w <= w:
            h += 1
            w = 0
        r, g, b, a = image_matrix[h, w]
        r_bit = int(code[i])
        r = (r & 0xFE) | r_bit
        image_matrix[h, w] = [r, g, b, a]
        w += 1

    modified_image = Image.fromarray(image_matrix, mode="RGBA")
    modified_image.save(save_image_path)


def extract_watermark_png(watermarked_image_path, code_len):
    img = Image.open(watermarked_image_path)
    img_rgb = img.convert("RGBA")

    image_matrix = np.array(img_rgb)
    max_h = len(image_matrix)
    max_w = len(image_matrix[0])

    w = 0
    h = 0
    reCode = ""
    for i in range(code_len):
        if max_w <= w:
            h += 1
            w = 0
        r, g, b, a = image_matrix[h, w]
        r_code = r & 1
        if r_code == 0:
            reCode += "0"
        else:
            reCode += "1"
        w += 1
    
    return binary_to_text(reCode)


code = "kindofindexlike23rt92kdfo234 " * 300
#embed_watermark_png("original.png", "embeded.png", code)
print(extract_watermark_png("embeded.png", len(text_to_binary(code))))
