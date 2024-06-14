from logging import Logger
from typing import Any, Coroutine, override

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSerializable

from memos_webhook.dependencies.config import ZhipuPluginConfig
from memos_webhook.dependencies.memos_cli import MemosCli
from memos_webhook.langchains.zhipu import ZhipuAIChatModel
from memos_webhook.proto_gen.memos.api.v1 import Memo, WebhookRequestPayload

from .base_plugin import BasePlugin, pluginLogger


class ZhipuPlugin(BasePlugin):
    logger: Logger = pluginLogger.getChild("ZhipuPlugin")
    _name: str
    _tag: str
    cfg: ZhipuPluginConfig
    llm: ZhipuAIChatModel

    def __init__(self, name: str, tag: str, cfg: ZhipuPluginConfig) -> None:
        super().__init__()
        self._name = name
        self._tag = tag
        self.cfg = cfg
        self.llm = ZhipuAIChatModel(api_key=cfg.api_key)

    @override
    def activity_types(self) -> list[str]:
        return ["memos.memo.created"]

    @override
    def tag(self) -> str:
        return self._tag

    @override
    async def task(self, payload: WebhookRequestPayload, memos_cli: MemosCli) -> Memo:
        self.logger.debug("start zhipu plugin task")
        content = payload.memo.content
        self.logger.debug(f"content: {content}")
        chain: RunnableSerializable = (
            {"content": RunnablePassthrough()}
            | PromptTemplate.from_template(self.cfg.prompt)
            | self.llm
            | StrOutputParser()
        )

        res: str = await chain.ainvoke({"content": content})
        res_content = f"""{payload.memo.content}

---AI Generated---

{res}
"""

        payload.memo.content = res_content
        return payload.memo
