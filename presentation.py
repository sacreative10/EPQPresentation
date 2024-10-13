
from manim import *
from manim_slides import *


config.assets_dir = "assets"

class Presentation(Slide, ThreeDScene):
    def construct(self):

        image = ImageMobject("Chess1920x1080.png")

        # Slide 1 show image
        self.play(
            FadeIn(image, run_time = 3),
        )
        self.next_slide()

        # Show EPQ Title
        text = "Raytracing"
        title = Text(text).scale(1.5)

        self.play(
            Write(title),
            FadeOut(image),
            run_time = 3
            )

        self.next_slide()
        self.play(
            title.animate.to_edge(UP),
            run_time = 2
        )
        # 3 arrows pointing to the left of the screen 
        # Second arrow points to the center of the screen
        # Third arrow points to the right of the screen
        self.next_slide()
        arrow1 = Arrow(start = title.get_bottom(), end = LEFT*4)
        arrow2 = Arrow(start = title.get_bottom(), end = ORIGIN)
        arrow3 = Arrow(start = title.get_bottom(), end = RIGHT*4)

        simpleModelText = Text("A simple model of light").scale(0.5).next_to(arrow1, DOWN + LEFT*0.5)
        self.play(
            GrowArrow(arrow1),
            Write(simpleModelText),
            run_time = 2
        )
        self.next_slide()
        TechnicalExplanationsText = Text("What I did in my EPQ").scale(0.5).next_to(arrow2, DOWN*1.5)
        self.play(
            GrowArrow(arrow2),
            Write(TechnicalExplanationsText),
            run_time = 2
        )
        self.next_slide()
        RayTracingText = Text("Evaluations").scale(0.5).next_to(arrow3, DOWN + RIGHT*0.5)
        self.play(
            GrowArrow(arrow3),
            Write(RayTracingText),
            run_time = 2
        )
        self.next_slide()
        # clear screen
        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(simpleModelText),
            FadeOut(TechnicalExplanationsText),
            FadeOut(RayTracingText),
            FadeOut(title),
            run_time = 0.5
        )
        self.next_slide()

        # line on the right vertical
        line = Line(RIGHT* 3 + UP*3, RIGHT*3 + DOWN*3)
        line.set_stroke([BLUE, RED, GREEN])
        screenText = Text("Screen").scale(0.5).next_to(line, UP)

        # show eye on the right
        eye = SVGMobject("eye.svg").scale(0.5).move_to(LEFT*5)
        eye.set_stroke(WHITE)
        eyeText = Text("Eye").scale(0.5).next_to(eye, DOWN)
        self.play(
            Write(line),
            Create(eye),
            run_time = 2
        )
        self.play(
            Write(screenText),
            Write(eyeText),
            run_time = 1
        )

        self.next_slide()
        arrow1 = Arrow(start = line.get_start(), end = eye.get_center() + RIGHT*0.5)
        arrow1.set_color(GREEN)
        arrow1.stroke_width = 2
        arrow2 = Arrow(start = line.get_center(), end = eye.get_center() + RIGHT*0.5)
        arrow2.set_color(RED)
        arrow2.stroke_width = 2
        arrow3 = Arrow(start = line.get_end(), end = eye.get_center() + RIGHT*0.5)
        arrow3.set_color(BLUE)
        arrow3.stroke_width = 2

        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            run_time = 1
        )

        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # Key Takeaway number 1
        title = Title(f"Key Takeaways")
        title.to_edge(UP)
        self.play(
            Write(title),
            run_time = 1.5
        )
        d = r'\begin{enumerate} \item If no light enters the eye, no image is formed [in the retinas] \end{enumerate}'
        text = Tex(d)
        text.next_to(title, DOWN)
        self.play(
            Write(text),
            run_time = 1.5
        )



        


