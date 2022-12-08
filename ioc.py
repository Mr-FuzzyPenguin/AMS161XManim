from manim import *
"""
manim ioc.py ioc; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/ioc/1080p60/ioc.mp4 2>/dev/null >/dev/null
"""


class ioc(Scene):
    def construct(self):
        # Chapter 6
        # self.next_section(skip_animations=True)

        chapter = Text("7: Ratio test", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT), run_time=0.5)
        self.wait(0.5)
