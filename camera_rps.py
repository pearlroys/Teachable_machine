from enum import IntEnum
import random
import cv2 
from keras.models import load_model
import numpy as np
import time

class items(IntEnum):
        Scissors =  0
        Rock = 1
        Paper = 2
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
    def left_click(event, x, y, flags, param):
        event == cv2.EVENT_LBUTTONDOWN
                    

    # to get user choice
    def get_prediction(self):
        prediction = self.model.predict(self.data)
        choice = np.argmax(prediction[0])
        return choice

    # to get name of choice
    def get_user_choice(self):
        choice = self.get_prediction()
        self.user_choice = items(choice)
        return self.user_choice

    # get computer choice and choice name
    def get_comp_choice(self):
        self.pick = random.randint(0, len(items) - 1)
        self.comp_choice = items(self.pick)
        return self.comp_choice
    
    # get winner
    def get_winnner(self, computer_choice, users_choice):
        if computer_choice == users_choice:
            self.rounds += 1
            self.winner = "it's a tie!"
        
        elif users_choice == items.Rock:
            if computer_choice == items.Scissors:
                self.user_score += 1
                self.winner = self.name
                self.rounds += 1
            
            else:
                self.computer_score += 1
                self.winner = "comp"
                self.rounds += 1

        elif users_choice == items.Paper:
            if computer_choice == items.Rock:
                self.user_score += 1
                self.winner = self.name
                self.rounds += 1
            
            else:
                self.computer_score += 1
                self.winner = "comp"
                self.rounds += 1
        elif users_choice == items.Scissors:
            if computer_choice == items.Paper:
                self.user_score += 1
                self.winner = self.name
                self.rounds += 1
            else:
                self.computer_score += 1
                self.winner = "comp"
                self.rounds += 1
        elif users_choice == items.Nothing:
            self.winner = "wake-up!!"
        
        return self.winner
    

    def play(self):

        game = VisualRps()
        game.introduction()
        while True:
            timer = 5
            ret, frame = game.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            game.data[0] = normalized_image
            prediction = game.model.predict(game.data)
            cv2.imshow('frame', frame)

            # Generate persistent items
            cv2.rectangle(frame, (10,10), (442, 50), (255,255,0), -1)
            message = "Stage: " + str(self.rounds) + "     " + "Score: " + str(self.user_score) + ":" + str(self.computer_score)
            cv2.putText(frame, message, (20,40), 1, 2, (0,0,0))

            # left click mouse to start game
            cv2.setMouseCallback('frame', game.left_click)
            prev_time = time.time()

            # rectangle for user to play
            cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
            # rectangle for computer to play
            cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)
            cv2.putText(frame, str(timer), (190,420), 2, 3, (0,0,0))

            # decrease timer by one
            curr_time = time.time()
            if curr_time - prev_time >= 1:
                prev_time = curr_time
                timer = timer - 1

            # extract the region of image within the user rectangle
            roi = frame[100:500, 100:500]
            img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (227, 227))

            #call the get choices and winner methods
            game.get_prediction()
            computer_choice = game.get_comp_choice()
            users_choice = game.get_user_choice()
            game.get_winnner(computer_choice, users_choice)


            # display the information
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Your Move: " + self.user_choice,
                        (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "Computer's Move: " + self.comp_choice,
                        (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "Winner: " + self.winner,
                        (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)

            # pick overall winner
            if game.computer_score == 3:
                cv2.rectangle(frame, (50,80), (402, 160), (180,170,50), -1)
                cv2.putText(frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                cv2.putText(frame, "CPU" + " wins!", (110,150), 3, 1, (0,0,0))
           

            elif game.user_score == 3:
                cv2.rectangle(frame, (50,80), (402, 160), (180,170,50), -1)
                cv2.putText(frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                cv2.putText(frame, game.name + " wins!", (110,150), 3, 1, (0,0,0))
           
                
            #if user press q camera and game stops
           
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            else:
                timer = int(5)
        
            
        # After the loop release the cap object
        game.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
                    

    
               
      
        
                



    


    

        