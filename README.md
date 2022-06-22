
# Computer-Vision-Project
Using the google teachable machine web-based tool, I trained a machine-model to recognize four images: Rock, Paper, Scissors and Nothing. The trained model was then used to play a game of Rock, Paper and Scissors using inputs from the camera. Object oriented programming and Computer Vision methods were used to achive this.
## Milestone 1: Training the model:
Using the google [Teachable Machine](https://teachablemachine.withgoogle.com/train/image) , a model with four different classes: Rock, Paper, Scissors and Nothing was trained. This enabled the model to recognise when any of these images were shown. The trained model was then downloaded via TensorFlow and saved in a directory.
<img width="1423" alt="Screen Shot 2022-06-16 at 04 50 21" src="https://user-images.githubusercontent.com/103274172/174917323-bc0c27bc-bebf-460d-a76d-e50610c02355.png">



### Milestone 2: Installing the dependencies:
To prevent dependency version conflicts, creating virtual environments helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. A conda environment with python 3.8 was created for this project as this was easier to use than the current version 3.9 at the time. 
Intasllation of these dependencies were necessary for this project: 
opencv python - a library for computer vision
tenserflow - a library for machine learning & AI
ipykernel - a package that provides a IPython kernel for Jupyter

This project was created using an Apple M1 chip Macbook and the procedure for both creating a virtual environment and installing of tensorflow and opencv was tricky, I have put the exact codes used:

```
conda create -n tensorflow-env python=3.8
conda activate tensorflow-env
conda install pip
chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
source ~/miniforge3/bin/activate
conda activate tensorflow-env
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
conda install -c conda-forge opencv
pip install ipykernel
```

The model was then run on a local machine using the previously made conda environment on a Jupyter/Python interpreter. 



#### Milestone 3: Creating the Rock, Paper, Scissor Game:
Using object oriented programming a class with several methods that represented the backbone of the project was created, namely:

Methods that controlled the acquistion of frames from the camera 
Methods that recorded the user's choice and randomly chose those of the computer's
A method for determining the winner for each round of the game
```
game.open()
game.get_prediction()
user_choice = game.get_prediction()
comp_choice = game.get_comp_choice()
game.get_winnner(comp_choice, user_choice)
```

##### Milestone 4: Putting it together:
A play() fuction that held the whole logic of the game was created after. It instantited the class VisualRps(), using the time.time() fuction a countdown for the user to make a choice was also created. Methods needed for the game were called and displays on the screen were added to make the game more understandble and easily follow the progress of the game. 


###### Conclusion:
Positives: Instead of using global variables, object- oriented programming was used to make sure each of the variables I initialized would translate throughout the different functions. I learned that it is easier to break the content up based on the proposed function and group them together using a clearly defined class. Therefore, it is easier to call each of the functions and I know there isn't any confusion in terms of the variables used.

Future Goals: Incorporating  an audio intro to enable the user prepare for the game, also while the teachable machine tool made training of the model easier. It was however difficult to recognise some of the displays and made frequent errors, training the model from scratch should be a better option to assist readability 

Problem Solving: In terms of programming, I found the hardest part was integrating the camera into the game but after going through the opencv documentation I discovered several of my functions required the ret, frame = cap.read function to read the screen before it would give an output, i created tghe open() method to enableme call this whenever i wanted to print on the screen. 




<img width="1440" alt="Screen Shot 2022-06-21 at 23 59 52" src="https://user-images.githubusercontent.com/103274172/174920730-f1355bc0-3541-4d2f-871a-60085b397e64.png"> 
The screen of the game after a choice is made


