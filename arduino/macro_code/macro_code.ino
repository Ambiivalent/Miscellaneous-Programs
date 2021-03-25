#include "Keyboard.h"
#include <Keypad.h>
#include <Mouse.h>
#include <Encoder.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN A2
#define NUMPIXELS 13

const int modeButton = A0; // Mode hard-wired to A0

const byte rows = 3;
const byte cols = 4;
char lastKey; 
boolean heldKey = false;

Encoder RotaryEncoder(10,16);

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
boolean updateColour = false;
const int brightness = 2;

char keys[rows][cols] = { {'1','2','3','4'}, {'5','6','7','8'}, {'9','0','A','B'} };

int currentMode = 0; // Counter for current mode
int buttonState = 0; // Current state of button
int lastButtonState = 0; // Last state of button to compare

long pos_encoder = -999;

byte rowPins[rows] = {4, 5, A3 };  
byte colPins[cols] = {6, 7, 8, 9 };
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, rows, cols );

void checkModeButton()
{
  buttonState = digitalRead(modeButton);
  if (buttonState != lastButtonState)
  {
    if (buttonState == LOW){ currentMode++; updateColour = false; } // <-- Means button is released and mode needs to change
    delay(50);
  }
  lastButtonState = buttonState;
  if (currentMode > 3) { currentMode = 0;}
}

void setup()
{
  pinMode(modeButton, INPUT_PULLUP);
  Serial.begin(9600);
  Keyboard.begin();
  pixels.begin();
}

void loop()
{
  char key = keypad.getKey();
  checkModeButton();
  switch(currentMode)
  {
    case 0:
    // MODE ZERO == BASE FUNCTION KEYS + ROTARY ENCODER LEFT + RIGHT
      encoder0();    // RUN ENCODER MODE FOR CASE 0
      setColorsMode0(); // RUN COLOR MODE FOR CASE 0
      if (key)
      {
        switch(key){
          case '1':
          Keyboard.press(KEY_ESC);
          break;
          case '2':
          Keyboard.press(KEY_F1);
          break;
          case '3':
          Keyboard.press(KEY_F2);
          break;
          case '4':
          Keyboard.press(KEY_F3);
          break;
          case '5':
          Keyboard.press(KEY_F4);
          break;
          case '6':
          Keyboard.press(KEY_F5);
          break;
          case '7':
          Keyboard.press(KEY_F6);
          break;
          case '8':
          Keyboard.press(KEY_F7);
          break;  
          case '9':
          Keyboard.press(KEY_F8);
          break;
          case '0':
          Keyboard.press(KEY_F9);
          break;
          case 'A':
          Keyboard.press(KEY_F10);
          break;
          case 'B':
          Keyboard.press(KEY_F11);
          break;
      }
      delay(100); Keyboard.releaseAll();
      }break;
      
      //case 1:
  }
  
}
void encoder0()
{
   long newPos = RotaryEncoder.read()/2; //When the encoder lands on a valley, this is an increment of 4.

  if (newPos != pos_encoder && newPos > pos_encoder) {
    pos_encoder = newPos;
    Keyboard.press(KEY_LEFT_ARROW);
    Keyboard.release(KEY_LEFT_ARROW);                      }

  if (newPos != pos_encoder && newPos < pos_encoder) {
    pos_encoder = newPos;
    Keyboard.press(KEY_RIGHT_ARROW);
    Keyboard.release(KEY_RIGHT_ARROW);                      }
}
void setColorsMode0()
{
  if (!updateColour)
  {
      pixels.setPixelColor(0, pixels.Color(127,0,255));     
      pixels.setPixelColor(1, pixels.Color(127,0,255));     
      pixels.setPixelColor(2, pixels.Color(127,0,255));     
      pixels.setPixelColor(3, pixels.Color(127,0,255));     
      pixels.setPixelColor(4,pixels.Color(127,0,255));     
      pixels.setPixelColor(5, pixels.Color(127,0,255));     
      pixels.setPixelColor(6, pixels.Color(127,0,255));     
      pixels.setPixelColor(7, pixels.Color(127,0,255));     
      pixels.setPixelColor(8, pixels.Color(127,0,255));     
      pixels.setPixelColor(9, pixels.Color(127,0,255));     
      pixels.setPixelColor(10,pixels.Color(127,0,255));     
      pixels.setPixelColor(11, pixels.Color(127,0,255));     
      pixels.setPixelColor(12, pixels.Color(127,0,255));     
      pixels.show();
      updateColour = true;    
  }
}
