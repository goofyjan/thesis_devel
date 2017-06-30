rostopic pub /gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["l_finger_joint","r_finger_joint"], points: [{positions: [0.09,0.09], time_from_start: [1.0, 0.0]}]}' -1
