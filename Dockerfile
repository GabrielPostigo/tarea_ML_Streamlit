FROM python:3.8
RUN pip install pandas scikit-learn streamlit
COPY src/app.py /app/
COPY model/stroke_model.pkl /app/model/stroke_model.pkl
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]