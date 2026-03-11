FROM python:3.14-alpine
WORKDIR /usr/src/api
ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install --root-user-action=ignore --no-cache-dir -U fastapi uvicorn
COPY *.py *.json ./
EXPOSE 8888
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8888", "--workers", "2"]