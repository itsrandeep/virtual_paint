import cv2


def merge_image_and_canvas(image, canvas):
    ''' Return the image after merging it with input canvas. Canvas contains the lines drawn
    by user'''

    # Convert canvas to grayscale binary to create a mask on original image
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inverse_gray_canvas = cv2.threshold(gray_canvas, 50, 255, cv2.THRESH_BINARY_INV)
    bgr_inverse_canvas = cv2.cvtColor(inverse_gray_canvas, cv2.COLOR_GRAY2BGR)

    # Merge original image and canvas 
    image = cv2.bitwise_and(image, bgr_inverse_canvas)
    image = cv2.bitwise_or(image, canvas)

    return image