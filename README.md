# Mock Custom LLM Server

This is a **mock server** that simulates a Custom LLM endpoint for testing integration with the **NevronixAI Digital Human platform**.

---

## Features

- Accepts **POST requests** with a JSON payload containing:
  - `prompt` – full conversation + question
  - `model` – model name
- Requires **API Key** via `Authorization: Bearer <API_KEY>` header
- Responds with a simple JSON object:  
  ```json
  { "response": "It works" }
```


### Installation
Clone the repository:


git clone https://github.com/NevronixAI/customLLM.git
cd customLLM


## Run the server:

python customLLM.py

The default port is 5005. You can change it in the script if needed.



## Configure Your Custom LLM in NevronixAI platform

Sign up or log in to the platform: https://nevronix.ai/

Create a Digital Human.

At Step 5 → Custom LLM, select:
"Connect your Digital Human to your Own LLM Solution (Optional)"

Provide the required fields:

- API Key – for this example, use NevronixAI

- Host – your public IP with port 5005 (or your chosen port)

- Model – optional; if using multiple models, you can control which model each Digital Human uses




This is the Example response which your LLM should return as well as status code 200


{ "response": "It works!" }


Next Steps

Use this server as a reference to implement your own LLM endpoint which can be connected to NevronixAI.
It demonstrates the POST request format you will receive and the response format expected by NevronixAI platform.

For support, please reach out: hi@nevronix.ai
