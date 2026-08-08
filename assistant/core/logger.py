import logging

logging.basicConfig(
    filename="logs/amna.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("AMNA")