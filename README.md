
# Project Overview

Vs code configuration:

```json
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
```