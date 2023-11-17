FROM cgr.dev/chainguard/python:latest-dev as build-env
WORKDIR /app
RUN pip3 install --no-cache-dir pip==23.3 setuptools==65.5.1
COPY app/requirements.txt .
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip3 list && sleep 20  

FROM cgr.dev/chainguard/python:latest
WORKDIR /app
COPY --from=build-env /home/nonroot/.local/lib/python3.11/site-packages /home/nonroot/.local/lib/python3.11/site-packages
COPY ../app/app.py .
COPY ../app/static/ static/
COPY ../app/templates/ templates/
#CMD ["app.py"]
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
