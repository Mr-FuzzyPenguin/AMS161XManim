from manim import *
"""
manim ratio-test.py ratio_test; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/ratio_test/1080p60/ratio_test.mp4 2>/dev/null >/dev/null
"""


class ratio_test(Scene):
    def construct(self):
        # Chapter 7
        # self.next_section(skip_animations=True)

        chapter = Text("7: Ratio ratio_test", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT), run_time=0.5)
        self.wait(0.5)

        dg, tvg = VGroup(), VGroup()

        # 0
        text = Tex("Sometimes, you may need to solve:", font_size=40)
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP))
        dg.add(text)

        # 0 2
        text = MathTex(r"\sum _{n=0}^{\infty }", "{1", r"\over" ,
                       "n!}")
        self.play(Write(text), run_time=0.5)
        tvg.add(text)

        # 1
        text = Tex(r"You will see that you cannot put it in the format of $a\left( r \right)^n$").shift(DOWN)
        dg.add(text)
        self.play(Write(text), run_time=0.5)

        # 2
        text = Tex(r"To solve this, we need the ratio ratio_test.").shift(2*DOWN)
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        self.play(FadeOut(dg))

        # 0
        text = tvg[0]
        tvg = VGroup()
        dg = VGroup()
        self.play(text.animate.shift(2*UP), run_time=0.5)
        dg.add(text)

        # t0
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over", r"\left(", "n+1", r"\right)", '!', "}",
                       r"\over",
                       "{1", r"\over", "n!}", '}'
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[0]), run_time=0.5)
        dg[0] = tvg[0]

        # t1
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                       r"\left(", "n+1", r"\right)", '!', "}", r"\cdot"
                       "{n!", r"\over", "1}", '}'
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[1]))
        dg[0] = tvg[1]

        # t2
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{n!", r"\over",
                       r"\left(", "n+1", r"\right)", '!', "}"
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[2]))
        dg[0] = tvg[2]

        # t3
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{n!", r"\over",
                       r"\left(", "n+1", r"\right)", r"\left(", "n", r"\right)",
                       '!', "}"
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[3]))
        dg[0] = tvg[3]

        # t4
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                       r"\left(", "n","+1", r"\right)", "}"
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[4]))
        dg[0] = tvg[4]

        # t5
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                       r"\left(", "n","+1", r"\right)", "}", '=',
                       '{', "{1", r"\over",
                       r"\left(", r"\infty", r"\right)", "}"
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[5]))
        dg[0] = tvg[5]

        # t6
        text = MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                       r"\left(", "n","+1", r"\right)", "}", '=',
                       '{', "{1", r"\over",
                       r"\left(", r"\infty", r"\right)", "}", "=0"
                       ).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[6]))
        dg[0] = tvg[6]

        # t7
        text = VGroup(
                    MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                    r"\left(", "n","+1", r"\right)", "}", '=',
                    '{', "{1", r"\over",
                    r"\left(", r"\infty", r"\right)", "}", "=0").shift(2*UP),
                    MathTex("r=0"), MathTex("-1<", "r", "<1")
                ).arrange(DOWN).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[7]))
        dg[0] = tvg[7]

        # t8
        text = VGroup(
                    MathTex(r"\lim_{n \rightarrow \infty}", '{', "{1", r"\over",
                    r"\left(", "n","+1", r"\right)", "}", '=',
                    '{', "{1", r"\over",
                    r"\left(", r"\infty", r"\right)", "}", "=0"),
                    MathTex("r=0"), MathTex("-1<", "0", "<1")
                ).arrange(DOWN).shift(2*UP)
        tvg.add(text)
        self.wait(2)
        self.play(TransformMatchingTex(dg[0], tvg[8]))
        dg[0] = tvg[8]

        text = Tex("This is how we know the function converges.")
        self.play(Write(text), run_time=0.5)
        self.wait(2)
        self.play(Unwrite(VGroup(chapter, dg, text, dg[0])), run_time=0.5)
