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


### Move Method 

This method is used to move the robot around the world given ```dx``` & ```dy``` (The Displacement in x and y Directions) and make sure that the robot will not move outside the world.

```python
def move(self, dx, dy):

        x = self.x + dx + self.rand() * self.motion_noise
        y = self.y + dy + self.rand() * self.motion_noise

        if x < 0.0 or x > self.world_size or y < 0.0 or y > self.world_size:
            return False
        else:
            self.x = x
            self.y = y
            return True
```

### Sense Method 

This method is used to sense the distance between each robot location ```Xi``` at a certain time step```i``` and the locations of the ```landmarks``` with a certain noise ```self.measurement_noise``` and returns a ```measurments``` list which contains the distances between current robot location and all the landmarks in the form of  ```[idx,dx,dy]``` where idx is the n'th landmark.


```python
    # sense: returns x- and y- distances to landmarks within visibility range
    #        because not all landmarks may be in this range, the list of measurements
    #        is of variable length. Set measurement_range to -1 if you want all
    #        landmarks to be visible at all times
    #
    
    def sense(self):
        ''' This function does not take in any parameters, instead it references internal variables
            (such as self.landamrks) to measure the distance between the robot and any landmarks
            that the robot can see (that are within its measurement range).
            This function returns a list of landmark indices, and the measured distances (dx, dy)
            between the robot's position and said landmarks.
            This function should account for measurement_noise and measurement_range.
            One item in the returned list should be in the form: [landmark_index, dx, dy].
            '''
           
        measurements = []
 
        for idx in range(self.num_landmarks):
            dx = (self.landmarks[idx][0] - self.x)
            dy = (self.landmarks[idx][1] - self.y)
            
            dx , dy = dx + (self.rand() * self.measurement_noise), dy + (self.rand() * self.measurement_noise)
            
            if (abs(dx) < self.measurement_range) and (abs(dy) < self.measurement_range):
                measurements.append([idx, dx, dy])

        return measurements
```

> Code for robot class can be found in [robot_class.py](robot_class.py) file.

## Dependencies
The minimal dependencies for this project can be found in `requirements.txt`. To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`