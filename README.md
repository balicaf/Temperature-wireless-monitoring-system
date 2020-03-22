# Temperature-wireless-monitoring-system

Hardware:
-Arduino+wifi: Lolin Nodmcu
-DS1820 DS18b20 temperature probe temperature sensor 18B20 For Arduino

https://www.instructables.com/id/IoT-Temperature-Sensor-With-ESP8266/
https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806
https://arduino.stackexchange.com/questions/45175/compilation-error-in-nodemcu-along-with-onewire-temperature-sensor-ds18b20-and

all in one
https://randomnerdtutorials.com/esp8266-ds18b20-temperature-sensor-web-server-with-arduino-ide/

this one is working better for server/web part
https://randomnerdtutorials.com/esp8266-dht11dht22-temperature-and-humidity-web-server-with-arduino-ide/

weirdly "#define ONE_WIRE_BUS 2 " is corresponds to D4 digital pin...
make sure you install the latest version of oneWire through arduino IDE.
