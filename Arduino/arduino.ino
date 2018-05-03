
#include "rc.h"

#define TIME 50

void setup() 
{
  init_rc();
  Serial.begin(115200);
}

void loop() 
{
  if(Serial.available() > 0)
  {
  	int cmd = Serial.read();
    Serial.println(cmd);
  	switch(cmd)
  	{
      case 0: straight(); rest(); break;

     // single command
      case 1: forward(); delay(TIME); break;
      case 2: reverse(); delay(TIME); break;
      case 3: right(); delay(TIME); break;
      case 4: left(); delay(TIME); break;

     //combination command
      case 6: forward(); right(); delay(TIME); break;
      case 7: forward(); left(); delay(TIME); break;     
      case 8: reverse(); right(); delay(TIME); break;     
      case 9: reverse(); left(); delay(TIME); break;
      
      default: Serial.print("Invalid Command\n"); break;
  	}
  }
  else
  {
  	straight();
  	rest();
  }
}
