from manim import *
import numpy as np

class BasicRaycaster(Scene):
    def construct(self):
        # Define player position
        player_pos = np.array([0, 0, 0])
        player_dot = Dot(point=player_pos, color=YELLOW)

        # Define walls as line segments
        walls = [
            Line(start=[-4, -2, 0], end=[4, -2, 0], color=WHITE),  # Bottom Wall
            Line(start=[-4, -2, 0], end=[-4, 2, 0], color=WHITE),  # Left Wall
            Line(start=[4, -2, 0], end=[4, 2, 0], color=WHITE),    # Right Wall
            Line(start=[-4, 2, 0], end=[4, 2, 0], color=WHITE),    # Top Wall
        ]

        # Add walls and player
        self.add(player_dot)
        for wall in walls:
            self.add(wall)

        # Cast rays from player in different directions
        num_rays = 90
        max_ray_length = 6

        for i in range(num_rays):
            # Angle of the ray in radians
            angle = i * (2 * PI / num_rays)

            # Compute ray direction
            ray_dir = np.array([np.cos(angle), np.sin(angle), 0])

            # Create the ray
            ray = self.cast_ray(player_pos, ray_dir, walls, max_ray_length)
            self.add(ray)

        # Animation to visualize the raycasting
        self.wait(2)

    def cast_ray(self, origin, direction, walls, max_length):
        # Create a temporary long ray
        end_point = origin + direction * max_length
        ray = Line(origin, end_point, color=BLUE)

        # Find the closest intersection with the walls
        closest_intersection = None
        closest_dist = max_length

        for wall in walls:
            intersection = self.line_intersection(origin, direction, wall)

            if intersection is not None:
                # Compute the distance to the intersection point
                dist = np.linalg.norm(intersection - origin)

                if dist < closest_dist:
                    closest_intersection = intersection
                    closest_dist = dist

        if closest_intersection is not None:
            # Update ray to stop at the closest intersection
            ray.put_start_and_end_on(origin, closest_intersection)

        return ray

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
