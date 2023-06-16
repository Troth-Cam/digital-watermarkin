# digital-watermarkin
---
 ## LVC Method(Last Value Change Method)
 ### 기본 원리
 RGB값 중 R(Red)값을 이진화 하고, 이진화 마지막 값을 원하는 값(0 or 1)로 변경한다. 이를 png로 저장하여 데이터 손실율을 줄이고, 해당 값을 추후 인식 가능하도록 한다.   
 ### Functions
     
    def text_to_binary(text)

text를 UTF-8을 통해 유니코드화 하고, 이를 이진화하여 String 형태로 반환한다.
    
    def binary_to_text(binary_string)

String으로 된 Binary String을 유니코드를 통해 문자로 바꾼다.

    def embed_watermark_png(target_image_path, save_image_path, watermark_text)

target_image_path(String)에 존재하는 png파일에 watermark_text(String)을 LVC 방식을 이용해 워터마킹하고, 이를 save_image_path(String)에 png로 저장한다.

   def extract_watermark_png(watermarked_image_path, code_len)

watermarked_image_path(String)에 존재하는 png 파일에 있는 code_len(int)만큼의 픽셀을 읽고, 숨겨져있는 워터마크를 Text로 리턴한다.

---