from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ChatMessage(BaseModel):
    from_creator: bool
    content: str
    context: list

    def __str__(self):
        role = "YOU" if self.from_creator else "THE FAN"
        # message = role + ": " + self.content
        message = f"{self.context}\n{role}: {self.content} [Sent at {self.context[0]}]\n[Chat duration: {self.context[1]}]"
        return message

class ChatHistory(BaseModel):
    messages: List[ChatMessage] = []

    def __str__(self):
        messages = []
        for i, message in enumerate(self.messages):
            message_str = str(message)
            # if i == len(self.messages) - 1 and not message.from_creator:
            #     message_str = (
            #         "(The fan just sent the following message which your message must respond to): "
            #         + message_str
            #     )
            messages.append(message_str)
        return "\n".join(messages)
    
    def model_dump_json(self, **kwargs):
        return str(self)