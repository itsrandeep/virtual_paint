<h3 align="center">Virtual Paint</h3>

  <p align="center">
    A Python application that uses hands detection and movement to do painting on live camera stream.
    <br />
  </p>
</p>


## About The Project

Virtual paint can be used to paint in real time with hands detection, It can be useful in drawing basic paintings or in online meetings when trying to explain something.


## Demo

   ![demo](https://user-images.githubusercontent.com/15001968/122640216-e1599a00-d11b-11eb-9055-8bf886192894.gif)



## Getting Started

This project is built on Python 3.8.5 mainly using OpenCV and mediapipe.

### Prerequisites

I would recommend to create a new virtual environment as it's always a good practice to use seperate environements for separate projects and not mix up diffrent libraries with diffrent versions. I have used virtualenv for that purpose.

  ```sh
  pip3 install virtualenv
  python3 -m virtualenv <ENVIRONMENT_NAME>
  source <ENVIRONMENT_NAME>/bin/activate
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/itsrandeep/virtual_paint.git
   ```
2. Install Required Libraries
   ```sh
   pip install -r requirements.txt
   ```
3. Start the Python app
   ```sh
   python main.py
   ```


## Usage

There are two modes in this application

1) Selection Mode - When two fingers(Index and middle) are up, It will show a rectangle to show that application is in selction mode and nothing will be drawn.
2) Drawing Mode - When only Index finger is up, then application is in drawing mode and moving your finger will draw a line on Screen.

press q to exit.


## Roadmap

It is currently only a basic app. I'm planning to add many features to make it more usable.

* Enabling/Disabling showing of hand landmarks points.
* Instead of drawing with a single color, give multiple options of colors on frame. (Done)
* Colors can be switched in selection mode. (Done)
* Option of saving the entire video of drawing session.
* Option of saving only Drawing in diffrent image formats.
* Currently it supports only 1 hand, Add 2 hands support.
* Integration in meeting apps like zoom.


## Acknowledgements
* [Python OpenCV Library](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
* [Google's Mediapipe for Hand Detection](https://google.github.io/mediapipe)

