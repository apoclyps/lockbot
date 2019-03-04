import os

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

STORAGE_BACKEND = 'machine.storage.backends.memory.MemoryStorage'

PLUGINS = [
    "machine.plugins.builtin.help.HelpPlugin",
    "plugins.lockbot.DeploymentPlugin",
]
