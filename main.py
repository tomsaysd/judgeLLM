from pipeline.generator import generate_responses
from pipeline.judge import judge

def main():
    prompt = input("Enter your prompt: ")

    print("\nGenerating responses...\n")
    responses = generate_responses(prompt)

    print("Response A (GPT):\n", responses["A"], "\n")
    print("Response B (Gemini):\n", responses["B"], "\n")

    print("Judging...\n")
    result = judge(prompt, responses)

    print("FINAL RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()