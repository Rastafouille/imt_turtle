#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from imt_turtle.srv import Setcolor

def turtleTurn():
    rospy.init_node('turtleturn')
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, poseCallback)
    rate = rospy.Rate(1) #hz

# modification lecture et affichage d'un paramètre
    rospy.set_param("/turtle/background_r", 200)
    r=rospy.get_param("/turtle/background_r", 0)
    print ("nouveau fond r=",r)
    
# appel de service
    clear= rospy.ServiceProxy("/clear",Empty)
    clear()    
    
    
    rospy.Service("/Setcolor",Setcolor,set_color_cb)
    rospy.wait_for_service("/Setcolor")
    
    
    while not rospy.is_shutdown():
        message = Twist()
        message.linear.x=random.uniform(0, 1)
        message.linear.y=0
        message.linear.z=0
        message.angular.x=0
        message.angular.y=0
        message.angular.z=random.uniform(-1, 1)
        print ("turning ",message.angular.z)
        pub.publish(message)
        rospy.sleep(2) # ou rate,sleep()

def poseCallback(data):
	print ("turtle position ",data.theta)

def set_color_cb(req):
    rospy.set_param("/turtle/background_r", req.r)	
    rospy.set_param("/turtle/background_g", req.g)	
    rospy.set_param("/turtle/background_b", req.b)	
    clear= rospy.ServiceProxy("/clear",Empty)
    clear()  
    return []
#imt_turtle.srv.SetcolorResponse()
    

if __name__ == '__main__':
	try:
		turtleTurn() #our main function
	except rospy.ROSInterruptException:
		print ("interrupted !")
