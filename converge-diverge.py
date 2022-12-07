from manim import *
"""
manim converge_diverge.py converge_diverge; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/converge_diverge/1080p60/converge_diverge.mp4 2>/dev/null >/dev/null
"""


class converge_diverge(Scene):
    def construct(self):
        # Chapter 4
        # self.next_section(skip_animations=True)

        # self.next_section(skip_animations=True)
        chapter = Text("4: Converge or diverge?", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT), run_time=0.5)
        self.wait(0.5)

        dg = VGroup()
        text = Tex("On the topic of summations...")  # 0
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP))

        text = Tex("We will now learn how to solve:")  # 1
        dg.add(text)

        # 2
        text = MathTex(r"\sum _{n=0}^{\infty }", "4",
                       r"\left(", r"\frac{1}{2}", r"\right)", "^n").shift(DOWN)
        dg.add(text)
        self.wait(1)
        self.play(Write(dg[1]), Write(text), run_time=0.5)
        self.wait(3)
        self.play(Unwrite(dg[1]))
        self.play(text.animate.shift(UP))

        text = Tex("Let's rewrite the summation:")  # 3
        dg.add(text)

        self.play(dg[0].animate.shift(UP), dg[2].animate.shift(UP))
        self.play(Write(text))

        # 4
        text = MathTex(r"\sum _{n=0}^{\infty }", "a",
                       r"\left(", r"r", r"\right)", "^n")
        dg.add(text)

        self.play(dg[0].animate.shift(UP), dg[2].animate.shift(UP), dg[3].animate.shift(UP))
        self.play(Write(text))

        # self.add(index_labels(dg[2]).set_opacity(0.2))
        # self.add(index_labels(dg[4]).set_opacity(0.2))

        self.wait(0.1)

        self.play(dg[2][1].animate.set_color(RED), dg[4][1].animate.set_color(RED))

        self.play(dg[2][3].animate.set_color(GREEN), dg[4][3].animate.set_color(GREEN))

        self.play(dg[2][5].animate.set_color(BLUE), dg[4][5].animate.set_color(BLUE))

        # self.next_section(skip_animations=True)
        text = MathTex("r")  # 5
        dg.add(text, MathTex("-1", '<', r"\frac{1}{2}", '<', '1').shift(UP*2+0.2*LEFT))  # 6
        dg.add(MathTex(r"\uparrow").shift(UP))  # 7
        self.play(TransformMatchingTex(dg[4],
                                       text
                                       ),
                  TransformMatchingTex(dg[2], dg[6]),
                  TransformMatchingTex(dg[3], dg[7])
                  )

        text = MathTex(r"\text{Notice how } r \text{ is between -1 and 1? We know it converges.}").shift(DOWN)

        dg.add(text)
        dg.remove(dg[2], dg[4], dg[3])
        self.play(Write(text), run_time=0.5)

        self.wait(2)
        self.play(Unwrite(dg), run_time=0.5)
        # self.play(Unwrite(dg))

        # RESETTING SCENE, RESETTING dg
        dg = VGroup()
        text = Tex("Let's try a different scenario")
        self.play(Write(text), run_time=0.5)
        self.wait(0.5);
        self.play(Unwrite(text), run_time=0.5)

        text = Tex("Solve for:").shift(UP)  # 0
        dg.add(text)

        text = MathTex(r"\sum _{n=0}^{\infty }", r"\frac{1}{3}",
                       r"\left(", "3", r"\right)", "^n")  # 1

        dg.add(text)
        self.play(Write(dg))

        text = MathTex(r"\sum _{n=0}^{\infty }", "a",
                       r"\left(", r"r", r"\right)", "^n").shift(DOWN*1.6)  # 2
        dg.add(text)
        self.play(Write(text))
        self.wait(2)

        tvg = VGroup()
        tvg.add(MathTex(r"\text{Converges if: }", "-1<", "r<", "1").shift(DOWN*1.6), MathTex('3'), MathTex("-1<1<",'3'))
        self.play(TransformMatchingTex(dg[2], tvg[0]), TransformMatchingTex(dg[1], tvg[1]))
        dg[2] = tvg[0]
        dg[1] = tvg[1]
        self.wait(0.25)
        self.play(TransformMatchingTex(dg[1], tvg[2]))
        dg[1] = tvg[2]

        # 3
        dg.add(VGroup(Tex("That is how we know that this function diverges."), MathTex(r"\text{Divergence: } -\infty \text{ or } \infty")).arrange(DOWN).to_edge(DOWN))
        self.play(Write(dg[3]))
        self.next_section()

        # self.add(index_labels(dg[3][1][0]).set_opacity(0.8))
        # self.add(index_labels(dg[2]).set_opacity(0.8))
        # self.add(index_labels(dg[1]).set_opacity(0.8))

        self.play(dg[3][1][0][15].animate.set_color(BLUE), dg[2][3].animate.set_color(BLUE), dg[1][1].animate.set_color(BLUE))

        self.wait(1)
        self.play(Unwrite(VGroup(dg, chapter)))
