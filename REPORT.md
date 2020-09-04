[//]: # (Image References)

[average_score_over_episodes]: average_score_over_episodes.png "Training result"

# Project 1: Banana navigation - report

This report describes my solution and some findings along the way.

### Solution architecture and training algorithm

My solution consists of a deep Q network (DQN) with the following architecture

- 1. inner layer: fully connected 128 with ReLU activation
- 2. inner layer: fully connected 64 with ReLU activation

I experimented with an additional inner layer but that did not seem to improve
the result so I stayed with 2 inner layers. The model weights of a solution that
reaches an average score above 13 can be found in `model_weights.pth`.

The training algorithm used for the final solution was the vanilla DQN training
algorithm with a replay buffer, well known in the literature. This decision was
made because it exhibited quite acceptable results and could not be improved
much with the Double DQN algorithm. The following hyperparameters have been
used:

- Initial exploration coefficient: <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{start}=1.0">
- Final exploration coefficient: <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{end}=0.01">
- Exploration decay: <img src="https://render.githubusercontent.com/render/math?math=\epsilon_\text{decay}=0.98">
- Discount factor: <img src="https://render.githubusercontent.com/render/math?math=\gamma=0.99">
- Soft update coefficient: <img src="https://render.githubusercontent.com/render/math?math=\tau=1\times10^{-3}">
- Replay buffer size: <img src="https://render.githubusercontent.com/render/math?math=1\times10^{5}">
- Batch size: <img src="https://render.githubusercontent.com/render/math?math=64">
- Learning rate: <img src="https://render.githubusercontent.com/render/math?math=5\times10^{-4}">

### Findings
- It was difficult to work with the fullscreen Unity environment. I therefore
  patched the code and created a [pull request](https://github.com/udacity/deep-reinforcement-learning/pull/52) for window mode.
- The maximum number of steps per episode has a HUGE impact. When limiting the
  number of steps to 100 I couldn't seem to get an average score higher than
  about 2-4 in about 1000 episodes. Limiting to 1000 steps per episode helped
  dramatically. This seems to be very important to learn some more long term
  strategies.
- The exploration decay is multiplicatively applied in each episode. A slightly
  stronger decay seems to be beneficial for the result. The environment is
  solved in less episodes when going from 0.99 to 0.98.
- Updating the network more or less often makes a large difference. Updating
  every step and every 10th step leads to the network not being able to learn
  the solution within 1000 iterations. Updating every 4 time steps seems to be
  working well.
- Double DQN seemed to not really help that much for this environment, therefore
  in the end I went with the vanilla DQN.
- Finally I was able to train an agent that solves the environment (average
  score of 13.0) within 333 episodes. The agent reached a score of 14.92 at the
  end of the training (500 episodes)

![Traning result][average_score_over_episodes]

### Things to look at

In the future I might have a look at

- Prioritized replay: There are certain situations that could be learned quicker
  like moving around blue bananas or avoid staring at walls
- More complex network architecture: Some more complex network architectures
  might allow the agent to find an optimum route between yellow bananas. This
  requires memory and some kind of mapping approach.
