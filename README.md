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

\## Architecture Diagram



```mermaid

graph TD

&#x20;   A\[User Input] --> B\[Streamlit UI]

&#x20;   B --> C\[Response Generator]

&#x20;   C --> D\[GPT-4o-mini]

&#x20;   C --> E\[Gemini 3 Flash]

&#x20;   D --> F\[Display Responses]

&#x20;   E --> F

&#x20;   F --> G\[Judge Engine]

&#x20;   G --> H\[Claude 3 Haiku]

&#x20;   H --> I\[Final Judgment]

&#x20;   

&#x20;   style A fill:#667eea,stroke:#333,stroke-width:2px

&#x20;   style B fill:#f093fb,stroke:#333,stroke-width:2px

&#x20;   style C fill:#4ecdc4,stroke:#333,stroke-width:2px

&#x20;   style G fill:#4ecdc4,stroke:#333,stroke-width:2px

&#x20;   style I fill:#ff6b6b,stroke:#333,stroke-width:2px

```

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

