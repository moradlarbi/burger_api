FROM python:3.7

WORKDIR /app
RUN pip install pymongo fastapi pydantic uvicorn typing

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]