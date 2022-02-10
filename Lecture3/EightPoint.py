class CheckEightPoint:
    """
    Give 8 point, then you check if:
    8 point make from 3 horizontal line, 3 vertical line
    8 point make the rectangle and not contain center point.
    INPUT:
    8 point (x,y)
    OUTPUT:
    respectable or ugly
    O TIME: 1
    O SPACE: 1
    """
    def process(self, points):
        list_x, list_y = [],[]
        for point in points:
            x,y = point
            if x not in list_x:
                list_x.append(x)
            if y not in list_y:
                list_y.append(y)

        if len(list_x) != 3 or len(list_y) != 3:
            return False
        list_x = sorted(list_x)
        list_y = sorted(list_y)

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    if (list_x[i],list_y[j]) in points:
                        return False
                elif (list_x[i],list_y[j]) not in points:
                    return False

        return True


if __name__ == "__main__":
    checkPointObj = CheckEightPoint()

    points = []
    for i in range(8):
        points.append(tuple([int(j) for j in input().split()]))
    res = checkPointObj.process(points)
    if res:
        print("respectable")
    else:
        print("ugly")