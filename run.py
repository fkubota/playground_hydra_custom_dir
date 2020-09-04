import hydra
from omegaconf import DictConfig
# from loguru import logger
import logging
import hello

# A logger for this file
logger = logging.getLogger(__name__)


@hydra.main(config_path="config.yaml")
def run(cfg: DictConfig) -> None:
    logger.info('logger start')
    logger.info(f'all params\n{"="*70}\n{cfg.pretty()}\n{"="*70}')
    hello.hello()
    import os
    logger.info(os.getcwd().split('/hydra_outputs/'))


if __name__ == "__main__":
    run()
