import gym 
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.evaluation import evaluate_policy
import os
import pygame
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

model = PPO.load("630K_racing_model.zip")
env = gym.make("CarRacing-v2", render_mode="human")
env = DummyVecEnv([lambda: env])
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=1, render=True)
print("Mean Reward:", mean_reward)
print("Std Reward:", std_reward)
env.close()