import gym
import numpy as np

division = 6
max_step = 200

class QLearning:
    def __init__(self, env, ratio, alpha):
        self.env        = env
        self.ratio      = ratio
        self.alpha      = alpha
        self.qtable     = np.zeros(division**4, self.env.action_space.n)

		'''
			状態の離散化
		'''
		def state_discretization(self):

		'''
			t+1時刻での行動
		'''
    def get_action(self):

		'''
			Q値の更新
		'''
    def update_Qtable(self):

		'''
			メインループ
		'''
    def run(self, max_espisode):
        for i_episode in range(max_episode):
            observation = self.env.reset()
            for t in range(max_step):
                if is_done is True:
                    self.env.render()

if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    qlearning = QLearning(env, 0.5, 0.5)
    qlearning.run(1000)

env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
