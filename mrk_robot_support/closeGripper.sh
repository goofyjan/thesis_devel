rostopic pub /gripper_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["gripper_r_finger_to_ankle"], points: [{positions: [0.0], effort:[1.0], time_from_start: [1.0, 0.0]}]}' -1
