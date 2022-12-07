from manim import *
"""
manim sum.py sum; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/sum/1080p60/sum.mp4 2>/dev/null >/dev/null
"""


class sum(Scene):
    def construct(self):
        # Chapter 5
        # self.next_section(skip_animations=True)

        chapter = Text("5: Find the sum", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT), run_time=0.5)
        self.wait(0.5)

        dg = VGroup()
        text = Tex("Let's bring up a previous problem:")  # 0
        dg.add(text)
        self.play(Write(text), run_time=0.25)
        self.play(text.animate.shift(UP))

        # 1
        text = MathTex(r"\sum _{n=0}^{\infty }", "4",
                       r"\left(", r"\frac{1}{2}", r"\right)", "^n")
        dg.add(text)
        self.play(Write(text), run_time=0.5)

        # 2
        text = Tex("Again, let's rewrite in the following format:").shift(DOWN)
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        self.play(dg.animate.shift(UP))

        # 3
        text = MathTex(r"\sum _{n=0}^{\infty }", "a",
                       r"\left(", r"r", r"\right)", "^n").shift(DOWN)
        dg.add(text)

        self.play(Write(dg[3]))

        self.play(dg[3][1].animate.set_color(RED),
                  dg[1][1].animate.set_color(RED), run_time=0.25)

        self.play(dg[3][3].animate.set_color(GREEN),
                  dg[1][3].animate.set_color(GREEN), run_time=0.25)

        self.play(dg[3][5].animate.set_color(BLUE),
                  dg[1][5].animate.set_color(BLUE), run_time=0.25)

        tvg = VGroup()
        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "a",
                        r"\left(", r"r", r"\right)", "^n", '=',
                        "a", r"{\left(", "1-", "r", "^n", r"\right)",
                        r"\over", "1-", "r", '}').shift(DOWN)
                )
        tvg[0][1].set_color(RED)
        tvg[0][7].set_color(RED)
        tvg[0][10].set_color(GREEN)
        tvg[0][3].set_color(GREEN)
        tvg[0][15].set_color(GREEN)
        tvg[0][11].set_color(BLUE)
        tvg[0][5].set_color(BLUE)

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "4",
                        r"{\left(", "1-", r"\frac{1}{2}", "^n", r"\right)",
                        r"\over", "1-", r"\frac{1}{2}", '}').shift(DOWN)
                )
        tvg[1][1].set_color(RED)
        tvg[1][7].set_color(RED)
        tvg[1][10].set_color(GREEN)
        tvg[1][3].set_color(GREEN)
        tvg[1][15].set_color(GREEN)
        tvg[1][11].set_color(BLUE)
        tvg[1][5].set_color(BLUE)

        self.play(TransformMatchingTex(dg[3], tvg[0]))
        dg[3] = tvg[0]
        self.play(TransformMatchingTex(dg[3], tvg[1]))
        dg[3] = tvg[1]
        # self.add(index_labels(dg[3]).set_opacity(0.8))

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "4",
                        r"{\left(", "1-", r"\frac{1}{2}", r"^\infty", r"\right)",
                        r"\over", "1-", r"\frac{1}{2}", '}').shift(DOWN)
                )
        tvg[2][1].set_color(RED)
        tvg[2][7].set_color(RED)
        tvg[2][10].set_color(GREEN)
        tvg[2][3].set_color(GREEN)
        tvg[2][15].set_color(GREEN)
        tvg[2][11].set_color(BLUE)
        tvg[2][5].set_color(BLUE)

        self.play(TransformMatchingTex(dg[3], tvg[2]))
        dg[3] = tvg[2]

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "4",
                        r"{\left(", "1-", "0", r"\right)",
                        r"\over", r"\frac{1}{2}", '}').shift(DOWN)
                )

        tvg[3][1].set_color(RED)
        tvg[3][7].set_color(RED)
        tvg[3][3].set_color(GREEN)
        tvg[3][13].set_color(GREEN)
        tvg[3][5].set_color(BLUE)
        self.play(TransformMatchingTex(dg[3], tvg[3]))
        dg[3] = tvg[3]

        # self.add(index_labels(tvg[3]).set_opacity(0.8))
        self.wait(0.1)

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "4",
                        '{', "1", r"\over", r"\frac{1}{2}", '}').shift(DOWN)
                )
        self.play(TransformMatchingTex(dg[3], tvg[4]))
        dg[3] = tvg[4]

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "4",
                        r'\cdot', '2').shift(DOWN)
                )
        self.play(TransformMatchingTex(dg[3], tvg[5]))
        dg[3] = tvg[5]

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", "4",
                        r"\left(", r"\frac{1}{2}", r"\right)", "^n", '=', "8",
                        ).shift(DOWN)
                )
        self.play(TransformMatchingTex(dg[3], tvg[6]))
        dg[3] = tvg[6]

        self.play(FadeOut(dg))

        dg, tvg = VGroup(), VGroup()

        self.next_section()

        # 0
        text = Text("Now try this one! Be careful, it's quite indecisive!",
                    font_size=38)
        dg.add(text)

        # 1
        text = MathTex(r"\sum _{n=0}^{\infty }",
                       r"\left(-1\right)^n").shift(DOWN)
        dg.add(text)

        tvg.add(MathTex(r"\sum _{n=0}^{\infty }", r"\left(-1\right)^n", '=',
                        '-1', '+', '1', '+', r"\cdots").shift(DOWN))
        self.play(Write(dg))
        self.play(dg.animate.shift(UP))
        self.play(TransformMatchingTex(dg[1], tvg[0]))
        dg[1] = tvg[0]

        # 2
        text = VGroup(Tex("Converge means to equate to a finite sum."),
                      Tex("One, and only one finite sum. In this case,"),
                      Tex(r"The answer does not diverge to $\infty$.")
                      ).arrange(DOWN).to_edge(DOWN)
        dg.add(text)

        self.play(Write(text))
        self.play(dg[2].animate.shift(UP), dg[1].animate.shift(UP))

        text = Tex(r"Divergence does not necessarily mean $\pm \infty$").to_edge(DOWN)
        dg.add(text)
        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(VGroup(dg, chapter)))
