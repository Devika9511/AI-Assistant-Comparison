# AI Assistant Comparison

## Overview

This project compares two AI personal assistants:

### 1. Open Source Assistant

* Model: Qwen2.5-0.5B
* Deployment: Ollama
* Interface: Streamlit

### 2. Frontier Model Assistant

* Model: Gemini 2.5 Flash
* Deployment: Google AI Studio API
* Interface: Streamlit

Both assistants support:

* Multi-turn conversations
* Short-term conversational memory
* Safety guardrails
* Assistant-style interactions

---

## Project Structure

```text
AI-Assistant-Comparison/
├── assistants/
├── evaluation/
├── guardrails/
├── memory/
├── observability/
├── screenshots/
├── report/
├── app.py
├── requirements.txt
├── README.md
```

---

## Architecture

User → Streamlit UI → Safety Guardrail → Memory Layer → Assistant

### OSS Assistant

User → Streamlit → Ollama → Qwen2.5

### Frontier Assistant

User → Streamlit → Gemini API

---

## Setup Instructions

### Clone Repository

```bash
git clone <repo-url>
cd AI-Assistant-Comparison
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start Ollama

```bash
ollama pull qwen2.5:0.5b
```

### Run Streamlit

```bash
python -m streamlit run app.py
```

---

## Evaluation Methodology

The assistants were evaluated on:

1. Factual Accuracy
2. Bias & Harmful Outputs
3. Content Safety
4. Jailbreak Resistance

Test prompts were stored inside:

```text
evaluation/
```

---

## Results

| Category         | Qwen | Gemini |
| ---------------- | ---- | ------ |
| Factual Accuracy | 4/5  | 5/5    |
| Bias Handling    | 4/5  | 5/5    |
| Safety           | 5/5  | 5/5    |

---

## Tradeoffs

### Qwen

Advantages:

* Local deployment
* Privacy preserving
* No API cost

Limitations:

* Less accurate
* Slower responses

### Gemini

Advantages:

* Better reasoning
* Better factual accuracy
* Better structured responses

Limitations:

* Requires API access
* Internet dependency

---

## Future Improvements

* Long-term memory
* Vector database integration
* RAG support
* Advanced guardrails
* Monitoring dashboard
* Cloud deployment

---

## Recommendation

Gemini is recommended for production-quality reasoning and factual accuracy.

Qwen is recommended for privacy-sensitive and low-cost deployments.
