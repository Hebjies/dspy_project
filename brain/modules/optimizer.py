import json
import dspy
from dspy.teleprompt import KNNFewShot
from modules.chatter import ChatterModule
from models import ChatMessage, ChatHistory

class ChatOptimizer:

    def __init__(self, converstion_path: str):
        self.converstion_path = converstion_path

    def _conversation_loader(self,):

        with open(self.converstion_path, encoding='utf-8', mode='r') as file:
            chat_data = json.load(file)

        train_chat_history = []
        for chat in chat_data:
            chat_history = ChatHistory()
            for sub_chat in chat["chat_history"]['messages']:
                chat_history.messages.append(
                    ChatMessage(
                        from_creator=sub_chat['from_creator'],
                        content=sub_chat['content'],
                        context=[None, None]
                    ),
                )
            response = ChatMessage(
                        from_creator=True,
                        content=chat['output'],
                        context=[None, None]
                    ),
            train_chat_history.append({"hisotry": chat_history, "output": response})
        
        return train_chat_history

    def knn_teleprompter(self, k: int = 3):

        self.chat_history = [
            dspy.Example(chat_history=chat["hisotry"], response=chat["output"])
            .with_inputs("chat_history")
            for chat in self._conversation_loader()
        ]

        knn = KNNFewShot(k, self.chat_history)
        compiled_knn = knn.compile(ChatterModule(examples=None), trainset=self.chat_history)

        return compiled_knn