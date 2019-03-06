import os
import re

from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to
from machine.storage.backends.redis import RedisStorage

settings = {"REDIS_URL": os.getenv("REDIS_URL")}

storage = RedisStorage(settings)


class DeploymentPlugin(MachineBasePlugin):
    """Deployment"""

    @respond_to(r"^list$")
    @respond_to(r"^list services$")
    def list(self, msg):
        """list services: list all registered services"""
        services = [key.decode("utf-8") for key in storage._redis.keys()]

        response = "All Services:\n\n"
        for service in services:
            service = service.replace("SM:", "")
            response += f"* {service}\n\n"

        msg.say(response)

    @respond_to(r"^lock (?P<service>.*)$")
    def lock(self, msg, service):
        """lock <service>: lock a given service"""
        state = storage.get(service).decode("utf-8")

        if state == "locked":
            msg.say(f"Service {service} is already locked :lock:")
        else:
            storage.set(service, "locked")
            msg.say(f"Service {service} locked :lock:")

    @respond_to(r"^release (?P<service>.*)$")
    def release(self, msg, service):
        """release <service_name>: release a given service"""
        state = storage.get(service).decode("utf-8")

        if state == "locked":
            storage.set(service, "released")
            msg.say(f"Service {service} is now available to deploy :white_check_mark:")
        else:
            msg.say(f"Service {service} is already released :white_check_mark:")
