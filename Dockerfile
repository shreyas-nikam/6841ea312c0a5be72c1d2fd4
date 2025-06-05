# ---- base ---------------------------------------------------
FROM python:3.12-slim
WORKDIR /app

# ---- dependencies ------------------------------------------
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# ---- app code ----------------------------------------------
COPY . .

# ---- config -------------------------------------------------
ENV PORT=8501
EXPOSE 8501                     # must be a concrete number

# ---- entrypoint ---------------------------------------------
# shell form expands $PORT; headless avoids opening browser
CMD bash -c "streamlit run app.py --server.port 8501 --server.headless true"
