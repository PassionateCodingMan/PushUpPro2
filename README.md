# PushUpPro2
## Inspiration
My primary inspiration was to innovate physical health in people worldwide, especially in areas where the importance of physical health is not explicitly ensured and for people who cannot access the gym, whether it is due to locational or financial issues.
My secondary inspiration for creating the program was to motivate myself to work harder on my physical health. I knew that continuously testing the program to see whether it would increase the amount of push-ups I do, and I wondered whether I could increase the amount of proper form push-ups I do every day using the app. 

## What it does
It is a web app that tracks the user's joints when they are at an appropriate distance away from their camera, guides the user through their push-ups by informing them when to go down and up, checks the push-up form of the user, and adds one to the counter every time they do a properly formed push-up.

## How we built it
Built the program through Python and used the Streamlit library for a seamless UI. Used OpenCV to capture video frames that could be analyzed on the webcam. Integrated Mediapipe by using the framework to track critical points on the body (Joints) and analyze user movements. The program can detect whether the user form is correct and provides real-time feedback. It has a 30-second timer and a counter at the end to finally display how many correct push-ups the user did.

## Challenges we ran into
Significant issues include navigating Mediapipe and integrating it into the program, using streamlit as the front end because it was challenging to learn and display the video using the library, and user positioning (the program will only detect joints from a specific camera placement), logic in form detection and appropriate sizing and color scheme for the remark section in the program.

## Accomplishments that we're proud of
It is successfully integrating streamlit, media pipe, and OpenCV into the web app to provide a clean, simple, fully functional, and navigable app and UI. The actual idea and the level of impact it can have on the user.

## What we learned
I learned how to use Streamlit to create simple web apps for Python code, the importance of navigability in UI, an understanding of OpenCV, and pose estimation of media pipe.

## What's next for PushUpPro
AI will give the user feedback based on how many push-ups they do and how often they were instructed to fix their form. Using similar logic to help with other exercises that do not require equipment, such as squats, planks, sit-ups, etc.



