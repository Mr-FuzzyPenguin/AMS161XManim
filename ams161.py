from manim import *
# manim ams161.py greeting; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/ams161/1080p60/greeting.mp4 2>/dev/null >/dev/null

class greeting(Scene):
    def construct(self):
        text = Text("Calculus 2 in 5 minutes", font_size=50)


        # BEAUTIFUL start for sbu logo
        sbu = SVGMobject(file_name="/home/penguin/Desktop/Code/manim-showcase/ams/assets/sbu.svg")
        self.play(DrawBorderThenFill(sbu))
        self.wait(1)
        self.play(FadeOut(sbu))

        self.play(Write(text))
        self.play(text.animate.shift(UP))
        self.wait(1)

        acknowledgement = Tex(
                    """
                    With many thanks to Dr. Bernhard
                    for making an enjoyable Calculus 2 experience
                    """
                    , font_size=45
                ).scale_to_fit_width(config.frame_width/2)

        text_group = VGroup()
        text_group.add(text)
        text_group.add(acknowledgement)

        # Intro and acknowledgement
        self.play(Write(acknowledgement))
        self.wait(2)
        self.play(Uncreate(text_group), run_time=0.5)


        # Chapter 1
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

        text = VGroup(Tex("There are special functions called ``transcendental\" functions.", font_size=38), MathTex(r"\text{They are special because they \underline{transcend} algebra. Here are examples:}", font_size=38)).arrange(DOWN).to_edge(UP).shift(DOWN/2)
        self.play(Write(text))

        dg=VGroup(text)

        text = VGroup(MathTex(r"\cos \left( x \right)"), MathTex(r"\sin \left( x \right)"), MathTex(r"\ln \left( x \right)"), MathTex(r"e^x")).arrange(RIGHT, buff=1.5)
        dg.add(text)


        self.play(Write(text))
        self.wait(3)

        self.play(Uncreate(dg))
        text = Tex("So how do computers calculate those functions?", font_size=38)
        self.play(Write(text))
        self.play(Unwrite(text), Unwrite(chapter))




        # Chapter 2

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
        self.wait(5)
        self.play(*map(cc(GREEN), [10, 11, 16, 18]))
        self.wait(5)
        self.play(*map(cc(BLUE), [21, 22, 23, 28, 30]))
        self.wait(5)
        self.play(*map(cc(YELLOW), [37, 39, 45, 47]))
        self.wait(2)
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
        self.wait(2)
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

        # CHAPTER 3
        chapter = Text("3: Special integrals", font_size=50)
        self.play(Write(chapter))
        self.play(chapter.animate.scale(0.3).to_edge(UP+LEFT))
        self.wait(1)

        dg = VGroup()
        text = Tex("Are all functions integrateable?")
        dg.add(text)
        self.play(Write(text))
        self.play(text.animate.shift(UP*3))

        text = VGroup(Tex("Try to integrate the following:"), MathTex(r"\int \cos \left(x^2 \right) dx")).arrange(DOWN)
        dg.add(text)
        self.play(Write(text))
        self.wait(3)
        text = Tex("You will quickly realize this is impossible.").shift(DOWN*1.5)

        self.play(Write(text))


        text2 = Tex("You will quickly realize this is impossible.", "OR IS IT?").shift(DOWN*1.5)
        self.play( TransformMatchingTex(text, text2) )
        dg.add(text2)

        # Hide all the stuff except for the integral and prompt
        self.play (Unwrite(VGroup(dg, text2)), run_time=0.5)

        self.next_section()
        dg = VGroup()
        text = MathTex(r"\text{Recall the Taylor series for } f\left( x \right) = \cos \left( x \right)")
        dg.add(text)
        self.play(Write(text), run_time=0.5)
        self.play(text.animate.to_edge(UP), run_time=0.5)
        dg.add(text)
        text = MathTex(r"\cos \left( x \right) = \sum_{n=0}^{\infty}  ", r"\frac{\left(-1\right)^{n}\left(x^{2n}\right)}{\left(2n\right)!}")
        self.wait(2)
        self.play(Write(text), run_time=0.5)
        text2 = MathTex(r"\cos \left( x^2 \right) = \sum_{n=0}^{\infty}  ", r"\frac{\left(-1\right)^{n}\left[ \left(x^2 \right)^{2n} \right]}{\left(2n\right)!}")
        self.wait(2)
        self.play(TransformMatchingTex(text, text2))
        text = MathTex(r"\cos \left( x^2 \right) = \sum_{n=0}^{\infty} \frac{\left(-1\right)^{n}\left( x^{4n} \right)}{\left(2n\right)!}")
        self.wait(2)
        self.play(TransformMatchingTex(text2, text))
        text2 = MathTex(r"\int \cos \left( x^2 \right) dx = \sum_{n=0}^{\infty} \frac{\left(-1\right)^{n}\left( x^{4n+1} \right)}{\left(2n\right)!\left(4n+1\right)}")
        self.wait(2)
        self.play(TransformMatchingTex(text, text2))
        text = MathTex(r"\int \cos \left( x^2 \right) dx = C+ \sum_{n=0}^{\infty} \frac{\left(-1\right)^{n}\left( x^{4n+1} \right)}{\left(2n\right)!\left(4n+1\right)}")
        self.wait(4)
        self.play(TransformMatchingTex(text2, text))

        self.play(FadeOut(VGroup(text, dg)))

        dg = VGroup()
        text = VGroup(Tex("How to do it:"), Tex("Find the taylor series of the function."),MathTex(r"\text{Replace all instances of }x\text{ with the }x^n."), MathTex(r"\text{Add one to the power of }x"), MathTex(r"\text{divide the taylor series by the new power. i.e.} \frac{x^{n+1}}{n+1}")).arrange(DOWN)
        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text))

        text = MathTex(r"\text{Try to solve for } \int \sin \left( x^4 \right) dx \text{ now. Pause the video.}").to_edge(DOWN).shift(UP/2)
        dg.add(text)
        self.play(Write(text))
        self.wait(3)
        text = MathTex(r"\int \sin \left(x^4\right) dx =\sum _{n=0}^{\infty }\frac{\left(-1\right)^n\left(x^{8n+5}\right)}{\left(2n+1\right)!\left(8n+5\right)}").to_edge(DOWN).shift(UP*1.5)
        dg.add(text)
        self.play(Write(text))
        self.play(Unwrite(VGroup(dg, chapter)))

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
        self.wait(1)


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
        self.wait(1)


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


        # Chapter 7
        # self.next_section(skip_animations=True)

        chapter = Text("7: Ratio test", font_size=50)
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
        text = Tex(r"To solve this, we need the ratio test.").shift(2*DOWN)
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
