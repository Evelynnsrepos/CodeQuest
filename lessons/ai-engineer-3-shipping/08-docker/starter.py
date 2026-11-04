def lint(dockerfile):
    return []


DOCKERFILE = """FROM python
COPY . .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY=sk-123
CMD ["uvicorn", "main:app"]
"""

DOCKERIGNORE = ""

print(lint(DOCKERFILE))
