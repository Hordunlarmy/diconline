FROM python:3.12.3-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y curl screen netcat-openbsd libpq-dev python3-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# RUN pip install --no-cache-dir poetry

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

# Install dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

