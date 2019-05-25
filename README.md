# holistic


## Установка зависимостей
```
pip install pip-tools
make install
npm install admin-lte --save
```

Сбор статики
```
python holistic/manage.py collectstatic
```

## Дополнительные команды

Автоматическое форматирование кода
```
make format
```

Запуск локального сервера
```
make run
```


## Шаблоны
Документация
```
https://adminlte.io/docs/2.4/installation
```

Базовый шаблон
```
https://adminlte.io/themes/AdminLTE/starter.html
```


## Описание набора данных

Участникам хакатона будет предоставлен архив текстов  за 2018 год. 
Данный архив содержит около 30 миллионов документов Public.ru 
российских печатных СМИ и новостных сайтов. Каждый документ содержит метаданные и полный текст. 
Метаданные включают: заголовок, автор, издание, дата публикации и др. Полный текст представлен в формате XML 
(с частичным сохранением форматирования), а также в виде plain-text с разбивкой по предложениям и абзацам. 
Документы проиндексированы в базе Elasticsearch (общий объем данных около 300 GB). 
Участникам будет предоставлен доступ к базе  на чтение через стандартный REST API Elasticsearch.


## Доступ к API

Сервер: https://hackaton-elk.public.ru/

Логин: elastic

Пароль: ASLlsdf8jf0lNdas)

```python
from elasticsearch import Elasticsearch
es = Elasticsearch(
    ["http://elastic:ASLlsdf8jf0lNdas)@hackaton-elk.public.ru"],
    send_get_body_as='POST'
)
```


## Описание индексов

Индекс public_edition содержит описание 16877 изданий

Индексы документов: public_doc_pd_y2018_1_v2 и public_doc_pd_y2018_2_v2 содержат в общей сложности 33206576 документов. 

Связь с индексом public_edition через поле edition_id.

Алиас public_doc_alias_pd_all позволяет искать по всем документам.


## Поиск по изданиям
```
http --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_edition/_mapping

http --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_edition/_settings

http --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_edition/_count

http --auth='elastic:ASLlsdf8jf0lNdas)' POST https://hackaton-elk.public.ru/public_edition/_search query:='{"match": {"name": "RBC"}}'
```

## Поиск по документам
```
http -v --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_doc_alias_pd_all/_mapping

http -v --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_doc_alias_pd_all/_settings

http -v --auth='elastic:ASLlsdf8jf0lNdas)' GET https://hackaton-elk.public.ru/public_doc_pd_y2018_1_v1/_count

$ http -v --auth='elastic:ASLlsdf8jf0lNdas)' POST https://hackaton-elk.public.ru/public_doc_pd_y2018_1_v1/_search query:='{"match": { "body":"Penza" }}'
```

```python
from elasticsearch import Elasticsearch
es = Elasticsearch(
    ["http://elastic:ASLlsdf8jf0lNdas)@hackaton-elk.public.ru"],
    send_get_body_as='POST'
)
start = 1
stop = 2
index = "public_doc_alias_pd_all"
search_body_pub_date = {
    "query": {
        "range": {
            "pub_date": {
                "lt": start,
                "gt": stop,
            }
        }
    }
}
res = es.search(index=index, body=search_body_pub_date)

```




