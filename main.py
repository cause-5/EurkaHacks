from fastapi import FastAPI, HTTPException
from openai import OpenAI
import json

app = FastAPI()
client = OpenAI()

@app.post("/generate-plan")
async def generate_plan(skill: str, level: str, time_per_day: int):
    # Notice the double {{ }} to escape the f-string curly braces
    prompt = f"""You are an expert learning designer.
Create a structured 7-day plan for: "{skill}"
User preferences: Level: {level}, Daily time: {time_per_day} minutes.

STRICT REQUIREMENTS:
- Output ONLY valid JSON.
- Include 1 real resource per day.
- Focus on actionable tasks.

JSON STRUCTURE:
{{
  "skill": "{skill}",
  "level": "{level}",
  "days": [
    {{
      "day": 1,
      "title": "Introduction",
      "tasks": ["task1", "task2"],
      "resources": [{{ "type": "video", "url": "https://..." }}]
    }}
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        return json.loads(content)
        
    except Exception as e:
        # In a real API, you want to return a proper error code
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/test-plan")
async def test_plan():
    return {"message": "it works"}
    eg = generate_plan("Python programming", "Beginner", 15)
    print (eg)
