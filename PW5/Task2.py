class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        return ((self.second_point.x - self.first_point.x)**2 + (self.second_point.y - self.first_point.y)**2)**(1/2)


class Triangle:
    def __init__(self, first_segment, second_segment, third_segment):
        self.first_segment = first_segment
        self.second_segment = second_segment
        self.third_segment = third_segment

    def perimetr(self):
        return self.first_segment.length() + self.second_segment.length() + self.third_segment.length()


fpoint = Point(2, 4)
spoint = Point(5, 7)
tpoint = Point(7, 5)

fsegment = Segment(spoint, fpoint)
ssegment = Segment(tpoint, spoint)
tsegment = Segment(fpoint, tpoint)

triangle = Triangle(fsegment, ssegment, tsegment)

print(f"Довжина 1-го відрізка - {fsegment.length()} \n"
      f"Довжина 2-го відрізка - {ssegment.length()} \n"
      f"Довжина 3-го відрізка - {tsegment.length()} \n"
      f"Периметр трикутника - {triangle.perimetr()}")


