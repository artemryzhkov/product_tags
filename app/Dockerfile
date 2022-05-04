FROM python:3.9 AS builder

WORKDIR /app/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download de_core_news_lg

FROM builder AS final
WORKDIR /app/
COPY src .

CMD [ "python", "./main.py" ]