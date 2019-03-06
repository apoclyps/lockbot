import os
import re

from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to
from machine.storage.backends.redis import RedisStorage

settings = {"REDIS_URL": os.getenv("REDIS_URL")}

storage = RedisStorage(settings)


class DeploymentPlugin(MachineBasePlugin):
    """Deployment"""

    @respond_to(r"^lock$")
    def lock(self, msg):
        """lock: spread the lock"""
        storage.set("services", "locked")
        msg.say("Serviced locked")

    @respond_to(r"^release$")
    def release(self, msg):
        """release: spread the release"""
        storage.set("services", "locked")
        msg.say("Serviced released")
