# Description
A python program to solve 3x3 rubik's cube Using Kociemba's Two-Phase algorithm. <a href="https://pypi.org/project/kociemba">Description</a>

# Demo
Here is a <a href="https://tinyurl.com/3t5sc9yk">Video</a> of this Project.

# Packages
* `Opencv` to capture the cube
* `matplotlib` to show a 3d animation of the cube
* `pygame` is used for a virtual cube

# Installation
Clone the repository
```
git clone https://github.com/Nishan45/Rubik-s-Cube-Solver.git
```
Install the requirements using pip
```
pip install -r requirements.txt
```

# Usage
* Run the image_capture.py file within the directory
## Capturing the Cube
6 keys for 6 different faces of the cube.<br>
`u`, `l`,`f`,`r`,`b`,`d` keyboard keys for  `Up`, `Left`, `Front`, `Right`, `Back`, and `Down` faces of the cube.

* Hold `i` key while capturing colours of one face of the cube.
* After capturing the colors press one of the keys describe above to save it on that face. Press `n` to see the face.
* make sure all the faces are correct else cube would be invalid.
* Press `m` to see the cube. Press `enter` to start the animation.
* See this <a href="https://tinyurl.com/3t5sc9yk">Video</a> for example.


## Without capturing the Cube
* Run the main.py file within the directory. A window would appear containing a cube.
### To suffle the cube
* Use `<`, `>` with `a` for left and `d` for right side.
* Use `UP`, `BOTTOM` with `w` for up and `x` for down side.
* press `1` to solve the cube.
<img src="https://github.com/Nishan45/Rubik-s-Cube-Solver/assets/114748319/1c183218-9241-4e47-b033-306e15741b9d" width=500>


