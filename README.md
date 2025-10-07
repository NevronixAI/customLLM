# Mock Custom LLM Server

This is a **mock server** that simulates a Custom LLM endpoint for testing integration with the **NevronixAI Digital Human platform**.

---


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



## Additional information

- Accepts **POST requests** with a JSON payload containing:
  - `messages` – "system" prompt with previous history and context and "user" question

=== Received JSON payload ===
{
    "model": "llama-3.3-70b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Always respond in this language: en-AU......"
        },
        {
            "role": "user",
            "content": "Tell me mode about your product? "
        }
    ]
}


  - `model` – model name. For example: llama-3.3-70b-instruct
- Requires **API Key** via `Authorization: Bearer <API_KEY>` header
- Responds with a simple JSON object and status code 200:  
  ```json
  { "response": "It works" }
```


## Next Steps

Next, use the response from this script as a reference to implement your own Custom LLM solution with NevronixAI. This mock server demonstrates the exact POST request format you will receive from the platform, as well as the response format that NevronixAI expects.

For support, contact us at hi@nevronix.ai
