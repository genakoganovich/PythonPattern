class LeverArmX:
    def __init__(self, x):
        self.x = x

    def pull(self):
        self.x -= 1 if self.x >= 0 else -0
        print(f"Подтянули ковш до: {self.x}")

    def distanse(self):
        self.x += 1 if self.x <= 100 else +0
        print(f"Отдалили ковш до: {self.x}")


class LiftingGearY:
    def __init__(self, y):
        self.y = y

    def rise(self):
        self.y += 1 if self.y <= 100 else +0
        print(f"Подняли ковш до: {self.y}")

    def down(self):
        self.y -= 1 if self.y >= 0 else -0
        print(f"Опустили ковш до: {self.y}")


class RotaryDeviceR:
    def __init__(self, r):
        self.r = r

    def rotate(self):
        self.r = (self.r + 10) % 360
        print(f"Повернули ковш до: {self.r}")


class Obstacle:
    def __init__(self, x, y, r, d):
        self.x = x
        self.y = y
        self.r = r
        self.d = d

    def check_conflict(self, excavator):
        if (self.r < excavator.r < self.r + self.d) \
                and (self.y < excavator.y < self.y + self.d) \
                and (self.x < excavator.x < self.x + self.d):
            print("Вы наткнулись на препятствие")
            return True
        return False


class Excavator(LeverArmX, LiftingGearY, RotaryDeviceR):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class Mover(Excavator):
    def __init__(self, x, y):
        super().__init__(0, 0, 0)
        for _ in range(x):
            self.distanse()
        for _ in range(y):
            self.rise()


x, y = map(int, input().split())
print(x + y)
