from pathlib import Path
from PIL import Image

def resize_image(img_path: Path, out_path: Path, width: int, height: int, reducing_gap: int = 3):
    """Resize an image to the target dimension (w,h)"""
    with Image.open(img_path) as im:
        im.thumbnail([width, height], Image.Resampling.LANCZOS, reducing_gap=reducing_gap)
        im.save(out_path, "JPEG")
        
        
def resize_all_images(
    img_folder: Path, 
    width: int, 
    height: int,
    out_folder: Path,
    file_prefix: str,
    img_format: str = "jpeg"
    ):
    """Resize all images in folder to target dimensions"""
    for i, img_path in enumerate(img_folder.glob(f"*.{img_format}")):
        out_path = out_folder / f'{file_prefix} ({i+1}).jpeg'
        resize_image(img_path, out_path, width=width, height=height)