/*Arduino script to stablish a serial connection*/

#include "DHT.h"              // DHT sensor library
#define DHTPIN 22             // Arduino port connected to DHT signal output
#define DHTTYPE DHT11         // Type of sensor (could be DHT22)
DHT dht(DHTPIN, DHTTYPE);     // define it as object

const int cooler = 12;        // Output port for led
const int led    = 13;        // Output port for led

const int analogTemp = A0;      // Analog input Temperature Sensor
const int photoRes   = A2;      // Analog input for Photo Resistance
const int flameDet   = A4;      // Analog input for flame detector

int value;
unsigned int dato;              // Variable to store data received from python script

void setup() {
  Serial.begin(9600);           // Baudrate of the serial connection
  pinMode(led, OUTPUT);
  pinMode(cooler, OUTPUT);      // Set led ports as outputs
  pinMode(analogTemp, INPUT);    
  pinMode(photoRes, INPUT);     
  pinMode(flameDet, INPUT);
  dht.begin();
}

void loop() {
  while (Serial.available() > 0) { // while to test if the serial communication is available
    dato = Serial.read();       // read the serial port.

    /*Logic based on the data received*/
    //Turn on/off leds
    if (dato == 'Y')digitalWrite(led, HIGH);
    if (dato == 'N')digitalWrite(led, LOW);
    if (dato == 'P')digitalWrite(cooler, HIGH);
    if (dato == 'A')digitalWrite(cooler, LOW);
    // Send PhotoResistance data.
    if (dato == 'L') {
      value = analogRead(photoRes);
      Serial.println(value);
    }
    // Send temperature.
    if (dato == 'T') {
      float t = dht.readTemperature();
      Serial.println(t);
    }
    // Send Humidity
    if (dato == 'H') {
      float h = dht.readHumidity();
      Serial.println(h);
    }
    // Send Flame data.
    if (dato == 'F') {
      value = analogRead(flameDet);
      int range = map(value, 0, 1024, 0, 3);
       switch (range) {
       case 0:    // A close fire.
        Serial.println("** Fuego cercano **");
        break;
       case 1:    // A distant fire.
        Serial.println("** Fuego lejano **");
        break;
       case 2:    // No fire detected.
        Serial.println("Todo tranqui");
        break;
      }
    }
    // Sent analog temperature
    if (dato == 'U') {
      value = analogRead(analogTemp);
      Serial.println(value);
    }
  }

}
