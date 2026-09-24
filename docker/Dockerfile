FROM python:3.11-slim
WORKDIR /service
COPY app/requirements.txt /service/requirements.txt
RUN pip install --no-cache-dir -r /service/requirements.txt
COPY app/ /service/app/
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
