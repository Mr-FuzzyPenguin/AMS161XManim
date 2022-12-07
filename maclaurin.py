from manim import *
# manim maclaurin.py maclaurin; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/maclaurin/1080p60/maclaurin.mp4 2>/dev/null >/dev/null

class maclaurin(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        chapter = Text("2: MacLaurin series and approximation", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT))
        self.wait(1)

        # Defining the graph
        ax = Axes(
            x_range=[-2*PI, 2*PI],
            y_range=[-5, 5],
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        )

        labels = ax.get_axis_labels(x_label="\\text{x}", y_label="\\text{y}")
        graph = ax.plot(
            lambda x: np.sin(x),
            dt=0.1,
            color=RED,
        )

        # Group the graph
        graph_group = VGroup(ax, graph, labels)
        # Draw sinx graph
        self.play(Write(graph_group))

        text =  Tex("How do we estimate a sin function using only polynomials?")

        text.to_edge(DOWN)

        self.play(Write(text))
        self.wait(3)

        self.play(FadeOut(graph_group), FadeOut(text))

        # Introduce the viewer to the MacLaurin polynomial
        text = Tex("The MacLaurin series!").shift(UP)
        mcequ = MathTex(
            r"\sum _{n=0}^{\infty }f^{\left(n\right)}\left(0\right)\frac{x^n}{n!}=", r"\frac{f\left(0\right)x^0}{0!}+\frac{f'\left(0\right)x^1}{1!}+\frac{f''\left(0\right)x^2}{2!}+\cdots +\frac{f^{\left(k\right)}\left(0\right)x^k}{k!}+\cdots"
        )

        mcequ=mcequ.scale(0.75)
        mcequ.save_state()

        self.play(Write(text), Write(mcequ))
        self.play(FadeOut(text))
        self.wait(2)

        # self.next_section()

        # Change color for the latex
        # To find the indexes, you want to use
        # self.add(index_labels(mcequ[1]).set_opacity(0.2))


        cc = lambda color: lambda index: mcequ[1][index].animate.set_color(color)

        self.play(*map(cc(RED), [5, 7, 0]))
        self.wait(8)
        self.play(*map(cc(GREEN), [10, 11, 16, 18]))
        self.wait(8)
        self.play(*map(cc(BLUE), [21, 22, 23, 28, 30]))
        self.wait(8)
        self.play(*map(cc(YELLOW), [37, 39, 45, 47]))
        self.wait(8)
        # self.next_section(skip_animations=True)


        self.play(FadeOut(mcequ))
        self.wait(1)



        # MACLAURIN FUNCTION (First beautiful animation made... it's absolutely insane(ly hacky))

        graph2 = ax.plot(
            lambda x: 0,
            dt=0.1,
            color=BLUE,
        )

        # let's see this in action (say)
        self.play(Write(graph_group))

        text = MathTex(r"f \left(x \right)=", r"\frac{ \sin \left(0 \right) \cdot x^0}{0!}", font_size=35).to_edge(DOWN).shift(DOWN/2)
        text2 = MathTex(r"f \left(x \right)=", "0", font_size=35).to_edge(DOWN)

        self.play(Create(graph2), Write(text))
        self.play(TransformMatchingTex(text, text2))


        graph3 = ax.plot(
            lambda x: x,
            dt=0.1,
            color=BLUE,
        )

        # Hacky solution #1
        text = MathTex(r"f \left(x \right)=", "0", r"+\frac{ \cos \left( 0 \right) x^1}{1!}", font_size=35).to_edge(DOWN)
        self.play(ReplacementTransform(graph2, graph3), TransformMatchingTex(text2, text))
        text2 = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", font_size=35).to_edge(DOWN)
        self.play(TransformMatchingTex(text, text2))
        text = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", r"+ \left( -\frac{ \sin \left( 0\right)}{2!} \right)", font_size=35).to_edge(DOWN).shift(DOWN/2)
        self.play(TransformMatchingTex(text2, text))
        text2 = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", r"-0", font_size=35).to_edge(DOWN)
        self.play(TransformMatchingTex(text, text2))
        text = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", font_size=35).to_edge(DOWN)
        self.play(TransformMatchingTex(text2, text))
        text2 = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", r"+ \left( - \frac{ \cos \left( 0 \right) x^3}{3!} \right)", font_size=35).to_edge(DOWN).shift(DOWN/2)
        graph2 = ax.plot(
            lambda x: x+ ((-1*(x**3))/6),
            dt=0.1,
            color=BLUE,
        )

        self.play(ReplacementTransform(graph3, graph2), TransformMatchingTex(text, text2))
        text = MathTex(r"f \left(x \right)=", r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", font_size=35).to_edge(DOWN).shift(DOWN/2)
        self.play(TransformMatchingTex(text2, text))

        # Swaps out the texts and graphs. Intended to replace all of the above swapping TransformMatchingTex code above.
        current_text = text
        current_graph = graph2

        def tcg(new_text, ted=False, f=False, customShift = 0, font_size=35):
            nonlocal current_text
            nonlocal current_graph
            new_text_object = MathTex(r"f \left(x \right)=", *new_text, font_size=font_size).to_edge(DOWN)

            # hacky solution #2
            if ted:
                new_text_object.shift(DOWN/2+customShift)

            if not f:
                self.play(TransformMatchingTex(current_text, new_text_object))
            else:
                new_graph = ax.plot(
                    f,
                    dt=0.1,
                    color=BLUE
                )
                self.play(ReplacementTransform(current_graph, new_graph), TransformMatchingTex(current_text, new_text_object))
                current_graph = new_graph
            current_text = new_text_object

        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r"+ \frac{ \sin \left( 0\right)}{4!}"], True)
        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r" + 0"], True)
        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}"], True)

        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r"+ \frac{ \cos \left( 0 \right) x^5 }{5!}"], True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120))
        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r"+ \frac{ x^5 }{5!}"], True)

        note = Tex(r"Note: Notice how every other term in the series gives us a non-zero value? \\ From now on, we will be skipping every other term, and increase the degree by 2.", font_size=18).to_edge(DR).shift(UP)

        self.play(Write(note))

        self.play(Uncreate(note))

        tcg([r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r"+ \frac{ x^5 }{5!}", r"+ \left(-\frac{ \cos \left( 0 \right) x^7 }{7!} \right)"], True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120), RIGHT)

        # The ever growing text. Hacky solution #3
        # I decided to now use an array, and from here on forth,
        # I will be altering tegt before using tcg
        tegt = [r"\frac{x^1}{1!}", r"- \frac{ x^3 }{3!}", r"+ \frac{ x^5 }{5!}", r"+ \left(-\frac{ \cos \left( 0 \right) x^7 }{5040} \right)"]

        tegt[-1] = r"-\frac{x^7}{7!}"
        tcg(tegt, True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120) - ((x**7/5040)))

        tegt.append(r"+\frac{\cos \left( 0 \right)x^9}{9!}")
        tcg(tegt, True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120) - ((x**7/5040)) + (x**9/362880) )
        tegt[-1] = r"+\frac{x^9}{9!}"
        tcg(tegt, True)

        tegt.append(r"+\left( - \frac{\cos \left( 0 \right)x^{11}}{11!} \right)")
        tcg(tegt, True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120) - ((x**7/5040)) + (x**9/362880) - (x**11/39916800), LEFT+UP*0.15)
        tegt[-1] = r"-\frac{x^{11}}{11!}"
        tcg(tegt, True, customShift=LEFT+UP*0.15)

        tegt.append(r"+ \frac{\cos \left( 0 \right)x^{13}}{13!}")
        tcg(tegt, True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120) - ((x**7/5040)) + (x**9/362880) - (x**11/39916800) + (x**13/6227020800), LEFT+UP*0.15, font_size=28)
        tegt[-1] = r"+ \frac{x^{13}}{13!}"
        tcg(tegt, True, customShift=UP*0.15, font_size=28)

        tegt.append(r"-\frac{\cos \left( 0 \right)x^{15}}{15!} \right)")
        tcg(tegt, True, lambda x: x+ ((-1*(x**3))/6) + ((x**5)/120) - ((x**7/5040)) + (x**9/362880) - (x**11/39916800) + (x**13/6227020800) - (x**15/1307674368000), LEFT+UP*0.15, font_size=28)
        tegt[-1] = r"-\frac{x^{15}}{15!}"
        tcg(tegt, True, customShift=UP*0.15, font_size=28)

        tegt.append('...')
        tcg(tegt, True, f = lambda x: np.sin(x), customShift=UP*0.15, font_size=28)
        things_to_clear = VGroup(current_text)

        # BEGIN FROM HERE. Initialize required variables
        self.play(FadeOut(graph_group) , FadeOut(current_graph))
        self.play(current_text.animate.move_to(ORIGIN).shift(UP))
        self.wait(1)
        text = MathTex(r"\text{The series would continue infinitely, with each added term to the series} \\ \text{increasing its accuracy. How would we represent it using }\Sigma \text{ notation?}", font_size=38).shift(DOWN*1.3)

        # text2 is very similar to the mcequ
        text2 = MathTex(r"\sum _{n=0}^{\infty }f^{\left(n\right)}\left(0\right)\frac{x^n}{n!}=")
        text2 = text2.scale(0.75)

        # CHANGE COLOR TO WHITE
        self.play(Write(text), Write(mcequ.restore()))
        # self.play(FadeOut(current_text))

        # Another hacky solution. :/
        # current_text is the thing to mutate.

        self.remove(mcequ)
        self.play(TransformMatchingTex(mcequ, text2))

        current_text = text2
        def tc(new_text):
            nonlocal current_text
            new_text_object = MathTex(*new_text).scale(0.75)
            self.play(TransformMatchingTex(current_text, new_text_object))
            current_text = new_text_object


        # MacLaurin series for sin being built in action.
        tl = [r"\sum _{n=0}^{\infty }", r"f^{\left(n\right)}\left(0\right)",r"\frac{x^n}{n!}="]
        self.remove(current_text)
        current_text = MathTex(*tl)
        self.add(current_text.scale(0.75))

        tl.append(r"\sin \left( x \right)")
        tl.remove(tl[1])
        tc(tl)

        self.play(Unwrite(text))
        text = Tex("Notice how the factorials (in the denominators) increases by 2 and starts off at 1?", font_size=38).shift(DOWN*1.3)
        self.play(Write(text), run_time=0.5)
        self.wait(1)

        tl[1] = r"\frac{x^n}{ \left( 2n+1 \right)!}="
        tc(tl)

        self.play(Unwrite(text))
        text = Tex("Notice how the powers of x (in the numerators) increases by 2 and starts off at 1?", font_size=38).shift(DOWN*1.3)
        self.play(Write(text), run_time=0.5)
        self.wait(1)

        tl[1] = r"\frac{x^{2n+1}}{ \left( 2n+1 \right)!}="
        tc(tl)

        self.play(Unwrite(text))
        text = VGroup(
            Tex(r"Lastly, notice how the adding and subtracting alternates?", font_size=38),
            MathTex(r"\text{Raising } \left(-1 \right) \text{ to the } n \text{th power will allow this alternating}", font_size=38),
            Tex(r"behavior to be possible.", font_size=38)
        ).arrange(DOWN).shift(DOWN*1.3)
        self.play(Write(text), run_time=0.5)
        self.wait(1)

        tl[1] = r"\frac{ \left( -1 \right)^{n} x^{2n+1}}{ \left( 2n+1 \right)!}="
        print(''.join(tl))
        tc(tl)
        things_to_clear.add(current_text)
        things_to_clear.add(text)
        self.play(FadeOut(things_to_clear))

        text = VGroup(Tex("Try to solve for "), MathTex(r"\frac{a}{1-x}"), Tex(", cos, and "), MathTex('e...')).arrange().scale(0.75)
        self.play(Write(text))
        self.wait(3)
        self.play(text.animate.shift(UP*3))
        t0 = MathTable(
            [[r"e^x=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}", r"\cos \left( x \right) = \sum_{n=0}^{\infty}  \frac{\left(-1\right)^{n}\left(x^{2n}\right)}{\left(2n\right)!}"],
            [r"\sin\left(x\right)=\sum_{n=0}^{\infty}\frac{\left(-1\right)^{n}\left(x^{2n+1}\right)}{\left(2n+1\right)!}", r"\frac{a}{1-x}=\sum _{n=0}^{\infty }a\cdot x^n"]],
            include_outer_lines=True)
        text2 = Tex("MEMORIZE THIS!").shift(DOWN*3)
        self.play(Write(t0),Write(text2))
        self.wait(3)
        self.play(FadeOut(VGroup(text, text2, t0, chapter)))

        # self.next_section()
