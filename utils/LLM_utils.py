import os
import openai
import pickle
from collections import defaultdict
from utils.io.io_utils import add_to_log
import requests

def create_or_load_cache(cache_file):
    if not os.path.exists(os.path.dirname(cache_file)):
        # add_to_log(f"Creating directory for {cache_file}")
        os.makedirs(os.path.dirname(cache_file))

    cache: defaultdict[str, dict] = defaultdict(dict)
    if os.path.exists(cache_file):
        # add_to_log(f"loading cache from {cache_file}")
        cache = pickle.load(open(cache_file, "rb"))
    return cache


def query_LLM(prompt, stop_sequences, cache_file):
    cache = create_or_load_cache(cache_file)
    response = cache[prompt].get("gpt-4", None)
    if response is None:
        success = False
        max_retry = 3
        while not success and max_retry > 0:
            try:
                openai.api_base = "https://one-api.bltcy.top/v1"
                openai.api_key = "sk-xxx"
                response = openai.ChatCompletion.create(
                    model='gpt-4',
                    messages=[{'role':'system', 'content':prompt}],
                    temperature=1,
                    stop=stop_sequences,
                    max_tokens=3000
                )
                success = True
            except Exception as e:
                print("Error encountered")
                max_retry -= 1
                if max_retry == 0:
                    raise e
                else:
                    print(e)
        cache[prompt]["gpt-4"] = response
    pickle.dump(cache, open(cache_file, "wb"))
    response.text = response.choices[0].message['content']
    return response

# def query_LLM(prompt, stop_sequences, cache_file):
#     cache = create_or_load_cache(cache_file)
#     response = cache[prompt].get("gpt-4", None)
#     api_key = "sk-wgfnICtif7oeeCuZD3D2E3D09c7a43D6954a697eAb2b8dB7"
#     base_url = "https://one-api.bltcy.top/v1"
#     model_name = "gpt-4-turbo-2024-04-09"
#     temperature = 0.0
#     if response is None:
#         success = False
#         max_retry = 3
#         while not success and max_retry > 0:
#             try:
#                 headers = {
#                     "Content-Type": "application/json",
#                     "Authorization": f"Bearer {api_key}"
#                 }

#                 payload = {
#                     "model": model_name,
#                     "messages": [
#                         {   
#                             "role": "system",
#                             "content": prompt,
#                             "role": "assistant",
#                             "content": "",
#                             "role": "user",
#                             "content": "",
#                         }
#                     ],
#                     "temperature": temperature,
#                     "stop": stop_sequences,
#                     "max_tokens": 3000
#                 }
#                 response = requests.post(base_url+"/chat/completions", headers=headers, json=payload)
#                 print("inner response", response)
#                 response_json = response.json()
#                 success = True
#             except Exception as e:
#                 print("Error encountered", e)
#                 max_retry -= 1
#                 if max_retry == 0:
#                     raise e
#                 else:
#                     print(e)
#         cache[prompt]["gpt-4"] = response
#     pickle.dump(cache, open(cache_file, "wb"))
#     response.text = response_json['choices'][0]['message']['content']
#     print("response", response)
#     # response.text = response['choices'][0]['message']['content'],
#     return response



if __name__ == "__main__":
    prompt = 'say hi'
    stop_sequences = []
    cache_file = 'cache/llm_test_correction.pkl'
    response = query_LLM(prompt, stop_sequences, cache_file)
    print(response['usage'])
    print(response.choices[0].message['content'])
    print(response.text)