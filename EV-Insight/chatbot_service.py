
import os
import openai
import random

OPENAI_KEY = os.environ.get("OPENAI_API_KEY", "").strip()

def get_chatbot_response(prompt, api_key=None):
    '''
    If OPENAI_API_KEY environment variable is set (or api_key passed), this function will
    call OpenAI's ChatCompletion API. Otherwise it will return a simulated helpful answer
    using simple heuristics and canned responses so the app works without a paid key.
    '''
    key = api_key or os.environ.get("OPENAI_API_KEY")
    if key:
        openai.api_key = key
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"system","content":"You are an assistant knowledgeable about electric vehicles."},
                          {"role":"user","content": prompt}],
                max_tokens=250,
                temperature=0.2
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"OpenAI API error: {e}"
    else:
        # Simple rule-based / canned fallback
        lower = prompt.lower()
        if "charge" in lower or "charging" in lower:
            return ("Charging basics: Most EVs support slow (AC) and fast (DC) charging. "
                    "Level 2 (AC) charges overnight (6-10 hrs), DC fast chargers can replenish ~80% in 20-60 mins depending on the vehicle.")
        if "battery" in lower or "degradation" in lower:
            return ("Battery health tips: avoid frequent 0-100% full cycles, prefer charging to 80-90% for daily use, "
                    "and keep the battery within moderate temperature range to extend life.")
        if "range" in lower or "predict" in lower:
            return ("Range depends on battery state, driving speed, temperature, accessory load (AC/heater), and terrain. "
                    "Slower speeds and moderate temperatures increase range.")
        # generic
        canned = [
            "EVs are more efficient at steady moderate speeds; heavy acceleration reduces range.",
            "For practical trips, plan charging stops and account for 10-20% buffer for unexpected delays.",
            "Maintenance: check tire pressure, regenerative braking settings, and keep software up to date."
        ]
        return random.choice(canned)
