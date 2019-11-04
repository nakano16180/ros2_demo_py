from setuptools import setup

package_name = 'ros2_demo_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'py_node.demo',
        'py_node.sub',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='yourname',
    author_email='email@hoge',
    maintainer='yourname',
    maintainer_email='email@hoge',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo = py_node.demo:main',
            'sub = py_node.sub:main',
        ],
    },
)