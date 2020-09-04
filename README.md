[//]: # (Image References)

[banana_world_animation]: banana_world.gif "Trained agent"

# Udacity deep reinforcement learning course - project 1

### Introduction

For this project, I trained an agent to navigate and collect bananas in a square
world. The world can be visualized in a Unity application.

![Trained Agent][banana_world_animation]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is
provided for collecting a blue banana. Thus, the goal of the agent is to collect
as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with
ray-based perception of objects around agent's forward direction. Given this
information, the agent has to learn how to best select actions. Four discrete
actions are available, corresponding to:

- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, the agent must get
an average score of +13 over 100 consecutive episodes.

### Unity environment download

1. Download the environment from one of the links below. You need only select
   the environment that matches your operating system:

    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this
    link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64)
    if you need help with determining if your computer is running a 32-bit
    version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a
    virtual
    screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)),
    then please use [this
    link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip)
    to obtain the environment.

2. Extract it to a subdirectory.
3. Update the path to the executable in the Jupyter notebook.

### Python dependencies

Please make sure the following Python requirements are fulfilled in your environment:

- jupyter
- unityagents
- numpy
- matplotlib
- torch

This can be done with

    pip3 install -r requirements.txt

Or your own favorite way of Python dependency management.

### How to run

After downloading and extracting the Unity environment and installing the Python
dependencies, execute the [Navigation.ipynb](Navigation.ipynb) Jupyter notebook
in order to train the agent and/or see the trained agent in action.

### Solution report

See [report](REPORT.md) for more information about my solution.
