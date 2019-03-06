import os

REDIS_URL = os.getenv("REDIS_URL")
SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

STORAGE_BACKEND = "machine.storage.backends.redis.RedisStorage"

PLUGINS = [
    "machine.plugins.builtin.help.HelpPlugin",
    "plugins.lockbot.DeploymentPlugin",
]
