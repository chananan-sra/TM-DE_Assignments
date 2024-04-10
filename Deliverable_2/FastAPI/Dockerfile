FROM python:3.10-slim
WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --ignore-installed uvicorn==0.29.0

COPY . .

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
