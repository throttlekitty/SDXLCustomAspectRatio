# quick node to set SDXL-friendly aspect ratios in 1024^2
# by throttlekitty
import re


class SDXLAspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "width": ("INT", {"default": 64, "min": 64, "max": 2048,}),
                    "height": ("INT", {"default": 64, "min": 64, "max": 2048}),
                    "aspectRatio": ([
                    "1:1  - 1024x1024 square", 
                    "2:3  - 832x1216 portrait", 
                    "3:4  - 896x1152 portrait", 
                    "5:8  - 768x1216 portrait", 
                    "9:16 - 768x1344 portrait", 
                    "9:19 - 704x1472 portrait", 
                    "9:21 - 640x1536 portrait", 
                    "3:2  - 1216x832 landscape", 
                    "4:3  - 1152x896 landscape", 
                    "8:5  - 1216x768 landscape", 
                    "16:9 - 1344x768 landscape", 
                    "19:9 - 1472x704 landscape", 
                    "21:9 - 1536x640 landscape"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "SDXL_AspectRatio"
    CATEGORY = "image"

    def SDXL_AspectRatio(self, width, height, aspectRatio):
        # Matches aspectRatio text on any number of digits, an x and any number of digits
        pattern = r"(\d+)\s*x\s*(\d+)"
        match = re.search(pattern, aspectRatio)
    
        if match:
            width = int(match.group(1))
            height = int(match.group(2))
        
        return width, height

            
NODE_CLASS_MAPPINGS = {
    "SDXLAspectRatio": SDXLAspectRatio
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLAspectRatio": "SDXL Aspect Ratio"
}