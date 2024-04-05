import os

import torch
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk

from textSummarizer.entity import ModelTrainerConfig




class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
        # self.corrected_model_ckpt = str(config.model_ckpt).replace("\\", "/")

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.corrected_model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Using TrainingArguments from the configuration directly
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, 
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=1,  
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, 
            save_steps=int(float(self.config.save_steps)),
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        ) 

        trainer = Trainer(
            model=model_pegasus, args=trainer_args,
            tokenizer=tokenizer, data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"], 
            eval_dataset=dataset_samsum_pt["validation"]
        )
        
        trainer.train()

        # Save model and tokenizer
        model_save_path = os.path.join(self.config.root_dir, "pegasus-samsum-model")
        tokenizer_save_path = os.path.join(self.config.root_dir, "tokenizer")
        model_pegasus.save_pretrained(model_save_path)
        tokenizer.save_pretrained(tokenizer_save_path)
