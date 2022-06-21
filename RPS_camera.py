from enum import IntEnum
import random
import cv2
from keras.models import load_model
import numpy as np
import time

class items(IntEnum):
        Rock =  0
        Paper = 1
        Scissors = 2
        Nothing = 3
        

class VisualRps():    

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.computer_score = 0
        self.user_score = 0
        self.rounds = 0
        
        

    # audio intro into the game with instruction to click
    def introduction(self):
       self.name = input("pls your name: ")
        
    
    # left click to begin and move along in the game
    def left_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            time.time()

                    

    # to get user choice
    def get_prediction(self):
        prediction = self.model.predict(self.data)
        choice = np.argmax(prediction[0])
        print(choice)
        self.user_choice = items(choice)
        print(self.user_choice)
        return self.user_choice
        
        

    
        

    # get computer choice and choice name
    def get_comp_choice(self):
        
        self.pick = random.randint(0, len(items) - 1)
        self.comp_choice = items(self.pick)
        print(self.comp_choice)
        return self.comp_choice
    
    # get winner
    def get_winnner(self, comp_choice, user_choice):
  
        if comp_choice == user_choice:
            self.rounds += 1
            self.winner = "it's a tie!"
        
        elif user_choice == items.Rock and comp_choice == items.Scissors:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
            
        elif user_choice == items.Rock and comp_choice == items.Paper:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1

        elif user_choice == items.Paper and comp_choice == items.Rock:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
            
        elif user_choice == items.Paper and comp_choice == items.Scissors:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1
        elif user_choice == items.Scissors and comp_choice == items.Paper:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
        elif user_choice == items.Scissors and comp_choice == items.Rock:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1
        else:
            
            self.winner = "NO WINNER!!"
            print(self.winner)
            print("play again")
            return(self.winner)
        
        

    def open(self):
        global frame
        #displays instruction for starting a round & stopping the game
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = self.cap.read()
        if frame is None:
            print('No image')
        else: 
            frame = frame[32:, 188:]
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
     # records box
        cv2.rectangle(frame, (10,10), (600, 50), (255,255,0), -1)
        message = "Stage: " + str(self.rounds) + " "  + "Scores " + str(self.name) + ":" + str(self.user_score) + " CPU:" + str(self.computer_score)
        cv2.putText(frame, message, (20,40), 1, 2, (0,0,0))

        # cv2.putText(frame, 'Hold s to start countdown', (0, 100), font, 2, (118, 237, 250), 2, cv2.LINE_AA)
        # cv2.putText(frame, 'Hold q to stop game', (800, 700), font, 2, (78, 99, 235), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
    def display(self):
        self.open()
       

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f" {self.name}'s  Move: {self.user_choice}",
                    (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f" Computer's Move: {self.comp_choice}",
                    (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.putText(frame, f" Winner: {self.winner}",
                    (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)
        
        

       
    
    def end_game(self):
    
        self.cap.release()
        # Destroy all the windows
        if self.computer_score == 3 or self.user_score == 3:
            print(f'Game over we have a winner')
        else:
            print(f'You left game before the outcome was determined')
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)



def play():

    game = VisualRps()
    game.introduction()
    
    while True:
        timer = 5
        #opens camera
        game.open()
         # left click mouse to start game
        if cv2.waitKey(80) & 0xFF == ord('s'):
            prev_time = time.time()
            
            while timer > 0:
                game.open()
                cv2.putText(frame, str(timer), (190,420), 2, 3, (0,0,0))
                cv2.imshow('frame', frame)
                cv2.waitKey(1)
  
                #countdown
                curr_time = time.time()
                if curr_time - prev_time >= 1:
                    prev_time = curr_time
                    timer = timer - 1
            else:
                game.open()
                game.get_prediction()
                user_choice = game.get_prediction()
                comp_choice = game.get_comp_choice()
                game.get_winnner(comp_choice, user_choice)

                for i in range(10):
                    game.display()
                
                
                
           


                # pick over all winner
                if game.computer_score == 3:
                    print("winner is cpu")
                    game.end_game()
                    game.open()

                    cv2.rectangle(frame, (50,80), (402, 160), (180,170,50), -1)
                    cv2.putText(frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                    cv2.putText(frame, "CPU" + " wins!", (110,150), 3, 1, (0,0,0))
                    cv2.imshow('frame', frame)
                    cv2.waitKey(30)

                elif game.user_score == 3:
                    print(f" winner is {game.name}")
                    game.end_game()
                    game.open()

                    cv2.rectangle(frame, (50,80), (402, 160), (180,170,50), -1)
                    cv2.putText(frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                    cv2.putText(frame, game.name + " wins!", (110,150), 3, 1, (0,0,0))
                    cv2.imshow('frame', frame)
                
            
    #     #if user press q camera and game stops
        
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #     else:
    #         timer = int(5)
    
        
    # # After the loop release the cap object
    # game.cap.release()
    # # Destroy all the windows
    # cv2.destroyAllWindows()
                    
play()
               
      
        
                



    


    

        