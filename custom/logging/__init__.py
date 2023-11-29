import yaml

import logging
import logging.config

import os


# Uso del archivo YAML llamado config.yaml
logging_config_dir = os.path.dirname(__file__)
config_file = logging_config_dir + '/config.yml'

with open(config_file, 'r') as file:
    config = yaml.safe_load(file)
logging.config.dictConfig(config)

logger = logging.getLogger("customLogger")