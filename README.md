# Lockbot

A project that uses the [slack-machine](https://slack-machine.readthedocs.io/) package and the [Slack Developer Kit for Python](https://slackapi.github.io/python-slackclient/) to provide a customisable Slack bot for managing lockments.

<p align="center">
  <img src="https://i.ytimg.com/vi/U2TQyuxzWRA/mqdefault.jpg" alt="lenny" height="240" width="320" />
</p>

### Quickstart

After you clone this repository, you can provide your environment configuration within a `.env` file located in the root directory. The following variables are required:

```bash
# The token associated with a given Slack workspace used by the Bot.
SLACK_API_TOKEN=some-key
# The Redis URL associated with a local or remote instance
REDIS_URL=
```

To run the slack machine, you can build the docker container and run the slack machine by providing the following commands (this will load your token from the .env file for you):

```python
docker-compose build bot
docker-compose run bot
```

### Commands

#### help

Display's all available commands listed below:

#### list services

Show a list of all known services.

#### lock service

Lock the service.

#### release service

Release the deployments locks for the service.

### Contributing

Pull requests on this bot are very welcome. Please read CONTRIBUTING.md for details on the code of conduct, and the process for submitting pull requests.
