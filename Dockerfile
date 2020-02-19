FROM python:3.8.1-buster

RUN pip install spacy
RUN python -m spacy download en_core_web_sm

WORKDIR /app
COPY strip_description.py .

CMD ["python", "strip_description.py"]
