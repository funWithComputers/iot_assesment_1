#define LEDPIN 11

void setup() {
        // Setup serial for monitor and Setup Serial1 for BlueTooth
        Serial.begin(9600); //baud rate The baud rate signifies the data rate in bits per second. 
        //The default baud rate in Arduino is 9600 bps (bits per second). 
        //We can specify other baud rates as well, such as 4800, 14400, 38400, 28800, etc.
        Serial1.begin(9600);
        Serial.println("starting communication : ");
        pinMode(LEDPIN, OUTPUT);
}

void loop() {
// Process commands from bluetooth first.
        if(Serial1.available() > 0){
                String str = Serial1.readString();
                str = str.substring(2,str.length()-1);
                Serial.println(str);
                if(str == "LED_ON"){
                        digitalWrite(LEDPIN, HIGH);
                        Serial.println("LED ON");
                } else if(str == "LED_OFF"){
                        digitalWrite(LEDPIN, LOW);
                        Serial.println("LED OFF");
                }
        }
        if(Serial.available() > 0) {
            Serial1.write(Serial.read());
        }
}