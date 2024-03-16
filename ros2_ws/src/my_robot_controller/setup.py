from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ypearson',
    maintainer_email='yvan.pearson@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'test_node = {package_name}.my_first_node:main',
            f'draw_circle = {package_name}.draw_circle:main',
            f'pose_subscriber = {package_name}.pose_subscriber:main',
            f'turtle_controller = {package_name}.turtle_controller:main',
        ],
    },
)

# executable_name = package_name.file_name.main_function