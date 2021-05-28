import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
draw_util = mp.solutions.drawing_utils
HAND_LANDMARK = mp_hands.HandLandmark


class HandTracking():

    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) -> None:

        self.hands = mp_hands.Hands(static_image_mode, max_num_hands, min_detection_confidence, min_tracking_confidence)

    def draw_landmarks(self, image):
        ''' Draw the hand landmarks on image and returns new image'''
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_util.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        return image

    def get_coordinates(self, image, hand_id=0):
        ''' Return list of all the 21 landmarks of hand of input hand_id'''
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)
        h, w, _ = image.shape
        self.coordinates = []

        if results.multi_hand_landmarks:
            selected_hand = results.multi_hand_landmarks[hand_id]
            landmarks =  selected_hand.landmark
    
            for landmark in landmarks:
                x, y = int(landmark.x * w), int(landmark.y * h)
                self. coordinates.append([x, y])

        return self.coordinates

    def is_finger_up(self, finger_tip_id):
        ''' Returns true if input finger_tip_id is up and False if finger is down(clenched in fist)'''
        _, finger_tip_y = self.coordinates[finger_tip_id]
        _, finger_pip_y = self.coordinates[finger_tip_id - 2] # finger pip is a joint below the tip of the finger
        if finger_tip_y < finger_pip_y:
            return True
        else:
            return False
