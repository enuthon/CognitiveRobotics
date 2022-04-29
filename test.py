from Functions_and_Declarations import *
import pickle

with open('cozmo_commands.pkl', 'rb') as f:
    model = pickle.load(f)


cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
 
    while cap.isOpened():
        
        # read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)


        # Draw landmarks
        draw_styled_landmarks(image, results)

        # Prediction logic
        
        keypoints = extract_keypoints(results)
        print(keypoints)
        #X = pd.DataFrame([keypoints])
        command = model.predict([keypoints])[0]
        command_prob = model.predict_proba([keypoints])[0]
        print(command, ',   ', command_prob)

        cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, command, (3,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # show to screen
        cv2.imshow('OpenCV Feed', image)
        
        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
      
cap.release()
cv2.destroyAllWindows()