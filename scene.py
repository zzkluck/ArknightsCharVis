from manim import *
from pathlib import Path
from fetch_data import fetch_char_data

class ArkVis(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        x_range, y_range = [300, 1550, 100], [0, 1050, 100]
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_axis_config={
                "numbers_to_include": np.arange(*x_range),
            },
            y_axis_config={
                "numbers_to_include": np.arange(*y_range),
            },
            axis_config= {
                'include_ticks': True,
                'font_size': 24,
            },
            tips=False
        )
        axes.set_color(BLACK)
        self.add(axes)

        char_data = fetch_char_data()
        for px, py, pz, image_path in char_data:
            if not Path(image_path).exists(): continue
            img = ImageMobject(image_path)
            img.scale(0.1 * pz / pz)    # TODO: image size should be adjusted by pz
            img.move_to(axes.c2p(px, py))
            self.add(img)