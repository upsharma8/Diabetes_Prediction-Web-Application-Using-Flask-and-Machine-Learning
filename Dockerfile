FROM centos:latest
WORKDIR /ws
RUN yum install python3 -y
RUN pip3 install flask 
RUN pip3 install keras 
RUN yum install gcc-c++ -y

RUN yum install python3-devel -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow --no-cache-dir  tensorflow
RUN pip3 install --upgrade tensorflow  
COPY diabetes_model.h5 /ws/
COPY web_app.py /ws/
COPY diabetes.html /ws/templates/
CMD python3 web_app.py
