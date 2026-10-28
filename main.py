import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from prompts import system_prompt

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]


def main():
    load_dotenv()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY is not set.")

    parser = argparse.ArgumentParser(description="AI agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    if response.usage is None:
        raise RuntimeError("error getting chat completion via OpenRouter.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message

    if message.tool_calls is not None:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            if args.verbose:
                print(f"-> {result_message['content']}")

    print("Response:")
    print(message.content)


if __name__ == "__main__":
    main()
