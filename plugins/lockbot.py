import re

from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to
from machine.storage.backends.memory import MemoryStorage

memory_storage = MemoryStorage({})


class DeploymentPlugin(MachineBasePlugin):
    """Deployment"""

    @respond_to(r"^lock$")
    def lock(self, msg):
        """lock: spread the lock"""
        memory_storage.set("services", "locked")
        msg.say("Serviced locked")

    @respond_to(r"^release$")
    def release(self, msg):
        """release: spread the release"""
        memory_storage.set("services", "locked")
        msg.say("Serviced released")
