FROM python:3.11-slim
WORKDIR /pymdbapi
COPY . .
RUN pip install .
CMD ["pymdbapi"]
