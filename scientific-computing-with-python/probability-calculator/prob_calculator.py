"""
@name: probability_calculator.py
@date: 07/11/2023 (dd/mm/yy)
@author: github.com/chrvstian
"""

import random


class Hat:
    def __init__(self, **balls) -> None:
        """
        Initializes a Hat object with specified quantities of different colored balls.

        Args:
            **balls: Variable keyword arguments specifying the quantity of each colored ball.
        """
        self.contents = [
            color for color, quantity in balls.items() for _ in range(quantity)
        ]

    def draw(self, num_balls: int) -> list:
        """
        Simulates drawing a specified number of balls from the hat without replacement.

        Args:
            num_balls (int): The number of balls to draw.

        Returns:
            list: A list of strings representing the drawn balls.
        """
        drawn_balls = random.sample(
            self.contents, min(num_balls, len(self.contents))
        )

        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(
        hat: tuple,
        expected_balls: dict,
        num_balls_drawn: int,
        num_experiments: int
    ) -> float:
    """
    Conducts a series of experiments with a Hat object to estimate the probability
    of drawing a specified set of balls.

    Args:
        hat (tuple): An instance of the Hat class representing the collection of balls.
        expected_balls (dict): A dictionary specifying the expected quantities of each color of ball.
        num_balls_drawn (int): The number of balls to draw in each experiment.
        num_experiments (int): The total number of experiments to perform.

    Returns:
        float: The estimated probability of successfully drawing the expected set of balls.
    """
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat()
        hat_copy.contents = hat.contents.copy()

        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_counts = {
            color: drawn_balls.count(color) for color in set(drawn_balls)
        }

        success = all(
            drawn_counts.get(color, 0) >= expected_balls.get(color, 0) 
            for color in expected_balls
        )

        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
