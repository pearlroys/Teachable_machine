
# Computer-Vision-Project
Using the google teachable machine web-based tool, I trained a machine-model to recognize four images: Rock, Paper, Scissors and Nothing. The trained model was then used to play a game of Rock, Paper and Scissors using inputs from the camera. Object oriented programming and Computer Vision methods were used to achive this.
## Milestone 1: Training the model (Completed):
Using the google [Teachable Machine](https://teachablemachine.withgoogle.com/train/image) , a model with four different classes: Rock, Paper, Scissors and Nothing was trained. This enabled the model to recognise when any of these images were shown. The trained model was then downloaded via TensorFlow and saved in a directory.
<img width="1423" alt="Screen Shot 2022-06-16 at 04 50 21" src="https://user-images.githubusercontent.com/103274172/174917323-bc0c27bc-bebf-460d-a76d-e50610c02355.png">



### Milestone 2: Installing the dependencies (Completed):
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











The model was then run on a local machine using the previously made conda environment as the Jupyter/Python interpreter. The following code was used to test the decision accuracy of the model and ensure it recognized the different classes.



#### Milestone 3: Creating the Rock, Paper, Scissor Game: (Completed)
##### Milestone 4: Putting it together (Completed):
###### Conclusion:
