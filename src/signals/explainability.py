import shap
import pandas as pd

def feature_importance_shap(model, df, top_n=10):
    # Remove non-feature columns
    features = df.drop(columns=["timestamp", "close", "target"], errors="ignore").fillna(0)
    explainer = shap.Explainer(model, features)
    shap_values = explainer(features)
    shap_sum = np.abs(shap_values.values).mean(axis=0)
    importance_df = pd.DataFrame({"feature": features.columns, "importance": shap_sum})
    return importance_df.sort_values("importance", ascending=False).head(top_n)

def llm_explain_signal(signal, context):
    """
    (Stub) Send a prompt to LLM (e.g. OpenAI GPT-4) for plain-language explanation.
    """
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Explain this trading signal in plain English:\nSignal: {signal}\nContext: {context}"
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content