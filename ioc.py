from manim import *
"""
manim ioc.py ioc; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/ioc/1080p60/ioc.mp4 2>/dev/null >/dev/null
"""


class ioc(Scene):
    def construct(self):
        # Chapter 6
        # self.next_section(skip_animations=True)

        chapter = Text("6: Interval of Convergence", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT), run_time=0.5)
        self.wait(0.5)

        dg, tvg = VGroup(), VGroup()
        # 0
        text = Tex("Consider the following:")
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP), run_time=0.25)

        # 1
        text = MathTex("1",r"\over", "1","-","x")
        dg.add(text)
        self.play(Write(text))

        self.play(dg.animate.shift(UP), run_time=0.25)
        text = VGroup(Tex("The Maclaurin approximation for the function above equates to", font_size=28),
                      MathTex(r"\sum _{n=0}^{\infty }", "x", "^n")).arrange(DOWN).shift(DOWN)
        tvg.add(text)
        self.play(Write(text))

        # 2
        text = Tex("Which begs the question:").shift(2.5*DOWN)
        dg.add(text)
        self.play(Write(text))

        # 3
        text = MathTex(r"\text{Can the Maclaurin series approximate }",r"\text{...}").shift(3*DOWN)
        dg.add(text)
        self.play(Write(text))

        text = MathTex(r"\text{Can the Maclaurin series approximate }", r"\text{EVERYTHING?}").shift(3*DOWN)
        tvg.add(text)

        self.play(TransformMatchingTex(dg[3], tvg[1]))
        dg[3] = tvg[1]

        self.play(FadeOut(dg), FadeOut(tvg[0][0]))

        # Cleared screen
        dg = tvg[0][1]
        tvg = VGroup()

        self.play(dg.animate.shift(UP*3))

        # 0
        # sigma x^n

        # 1
        text = Tex("By now, you should be able to tell that $x$ is the placeholder for ", r"$r$", font_size=38)
        dg.add(text)
        self.play(Write(text))

        # t0
        text = MathTex(r"\sum _{n=0}^{\infty }", "a",
                       r"\left(", r"r", r"\right)", "^n").shift(DOWN)
        tvg.add(text)
        self.play(Write(text))

        # t1
        text = MathTex(r"\sum _{n=0}^{\infty }",
                       r"\left(", r"x", r"\right)", "^n").shift(DOWN)
        tvg.add(text)
        self.wait(0.5)
        self.play(TransformMatchingTex(tvg[0], tvg[1]))
        self.wait(0.5)
        self.play(TransformMatchingTex(tvg[1], tvg[0]))

        # Cleared screen
        self.play(FadeOut(dg))
        dg = VGroup()

        # 0
        text = MathTex("-1<","r","<1").shift(UP)
        dg.add(text)
        self.play(TransformMatchingTex(tvg[0], dg[0]))
        tvg = VGroup()

        # 1
        text = Tex("Remember: $r$ in this instance is $x$ in the summation.", font_size=38)
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        tvg.add(MathTex("-1<","x","<1").shift(UP))
        self.play(TransformMatchingTex(dg[0], tvg[0]))
        dg[0]=tvg[0]

        # 2
        text = Tex("The function will only converge where $x$ meets the following criteria:", font_size=38).shift(UP*2.5)
        dg.add(text)
        self.play(Write(text))

        self.play(FadeOut(dg))
        self.wait(0.1)

        text = Tex("Let's graph it!").to_edge(DOWN)
        self.play(FadeIn(text), run_time=0.25)
        self.wait(0.5)
        self.play(FadeOut(text), run_time=0.25)

        # Defining the graph
        ax = Axes(
            x_range=[-10, 10],
            y_range=[-3, 16],
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        )


        line = DashedVMobject(Line(ax.c2p(-1, -3), ax.c2p(-1, 16), color=BLUE), num_dashes=38)


        labels = ax.get_axis_labels(x_label="\\text{x}", y_label="\\text{y}")
        graph = VGroup(
            ax.plot(
                lambda x: 1/(1-x),
                x_range = [-10,0.86,0.01],
                discontinuities=[1],
                dt=0.1,
                color=RED,
            ),
            ax.plot(
                lambda x: 1/(1-x),
                x_range=[4/3,10,0.01],
                color=RED,
            ),
            ax.plot(
                lambda x:sum([x**i for i in range(500)]),
                x_range=[-0.98,0.941,0.001],
                color=BLUE
            ),
        )


        graph_group = VGroup(ax, graph, labels, line)
        self.play(Write(graph_group))

        text = Tex("Notice how the graph converges when x is between -1 and 1?", font_size=38).to_edge(DOWN)
        dg.add(text)
        self.play(Write(text))


        # Cleared screen
        self.play(FadeOut(graph_group), FadeOut(text))

        del dg
        dg = VGroup()
        tvg = VGroup()

        # 0
        text = Tex("What about the following:")
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP), run_time=0.5)
        dg.add(text)

        # 1
        text = MathTex("f",r"\left(", r"x", r"\right)", '=', "{2", r"\over", "4", "+", "5x", '}')
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP), dg.animate.shift(UP))
        dg.add(text)

        # 2
        text = Tex("Let's rewrite it in the following format:")
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.shift(UP), dg.animate.shift(UP))
        dg.add(text)

        # 3
        text = MathTex("f",r"\left(", r"x", r"\right)", '=', "{a", r"\over", '1', '-', 'r', '}')
        dg.add(text)
        self.play(Write(text), run_time=0.5)

        # t0
        text = MathTex("f", r"\left(", r"x", r"\right)", '=', "{2", r"\over", "4", "+", "5x", '}', '=',
                       "{2", r"\over", "4", "-", r"\left(", '-', "5x", r"\right)", '}'
                       ).shift(UP*2)
        tvg.add(text)

        # t1
        text = MathTex("f", r"\left(", r"x", r"\right)", '=',
                       "{2", r"\over", "4", "+", "5x", '}', '=',
                       '{', "{2", r"\over", "4", '}', r"\over",
                       '{', '4', r"\over", '4', r'}', "-", r"\left(", '-' '{',
                       "5x", r"\over", '4', '}', r"\right)"
                       ).shift(UP*2)
        tvg.add(text)

        self.play(TransformMatchingTex(dg[1], tvg[0]))
        self.wait(0.5)
        dg[1] = tvg[0]

        self.play(TransformMatchingTex(dg[1], tvg[1]))
        self.play(tvg[1][12:16].animate.set_color(RED),
                  tvg[1][18:22].animate.set_color(GREEN),
                  tvg[1][24:31].animate.set_color(BLUE),
                  dg[3][5].animate.set_color(RED),
                  dg[3][7].animate.set_color(GREEN),
                  dg[3][9].animate.set_color(BLUE)
                  )
        dg[1] = tvg[1]

        # 4
        text = Tex("And now to write the Maclaurin approximation:").shift(DOWN)
        self.play(Write(text), run_time=0.5)
        dg.add(text)

        # 5
        text = MathTex(r"\sum _{n=0}^{\infty }", "a",
                        r"\left(", r"r", r"\right)", "^n").to_edge(DOWN)
        self.play(Write(text))
        dg.add(text)

        self.wait(0.5)

        # t2
        text = MathTex(r"\sum _{n=0}^{\infty }", r"\frac{2}{4}",
                       r"\left(", r"-\frac{5x}{4}", r"\right)", "^n").to_edge(DOWN)
        tvg.add(text)
        tvg[2][1].set_color(RED)
        tvg[2][3].set_color(BLUE)

        self.play(TransformMatchingTex(dg[5], tvg[2]))
        dg[5] = tvg[2]
        dg.remove(dg[5])
        dg.remove(dg[1])

        # t3
        tvg.add(dg[1])

        self.play(FadeOut(dg))
        self.play(tvg[2].animate.shift(UP*3), run_time=0.5)
        text = Tex("Let's graph it!").to_edge(DOWN)
        self.play(Write(text), run_time=0.5)

        self.play(FadeOut(tvg[2], tvg[1], text))

        # Cleared screen
        tvg, dg = VGroup(), VGroup()



        # Defining the graph
        ax = Axes(
            x_range=[-10, 10],
            y_range=[-3, 16],
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        )


        line = DashedVMobject(Line(ax.c2p(0.8, -3), ax.c2p(0.8, 16), color=BLUE), num_dashes=38)


        labels = ax.get_axis_labels(x_label="\\text{x}", y_label="\\text{y}")
        graph = VGroup(
            ax.plot(
                lambda x: 2/(4+5*x),
                x_range=[-10, -0.933, 0.01],  # TUNED
                dt=0.1,
                color=RED,
            ),
            ax.plot(
                lambda x: 2/(4+5*x),
                x_range=[-0.775, 10, 0.01],  # TUNED
                color=RED,
            ),
            ax.plot(
                lambda x:sum([ 0.5 * ((-5/4)*x)**i for i in range(500)]),
                x_range=[-0.775,0.775, 0.001],
                color=BLUE
            ),
        )


        graph_group = VGroup(ax, graph, labels, line)
        self.play(Write(graph_group))

        text = Tex("Notice how the graph converges when x is between -0.8 and 0.8?", font_size=38).to_edge(DOWN)
        self.play(Write(text), run_time=0.5)

        # Cleared screen
        self.play(FadeOut(graph_group), FadeOut(text))
        tvg, dg = VGroup(), VGroup()

        self.next_section()
        # 0
        text = MathTex("-1", '<', 'r', '<', '1')
        dg.add(text)

        self.play(Write(text))

        text = MathTex("-1","<", r"-\frac{5}{4}", "x", "<","1")
        tvg.add(text)
        self.play(TransformMatchingTex(dg[0], tvg[0]))
        dg[0] = tvg[0]

        text = Tex("$x$ satisfies the above constraint only when...").to_edge(DOWN)
        dg.add(text)
        self.wait(0.5)
        self.play(Write(text), run_time=0.5)

        text = MathTex(r" - \frac{4}{5}", r"\cdot", "-1", "<", r"-\frac{5}{4}", "x", r"\cdot", r"- \frac{4}{5}", "<", "1", r"\cdot", r"- \frac{4}{5}")
        tvg.add(text)
        self.play(TransformMatchingTex(dg[0], tvg[1]), run_time=1)
        self.wait(0.5)
        dg[0] = tvg[1]

        text = MathTex(r"\frac{4}{5}",">", r"x", ">", r"- \frac{4}{5}")
        tvg.add(text)
        self.play(TransformMatchingTex(dg[0], tvg[2]), run_time=1)
        self.wait(0.5)
        dg[0] = tvg[2]

        self.play(Unwrite(VGroup(dg, chapter)))
