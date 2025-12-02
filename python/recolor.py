from PIL import Image
import colorsys

def replace_purple_with_green(input_path, output_path):
    img = Image.open(input_path).convert('RGB')
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Convert RGB → HSV
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            # --- Detect purple range ---
            # Purple hue roughly between 260°–300° → 0.72–0.83 in [0–1]
            if 0.72 < h < 0.83 and s > 0.25:
                
                # Replace hue with green (~120° → 0.33)
                new_h = 0.33
                new_s = s
                new_v = v

                # Convert back HSV → RGB
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                pixels[x, y] = (
                    int(nr * 255),
                    int(ng * 255),
                    int(nb * 255)
                )

    img.save(output_path)
    print("Done. Saved to:", output_path)


# Example use:
import os
dir = "assets/gcegames/textures/item/"
replace_purple_with_green(os.path.join(dir, "_nether_portal.png"), os.path.join(dir, "start_portal.png"))
