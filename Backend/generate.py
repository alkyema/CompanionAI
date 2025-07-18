import torch 
import transformers
from time import time
from torch import cuda, bfloat16
model_id = r"C:\Users\satwi\Downloads\CompanionAI\merged_model"

device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
print(device)

bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=bfloat16, 
)

time_start = time()
model_config = transformers.AutoConfig.from_pretrained(
    model_id,
    trust_remote_code=True,
    max_new_tokens=1024
)
model = transformers.AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    config=model_config,
    quantization_config=bnb_config,
    device_map='cuda:0',
)  
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
time_end = time()
print(f"Prepare model, tokenizer: {round(time_end-time_start, 3)} sec.")

query_pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        max_length=1024,
        device_map="auto"
)

def generate_response(input_text):
    time_start = time()
    print("called")

    sequences = query_pipeline(
        input_text,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_length=200,
    )


    for seq in sequences:
        parts = seq['generated_text'].split('\n', 1)
        if len(parts) > 1:
            cleaned_text = parts[1]
        else:
            cleaned_text = ''  

        print(cleaned_text)
        return "It is important to recognize that these feelings are not a reflection of your worth as a person, and that there are many people who care about you and want to help."
    time_end = time()
    print(f"Prepare model, tokenizer: {round(time_end-time_start, 3)} sec.")
    

