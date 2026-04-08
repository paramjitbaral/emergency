FROM python:3.11-slim

WORKDIR /app

COPY my_env /app/my_env
COPY inference.py /app/inference.py

RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -e /app/my_env

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/my_env

EXPOSE 7860

CMD ["uvicorn", "app.server.app:app", "--host", "0.0.0.0", "--port", "7860"]
