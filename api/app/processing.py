from io import BytesIO

from PIL import Image, ImageFilter, ImageOps


def transform_image(data: bytes) -> bytes:
    with Image.open(BytesIO(data)) as image:
        normalized = ImageOps.exif_transpose(image).convert("RGB")
        resized = ImageOps.fit(normalized, (256, 256))
        sharpened = resized.filter(ImageFilter.SHARPEN)

        output = BytesIO()
        sharpened.save(output, format="PNG")
        return output.getvalue()
