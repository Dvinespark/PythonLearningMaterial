class Robot:
    """
        Robot's basic function
    """
    def fetch(self, tool):
        print("fetching " + tool)

    def move_forward(self, tool):
        print("move forward")

    def move_backward(self, tool):
        print("move backward")

    def replace(self, tool):
        print("replacing")


class CleaningRobot(Robot):

    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


if __name__ == "__main__":
    t = CleaningRobot()
    t.clean('broom', 10)