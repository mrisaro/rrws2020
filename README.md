weather_station is a collaboration between PhD Daniela B. Risaro and PhD Matias A. Risaro

10/04/2020.

A first stage of the project is to test a few sensors with the Arduino Mega Board. In order to do the implementation we perform an arduino script (arduino_sensors.ino) and different communication scripts in python (python_scripts folder)

----Arduino Sketch----
The arduino script is very simple. Based on the data received through serial port the Arduino ask to the corresponding sensor. If the character "T" is sent, it will measure the temperature with the DHT11 sensor. So far with other characters.

----Python Scripts----

serial_data.py

plot_data.py

bot_


----Install Fritzing----
source : https://forum.fritzing.org/t/fixing-fritzing-on-ubuntu-18-04/6504

List of commands for Ubuntu 18.04

sudo apt update

sudo apt install fritzing

cd /usr/share/fritzing/

sudo git clone https://github.com/fritzing/fritzing-parts.git

sudo mv fritzing-parts/ parts

type "Fritzing" in terminal
