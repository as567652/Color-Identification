# Colour Identification Of An Image Using OpenCV
OpenCV program to determine whether color of a car in provided image is Red, Green, Blue or White.

## Table of contents
* [Introduction](#introduction)
* [Approach](#approach)
* [Technologies](#technologies)
* [Setup](#setup)
* [Launch](#launch)
* [Illustrations](#illustrations)
* [Status](#status)
* [Sources](#sources)
* [Other](#other)

## Introduction
OpenCV is simple and effective way to solve **Real Life Problems** faced by people in different sectors.<br/><br/>**This project is helpful in solving Problem Statements like -**<br/>
One automobile manufacturer is automating the placement of certain components on the bumpers of a limited-edition line of sports cars. The components are color coordinated, so the robots need to know the color of each car in order to select the appropriate bumper component. Models come in only four colors: blue, green, red, and white. 

## Approach
- HSV (Hue, Saturation, Value) is one of the scheme that describe the way colors combine to create the spectrum we see.
- We first generate HSV Values of respective colors using **cvtColor()** function in OpenCV.
- We then declare lower and upper bound to create mask such that hsv values between this range will be considered as white and out of this range will be considered as black.
- For Better result, image is cropped in such a way that centre of image is in focus.
- After successful creation of mask for all colors, we count number of white pixels in each masks and store them in a dictionary.
- We sort the dictionary and print the value corresponding to maxinmum white pixels in given mask.
- Hence, we are able to find color of given car / object from provided image.

## Technologies
  #### Software Used :
  * VS Code : 1.58.2
  #### Languages Used :
  * Python 3
  #### OS used :
  * Ubuntu 20.04.3 LTS 64-bit


## Setup
First you must have these libraries and languages installed on your system -
  * [Python 3](https://www.python.org/)
  * [OpenCV](https://opencv.org/)


## Launch
To run the code, run this commands in terminal with main.py as in current directory and images in Images folder along with main.py
```
$ python3 main.py
```
Windows will pop-up with resultant images. (Press **esc** to view next image).

## Illustrations
### Blue Car
<p align="center">
  <img src="ReadMe Images/Blue Car/Original Image.png" width=48% title="Original Image">
  <img src="ReadMe Images/Blue Car/Blue Mask.png" width=48% title="Blue Mask Of Original Image">
</p>
<p align="center">
  <img src="ReadMe Images/Blue Car/Red Mask.png" width=32% title="Red Mask Of Original Image">
  <img src="ReadMe Images/Blue Car/Green Mask.png" width=32% title="Blue Mask Of Original Image">
  <img src="ReadMe Images/Blue Car/White Mask.png" width=32% title="Blue Mask Of Original Image">
</p>
<p align="center">
   <img src="ReadMe Images/Blue Car/result.png" width=96% title="Output">
</p>

### White Car
<p align="center">
  <img src="ReadMe Images/White Car/Original Image.png" width=48% title="Original Image">
  <img src="ReadMe Images/White Car/White Mask.png" width=48% title="Blue Mask Of Original Image">
</p>
<p align="center">
  <img src="ReadMe Images/White Car/Red Mask.png" width=32% title="Red Mask Of Original Image">
  <img src="ReadMe Images/White Car/Green Mask.png" width=32% title="Blue Mask Of Original Image">
  <img src="ReadMe Images/White Car/Blue Mask.png" width=32% title="Blue Mask Of Original Image">
</p>
<p align="center">
   <img src="ReadMe Images/White Car/result.png" width=96% title="Output">
</p>

## Project status
  ***Completed***

## Sources
  * Images used in this project may be subject to copyright.
  * [Digital Image Processing (Third Edition) by Rafael C. Gonzalez and Richard E. Woods](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/013168728X)
  * [OpenCV Documentation](https://docs.opencv.org/2.4/opencv_tutorials.pdf)
  
## Other
  This code was contributed by Abhinav Sharma.
