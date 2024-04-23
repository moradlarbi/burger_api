FROM python:3.7

WORKDIR /app

# Install required packages
RUN pip install pymongo typing

COPY Burger.py /app/ 
COPY populate_db/populate_db.py /app/populate_db.py 

# Command to run the populate script
CMD ["python", "/app/populate_db.py"]
