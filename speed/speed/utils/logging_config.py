import logging
import coloredlogs

logger = logging.getLogger()
coloredlogs.install(level=logging.DEBUG, logger=logger,
                    fmt='  %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level_styles={'debug': {'color': 'green'},
                                  'info': {'color': 'blue'},
                                  'warning': {'color': 'yellow'},
                                  'error': {'color': 'red'},
                                  'critical': {'color': 'red', 'bold': True}})
