from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import torch

# 1. Force PyTorch to behave safely on a laptop CPU
torch.set_num_threads(2) 

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    device=-1, # <--- CRITICAL: -1 forces Hugging Face to use CPU instead of crashing on GPU checks
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of pakistan?")
print(result.content)