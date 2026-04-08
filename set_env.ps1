$env:HF_TOKEN = "hf_ATmRAthuExEpwZthGTdHnRLMkFLcYQKHYrt"
$env:API_BASE_URL = "https://api-inference.huggingface.co/v1"
$env:MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"
Write-Output "All variables set successfully!"
Write-Output $env:HF_TOKEN
Write-Output $env:API_BASE_URL
Write-Output $env:MODEL_NAME
