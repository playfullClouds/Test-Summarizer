# CONFIG_FILE_PATH = Path('C:/Test-Summarizer/config/config.yaml')  
# PARAMS_FILE_PATH = Path('C:/Test-Summarizer/params.yaml')


# CONFIG_FILE_PATH = "/app/config/config.yaml"
# PARAMS_FILE_PATH = "/app/config/params.yaml"



# # Assuming you've set environment variables for these paths
# CONFIG_FILE_PATH = Path(os.getenv('CONFIG_FILE_PATH', './config/config.yaml'))
# PARAMS_FILE_PATH = Path(os.getenv('PARAMS_FILE_PATH', './config/params.yaml'))

from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from pathlib import Path
import os

# Determine the environment (Windows or Linux)
if os.name == 'nt':  # Windows environment
    CONFIG_FILE_PATH = Path('C:/Test-Summarizer/config/config.yaml')  
    PARAMS_FILE_PATH = Path('C:/Test-Summarizer/params.yaml')
else:  # Linux environment (assumed)
    CONFIG_FILE_PATH = Path('/app/config/config.yaml')  
    PARAMS_FILE_PATH = Path('/app/params.yaml')


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH).get_model_evaluation_config()
        
    def predict(self, text, max_length):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8, 
            "num_beams": 8, 
            "min_length": 20,
            "max_length": max_length
        }
        
        # Adjusting model path based on the environment
        if os.name == 'nt':  # Windows environment
            model_path = self.config.model_path
        else:  # Linux environment (assumed)
            # Convert Linux path to POSIX path
            model_path = self.config.model_path.as_posix()
        
        pipe = pipeline("summarization", model=model_path, tokenizer=tokenizer)
        
        print("Dialogue:")
        print(text)  
        print("\n\n")      
        
        output = pipe(text, **gen_kwargs)[0]['summary_text']
        print("\nModel Summary:")
        print(output)
        
        return output

