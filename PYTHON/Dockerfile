FROM python

WORKDIR /test

COPY ./test.py .
COPY ./paragraphs.txt .

RUN pip install nltk

CMD ["python", "test.py"]
