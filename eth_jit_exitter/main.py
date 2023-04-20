import os
import argparse
import logging

import yaml

from eth_jit_exitter import webhook_server
from eth_jit_exitter import signer_server

logging.basicConfig()

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, help='Path to config file')
    args = parser.parse_args()

    config = {}

    if args.config:
        if os.path.isfile(args.config):
            # Load config.
            with open(args.config, 'r') as file:
                config = yaml.safe_load(file)

            if config['running_mode'] == 'WEBHOOK':
                LOGGER.info(f"Running in WEBHOOK mode on port {config['port']}")
                webhook_server.start_server(config)
            else:
                LOGGER.info(f"Running in SIGNER mode on port {config['port']}")
                signer_server.start_server(config)
        else:
            LOGGER.error("Path to config file is invalid.")
    else:
        LOGGER.error('Missing parameter --config')