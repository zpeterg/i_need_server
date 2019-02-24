FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
COPY code/ /code/