# 
FROM python:3.11.4

# 
WORKDIR /code/app

# 
COPY ./requirements.txt /code/app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

# 
COPY ./ /code/app
#
Expose 8000
# 
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port", "8000"]
