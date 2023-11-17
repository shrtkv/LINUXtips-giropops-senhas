FROM python:3.9 as build-env
WORKDIR /app
COPY ../app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian10
WORKDIR /app
COPY --from=build-env /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY ../app/app.py .
COPY ../app/static/ static/
COPY ../app/templates/ templates/
CMD ["app.py"]

