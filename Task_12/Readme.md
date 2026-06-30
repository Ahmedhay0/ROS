<img width="493" height="529" alt="Screenshot from 2026-07-01 00-36-49" src="https://github.com/user-attachments/assets/c3d2c212-b8b8-41c0-9ae7-8036f696cb68" />
<img width="1299" height="446" alt="Screenshot from 2026-07-01 00-36-14" src="https://github.com/user-attachments/assets/36d677b7-f014-4eb5-8981-97a8a49f8c96" />
To handle the data input i made a function called method in the manager file which is used by a method in the the robot class that runs it every time a message is published in either the prioreties or the positions
topics which then checks the message type and adds it to a dictionary with the robot name and the data of the message then compares it to the other robots to check the current state
while this is suboptitmal i failed misarably when i tried to make it work through one node that subscribes and checks the data but getting the info of who actually published the data was too hard so i scrapped the idea
btw in case you didn't watch the video  added the launch file i didn't use os library to get the path so you would have to edit it manually
