# Lockbot
A project that uses the [slack-machine](https://slack-machine.readthedocs.io/) package and the [Slack Developer Kit for Python](https://slackapi.github.io/python-slackclient/) to provide a customisable Slack bot for managing deployments.

## Quickstart
After you clone this repository, you can provide your `SLACK_API_TOKEN` within a `.env` file like so:

```bash
SLACK_API_TOKEN=some-key
```

To run the slack machine, you can build the docker container and run the slack machine by providing the following commands (this will load your token from the .env file for you):

```python
docker-compose build bot
docker-compose run bot
```
