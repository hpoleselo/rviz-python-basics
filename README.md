# RViz Python Basic Examples

Repository to provide out-of-the-box examples to work with RViz and Python.

## Installation

Clone this repository to your catkin workspace:

` $ git clone git@github.com:hpoleselo/rviz-python-basics.git`

Make it:

` $ catkin_make `

Make sure the recent-downloaded package is available in your local:

` $ rospack find rviz_with_python`

Make sure the Python script is executable:

` $ roscd rviz_with_python/src `

` $ chmod +x publish_spheres.py`

## Procedure to Run Simple Sphere Publisher

A launch file will be written to avoid following all those steps to reproduce the functionality, anyways following these steps are useful to understand what's going on under the hood:

1. Run ROS:

`$ roscore`

2. Create a transform `/tf` tree by publishing a static transformation between two frames that will start to exist from the moment we publish them:

` $ rosrun tf static_transform_publisher 0 0 0 0 0 0 1 map sphere 10 `

Basically we're saying the map frame is on the same XYZ and orientation as the sphere frame.

3. Run RViz:

` $ rosrun rviz rviz`

4. On RViz, make sure to click on `Add` -> `Marker` -> `Ok`:

![rviz-options](https://user-images.githubusercontent.com/24254286/202325675-5461fab0-956f-4799-b501-6b7b65ce45bb.jpg)

5. Run the sphere publisher script (file has to be executable):
   
` $ rosrun rviz_with_python publish_spheres.py`

Could be done without being in the package and by running Python directly:

` $ python3 sphere_publisher.py`

We should get the following result:

![photo_2022-11-16_21-37-07](https://user-images.githubusercontent.com/24254286/202325403-bb097f7e-a04d-4e2c-9d43-cc16d0429ede.jpg)

## Easier Way of Running the Sphere Publisher (TODO)

Although the launch file is already created, I must get somethings right:

` $ roslaunch rviz_with_python sphere_publisher.launch`