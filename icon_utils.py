"""Icon processing utilities: extraction, conversion, and enhancement."""

import os
from PIL import Image, ImageFilter, ImageEnhance

# Standard icon sizes for HD multi-resolution .ico files
ICO_SIZES = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]


def enhance_image(img: Image.Image) -> Image.Image:
    """Apply sharpening and contrast enhancement to an icon image."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15)
    return img


def save_as_ico(img: Image.Image, save_path: str, bitmap_format: str = None) -> None:
    """Save an image as a multi-resolution .ico file."""
    kwargs = {"format": "ICO", "sizes": ICO_SIZES}
    if bitmap_format:
        kwargs["bitmap_format"] = bitmap_format
    img.save(save_path, **kwargs)


def extract_icon_from_exe(exe_path: str, output_dir: str) -> str | None:
    """Extract icon from an .exe file, enhance it, and save as .ico.

    Returns the path to the saved .ico file, or None on failure.
    """
    from icoextract import IconExtractor

    temp_ico = os.path.join(output_dir, "pulled_temp.ico")
    save_path = os.path.join(output_dir, "local_converted_icon.ico")

    extractor = IconExtractor(exe_path)
    extractor.export_icon(temp_ico)

    if not os.path.exists(temp_ico):
        return None

    try:
        img = Image.open(temp_ico)
        img = enhance_image(img)
        save_as_ico(img, save_path)
        return save_path
    finally:
        try:
            os.remove(temp_ico)
        except OSError:
            pass


def convert_image_to_ico(image_path: str, output_dir: str) -> str:
    """Convert any supported image file to an enhanced HD .ico file.

    Returns the path to the saved .ico file.
    Raises an exception if the image cannot be processed.
    """
    save_path = os.path.join(output_dir, "local_converted_icon.ico")
    img = Image.open(image_path)
    img = enhance_image(img)
    save_as_ico(img, save_path, bitmap_format="bmp")
    return save_path
