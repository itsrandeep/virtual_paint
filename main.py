import cv2
import numpy as np

from drawing_mode import merge_image_and_canvas
from hand_tracking import HAND_LANDMARK, HandTracking
from selection_mode import place_header, select_color, BLUE

cap = cv2.VideoCapture(0)
frame_width = 1280
frame_height = 720
cap.set(3, frame_width)
cap.set(4, frame_height)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

def main():
    ''' Main driver function for virtual_paint application '''

    hand_tracking = HandTracking(min_detection_confidence=0.8)
    # Default color of sketch, which can be changed in selection mode
    color = BLUE

    canvas = np.zeros((frame_height, frame_width, 3), np.uint8)
    prvs_x, prvs_y = 0, 0 

    while True:
        success, image = cap.read()
        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        # Place header on image for color selection
        place_header(canvas)
        # Draw landmarks of detected hands in image
        # image = hand_tracking.draw_landmarks(image)
        # Get coordinates of all the 21 landmark points
        coordinates = hand_tracking.get_coordinates(image, 0)
        if coordinates:
            if (hand_tracking.is_finger_up(HAND_LANDMARK.INDEX_FINGER_TIP)
                    and hand_tracking.is_finger_up(HAND_LANDMARK.MIDDLE_FINGER_TIP)):
                # Selection mode
                prvs_x, prvs_y = 0, 0  # Need to reset prvs point in every case other than drawing mode

                idx_x, idx_y = coordinates[HAND_LANDMARK.INDEX_FINGER_TIP]
                mid_x, mid_y = coordinates[HAND_LANDMARK.MIDDLE_FINGER_TIP]
                cv2.rectangle(image, (idx_x-10, idx_y-20), (mid_x +10, mid_y+20),
                              color, 10, cv2.FILLED)
                # Select color based on index finger location
                color = select_color(idx_x, idx_y, color)

            elif hand_tracking.is_finger_up(HAND_LANDMARK.INDEX_FINGER_TIP):
                # Drawing mode
                idx_x, idx_y = coordinates[HAND_LANDMARK.INDEX_FINGER_TIP]
                cv2.circle(image, (idx_x, idx_y), 5, color, 10, cv2.FILLED)
                if prvs_x == 0 and prvs_y == 0:
                    prvs_x, prvs_y = idx_x, idx_y

                cv2.line(canvas, (prvs_x, prvs_y), (idx_x, idx_y), color, 10, cv2.FILLED)
                prvs_x, prvs_y = idx_x, idx_y

            else:
                # Need to reset prvs point in every case other than drawing mode
                prvs_x, prvs_y = 0, 0 

        # place canvas on top of video feed from camera
        image = merge_image_and_canvas(image, canvas)

        # out.write(image)
        cv2.imshow('Draw Board', image)

        if cv2.waitKey(5) & 0xff == ord('q'):
            break


    # Close the window / Release webcam
    cap.release()
    
    # After we release our webcam, we also release the output
    # out.release() 
    
    # De-allocate any associated memory usage 
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
