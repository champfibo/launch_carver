import os
from glob import glob
from setuptools import setup

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share',package_name), glob('launch/*launch.py')),
        (os.path.join('share',package_name), glob('urdf/*')),
        (os.path.join('share',package_name), glob('meshes/*')),
         # Path to the world file
        (os.path.join('share', package_name), glob('.world/*')),
        (os.path.join('share',package_name), glob('meshes2/*')),



    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='patcharapon',
    maintainer_email='patcharapon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [


            "led_panel =py_pkg.led_panel:main",
            "battery =py_pkg.battery:main",
            "turtlesim_control =py_pkg.turtlesim_control:main",
            "number_publisher=py_pkg.number_publisher:main",
            'spawn_carver = py_pkg.spawn_carver:main'

        ],
    },
)
