FROM markadams/chromium-xvfb-py2
ADD ./crontask /etc/cron.d/crontask
WORKDIR /srv/zstu
COPY * ./
COPY templates/index.html ./templates/index.html

RUN apt-get -y install jq
RUN apt-get -y install cron

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && echo "#!/bin/sh\n" > /home/boot.sh \
    && echo "service cron start" >> /home/boot.sh \
    && echo "\n" >> /home/boot.sh \
    && echo "flask run --host=0.0.0.0" >> /home/boot.sh \
    && echo "\n" >> /home/boot.sh \
    && echo "/bin/bash" >> /home/boot.sh \
    && cp run.sh /bin/report

WORKDIR /srv/zstu
CMD [ "/bin/bash", "/home/boot.sh" ]
