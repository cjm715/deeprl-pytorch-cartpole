from deeprl.vpg import vpg, PolicyNet
import gym
import matplotlib.pyplot as plt

env = gym.make('CartPole-v0')

agent, mean_return_list = vpg(env, num_iter=200)

# # Load saved model from file instead
# import torch
# input_size = env.observation_space.shape[0]
# output_size = env.action_space.n
# agent = PolicyNet(input_size, output_size)
# agent.load_state_dict(torch.load('vpg_policy.pt'))
# agent.eval()

plt.plot(mean_return_list)
plt.xlabel('Iteration')
plt.ylabel('Mean Return')
plt.savefig('vpg_returns.png', format='png', dpi=300)

state = env.reset()
for t in range(1000):
    action = agent.act(state)
    env.render()
    state, reward, done, _ = env.step(action)
    if done:
        break
env.close()
