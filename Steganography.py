from stegano import lsb
from PIL import Image

# 1. مخفی کردن اسکریپت در عکس
script = """
print("Hello from hidden script!")
for i in range(5):
    print(f"Count: {i}")
"""

image_path = "input1.jpg"  # مسیر عکس اصلی
secret = lsb.hide(image_path, script)
secret.save("image_with_script.png")

# 2. بازیابی اسکریپت از عکس
revealed_script = lsb.reveal("image_with_script.png")
print("Hidden script:\n", revealed_script)

# 3. اجرای اسکریپت استخراج شده
exec(revealed_script)

