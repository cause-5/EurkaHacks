from fastapi import FastAPI
from openai import OpenAI
import json

app = FastAPI()
client = OpenAI()

@app.post("/generate-plan")
async def generate_plan(skill: str, level: str, time_per_day: int):

    prompt = f"""[PASTE YOUR FINAL PROMPT HERE]"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}  # 🔥 IMPORTANT
    )

    data = json.loads(response.choices[0].message.content)

    return data

response_format={"type": "json_object"}
# This tells the model to return a JSON object, which we can easily parse in our code.
