# using vllm image
import json
import random
from openai import OpenAI

def meditron_inference(path_to_prompts = '../results/parsed_prompts_tasks_x_topics.json', nbr_return_sequences = 10, temp = 0.9):
    # Open and read the JSON file
    with open(path_to_prompts, 'r') as file:
        data = json.load(file)
    sample = random.sample(data, 1)
    prompt = sample[0]["prompt"]
    print("****PROMPT****")
    print(prompt)
    print("***************")

    # Load LLM using OpenAI style API
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="token-abc123",
    )

    completion = client.chat.completions.create(
    model="epfl-llm/meditron-70b",
    messages=[
        {"role": "user", "content": prompt}
    ],
    n = nbr_return_sequences,
    temperature = temp
    )

    print(f"{nbr_return_sequences} responses:")
    for i in range(nbr_return_sequences):
            print(f"response {i}: {completion.choices[i].message}")

if __name__ == "__main__":
    from jsonargparse import CLI
    CLI(meditron_inference)
    