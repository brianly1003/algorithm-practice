# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2/problem

# TODO: Approach 1: We loop through the obstacles given and keep track of the closest one to our queen in each of the 8 directions, 
# then we calculate the distance from our queen to each of the closest obstacles and return their sum.
# [O(k) & O(1)] - k is number of the obstacles


def queenAttack(n, k, r_q, c_q, obstacles) -> int:
    totalCount = 0

    # Right
    rRObstacle, cRObstacle = -1, -1
    # Bottom
    rBObstacle, cBObstacle = -1, -1
    # Left
    rLObstacle, cLObstacle = -1, -1
    # Top
    rTObstacle, cTObstacle = -1, -1
    # Bottom Left
    rBLObstacle, cBLObstacle = -1, -1
    # Bottom Right
    rBRObstacle, cBRObstacle = -1, -1
    # Top Left
    rTLObstacle, cTLObstacle = -1, -1
    # Top Right
    rTRObstacle, cTRObstacle = -1, -1

    for row in range(len(obstacles)):
        rObstacle = obstacles[row][0]
        cObstacle = obstacles[row][1]

        # Right
        if (cObstacle < cRObstacle or rRObstacle == -1) and cObstacle > c_q and rObstacle == r_q:
            rRObstacle = rObstacle
            cRObstacle = cObstacle
        # Bottom
        if (rObstacle < rBObstacle or rBObstacle == -1) and rObstacle < r_q and cObstacle == c_q:
            rBObstacle = rObstacle
            cBObstacle = cObstacle
        # Left
        if (cObstacle > cLObstacle or cLObstacle == -1) and cObstacle < c_q and rObstacle == r_q:
            rLObstacle = rObstacle
            cLObstacle = cObstacle
        # Top
        if (rObstacle < rTObstacle or rTObstacle == -1) and rObstacle > r_q and cObstacle == c_q:
            rTObstacle = rObstacle
            cTObstacle = cObstacle
        # Bottom Left
        if ((rObstacle > rBLObstacle and cObstacle > cBLObstacle) or rBLObstacle == -1)\
                and rObstacle < r_q and cObstacle < c_q\
                and r_q - rObstacle == c_q - cObstacle:
            rBLObstacle = rObstacle
            cBLObstacle = cObstacle
        # Bottom Right
        if ((rObstacle > rBRObstacle and cObstacle < cBRObstacle) or rBRObstacle == -1)\
                and rObstacle < r_q and cObstacle > c_q\
                and r_q - rObstacle == cObstacle - c_q:
            rBRObstacle = rObstacle
            cBRObstacle = cObstacle
        # Top Left
        if ((rObstacle < rTLObstacle and cObstacle > cTLObstacle) or rTLObstacle == -1)\
                and rObstacle > r_q and cObstacle < c_q\
                and rObstacle - r_q == c_q - cObstacle:
            rTLObstacle = rObstacle
            cTLObstacle = cObstacle
        # Top Right
        if ((rObstacle < rTRObstacle and cObstacle < cTRObstacle) or rTRObstacle == -1)\
                and rObstacle > r_q and cObstacle > c_q\
                and rObstacle - r_q == cObstacle - c_q:
            rTRObstacle = rObstacle
            cTRObstacle = cObstacle

    # Right
    totalCount += cRObstacle - c_q - 1 if cRObstacle != -1 else n - c_q
    # Bottom
    totalCount += r_q - rBObstacle - 1 if rBObstacle != -1 else r_q - 1
    # Left
    totalCount += c_q - cLObstacle - 1 if cLObstacle != -1 else c_q - 1
    # Top
    totalCount += rTObstacle - r_q - 1 if rTObstacle != -1 else n - r_q
    # Bottom Left
    totalCount += c_q - cBLObstacle - 1 if rBLObstacle != -1 else min(c_q - 1, r_q - 1)
    # Bottom Right
    totalCount += cBRObstacle - c_q - 1 if cBRObstacle != -1 else min(n - c_q, r_q - 1)
    # Top Left
    totalCount += c_q - cTLObstacle - 1 if cTLObstacle != -1 else min (c_q - 1, n - r_q)
    # Top Right
    totalCount += rTRObstacle - r_q - 1 if rTRObstacle != -1 else min(n - c_q, n - r_q)

    return totalCount


if __name__ == "__main__":
    # n = 5   # Size of the matrix
    # k = 3   # Number of obstacles
    # r_q, c_q = 4, 3  # Geolocation of Queen
    # obstacles = [
    #     [2, 3],
    #     [4, 2],
    #     [5, 5]
    # ]

    # Sample Input:
    # 4 0
    # 4 4
    n = 4   # Size of the matrix
    k = 0   # Number of obstacles
    r_q, c_q = 4, 4  # Geolocation of Queen
    obstacles = []

    result = queenAttack(n, k, r_q, c_q, obstacles)
    print(result)
