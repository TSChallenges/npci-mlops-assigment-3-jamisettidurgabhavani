# Docker file
# pull python base image with given instruction as python:3.9-slim
FROM python:3.9-slim

# add requirements file & trained model
ADD employee_stats_app.py dataset.csv requirements.txt  .

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# add application file
ADD employee_stats_app.py .

# expose port where your application will be running
EXPOSE 6080

# start application
CMD ["python", "employee_stats_app.py"]