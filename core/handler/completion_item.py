import os
from enum import Enum

from core.handler import Handler
from core.utils import *

class CompletionItem(Handler):
    name = "completion_item_resolve"
    method = "completionItem/resolve"
    cancel_on_change = True
    send_document_uri = False

    def process_request(self, label, item) -> dict:
        self.label = label
        return item

    def process_response(self, response: dict) -> None:
        if response is not None and "documentation" in response:
            eval_in_emacs("lsp-bridge-update-completion-item-info",
                          {
                              "filepath": self.file_action.filepath,
                              "label": self.label,
                              "additionalTextEdits": response["additionalTextEdits"] if "additionalTextEdits" in response else [],
                              "documentation": response["documentation"]["value"] if "value" in response else response["documentation"]
                          })
