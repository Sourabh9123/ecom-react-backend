FROM python:3.12.0

WORKDIR /ecommerce_project


COPY . .


RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

