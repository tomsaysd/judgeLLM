# LLM Judge System

An intelligent web application that compares responses from different Large Language Models (GPT-4 and Gemini) and automatically judges which response is better based on accuracy, clarity, and reasoning.

## Features

* **Dual Model Comparison**: Compare GPT-4 and Gemini responses side-by-side
* **AI-Powered Judging**: Third AI model (Claude) evaluates and selects the winner
* **Attractive UI**: Gradient cards with smooth scrolling for long responses
* **Three-Stage Workflow**:

  1. Input prompt
  2. View both AI responses
  3. Get final judgment with detailed scoring
* **Session Management**: Seamless navigation between screens
* **Responsive Design**: Works on desktop and mobile browsers

## Architecture



```mermaid

flowchart TD



&#x20;   %% UI Layer

&#x20;   subgraph UI\["User Interface Layer (Streamlit - app.py)"]

&#x20;       A1\["Screen 1: Input Prompt"]

&#x20;       A2\["Screen 2: View Responses"]

&#x20;       A3\["Screen 3: Final Judge"]

&#x20;       A1 --> A2 --> A3

&#x20;   end



&#x20;   %% Orchestrator Layer

&#x20;   subgraph ORCH\["Orchestrator Layer (pipeline/)"]

&#x20;       B1\["Response Generator (generator.py)"]

&#x20;       B2\["Judge Engine (judge.py)"]

&#x20;   end



&#x20;   %% API Layer

&#x20;   subgraph API\["API Client Layer"]

&#x20;       C1\["OpenRouter Client Adapter"]

&#x20;   end



&#x20;   %% External Models

&#x20;   subgraph MODELS\["External LLMs (via OpenRouter)"]

&#x20;       D1\["GPT-4o-mini (OpenAI)"]

&#x20;       D2\["Gemini 3 Flash (Google)"]

&#x20;       D3\["Claude 3 Haiku (Anthropic)"]

&#x20;   end



&#x20;   %% Flow

&#x20;   A2 --> B1

&#x20;   B1 --> D1

&#x20;   B1 --> D2

&#x20;   D1 --> B2

&#x20;   D2 --> B2

&#x20;   B2 --> D3

&#x20;   D3 --> A3

&#x20;   B1 --> C1

&#x20;   B2 --> C1

## Tech Stack

|Component|Technology|
|-|-|
|Frontend/UI|Streamlit 1.56+|
|LLM API|OpenRouter (Unified API)|
|Models|GPT-4o-mini, Gemini 3 Flash, Claude 3 Haiku|
|Language|Python 3.13|
|Styling|CSS3 with gradients|
|Environment|python-dotenv|

## Installation

### Prerequisites

* Python 3.13 or higher
* OpenRouter API key ([Get one here](https://openrouter.ai/))

