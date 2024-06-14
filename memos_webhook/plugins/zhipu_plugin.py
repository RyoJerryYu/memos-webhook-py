from logging import Logger

from memos_webhook.dependencies.config import ZhipuPluginConfig
from memos_webhook.langchains.zhipu import ZhipuAIChatModel

from .base_plugin import BasePlugin, pluginLogger


class ZhipuPlugin(BasePlugin):
    logger: Logger = pluginLogger.getChild("ZhipuPlugin")
    cfg: ZhipuPluginConfig
    llm: ZhipuAIChatModel

    def __init__(self, cfg: ZhipuPluginConfig) -> None:
        super().__init__()
        self.cfg = cfg
        self.llm = ZhipuAIChatModel(api_key=cfg.api_key)
