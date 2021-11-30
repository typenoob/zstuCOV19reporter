# 人生苦短，请用docker

```bash
docker build -t zstu https://github.com/typenoob/zstuCOV19reporter.git#docker

```

```bash
docker pull typenoob/zstu
docker run -d --name zstu --restart=always -p 5000:5000 typenoob/zstu

```

```bash
docker exec zstu sed -i '25s/=.*/="yourid"/' /bin/report

```


