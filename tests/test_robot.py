from datalayer import Robot, CleaningRobot
import unittest


class MockRobot(Robot):

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append("fetching " + tool)

    def move_forward(self, tool):
        self.tasks.append("move forward")

    def move_backward(self, tool):
        self.tasks.append("move backward")

    def replace(self, tool):
        self.tasks.append("replacing")


class MockedCleaningRobot(CleaningRobot, MockRobot):
    """
   This is just a demonstration
   """
    pass


class TestCleaningRobot(unittest.TestCase):

    def test_clean(self):
        t = MockedCleaningRobot()
        t.clean("broom")
        expected = (["fetching broom"] +
                    ["move forward", "move backward"] * 10 +
                    ["replacing"])
        self.assertEqual(t.tasks, expected)

# order first goes to CleaningRObot and before going to Robot checks MockRobot