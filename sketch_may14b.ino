
/*
  * SN74HC165N_shift_reg
  *
  * MidiFighter mit Funk
  * Mit RGB LEDs
  * Mit Taschenlampe
  *
  * Program to shift in the bit values from a SN74HC165N 8-bit
  * parallel-in/serial-out shift register.
  *
  * This sketch demonstrates reading in 16 digital states from a
  * pair of daisy-chained SN74HC165N shift registers while using
  * only 4 digital pins on the Arduino.
  *
  * You can daisy-chain these chips by connecting the serial-out
  * (Q7 pin) on one shift register to the serial-in (Ds pin) of
  * the other.
  *
  * Of course you can daisy chain as many as you like while still
  * using only 4 Arduino pins (though you would have to process
  * them 4 at a time into separate unsigned long variables).
  *
*/

/* How many shift register chips are daisy-chained.
*/
#define NUMBER_OF_SHIFT_CHIPS   2

/* Width of data (how many ext lines).
*/
#define DATA_WIDTH   NUMBER_OF_SHIFT_CHIPS * 8
boolean bVal[DATA_WIDTH];
boolean bValOld[DATA_WIDTH];

/* Width of pulse to trigger the shift register to read and latch.
*/
#define PULSE_WIDTH_USEC   5

/* Optional delay between shift register reads.
*/
#define POLL_DELAY_MSEC   1

/* You will need to change the "int" to "long" If the
  * NUMBER_OF_SHIFT_CHIPS is higher than 2.
*/
#define BYTES_VAL_T unsigned int

int ploadPin        = 14;  // Connects to Parallel load pin the 165
//int clockEnablePin  = 7;  // Connects to Clock Enable pin the 165
int dataPin         = 10; // Connects to the Q7 pin the 165
int clockPin        = 16; // Connects to the Clock pin the 165


int encoder0PinALast = LOW;
int encoder0PinBLast = LOW;
int encoder0Pos = 0;
int encoder0PosOld = 0;

long lVal = 0;
long lValOld = -1;

void setup(){

     //Init des Arrays fuer die Buttons-States
     for(int i=0; i<DATA_WIDTH; i++){
       bVal[i]=false;
       bValOld[i]=false;
     }

     Serial1.begin(9600);
     
     /* Initialize our digital pins...
     */
     pinMode(ploadPin, OUTPUT);
     pinMode(clockPin, OUTPUT);
     pinMode(dataPin, INPUT);

    

}


//irgendetwas senden, damit das bitmuster als antwort kommt

void loop(){

  queryPins();
  if(Serial1.available()){
    char command = Serial1.read();
    if(command=='b'){
      Serial1.println(lVal);
    }else if(command=='e'){
      Serial1.println(encoder0Pos);
    }
  }
/*  
    for(int i = 0; i < DATA_WIDTH; i++)
       {
           Serial.print(bVal[i], DEC);Serial.print(' ');
       }
       Serial.print(encoder0Pos);
       Serial.println();
*/

  //---- bVal[6] und bVal[7] sind belegt von den Pins des Drehgebers
  lVal = bVal[0] + 2*bVal[1] + 4*bVal[2] + 8*bVal[3] + 16*bVal[4] + 32*bVal[5] + 64*bVal[8] + 128*bVal[9] + 256*bVal[10] + 
                 512*bVal[11] + 1024 * bVal[12] + 2048*bVal[13] + 4096*bVal[14] + 8192*bVal[15];

  if(lVal != lValOld){
    //Serial.println(lVal);
    lValOld = lVal;
  }

  //----Rotary Encoder
  if ((encoder0PinALast == LOW) && (bVal[6] == HIGH)) {
     if (bVal[7] == LOW) {
       encoder0Pos++;
     } else {
       encoder0Pos--;
     }
     //Serial.println (encoder0Pos);
   } 
   
   if ((encoder0PinALast == HIGH) && (bVal[6] == LOW)) {
     if (bVal[7] == HIGH) {
       encoder0Pos++;
     } else {
       encoder0Pos--;
     }
     //Serial.println (encoder0Pos);
   }
   
   if (encoder0Pos != encoder0PosOld){
     //Serial.println (encoder0Pos);
     encoder0PosOld = encoder0Pos;
   }
   
   encoder0PinALast = bVal[6];
  
}





/**
  * Speichert den IST-Zustand der Buttons in den Array bVal;
  */
void queryPins(){
    /* Trigger a parallel Load to latch the state of the data lines,
     */
//    digitalWrite(clockEnablePin, HIGH);
     digitalWrite(ploadPin, LOW);
     delayMicroseconds(PULSE_WIDTH_USEC);
     digitalWrite(ploadPin, HIGH);
//    digitalWrite(clockEnablePin, LOW);

     /* Loop to read each bit value from the serial out line
      * of the SN74HC165N.
     */
     for(int i = 0; i < DATA_WIDTH; i++)
     {
         bVal[i] = digitalRead(dataPin);
         /* Pulse the Clock (rising edge shifts the next bit).
         */
         digitalWrite(clockPin, HIGH);
         delayMicroseconds(PULSE_WIDTH_USEC);
         digitalWrite(clockPin, LOW);
     }
}
