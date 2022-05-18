FROM python:3.9

WORKDIR /opt

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

COPY app app/.

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# CMD ["gunicorn", "app:app", "-b 0.0.0.0:5000", "-w 2"]