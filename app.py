import streamlit as st
import cv2
from pose_detector import poseDetector
from app_helpers import process_frame 
import time


def main():
    #styles
    st.markdown("<h1 style='color: #4CAF50; text-align: center;'>Start Using PushUpPro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #FF5722; text-align: center; font-size: 20px;'>Have you ever wondered whether you did your workouts wrong? Do you want something to help workout with utmost efficiency? Then use PushUpPro to help you reach your workout goals!</p>", unsafe_allow_html=True)

    st.sidebar.title("Start Now! (Click button below)")
    use_webcam = st.sidebar.button("Push Up Counter")
    st.sidebar.subheader("How It Works")
    st.sidebar.markdown("""
    - This application uses the MediaPipe library to detect poses and analyze movements.
    - It can track key points on the body to provide feedback on your form during exercises.
    - The percentage in the middle of the screen indicates the current position in the push-up movement:
        - 0%: Indicates the starting position of the push-up, with arms fully extended.
        - 100%: Indicates the lowest point of the push-up, with elbows bent at approximately 90 degrees.
    """)

    st.sidebar.subheader("Instructions")
    st.sidebar.markdown("""
    - Follow the bar on the top. Use it to understand when to go down and when to go up during push-ups.
    - To make sure the program works effectively, please make sure you are in push-up position and the camera is an appropriate distance away.
    - You will be given 30 seconds to complete as many push-ups as you can, and based on your results, the program will provide an AI-generated plan of action that will help you further your workout goals.
    """)

    stframe = st.empty()

    if use_webcam:
        detector = poseDetector() 
        cap = cv2.VideoCapture(0)
        count = 0
        direction = 0
        formVal = 0
        pushup_count = 0

        start_time = time.time()
        while cap.isOpened():
            ret, img = cap.read()
            if not ret:
                break

            img, count, direction, formVal, pushup_count = process_frame(detector, img, count, direction, formVal, cap, pushup_count)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            stframe.image(img)

            elapsed_time = time.time() - start_time
            if elapsed_time >= 30:
                break

        cap.release()
        cv2.destroyAllWindows()
        st.write("Time's up!")
        st.write(f"Number of push-ups completed: {pushup_count}. Good Job!")


if __name__ == "__main__":
    main()
