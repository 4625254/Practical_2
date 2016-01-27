side_1 = float(input("Enter side 1 (m): "))
side_2 = float(input("Enter side 2 (m): "))
side_3 = float(input("Enter side 3 (m): "))

triangle = [side_1,side_2,side_3]
triangle.sort()

if triangle[0] + triangle[1] > triangle[2]:
    perimeter = side_1 + side_2 + side_3
    print("Perimeter =",perimeter,"m")
else:
    print("Invalid triangle!")
