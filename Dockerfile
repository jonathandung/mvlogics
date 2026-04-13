FROM python:3.14.4-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONPATH="/Users/Jonathan Dung/mvlogics"
WORKDIR /Users/Jonathan Dung/mvlogics
COPY dist/*.tar.gz .
COPY dist/*.whl .
RUN pip install --no-cache-dir *.tar.gz
RUN python -c "import mvlogics"