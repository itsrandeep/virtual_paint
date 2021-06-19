import cv2

# Coords are set as cv2.rectangle function expects i.e upper left, bottom right
BLUE_RECTANGLE_COORDS = [(300, 50), (450, 150)]
GREEN_RECTANGLE_COORDS = [(500, 50), (650, 150)]
RED_RECTANGLE_COORDS = [(700, 50), (850, 150)]
YELLOW_RECTANGLE_COORDS = [(900, 50), (1050, 150)]

# BGR Color Values
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)


def place_header(image):
    ''' Place header on image with diffrent colors to be selected in
    selection mode '''

    # Blue Rectangle
    cv2.rectangle(image, BLUE_RECTANGLE_COORDS[0], BLUE_RECTANGLE_COORDS[1], BLUE, 10, cv2.FILLED)
    # Green Rectangle
    cv2.rectangle(image, GREEN_RECTANGLE_COORDS[0], GREEN_RECTANGLE_COORDS[1], GREEN, 10, cv2.FILLED)
    # Red Rectangle
    cv2.rectangle(image, RED_RECTANGLE_COORDS[0], RED_RECTANGLE_COORDS[1], RED, 10, cv2.FILLED)
    # Yellow Rectangle
    cv2.rectangle(image, YELLOW_RECTANGLE_COORDS[0], YELLOW_RECTANGLE_COORDS[1], YELLOW, 10, cv2.FILLED)
    # Eraser
    # cv2.putText(image, "Eraser", (1000, 200), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0), 1, cv2.FILLED)


def select_color(idx_x, idx_y, color):
    ''' Change color according to position of index finger in selection mode'''

    # If y is in below range, then index finger is in color selection header
    if idx_y in range(50, 150):
        if idx_x in range(BLUE_RECTANGLE_COORDS[0][0], BLUE_RECTANGLE_COORDS[1][0]):
            return BLUE
        elif idx_x in range(GREEN_RECTANGLE_COORDS[0][0], GREEN_RECTANGLE_COORDS[1][0]):
            return GREEN
        elif idx_x in range(RED_RECTANGLE_COORDS[0][0], RED_RECTANGLE_COORDS[1][0]):
            return RED
        elif idx_x in range(YELLOW_RECTANGLE_COORDS[0][0], YELLOW_RECTANGLE_COORDS[1][0]):
            return YELLOW

    # return same color if finger is not in selection area
    return color