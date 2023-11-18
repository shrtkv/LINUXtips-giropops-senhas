FROM cgr.dev/chainguard/python:latest-dev as build-env
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest
WORKDIR /app
COPY --from=build-env /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages

COPY --from=build-env /home/nonroot/.local/bin  /home/nonroot/.local/bin
#ENV PATH=$PATH:/home/nonroot/.local/bin
COPY app/app.py .
COPY app/templates templates/
COPY app/static static/
ENTRYPOINT ["python", "app.py", "--host=0.0.0.0"]
