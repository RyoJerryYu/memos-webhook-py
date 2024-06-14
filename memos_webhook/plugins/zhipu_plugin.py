from logging import Logger

from memos_webhook.dependencies.config import ZhipuPluginConfig

from .base_plugin import BasePlugin, pluginLogger


class ZhipuPlugin(BasePlugin):
    logger: Logger = pluginLogger.getChild("ZhipuPlugin")
    cfg: ZhipuPluginConfig

    def __init__(self, cfg: ZhipuPluginConfig) -> None:
        super().__init__()
        self.cfg = cfg
        