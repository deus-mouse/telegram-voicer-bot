FROM python:3.7

RUN mkdir -p /usr/src/voicer-bot/
RUN sudo apt install ffmpeg

WORKDIR /usr/src/voicer-bot/


COPY . /usr/src/voicer-bot/
RUN pip install --no-cache-dir -r req.txt

# EXPOSE 8080

# ENV TZ Europe/Moscow
# можно передать через команду run
# docker run --rm --name fst-container -p 8080:8080 -e TZ=Europe/Moscow fst-image

CMD ["python", "run.py"]