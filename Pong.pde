//Ball Variable Declaration 
float ballXpos = 400, ballYpos = 300, ballRadius = 20;
float ballXVelocity = moveBall_horizontally(), ballYVelocity = moveBall_vertically();
//Paddle Variable Declaration 
float rightPaddleXPos = 979, rightPaddleYPos = 250, rightPaddleWidth = 20, rightPaddleHeight = 100;
float leftPaddleXPos = 0, leftPaddleYPos = 250, leftPaddleWidth = 20, leftPaddleHeight = 100;
//Borders
float topBorder = 40, bottomBorder = 560;
//Interface variables
boolean reset, move = false, p1Scored, p2Scored, start = false;
int p1Score = 0, p2Score = 0;

void setup(){
  size(1000,600);  
  ballXpos = width/2;
  ballYpos = height/2;
  ballRadius = 20;
  ballXVelocity = moveBall_horizontally();
  ballYVelocity = moveBall_vertically();
  rightPaddleXPos = 979; 
  rightPaddleYPos = 250;
  leftPaddleXPos = 0; 
  leftPaddleYPos = 250;
  p1Score = 0;
  p2Score = 0;
  
  
  move=false;
}

void draw(){
  startMenu();
  if (start){
     draw_pong(); 
  }
  

   
}
void mousePressed(){
    start = true;
}
void startMenu(){
   background(0,0,255);
  fill(255,0,0);
  rect(width/2-200,height/2-50,400,100);
   fill(0);
  text(" WELCOME TO PONG ", width/2-200, height/2-60);
  text(" PLAY ", width/2-68, height/2+10);
  textSize(40);
}

void draw_pong(){
   background(0);
  display();
  leftPaddle();
  rightPaddle();
  createBall();
  if(move){
     moveBall(); 
  }
  reset();
  borders();
  
  //score configurations 
  if (ballXpos  == 0){
      p2Score += 1; 
  }
  else if(ballXpos == width){
    p1Score += 1;
 }
}

//User interface (text, score and borders)
void display(){
  int fontSize = 16;
  textSize(fontSize);
  fill(255,0,0);
  text("Player 1: " + p1Score, 10, 35);
  fill(0,0,255);
  text("Player 2: " + p2Score, 900, 580);
  //Border line top and bottom 
  stroke(0,255,0);
  line(0, topBorder, width, topBorder);
  line(0, bottomBorder, width, bottomBorder);

}
//Obects on the screen
void leftPaddle(){
   fill(255,0,0);
   stroke(255);
   rect(leftPaddleXPos, leftPaddleYPos, leftPaddleWidth, rightPaddleHeight);
   
   if((ballXpos - ballRadius == leftPaddleWidth) && (ballYpos - ballRadius >= (leftPaddleYPos) && ballYpos - ballRadius <= (leftPaddleYPos + leftPaddleHeight))){
       ballXVelocity *= -1;
     }
} 
void rightPaddle(){
   fill(0,0,255);
   rect(rightPaddleXPos, rightPaddleYPos, rightPaddleWidth, rightPaddleHeight);
      
   if((ballXpos + ballRadius == width - rightPaddleWidth) && (ballYpos - ballRadius >= (rightPaddleYPos) && ballYpos - ballRadius <= (rightPaddleYPos + rightPaddleHeight))){
     ballXVelocity *= -1;
   }
   
}

void createBall(){
  fill(0,255,0);
  circle(ballXpos, ballYpos, ballRadius); 
}
void keyPressed(){
  //Moving the paddles with the keys 
    if(keyPressed && key == 'w'){
      //move left paddle up with W
      leftPaddleYPos = movePaddle(leftPaddleYPos, true); 
    }
    if(keyPressed && key == 's'){
      leftPaddleYPos = movePaddle(leftPaddleYPos, false); 
    }
    if(keyPressed && key == 'i'){
      rightPaddleYPos = movePaddle(rightPaddleYPos, true);
    }
    if(keyPressed && key == 'k'){
      rightPaddleYPos = movePaddle(rightPaddleYPos, false);
    }
    if(keyPressed && key == 't'){
       move = true; 
    }
    if(keyPressed && key == 'n'){
       reset = true;
    }
    if (keyPressed && key == 'c'){
        newRound();
    }

}

void newRound(){
  rightPaddleXPos = 979; 
  rightPaddleYPos = 250;
  leftPaddleXPos = 0; 
  leftPaddleYPos = 250;  
  ballXpos = width/2;
  ballYpos = height/2;
}

float moveBall_vertically(){
   float yvel = random(-1, 1);
   if(yvel > -1 && yvel < 0){
     yvel = -5;
   }else if(yvel >= 0 && yvel < 1){
      yvel = 5; 
   }
   return yvel;
}
float moveBall_horizontally(){
   float xvel = random(-1, 1);
   if(xvel > -1 && xvel < 0){
     xvel = -5;
   }else if(xvel >= 0 && xvel < 1){
      xvel = 5; 
   }
   return xvel;
}
void moveBall(){
   ballYpos += ballYVelocity;
   ballXpos += ballXVelocity;
}

float movePaddle(float yPos, boolean up){
  if (up == true){
     if (yPos > topBorder){
       return yPos - 60;
     }else{
       return topBorder;  
     }
  }else{
      if (yPos < bottomBorder - 100){
       return yPos + 60;
     }else{
       return bottomBorder - 100; 
     }
  }
}
void reset(){
   if(reset){
      setup();
      reset = false;
   }
}
void borders(){
   if(ballYpos > bottomBorder - ballRadius || ballYpos < topBorder + ballRadius){
      ballYVelocity *= -1; 
   }
}
