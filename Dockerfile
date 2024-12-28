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

#for step4:Build the docker image and run a container.
#docker build -t employee_stats_app .
#docker run -d -p 6080:6080 --name employee_stats_app  employee_stats_app