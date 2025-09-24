import google.generativeai as genai
genai.configure(api_key="AIzaSyDsndhQ3rucYWzivfdZWHsmQFAPN4D1CBI")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Supported Model: {model.name}")