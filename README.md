# CR 2 team

## Решение задачи

1. Был проведена ручная разметка данных(классов) - выборка из 1080 новостей
2. На этих данных была обучена модель Multilingual-BERT


## Инструкция по запуску
Перейти по ссылке на Gitlab и скачать содержимое: https://git.codenrock.com/ai-news-hack/cnrprod-team-52934/news-classification.git

Запуск происходит в docker

1. Необходимо выполнить команду ```docker build -t ai-news```
2. Необходимо выполнить команду ```docker run ai-news```
3. В докер контейнере поднимется Flask API на порту 5000

## API
Апи принимает на вход:

{host}/processing_news   POST
```
{
    "text": ["news_1", "news_2", "news_3", ...]
}
```

На выходе получаем:
```
{
    "text": [
        {"news_text": "news_1", "category": "news_category_1"},
        {"news_text": "news_2", "category": "news_category_2"}
        {"news_text": "news_3", "category": "news_category_3"}
    ]
}
```

