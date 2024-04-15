FROM python:3.9

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the necessary ports
EXPOSE 5001 8501

# Run Flask and Streamlit
CMD ["sh", "-c", "python src/main.py & streamlit run --server.port 8501 streamlit_app.py"]
