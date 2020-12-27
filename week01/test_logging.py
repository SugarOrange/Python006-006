import logging
from datetime import *
from pathlib import Path

p = Path(f'/var/log/python-{datetime.now().date()}')
p.mkdir(parents=True, exist_ok=True)
log_filename = p.joinpath(f'{__name__}.log')

logging.basicConfig(filename=log_filename,
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %X',
                    format='%(asctime)s %(name)-8s %(levelname)-8s '
                    '[line: %(lineno)d] %(message)s'
                    )

logging.error("error message")