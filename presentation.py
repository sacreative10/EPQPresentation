
from manim import *
from manim_slides import *


config.assets_dir = "assets"
config.frame_rate = 120
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080


class NumberedList():
    def __init__ (self, *items):
        self.items = items
    
    def getTexStr(self):
        texStr = r"\begin{enumerate}"
        for item in self.items:
            texStr += r"\item " + item
        texStr += r"\end{enumerate}"
        return texStr

    def getTexStr(self, num):
        texStr = r"\begin{enumerate}"
        for i in range(num):
            texStr += r"\item " + self.items[i]
        texStr += r"\end{enumerate}"
        return texStr

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
        question = Tex("What is the fundamental property of the monitor, which allows you to see what's on it?").scale(0.65)
        question.to_edge(UP)
        question.to_edge(LEFT)
        self.play(
            Write(question),
            run_time = 1.5
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
        title = Title(f"Key Lemmas")
        title.to_edge(UP)
        self.play(
            Write(title),
            run_time = 1.5
        )
        insights = r"""If no light enters the eye, no image is formed [in the retinas]\n Light rays must originate from a light source\n Light rays [entering the camera] encode information about the scene """
        
        insightList = insights.split(r"\n")
        numList = NumberedList(*insightList)
        text = Tex(numList.getTexStr(1)).scale(0.8).next_to(title, DOWN).to_edge(LEFT)

        self.play(
            Write(text),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # show the eye again
        self.play(
            Create(eye),
            run_time = 1.5
        )
        apple = SVGMobject("apple.svg").scale(0.5).move_to(RIGHT*3)

        self.play (
            Create(apple),
            run_time = 1.5
        )

        lightbulb = SVGMobject("lightbulb.svg").scale(0.5).move_to(RIGHT*3 + UP*3)
        lightbulb.rotate(PI)
        lightbulb.set_stroke(WHITE)

        self.play(
            Create(lightbulb),
            run_time = 1.5
        )
        self.next_slide()
        blist = BulletedList(
            "Why/How do you see the apple?",
            "Why is the apple red?",
        ).scale(0.8)
        blist.to_edge(UP)
        blist.to_edge(LEFT)
        self.play(
            Write(blist[0]),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            Write(blist[1]),
            run_time = 1.5
        )
        self.next_slide()
        arrow1 = Arrow(start = lightbulb.get_center(), end = apple.get_center(), buff=1)
        arrow1.set_color(WHITE)
        arrow1.stroke_width = 2
        self.play(
            GrowArrow(arrow1),
            run_time = 1
        )
        self.next_slide()
        arrow2 = Arrow(start = apple.get_center(), end = eye.get_center(), buff=1)
        arrow2.set_color(RED)
        arrow2.stroke_width = 2
        self.play(
            GrowArrow(arrow2),
            run_time = 1
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        ax = Axes(
            x_range = [-2, 2],
            y_range = [-5, 5],
            tips = False,
            x_length=0,
            y_length=0
        )
        ax.to_edge(LEFT)
        graph = ax.plot(lambda x: np.sin(10 * x))
        whiteLight = Text("White Light").scale(0.5).next_to(graph, UP)

        self.play(
            Create(graph),
            Write(whiteLight),
            run_time = 1.5
        )
        self.next_slide()
        ax2 = Axes(
            x_range = [-2, 2],
            y_range = [-5, 5],
            tips = False,
            x_length=0,
            y_length=0
        )
        ax2.to_edge(RIGHT)
        graph2 = ax2.plot(lambda x: np.sin(10 * x))
        graph2.set_color(RED)
        graph3 = ax2.plot(lambda x: np.sin(12 * x) + 2)
        graph3.set_color(GREEN)
        graph4 = ax2.plot(lambda x: np.sin(13 * x) - 2)
        graph4.set_color(BLUE)
        arrow = Arrow(start = ax.get_right(), end = ax2.get_left())
        arrow.set_color(WHITE)
        multipleFreq = Text("An Aggregate of Multiple Frequencies").scale(0.4).next_to(graph3, UP)
        self.play(
            Create(arrow),
            run_time = 1.5
        )
        self.play(
            Create(graph2),
            Create(graph3),
            Create(graph4),
            Write(multipleFreq),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            FadeOut(arrow),
            FadeOut(graph),
            FadeOut(multipleFreq)
        )
        graph2.generate_target()
        graph3.generate_target()
        graph4.generate_target()
        graph2.target.to_edge(LEFT)
        graph3.target.to_edge(LEFT)
        graph4.target.to_edge(LEFT)
        whiteLight.generate_target()
        whiteLight.target.move_to(graph3.target.get_center() + UP*1.5)

        self.play(
            MoveToTarget(whiteLight),
            MoveToTarget(graph2),
            MoveToTarget(graph3),
            MoveToTarget(graph4),
            run_time = 1
        )
        apple = SVGMobject("apple.svg").scale(0.5).move_to(LEFT*1.5)
        eye = SVGMobject("eye.svg").scale(0.5).move_to(RIGHT*5).set_stroke(WHITE)
        eye.scale([-1, 1, 1])
        self.play(
            Create(apple),
            Create(eye),
            run_time = 1.5
        )
        self.next_slide()
        graph5 = ax2.plot(lambda x: np.sin(10 * x))
        graph5.set_color(RED)
        graph5.generate_target()
        graph5.target.shift(LEFT*4)
        graph5.move_to(graph5.target)

        albedo = Text("Albedo(colour) of the surface").scale(0.5).next_to(graph5, UP*3)

        self.play(
            Create(graph5),
            Write(albedo),
            run_time = 1
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        firstItem = Tex("1. If no light enters the eye, no image is formed [in the retinas]").scale(0.8).next_to(title, DOWN).to_edge(LEFT)
        self.play(
            FadeIn(title),
            FadeIn(firstItem),
        )
        self.wait(0.5)
        secondItem = Tex("2. Light rays must originate from a light source").scale(0.8).next_to(firstItem, DOWN).to_edge(LEFT)
        self.play(
            Write(secondItem),
            run_time = 1.5
        )
        self.next_slide()
        thirdItem = Tex("3. Light rays [entering the camera] encode information about the scene").scale(0.8).next_to(secondItem, DOWN).to_edge(LEFT)
        self.play(
            Write(thirdItem),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # Create the sun as a glowing yellow circle
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=1)
        sun.set_glow(0.8)  # Adds a glow effect to the sun
        sun.move_to(ORIGIN)  # Sun at the center

        eye = SVGMobject("eye.svg").scale(0.5).move_to(RIGHT*5 + DOWN*2).set_stroke(WHITE).rotate((270 - 60)*DEGREES)

        walls = VGroup(
            Line(LEFT*3 + DOWN, RIGHT*3 + DOWN*3),
            Line(LEFT*3, LEFT*2.5 + UP*3),
            Line(RIGHT*3, RIGHT*3.5 + UP*3),
        )
        walls.set_stroke(PURPLE)
        walls.set_fill(PURPLE, opacity=0.5)
        self.play(
            Create(sun),
            Create(eye),
            Create(walls),
            run_time = 1.5
        )

        self.next_slide()
        numRays = 36
        maxRayLength = 6
        maxbounces = 3
        rays = VGroup()

        for i in range(numRays):
            angle = i * (2 * PI / numRays)
            rayDir = np.array([np.cos(angle), np.sin(angle), 0])

            ray = self.cast_bouncing_ray(sun.get_center(), rayDir, walls, maxRayLength, maxbounces)
            rays.add(ray)
        

        self.play(
            Create(rays),
            run_time = 2,
            smooth = linear
        )
        self.next_slide()
        self.play(
            rays[31].animate.set_color(RED),
            run_time = 1
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        title = Title("The Raytracing Algorithm")
        title.to_edge(UP)
        self.play(
            Write(title),
            run_time = 1
        )
        self.next_slide()
        firstItem = Tex("1. All rays will begin from the camera.").scale(0.8).next_to(title, DOWN).to_edge(LEFT)
        self.play(
            Write(firstItem),
            run_time = 1.5  
        )
        self.next_slide()
        secondItem = Tex("2. The ray will bounce around within the scene, until it hits a light source.").scale(0.8).next_to(firstItem, DOWN).to_edge(LEFT)
        self.play(
            Write(secondItem),
            run_time = 1.5
        )
        self.next_slide()
        thirdItem = Tex("3. The colour of the ray is determined by the colour of the light source and the objects hit along the way.").scale(0.8).next_to(secondItem, DOWN).to_edge(LEFT)
        self.next_slide()
        self.play(
            Write(thirdItem),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        title = Title("What I did in my EPQ")
        title.move_to(ORIGIN)
        self.play(
            Write(title),
            run_time = 1.5
        )
        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        flouresentSPD = SVGMobject("fluorescent-spd.svg").scale(2)
        graphDesc = Text("Spectral Power Distribution of a Fluorescent Light").scale(0.2).next_to(flouresentSPD, DOWN)
        xAxis = Text("Wavelength (nm)").scale(0.2).next_to(flouresentSPD, DOWN*0.5)
        yAxis = Text("Intensity").scale(0.2).next_to(flouresentSPD, LEFT*0.3).rotate(PI/2)

        SlideTitle = Text("Spectral Power Distribution")
        SlideTitle.to_edge(UP)
        self.play(
            Write(SlideTitle),
            run_time = 1
        )
        
        self.play(
            Create(flouresentSPD),
            # Write(graphDesc),
            Write(xAxis),
            Write(yAxis),
            run_time = 2
        )

        self.next_slide()
        # RGBA 
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        R = Text("R").scale(3).move_to(LEFT*6).set_color(RED)
        G = Text("G").scale(3).move_to(LEFT*2).set_color(GREEN)
        B = Text("B").scale(3).move_to(RIGHT*2).set_color(BLUE)
        A = Text("A").scale(3).move_to(RIGHT*6).set_color(WHITE)
        self.play(
            Write(R),
            Write(G),
            Write(B),
            Write(A),
            run_time = 2
        )
        ed = Text("ed").scale(1).next_to(R, RIGHT*0.5).set_color(RED)
        reen = Text("reen").scale(1).next_to(G, RIGHT*0.5).set_color(GREEN)
        lue = Text("lue").scale(1).next_to(B, RIGHT*0.5).set_color(BLUE)
        lpha = Text("lpha").scale(1).next_to(A, RIGHT*0.5).set_color(WHITE)
        self.play(
            Write(ed),
            Write(reen),
            Write(lue),
            Write(lpha),
            run_time = 1
        )

        self.next_slide()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        square = Square(side_length=2).set_fill(RED, 1)
        square.set_color(RED)  # Set initial color to red
        square.move_to(UP * 2)  # Move square upwards
        self.play(Create(square), run_time = 1)

        # Create ValueTrackers for RGB components
        red_tracker = ValueTracker(1)  # Red starts at 1 (full red)
        green_tracker = ValueTracker(0)  # Green starts at 0 (no green)
        blue_tracker = ValueTracker(0)  # Blue starts at 0 (no blue)

        # Define sliders for RGB values
        red_slider = self.create_slider(color=RED, tracker=red_tracker, position=DOWN * 1, name="RED")
        green_slider = self.create_slider(color=GREEN, tracker=green_tracker, position=DOWN * 2, name="GREEN")
        blue_slider = self.create_slider(color=BLUE, tracker=blue_tracker, position=DOWN * 3, name="BLUE")

        # Add sliders to the scene
        self.play(
            Create(red_slider), Create(green_slider), Create(blue_slider), run_time = 1)

        # Define the update function for the square's color
        def update_square_color(square):
            red_value = float(red_tracker.get_value())
            green_value = float(green_tracker.get_value())
            blue_value = float(blue_tracker.get_value())
            square.set_color(ManimColor([red_value, green_value, blue_value]))
            square.set_fill(ManimColor([red_value, green_value, blue_value]))

        # Add updater to change color dynamically
        square.add_updater(update_square_color)

        # Animate the RGB sliders and their corresponding color change
        self.play(LaggedStart(
            red_tracker.animate.set_value(0),  # Fade out red
            green_tracker.animate.set_value(1),  # Fade in green
            blue_tracker.animate.set_value(1),  # Fade in blue
            run_time = 5,
            lag_ratio = 0.1
        )
        )
        self.play(LaggedStart(
            red_tracker.animate.set_value(1),  # Fade out red
            green_tracker.animate.set_value(0.5),  # Fade in green
            blue_tracker.animate.set_value(0.7),  # Fade in blue
            run_time = 5,
            lag_ratio = 0.1
        )
        )
        



    def create_slider(self, color, tracker, position, name=None):
        """Create a horizontal slider for RGB value."""
        # Base line for the slider
        line = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4)
        line.set_width(4)  # Set width of the slider

        # Indicator for the slider (the dot)
        dot = Dot(color=color)
        dot.scale(1.2)
        dot.add_updater(lambda m: m.move_to(line.point_from_proportion(tracker.get_value())))

        # Group slider components (line and dot)
        slider = VGroup(line, dot)
        slider.move_to(position)  # Position the slider

        # Label for the slider color
        label = Text(f"{name.capitalize()}", font_size=24).next_to(slider, LEFT)

        return VGroup(slider, label)

    def cast_bouncing_ray(self, origin, direction, walls, max_length, bounces_left):
        """ Cast a ray that can bounce off walls. """
        ray_segments = VGroup()  # To hold multiple segments if there are bounces
        current_origin = origin
        current_direction = direction

        for _ in range(bounces_left + 1):  # Includes the initial ray and any bounces
            # Cast a single ray and find the nearest wall intersection
            end_point, wall = self.cast_ray(current_origin, current_direction, walls, max_length)

            if end_point is None:
                # No intersection, so extend ray to max length
                end_point = current_origin + current_direction * max_length

            # Add the ray segment
            ray_segment = Line(current_origin, end_point, color=YELLOW)
            ray_segments.add(ray_segment)

            if wall is None:
                # If no wall was hit, stop casting
                break

            # Calculate the reflection direction
            wall_normal = self.get_wall_normal(wall)
            current_direction = self.reflect(current_direction, wall_normal)

            # Move origin to the intersection point for the next bounce
            current_origin = end_point

        return ray_segments

    def cast_ray(self, origin, direction, walls, max_length):
        """ Cast a single ray and return the closest intersection point and the wall hit. """
        closest_intersection = None
        closest_dist = max_length
        hit_wall = None

        for wall in walls:
            intersection = self.line_intersection(origin, direction, wall)

            if intersection is not None:
                # Compute the distance to the intersection point
                dist = np.linalg.norm(intersection - origin)

                if dist < closest_dist:
                    closest_intersection = intersection
                    closest_dist = dist
                    hit_wall = wall

        return closest_intersection, hit_wall

    def line_intersection(self, ray_origin, ray_dir, wall):
        """ Check for intersection between a ray and a wall segment. """
        x1, y1 = wall.get_start()[:2]
        x2, y2 = wall.get_end()[:2]
        x3, y3 = ray_origin[:2]
        x4, y4 = ray_origin[:2] + ray_dir[:2]

        # Line-line intersection formula
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None  # Parallel lines

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

        if 0 <= t <= 1 and u >= 0:
            # Calculate intersection point
            intersection_x = x1 + t * (x2 - x1)
            intersection_y = y1 + t * (y2 - y1)
            return np.array([intersection_x, intersection_y, 0])

        return None  # No intersection

    def get_wall_normal(self, wall):
        """ Compute the normal vector for the given wall segment. """
        start = wall.get_start()[:2]
        end = wall.get_end()[:2]
        wall_dir = end - start
        # Normal is perpendicular to wall direction
        normal = np.array([-wall_dir[1], wall_dir[0]])
        return normal / np.linalg.norm(normal)

    def reflect(self, ray_dir, wall_normal):
        """ Reflect the ray direction based on the wall normal. """
        # Use only the x, y components for the reflection in 2D
        ray_dir_2d = ray_dir[:2]  # Extract x and y components
        wall_normal_2d = wall_normal[:2]  # Make sure wall_normal is 2D

        # Perform the reflection in 2D
        reflected_2d = ray_dir_2d - 2 * np.dot(ray_dir_2d, wall_normal_2d) * wall_normal_2d

        # Return the reflected vector in 3D (keeping z=0)
        return np.array([reflected_2d[0], reflected_2d[1], 0])


        





        


