import os, argparse, json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]





def main():
    print("Hello from first-ai-agent!")
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call, verbose=False)
                messages.append(result_message)
                if not result_message["content"]:
                    raise Exception("Expected Content not Present")
                if result_message["tool_call_id"]:
                    print(f"-> {result_message['content']}")
        else:
            print(response.choices[0].message.content)
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")             
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")
            return
        if _ == 19:
            print("Model failed to return an acceptable answer")
        


if __name__ == "__main__":
    if api_key is None:
        raise RuntimeError("api key not found")    
    main()
