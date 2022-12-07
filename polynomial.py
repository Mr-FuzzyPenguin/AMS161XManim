from manim import *
# manim polynomial.py polynomial; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/polynomial/1080p60/polynomial.mp4 2>/dev/null >/dev/null

class polynomial(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        chapter = Text("1: Terminology and Polynomials", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT))
        self.wait(1)

        text = VGroup(Tex("What is a polynomial?"))
        self.play(Write(text))
        self.play(text.animate.shift(UP))

        text2 = VGroup(MathTex(r"\text{A polynomial is a function that can be represented using only}", font_size=35), MathTex(r"\text{arithmetic and }x\text{ raised to the power of a positive integer.}", font_size=35)).arrange(DOWN)
        text.add(text2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Unwrite(text))

        self.wait(1)

        text = Tex("Examples of valid and invalid polynomials").to_edge(UP).shift(DOWN/2)
        self.play(Write(text))

        # Define the symbols.
        check = SVGMobject(file_name="/home/penguin/Desktop/Code/manim-showcase/ams/assets/check.svg").scale(0.25)
        rx = SVGMobject(file_name="/home/penguin/Desktop/Code/manim-showcase/ams/assets/ex.svg").scale(0.25)

        # To be redefined at multiple times, so that you can add the
        # animation of the group fading.
        dg = VGroup()
        t0 = MathTable(
            [
                [r"x^2-4x", r"\sin \left( x \right)+ \cos \left( x \right)"],
                [r"x+\frac{1}{4}", r"e^x + \ln \left( x \right)"],
                [r"\left( x+2 \right) \left( x-8 \right)", r"\sqrt{x}+\sqrt[3]{x}"],
                [r"0", r"x^x"],
                [r"2x\cdot4x", r"\frac{1}{x^2}"],
            ],
            col_labels=[check, rx],
            include_outer_lines=True

        ).scale(0.5)
        dg.add(t0)
        dg.add(text)
        self.play(Write(t0))
        self.wait(3)
        self.play(Uncreate(dg))

        text = VGroup(Tex("There may be certain algebraic equations that are not necessarily polynomials.", font_size=38), Tex("Here are some examples:", font_size=38)).arrange(DOWN).to_edge(UP).shift(DOWN/2)
        self.play(Write(text))

        # rst dg and add new text
        dg = VGroup(text)
        # make new text, add again to group
        text = VGroup(MathTex(r"\sqrt{x}"), MathTex(r"\frac{1}{x}"), MathTex(r"x^{-0.4}"), MathTex(r"\left| x \right|")).arrange(RIGHT, buff=1.5)
        dg.add(text)

        self.wait(1)

        # show new text
        self.play(Write(text))
        self.wait(3)

        self.play(Unwrite(dg), run_time=0.5)

        text = VGroup(Tex("There are special functions called \"transcendental\" functions.", font_size=38), Tex("They are special because they transcend algebra. Here are examples:", font_size=38)).arrange(DOWN).to_edge(UP).shift(DOWN/2)
        self.play(Write(text))

        dg=VGroup(text)

        text = VGroup(MathTex(r"\cos \left( x \right)"), MathTex(r"\sin \left( x \right)"), MathTex(r"\ln \left( x \right)"), MathTex(r"e^x")).arrange(RIGHT, buff=1.5)
        dg.add(text)


        self.play(Write(text))
        self.wait(3)

        self.play(Uncreate(dg))
        text = Tex("So how do computers calculate those functions?", font_size=38)
        self.play(Write(text))
        self.play(Unwrite(text))
