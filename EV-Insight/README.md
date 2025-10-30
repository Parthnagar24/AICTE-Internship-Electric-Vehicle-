
# EV-Insight
End-to-end internship project: EV range prediction + EV chatbot + Streamlit UI.

## Setup
1. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Train model (creates model/ev_range_model.pkl)
   ```bash
   python model_train.py
   ```
4. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

## Chatbot API key
- The chatbot will use the `OPENAI_API_KEY` environment variable if you set it:
  ```bash
  export OPENAI_API_KEY="sk-..."
  # or on Windows (PowerShell)
  setx OPENAI_API_KEY "sk-..."
  ```
- If no API key is provided the app uses a built-in fallback (canned responses) so it still works offline.

## Files
- `data/ev_dataset.csv` — sample dataset
- `model/ev_range_model.pkl` — saved after running `model_train.py`
- `model_train.py` — trains and saves the model
- `chatbot_service.py` — wrapper for OpenAI calls with fallback
- `app.py` — Streamlit frontend
- `requirements.txt` — pip dependencies

## Notes
- The sample dataset is small and only illustrative. For better model performance, use a larger real-world dataset.
- Replace or expand `chatbot_service.py` if you want to use Google Gemini or other providers.
