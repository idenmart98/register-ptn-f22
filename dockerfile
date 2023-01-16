FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /registration
COPY req.txt /registration/
RUN pip install -r req.txt
COPY . /registration/