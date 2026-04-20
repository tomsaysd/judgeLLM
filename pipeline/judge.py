from llm_clients.openrouter_client import get_response

def judge(prompt, responses):

    judge_prompt = f"""
You are an AI judge.

Prompt:
{prompt}

Response A:
{responses['A']}

Response B:
{responses['B']}

Evaluate:
- Accuracy
- Clarity
- Reasoning

Return:
Score A:
Score B:
Winner:
Explanation:
"""

    return get_response("anthropic/claude-3-haiku", judge_prompt)