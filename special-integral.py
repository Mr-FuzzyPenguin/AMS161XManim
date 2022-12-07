from manim import *
"""
manim specialint.py specialint; ffplay /home/penguin/Desktop/Code/manim-showcase/ams/media/videos/specialint/1080p60/specialint.mp4 2>/dev/null >/dev/null
"""
class specialint(Scene):
    def construct(self):

        # CHAPTER 3
        self.next_section()
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
