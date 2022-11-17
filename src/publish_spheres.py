#!/usr/bin/env python3
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy

topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('register')

markerArray = MarkerArray()

count = 0
xpos = 0
MARKERS_MAX = 5

for i in range(MARKERS_MAX):
    marker = Marker()
    marker.id = count
    marker.lifetime = rospy.Duration()
    marker.header.frame_id = "sphere"
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.scale.x = 0.5
    marker.scale.y = 0.5
    marker.scale.z = 0.5
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = 0 + xpos
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    markerArray.markers.append(marker)
    xpos += 1
    count += 1
    publisher.publish(markerArray)
    rospy.sleep(1)