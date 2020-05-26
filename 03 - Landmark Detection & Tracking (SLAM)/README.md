# Landmark Detection & Robot Tracking (SLAM)Landmark Detection & Robot Tracking (SLAM)

## Overview
![Robot Location and Probability Distribution](https://video.udacity-data.com/topher/2018/May/5b073c5a_prob-dists/prob-dists.png)

In this project, I implemented SLAM (Simultaneous Localization and Mapping) for a 2 dimensional world! I combined what I knew about robot sensor measurements and movement to create a map of an environment from only sensor and motion data gathered by a robot, over time. SLAM gives a way to track the location of a robot in the world in real-time and identify the locations of landmarks such as buildings, trees, rocks, and other world features. This is an active area of research in the fields of robotics and autonomous systems.

## Description 

**Simultaneous Localization and Mapping** (SLAM) is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.

Statistical techniques used to approximate the above equations include ```Kalman filters``` and particle filters (aka. Monte Carlo methods). They provide an estimation of the posterior probability function for the pose of the robot and for the parameters of the map. 

![Sense and Motion Cycle](https://i.ibb.co/5W4tW3P/sense-move.png) 

Below is an example of a 2D robot world with landmarks (purple x's) and the robot (a red 'o') located and found using *only* sensor and motion data collected by that robot. This is just one example for a 50x50 grid world; in your work you will likely generate a variety of these maps.

![foo](images/robot_world.png)

## Robot Class Methods 

###### There're two important methods in ```Robot``` class which are ```sense``` and ```move``` methods.
