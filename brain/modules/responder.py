import dspy

from signatures.responder import Responder
from models import ChatHistory

class ResponderModule(dspy.Module):
    def __init__(self):
        super().__init__()
        reasoning = dspy.OutputField(
            prefix="Reasoning: Let's think step by step to decide on our message. Only social network we speak of is OnlyFans, and dont like in-person meetings. We",
        )
        self.prog = dspy.TypedChainOfThought(Responder, reasoning=reasoning)
    
    def forward(
        self,
        chat_history: dict,
    ):
        return self.prog(
            chat_history=ChatHistory.parse_obj(chat_history),
        )