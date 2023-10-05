from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = Flask(__name__)

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print(device)

tokenizer = BertTokenizer.from_pretrained('./model')
model = BertForSequenceClassification.from_pretrained('./model')

model.eval()

class_dict = {
    0: 'Fashion',
    1: 'Крипта',
    2: 'Образовательный',
    3: 'Общее',
    4: 'Политика',
    5: 'Путешествия/релокация',
    6: 'Развлечения',
    7: 'Технологии',
    8: 'Финансы',
    9: 'Шоубиз',
    10: 'Энергетика'
}

@app.route('/processing_news', methods=['POST'])
def processing_news():
    try:
        data = request.get_json()
        news = data['text']

        result_dict = {'text': []}
        for text in news:
            inputs = tokenizer(text, add_special_tokens=True, return_tensors="pt", padding=True)

            with torch.no_grad():
                outputs = model(**inputs)

            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()

            result_dict['text'].append({
                'news_text': text,
                'category': class_dict.get(predicted_class)
            })

        return jsonify(result_dict), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)