import fitz  # PyMuPDF
import openai
import time
from tqdm import tqdm

import fitz  # PyMuPDF
import openai
import time
from tqdm import tqdm
import json

# OpenAI 클라이언트 초기화 (openai>=1.0.0 방식)
from openai import OpenAI
client = OpenAI(api_key="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")  # 여기에 키 입력

# GPT 모델 설정
MODEL = "gpt-4o"

# Function calling용 함수 스펙 정의
functions = [
    {
        "name": "translate_text",
        "description": "Translate English text into Korean without summarizing.",
        "parameters": {
            "type": "object",
            "properties": {
                "translated": {
                    "type": "string",
                    "description": "The full Korean translation of the input text.",
                }
            },
            "required": ["translated"]
        }
    }
]

def extract_text_from_range(pdf_path, start_page, end_page):
    doc = fitz.open(pdf_path)
    extracted = []
    for i in range(start_page - 1, end_page):  # 페이지 번호는 0-indexed
        page = doc.load_page(i)
        text = page.get_text().strip()
        if text:
            extracted.append((i + 1, text))  # 페이지 번호 함께 저장
    return extracted

def call_translation_function(paragraph):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Translate the following English text into Korean. Do not summarize. But ignore the code blocks and tables."},
                {"role": "user", "content": paragraph}
            ],
            functions=functions,
            function_call={"name": "translate_text"},
        )
        args = json.loads(response.choices[0].message.function_call.arguments)
        return args.get("translated", "")
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""

def translate_selected_pages(pdf_path, start_page=206, end_page=210, output_path="translated_206_210.txt"):
    page_texts = extract_text_from_range(pdf_path, start_page, end_page)
    with open(output_path, "w", encoding="utf-8") as f:
        for page_num, text in tqdm(page_texts, desc="Translating pages"):
            if len(text.strip()) < 10:
                continue
            f.write(f"\n\n--- Page {page_num} ---\n")
            translated = call_translation_function(text)
            f.write(translated + "\n")
            time.sleep(1.5)

# 실행 예시
translate_selected_pages("Data Structures & Algorithms in Python.pdf", start_page=250, end_page=271)
