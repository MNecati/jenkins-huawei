FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
RUN pip install Flask
EXPOSE 8081  # Portu 8081 olarak değiştirdim
CMD ["python", "app.py"]
