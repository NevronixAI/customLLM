# Mock Custom LLM Server

This is a **mock server** that simulates a Custom LLM endpoint for testing integration with the **NevronixAI Digital Human platform**.

---

## Installation
Clone the repository:

```bash
git clone https://github.com/NevronixAI/customLLM.git
cd customLLM
```

## Run the server

```bash
python customLLM.py
```

The default port is 5005. You can change it in the script if needed.

---

## Configure Your Custom LLM in NevronixAI Platform

1. Sign up or log in to the platform: [NevronixAI](https://nevronix.ai/)
2. Create a Digital Human.
3. At Step 5 → Custom LLM, select:  
   "Connect your Digital Human to your Own LLM Solution (Optional)"
4. Provide the required fields:
   - **API Key** – for this example, use `NevronixAI`
   - **Host** – your public IP with port 5005 (or your chosen port)
   - **Model** – optional; if using multiple models, you can control which model each Digital Human uses

---

## Example Response

This is the example response your LLM should return, with status code `200`:

```json
{ "response": "It works!" }
```

---

## Additional Information

- Accepts **POST requests** with a JSON payload containing:
  - `messages` – array of system and user messages:

```json
{
    "model": "llama-3.3-70b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Always respond in this language: en-AU..."
        },
        {
            "role": "user",
            "content": "Tell me more about your product?"
        }
    ]
}
```

  - `model` – model name, e.g., `llama-3.3-70b-instruct`
- Requires **API Key** via `Authorization: Bearer <API_KEY>` header
- Responds with a simple JSON object and status code 200:

```json
{ "response": "It works" }
```

---

## Next Steps

Use this mock server as a **reference to implement your own Custom LLM solution** with NevronixAI:
- Demonstrates the exact POST request format you will receive from the platform
- Shows the expected JSON response format

For support, contact: **hi@nevronix.ai**