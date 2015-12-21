def circleData(radius):
    circumference = 6.282 * radius
    area = 3.141 * (radius ** 2)
    return circumference, area

c, a = circleData(5)

print("The circumference is", c, "units")
print("The area is", a, "units")