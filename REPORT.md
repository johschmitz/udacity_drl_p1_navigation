# Project 1: Banana navigation - report

This report describes my solution and some findings along the way.

### Solution architecture and strategy

My solution consists of a deep Q network with the following architecture

- 1. inner layer: fully connected 128 with ReLU activation
- 2. inner layer: fully connected 64 with ReLU activation

I experimented with an additional inner layer but that did not seem to improve
the result so I stayed with 2 inner layers. The model weights of a solution that
reaches an average score above 13 can be found in `model_weights.pth`.

The epsilon values for the training have been set to

- <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{start}=1.0">
- <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{end}=0.01">
- <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{decay}=0.98">

The decay is multiplicatively applied in each episode. A slightly stronger decay
seems to be beneficial for the result. The environment is solved in less
episodes when going from 0.99 to 0.98.

### Findings
- It was difficult to work with the fullscreen Unity environment. I therefore
  patched the code and created a [pull
  request](https://github.com/udacity/deep-reinforcement-learning/pull/52) for
  window mode.
- The maximum number of steps per episode has a HUGE impact. When limiting the
  number of steps to 100 I couldn't seem to get an average score higher than
  about 2-4 in about 1000 episodes. Limiting to 1000 steps per episode helped
  dramatically. This seems to be very important to learn some more long term
  strategies.
- Updating the network more or less often makes a large difference. Updating
  every step and every 10th step leads to the network not being able to learn
  the solution within 1000 iterations. Updating every 4 time steps seems to be
  working well.
- Double DQN seemed to not really help that much for this environment, therefore
  in the end I went with the vanilla DQN.

### Things to look at

In the future I might have a look at

- Prioritized replay: There are certain situations that could be learned quicker
  like moving around blue bananas or avoid staring at walls
- More complex network architecture: Some more complex network architectures
  might allow the agent to find an optimum route between yellow bananas. This
  requires memory and some kind of mapping approach.
