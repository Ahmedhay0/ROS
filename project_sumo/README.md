Robot Documentation
===================

1. Robot Design Overview
------------------------
A combat differential-drive robot built with a low-profile aluminum chassis for high stability and impact resistance. It features two central drive wheels, two passive casters, dual front ramps, and two vertical aluminum support structures holding a central high-speed vertical spinner weapon.

2. Attack and Defense Mechanism
-------------------------------
* Attack Mechanism: 
  Powered by a central high-RPM vertical spinner. Motor power transfers via two steel pulleys connected by a torque belt, which acts as a shock buffer during high-energy impacts. The dual front ramps lift opposing robots slightly off the ground, feeding them directly into the path of the spinner to deliver a flipping strike.

* Defense Mechanism: 
  Frontal defense relies entirely on the dual sloped front ramps. These angled ramps absorb head-on dynamic impacts, deflect opponent weapons, and prevent enemy robots from getting underneath the chassis. Additionally, the low-profile aluminum frame keeps the center of gravity low to maintain stability during engagements.

3. Camera Position & Protection
--------------------------------
The vision camera is mounted front-center, elevated between the two vertical aluminum structures, and tilted downwards at a 10° angle relative to the horizontal plane.
* Placement: Provides an unobstructed forward field of view above the spinner for target tracking, with the 10° tilt optimized to track approaching ground-level opponents accurately.
* Protection: The dual vertical side structures fully enclose the camera, protecting the lens and electronic module from direct impacts and flying debris.
<img width="1062" height="822" alt="a" src="https://github.com/user-attachments/assets/ef668a2d-5575-45aa-aa83-5dedb9da5f04" />
<img width="1041" height="777" alt="aa" src="https://github.com/user-attachments/assets/a75eebdf-834c-4283-9a43-8ea3c2059a66" />
<img width="1277" height="807" alt="aaa" src="https://github.com/user-attachments/assets/fd54be4b-06f2-4f47-b3c6-2e2a9d74bc85" />

Robot Dimensions
===================
1. Chassis
   - Length: 0.305 m
   - Width: 0.430 m
   - Height: 0.105 m

2. Left & Right Wheels
   - Radius: 0.06 
   - Diameter: 0.12 m
   - Width: 0.04 m

3. Left & Right Castor Wheels
   - Length: 0.06 m
   - Width: 0.06 m
   - Height: 0.06 m

4. Shield Link
   - Length: 0.4 m
   - Width: 0.1 m
   - Height: 0.28 m

5. Weapon
   - Length: 0.25 m
   - Width: 0.035 m
   - Height: 0.08 m

6. Left & Right Ramps
   - Length: 0.164 m
   - Width: 0.165 m
   - Height: 0.005 m

Properties of mass
===================
1. Chassis
   - Mass = 7.47 kilograms
   - X = -0.03
   - Y = 0.05
   - Z = 0.00
2. Camera Stand
   - Mass = 1.78  kilograms
   - Center of mass in meters:
   - X = 0.01
   - Y = 0.13
   - Z = 0.00
3. Wheels
   - Mass = 0.07 kilograms
   - Center of mass in meters:
   - X = -0.03
   - Y = 0.01
   - Z = 0.01
4. Sliders
   - Mass = 7.47 kilograms
   - Center of mass in meters:
   - X = -0.03
   - Y = 0.05
   - Z = 0.00

Ground Clearance 0.037 meter
==============================

Wheel separation 0.331 meter
==============================

Required dependencies
==============================
- Ros2 jazzy
- Gazebo Harmonic

Important Topics
==============================
- /camera/image_raw (camera topic displayed in rviz)
- tf
- /scan
- /odom

Important TF frames
==============================
- base_link
- shield (camera stand)

Movement Test
==============================
ros2 run teleop_twist_keyboard teleop_twist_keyboard

Installation
==============================
mkdir -p ros2_ws/src
cd ros2_ws/src
git clone 
cd ..
colcon build --packages-select sumo_bot --symlink-install








