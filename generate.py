import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv('posts-quest.csv')

# เลือกข้อมูลที่ต้องการใช้สร้างข้อความ
text_data = df['Posts Facebook'].tolist()

# เลือกข้อความตัวอย่างหนึ่งเพื่อนำมาสร้างข้อความ
input_text = text_data[0]

# โหลดโมเดล GPT2 และโทเคนไนเซอร์
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text based on input text
output = model.generate(
    input_ids, 
    max_length=50, 
    num_return_sequences=3, 
    temperature=0.7, 
    do_sample=True
)

# Decode generated text
generated_texts = [tokenizer.decode(output_text, skip_special_tokens=True) for output_text in output]

# Print generated texts
for text in generated_texts:
    print(text)
