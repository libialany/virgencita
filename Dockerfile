FROM python
LABEL authors="Libia E."

WORKDIR /app


COPY ./setup.py /app/setup.py
COPY ./src /app/src
RUN python3 setup.py install

EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["/app/src/main.py"]