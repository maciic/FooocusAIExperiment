import replicate
import os
import urllib.request
from tqdm import tqdm

def generatePicture(prompt, image_number = 2, style_selections = "Impressionism", resolution = "1216*832"):
    input={
        "prompt": prompt,
        "cn_type1": "ImagePrompt",
        "cn_type2": "ImagePrompt",
        "cn_type3": "ImagePrompt",
        "cn_type4": "ImagePrompt",
        "sharpness": 2,
        "image_seed": -1,
        "uov_method": "Disabled",
        "image_number": image_number,
        "guidance_scale": 4,
        "refiner_switch": 0.5,
        "negative_prompt": "",
        "style_selections": style_selections,
        "uov_upscale_value": 0,
        "outpaint_selections": "",
        "outpaint_distance_top": 0,
        "performance_selection": "Speed",
        "outpaint_distance_left": 0,
        "aspect_ratios_selection": resolution,
        "outpaint_distance_right": 0,
        "outpaint_distance_bottom": 0,
        "inpaint_additional_prompt": ""
    }

    return input

def upscaleImagePreset(path):
    input = {
        "prompt": "",
            "cn_type1": "ImagePrompt",
            "cn_type2": "ImagePrompt",
            "cn_type3": "ImagePrompt",
            "cn_type4": "ImagePrompt",
            "sharpness": 2,
            "image_seed": -1,
            "image_number": 1,
            "guidance_scale": 4,
            "refiner_switch": 0.5,
            "negative_prompt": "",
            "style_selections": "Impressionism",
            "outpaint_selections": "",
            "outpaint_distance_top": 0,
            "performance_selection": "Speed",
            "outpaint_distance_left": 0,
            "aspect_ratios_selection": "832*1216",
            "outpaint_distance_right": 0,
            "outpaint_distance_bottom": 0,
            "inpaint_additional_prompt": "",
            "uov_method": "Upscale (Custom)",
            "uov_upscale_value": 4,
            "uov_input_image": open(path, "rb")
    }

    return input

def main():
    mode = False

    if mode is True:
        #Generate new picture branch(not complete)
        output = replicate.run(
            "konieshadow/fooocus-api:fda927242b1db6affa1ece4f54c37f19b964666bf23b0d06ae2439067cd344a4",
            input=generatePicture("")
        )

        index = 5
        for x in output:
            urllib.request.urlretrieve(x, "huBeTaTa" + str(index) + ".png")
            index += 1

    else:
        #Upscale puctires with thsi branch (almost complete, need further testing)
        input_path = "C:\\Users\hu8MarRe\OneDrive\Saját ötletek\Programozás\FooocusAi\VSCode\For upscale"
        output_path = "C:\\Users\hu8MarRe\OneDrive\Saját ötletek\Programozás\FooocusAi\VSCode\\Upscaled"
    
        input_list = os.listdir(input_path)
        output_list = os.listdir(output_path)

        lastName = 1
        try:
            lastName = output_list[len(output_list)-1][:-4]
        except:
            pass

        for i in tqdm(input_list, desc="Processing...", ncols=100):
            output = replicate.run(
                "konieshadow/fooocus-api:fda927242b1db6affa1ece4f54c37f19b964666bf23b0d06ae2439067cd344a4",
                input=upscaleImagePreset(input_path + "\\" + i)
            )
            urllib.request.urlretrieve(output[0], output_path + "\\" + str(lastName) + ".png")
            lastName += 1
            
        print("Complete.")

if __name__ == "__main__":
    main()