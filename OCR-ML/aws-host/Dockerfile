# 1 
FROM python:3.9

# 3
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip3 install -r requirements.txt

# Install required libraries
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Install required Python modules
RUN pip install opencv-python

COPY . .

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y tesseract-ocr-all 
# To make sure that tesseract-ocr is installed, uncomment the following line.  
RUN tesseract --version

# 4
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
