# 1. Start with a lightweight, official Python environment
FROM python:3.12-slim

# 2. Create a working directory inside the container
WORKDIR /app

# 3. Copy our requirements file into the container
COPY requirements.txt .

# 4. Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our app code into the container
COPY . .

# 6. Hugging Face Spaces strictly requires web apps to listen on port 7860
EXPOSE 7860

# 7. Start the industrial server (Gunicorn) and bind it to port 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
