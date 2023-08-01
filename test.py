import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv

# Create a function that returns the environment
# This is necessary to pass a different seed to each instance of the environment
def make_env(env_id, rank):
    def _init():
        env = gym.make(env_id)
        env.seed(rank)
        return env
    return _init

# Define the number of parallel environments (e.g., 4)
num_envs = 4

# Create a single environment ID (same game environment in this case)
env_id = "CarRacing-v2"

# Create a list of environments using DummyVecEnv (for debugging) or SubprocVecEnv (faster)
envs = [make_env(env_id, rank) for rank in range(num_envs)]
# Use DummyVecEnv for debugging (single process)
# vec_env = DummyVecEnv(envs)
# Use SubprocVecEnv for parallelization (multiple processes)
vec_env = SubprocVecEnv(envs)

# Train the agent using PPO with the vectorized environment
model = PPO("CnnPolicy", vec_env, verbose=1, tensorboard_log="Data")
model.learn(total_timesteps=40000)

# Save the trained model
model.save("car_racing_model")

# Close the environment
vec_env.close()
