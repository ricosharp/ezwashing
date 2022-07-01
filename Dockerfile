FROM python:3.10.5-alpine
WORKDIR /opt/ezwashing
COPY . /opt/ezwashing
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "run:app", "-w", "2", "-b", "0.0.0.0:8000"]
