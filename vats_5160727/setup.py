import os
from glob import glob
from setuptools import setup

package_name = 'vats_5160727'
lib = 'vats_5160727/lib'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, lib],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "resource"), glob("resource/*.png")),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py"))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='simone',
    maintainer_email='simone.maccio@edu.unige.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'crane_sim_node = vats_5160727.crane_sim_node:main',
            'motorx_controller = vats_5160727.motorx_controller:main', 
            'motory_controller = vats_5160727.motory_controller:main', 
            'robot_logic = vats_5160727.crane_sim_node:main' 
        ],
    },
)
