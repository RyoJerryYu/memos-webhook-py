import asyncio

from memos_webhook.app import app
from memos_webhook.dependencies.config import new_config
from memos_webhook.utils.logger import logger as util_logger
from memos_webhook.utils.logger import logging_config

logger = util_logger.getChild("main")


def main():
    import uvicorn

    logger.info("webhook server started")
    cfg = new_config()
    logger.info(f"config: {cfg.dotenv_path}")
    logger.info(f"config: {cfg.webhook_host}")

    try:
        uvicorn.run(
            app,
            host=cfg.webhook_host,
            port=cfg.webhook_port,
            log_config=logging_config(cfg.log_level),
            log_level=cfg.log_level,
        )
    except (KeyboardInterrupt, SystemExit):
        logger.info("webhook server stopped")
    except asyncio.CancelledError:
        logger.error(
            "webhook server cancelled, But asyncio.CancelledError. Maybe a task cancelled incorrectly."
        )
    except Exception as e:
        logger.error(f"webhook server error: {e}")
        raise e


if __name__ == "__main__":
    main()
