# quick node to set SDXL-friendly aspect ratios in 1024^2
# by throttlekitty

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
        if aspectRatio == "1:1  - 1024x1024 square":
            width, height = 1024, 1024
        elif aspectRatio == "2:3  - 832x1216 portrait":
            width, height = 832, 1216
        elif aspectRatio == "3:4  - 896x1152 portrait":
            width, height = 896, 1152
        elif aspectRatio == "5:8  - 768x1216 portrait":
            width, height = 768, 1216
        elif aspectRatio == "9:16 - 768x1344 portrait":
            width, height = 768, 1344
        elif aspectRatio == "9:19 - 704x1472 portrait":
            width, height = 704, 1472
        elif aspectRatio == "9:21 - 640x1536 portrait":
            width, height = 640, 1536
        elif aspectRatio == "3:2  - 1216x832 landscape":
            width, height = 1216, 832
        elif aspectRatio == "4:3  - 1152x896 landscape":
            width, height = 1152, 896
        elif aspectRatio == "8:5  - 1216x768 landscape":
            width, height = 1216, 768
        elif aspectRatio == "16:9 - 1344x768 landscape":
            width, height = 1344, 768
        elif aspectRatio == "19:9 - 1472x704 landscape":
            width, height = 1472, 704
        elif aspectRatio == "21:9 - 1536x640 landscape":
            width, height = 1536, 640
        return(width, height)

            
NODE_CLASS_MAPPINGS = {
    "SDXLAspectRatio": SDXLAspectRatio
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLAspectRatio": "SDXL Aspect Ratio"
}