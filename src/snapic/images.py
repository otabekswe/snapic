import os

from PIL import Image, ImageOps


def basename(path: str):
    os.path.basename(path)


def resize(path: str, width: int, height: int):
    with Image.open(path) as img:
        img = img.resize(width, height)
        img = ImageOps.cover(img, img.size)
        img.save(f"snapic_{basename(path)}")
    print("Done!")


def crop(path: str, box: tuple):
    with Image.open(path) as img:
        img = img.crop(box)
        img = ImageOps.cover(img, img.size)
        img.save(f"snapic_{basename(path)}")
    print("Done!")


def convert(path: str, to: str):
    with Image.open(path) as img:
        if not img.mode == 'RGB':
            img = img.convert('RGB')
        img.save(f'snapic_{basename(path)}.{to}')
    print("Done!")


def compress(path: str, percent: int, size: str):
    with Image.open(path) as img:
        if size:
            width, height = map(int, size.split("x"))
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(f'snapic_{basename(path)}', quality=percent, optimize=True, subsampling=0)
    print("Done!")


def remove_watermark(path):
    pass


def edit_metadata():
    pass


def optimize_for_social_media():
    pass


def to_pdf():
    pass


def text_detection():
    pass


def search_for(word: str):
    pass


def remove_bg():
    pass


def reduce_noise():
    pass