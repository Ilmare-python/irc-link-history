FROM python:3.9.0-alpine

WORKDIR /usr/src/app

COPY requirements.txt main.py  history.dtek.db ./

RUN pip install --no-cache-dir -r requirements.txt

#use "-i <corporate_repo_link>" in above line if needed in your org
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
