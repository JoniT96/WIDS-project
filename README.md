# WIDS-project
This repository is for my thesis project WIDS

The main purpose of this project is to figure out how unknown wireless devices can be monitored and tracked with radio signals sent by the device. Similar systems can be found on the market, but this project was done using my own knowledge and open-source software.

The project includes a prototype of the intrusion detection system of wireless devices, which is running independently collecting data from unknown devices and coarsely locating them.

Necessary data can be collected from the devices, such as MAC address, timestamps, RSSI, BSSID and ESSID information.

Description of the system:

Data collection has been implemented with Raspberry Pi hardware and WLAN adapters.
The adapters listen to channels in the 2.4GHz and 5GHz ranges in monitor mode.
The collection uses the Airodump-ng program of the Aircrack-ng software package, which collects 802.11 data.
With the help of a Python script, the data is parsed from the .csv file into .json format, and it is sent forward to the server using netcat from each Raspberry Pi device.

Location tracking:

Based on the RSSI values between base stations and the device.
Base stations create a perimeter based on RSSI values, and based on devices that can hear more than -75 dB, the area where the device is located is painted.
-6dB = the distance is doubled
-3dB = wall in between
Requires at least 3 hearing base stations.
A calculation formula has been planned for this, but the premises of the test environment have proven to be difficult.
The positioning of the devices works roughly, but in the conditions of the test environment, radio heat mapping would achieve more accurate results.
Works best in open spaces.


