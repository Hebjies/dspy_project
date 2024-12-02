So instead of doing a basic off-the-shelf take home which is probably now easily solved using chatgpt or something, I thought it'd be better to have it be more custom-fit to the problem Whisper is solving.

# Project Overview

Vs code configuration:

{
    "name": "Python: local_chat",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/brain/chat_interface.py",
    "console": "integratedTerminal",
    "env": {
        "TOGETHER_API_KEY": ${api key here. You can make a free account at together.ai to get an api key},
    }
},
