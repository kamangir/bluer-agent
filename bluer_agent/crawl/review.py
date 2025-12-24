from bluer_options.logger.config import log_list

from bluer_agent.crawl.collect import load_binary
from bluer_agent.logger import logger

results = load_binary("site_text.pkl.gz")
log_list(logger, "loaded", results.keys(), "page(s)")
