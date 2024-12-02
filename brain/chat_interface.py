import dspy
from datetime import datetime
from lms.together import Together
from modules.optimizer import ChatOptimizer
from models import ChatMessage, ChatHistory
# from modules.chatter import ChatterModule

file_path = './training_data/conversations.json'

def duration_time(seconds):
    seconds = seconds.total_seconds()

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60

    if hours > 0:
        if minutes > 0:
            return f"{hours} h {minutes} min"
        else:
            return f"{hours} h"
    elif minutes > 0:
        return f"{minutes} min"
    else:
        return f"{int(seconds)} sec"

lm = Together(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    temperature=0.6,
    max_tokens=1000,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1.2,
    stop=["<|eot_id|>", "<|eom_id|>", "\n\n---\n\n", "\n\n---", "---", "\n---"],
    # stop=["\n", "\n\n"],
)

dspy.settings.configure(lm=lm)

chat_history = ChatHistory()
# chatter = ChatterModule(examples=None)
chatter = ChatOptimizer(file_path).knn_teleprompter()

start_time = datetime.now()

while True:
    # Get user input
    user_input = input("You: ")

    # Append user input to chat history
    sent_at = datetime.now()
    conversation_duration = duration_time(sent_at - start_time)
    sent_at = sent_at.strftime("%I:%M %p")

    chat_history.messages.append(
        ChatMessage(
            from_creator=False,
            content=user_input,
            context=[sent_at,conversation_duration]
        ),
    )

    # Send request to endpoint
    response = chatter(chat_history=chat_history).output

    sent_at = datetime.now()
    conversation_duration = duration_time(sent_at - start_time)
    sent_at = sent_at.strftime("%I:%M %p")

    # Append response to chat history
    chat_history.messages.append(
        ChatMessage(
            from_creator=True,
            content=response,
            context=[sent_at,conversation_duration]
        ),
    )
    # Print response
    print()
    print("Response:", response)
    print()
    # uncomment this line to see the 
    lm.inspect_history(n=1)