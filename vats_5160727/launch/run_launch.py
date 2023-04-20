from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
   return LaunchDescription([
       Node(
           package='vats_5160727',
           executable='motorx_controller',
       ),
       Node(
           package='vats_5160727',
           executable='motory_controller',
       ),
       Node(
           package='vats_5160727',
           executable='crane_sim_node',
       ),
   ])


