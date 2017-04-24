int pwm1 = 9;
int m1 = 8;       //right motors
int pwm2 = 10;
int m2 = 11;      // left motors
char buf;
void setup(){
Serial.begin(9600);
pinMode(pwm1,OUTPUT);
pinMode(m1,OUTPUT);
pinMode(pwm2,OUTPUT);
pinMode(m2,OUTPUT);
}

void loop()
{
  buf = Serial.read();
   switch(buf){
  case'a':digitalWrite(m1,HIGH);            //reverse
          analogWrite(pwm1,100);
          digitalWrite(m2,HIGH);
          analogWrite(pwm2,100); 
           break;
  case'b': digitalWrite(m1,LOW);         //s1 forward
           analogWrite(pwm1,50);
           digitalWrite(m2,LOW);
           analogWrite(pwm2,50);         
           break;
  case'c': digitalWrite(m1,LOW);             //s2 forward
           analogWrite(pwm1,100);
           digitalWrite(m2,LOW);
           analogWrite(pwm2,100);
           break;
  case'd': digitalWrite(m1,LOW);            //s3 forward
           analogWrite(pwm1,158);
           digitalWrite(m2,LOW);
           analogWrite(pwm2,158);
           break;
  case'e': digitalWrite(m1,LOW);         //s4 forward
           analogWrite(pwm1,200);
           digitalWrite(m2,LOW);
           analogWrite(pwm2,200);
           break;
  case'f': digitalWrite(m1,LOW);         //s5 forward
           analogWrite(pwm1,255);
           digitalWrite(m2,LOW);
           analogWrite(pwm2,255);
           break;
  case'g': digitalWrite(m1,LOW);         //stop
           analogWrite(pwm1,0); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,0);
           break;
  case'h': digitalWrite(m1,LOW);         //s1 forward a1 right
           analogWrite(pwm1,34); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,50);
           break;
  case'i': digitalWrite(m1,LOW);         //s1 forward a2 right
           analogWrite(pwm1,17); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,50);
           break;
  case'j': digitalWrite(m1,LOW);         //s1 forward a3 right
           analogWrite(pwm1,0); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,50);
           break;
  case'k': digitalWrite(m1,LOW);        // s1 forward a1 left 
           analogWrite(pwm1,50); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,34);
           break;
  case'l': digitalWrite(m1,LOW);         //s1 forward a2 left
           analogWrite(pwm1,50); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,17);
           break;
   case'm': digitalWrite(m1,LOW);         //s1 forward a3 left
           analogWrite(pwm1,50); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,0);
           break;
   case'n': digitalWrite(m1,LOW);         //s2 forward a1 right
           analogWrite(pwm1,85); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,100);
           break;
  case'o': digitalWrite(m1,LOW);         //s2 forward a2 right
           analogWrite(pwm1,68); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,100);
           break;
  case'p': digitalWrite(m1,LOW);         //s2 forward a3 right
           analogWrite(pwm1,51); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,100);
           break;
  case'q': digitalWrite(m1,LOW);        // s2 forward a1 left 
           analogWrite(pwm1,100); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,85);
           break;
  case'r': digitalWrite(m1,LOW);         //s2 forward a2 left
           analogWrite(pwm1,100); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,68);
           break;
   case's': digitalWrite(m1,LOW);         //s2 forward a3 left
           analogWrite(pwm1,100); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,51);
           break;
   case't': digitalWrite(m1,LOW);         //s3 forward a1 right
           analogWrite(pwm1,136); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,158);
           break;
  case'u': digitalWrite(m1,LOW);         //s3 forward a2 right
           analogWrite(pwm1,119); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,158);
           break;
  case'v': digitalWrite(m1,LOW);         //s3 forward a3 right
           analogWrite(pwm1,102); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,158);
           break;
  case'w': digitalWrite(m1,LOW);        // s3 forward a1 left 
           analogWrite(pwm1,158); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,136);
           break;
  case'x': digitalWrite(m1,LOW);         //s3 forward a2 left
           analogWrite(pwm1,158); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,119);
           break;
   case'y': digitalWrite(m1,LOW);         //s3 forward a3 left
           analogWrite(pwm1,158); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,102);
           break;
   case'z': digitalWrite(m1,LOW);         //s4 forward a1 right
           analogWrite(pwm1,187); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,200);
           break;
  case'A': digitalWrite(m1,LOW);         //s4 forward a2 right
           analogWrite(pwm1,170); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,200);
           break;
  case'B': digitalWrite(m1,LOW);         //s4 forward a3 right
           analogWrite(pwm1,153); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,200);
           break;
  case'C': digitalWrite(m1,LOW);        // s4 forward a1 left 
           analogWrite(pwm1,200); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,187);
           break;
  case'D': digitalWrite(m1,LOW);         //s4 forward a2 left
           analogWrite(pwm1,200); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,170);
           break;
   case'E': digitalWrite(m1,LOW);        //s4 forward a3 left
           analogWrite(pwm1,200); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,153);
           break;
   case'F': digitalWrite(m1,LOW);         //s5 forward a1 right
           analogWrite(pwm1,238); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,255);
           break;
  case'G': digitalWrite(m1,LOW);         //s5 forward a2 right
           analogWrite(pwm1,221); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,255);
           break;
  case'H': digitalWrite(m1,LOW);         //s5 forward a3 right
           analogWrite(pwm1,204); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,255);
           break;
  case'I': digitalWrite(m1,LOW);        // s5 forward a1 left 
           analogWrite(pwm1,255); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,238);
           break;
  case'J': digitalWrite(m1,LOW);         //s5 forward a2 left
           analogWrite(pwm1,255); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,221);
           break;
   case'K': digitalWrite(m1,LOW);         //s5 forward a3 left
           analogWrite(pwm1,255); 
           digitalWrite(m2,LOW);
           analogWrite(pwm2,204);
           break;        
   }
}   
