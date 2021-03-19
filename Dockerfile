# docker build -t hello-world-lambda .
# docker run -p 9001:8080 --rm hello-world-lambda

# FROM public.ecr.aws/lambda/python:3.8
FROM amazon/aws-lambda-python:3.8


ENV LAMBDA_TASK_ROOT=/var/task

COPY app.py ${LAMBDA_TASK_ROOT}
CMD ["app.handler"]
