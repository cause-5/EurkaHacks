from fastapi import FastAPI
from openai import OpenAI
import json

app = FastAPI()
client = OpenAI()
#EXAMPLE INPUT. change later. 
skill = "Python programming"
level = "Beginner"
time_per_day = 15

@app.post("/generate-plan")
async def generate_plan(skill: str, level: str, time_per_day: int):

    prompt = f"""You are an expert learning designer.

Create a structured 7-day plan to learn the following skill:
"{skill}"

User preferences:
- Level: {level} (Beginner / Intermediate / Advanced)
- Daily time available: {time_per_day} minutes

STRICT REQUIREMENTS:
- The plan must be practical and actionable (no fluff)
- Each day must build on the previous one
- Focus on real skill acquisition, not just passive learning
- Include hands-on practice or mini-projects when possible

OUTPUT FORMAT:
Return ONLY valid JSON. No explanations.

JSON STRUCTURE:
{
  "skill": string,
  "level": string,
  "estimated_total_time_hours": number,
  "days": [
    {
      "day": number,
      "title": string,
      "goal": string,
      "tasks": [string],      
      "resources": [
        {
          "type": "video" | "article",
          "title": string,
          "url": string,
          "reason": string
        }
      ],
      "estimated_time_minutes": number
    }
  ]
}

RESOURCE RULES:
- Include 1 resource per day
- On topic of specified goal
- Prefer high-quality beginner-friendly tutorials
- Pick increasing difficulty as the days progress. Start with very basic resources and move towards more comprehensive ones.
- Avoid generic resources that cover too much or too little. The resource should be just right for the day's goal.
- The video must be engaging and well-structured, ideally with clear explanations and examples. 
- The video must be within time limits to fit the daily time constraint. 
- Prioritize YouTube videos and reputable sites (MDN, freeCodeCamp, etc.)
- URLs must be real and complete (https://...)

TASK RULES:
- 2–5 tasks per day
- Tasks must be specific and actionable
- Include at least one "build" or "practice" task where possible

Make sure the difficulty matches the user level."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}  # 🔥 IMPORTANT
    )

    data = json.loads(response.choices[0].message.content)

    return data



# This tells the model to return a JSON object, which we can easily parse in our code.
