# RGB LED Control Server

![Alt Text](/img/demo.gif)

## Description
This is a school project demonstrating basics of REST API and web user interfaces. Project contains a simple server application that controls RGB LED and serves its functionality as a REST API. Additionaly the server also serves a simple, easy to use html interface.

## Quickstart
1. Connect your Raspberry Pi according to the following schematic:  
![Alt](/img/schematic.jpg)
2. SSH into your Raspberry Pi
```
ssh pi@<your rpi ip>
```
3. Download this repository
```
git clone https://github.com/smolagakuba/PBL3-W7.git
```
4. Enter the repository
```
cd PBL3-W7
```
5. Activate virtual enviroment
```
source venv/bin/activate
```
6. Start the server
```
python3 app.py
```
7. Open `http://<your rpi ip>:5000/` in your web browser

## Documentation
API documentation can be found at: https://smolagakuba.github.io/PBL3-W7