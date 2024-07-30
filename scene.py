from manim import *
from pathlib import Path
from fetch_data import fetch_char_data, fetch_enemy_data
from utils import Circle, circle_collide_sim

class ArkVisChar(Scene):
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

        img_obj_list, circles = [], []
        for px, py, pz, image_path in char_data:
            if not Path(image_path).exists(): continue
            img = ImageMobject(image_path)
            img.scale(0.1 * pz / pz)    # TODO: image size should be adjusted by pz
            self.add(img)
            img.move_to(axes.c2p(px, py))
            
            img_obj_list.append(img)
            circles.append(Circle(axes.c2p(px, py)[0], axes.c2p(px, py)[1], img.height/2))

        for _ in range(10):
            circle_collide_sim(circles)
            # animations = []
            for i, circle in enumerate(circles):
                px, py = circle.x, circle.y
                # animations.append(ApplyMethod(img_obj_list[i].move_to, np.array([px, py, 0])))
                img_obj_list[i].move_to(np.array([px, py, 0]))
            # self.play(*animations, run_time=2)