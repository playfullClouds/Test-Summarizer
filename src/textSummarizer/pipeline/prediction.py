from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from pathlib import Path


CONFIG_FILE_PATH = Path('C:/Test-Summarizer/config/config.yaml')  
PARAMS_FILE_PATH = Path('C:/Test-Summarizer/params.yaml')


class PredictionPipeline:
    def __init__(self):
        
        self.config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH).get_model_evaluation_config()
        
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8, 
            "num_beams": 8, 
            "max_length": 128
            }
        
        # pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        
        pipe = pipeline("summarization", model=str(self.config.model_path), tokenizer=tokenizer)

        # print(f"Model path: {self.config.model_path} (Type: {type(self.config.model_path)})")

        
        print("Dialogue:")
        print(text)        
        
        output = pipe(text, **gen_kwargs)[0]['summary_text']
        print("\nModel Summary:")
        print(output)
        
        return output