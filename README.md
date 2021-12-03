# 人生苦短，请用docker

## 自己构建

```bash
docker build -t zstu https://github.com/typenoob/zstuCOV19reporter.git#docker

```

## 用我的镜像

```bash
docker pull typenoob/zstu
docker run -d --name zstu --restart=always -p 5000:5000 -v /home/zstu:/srv/zstu typenoob/zstu

```

## 设置静态代理

```bash
docker pull typenoob/zstu
sed -i 's/proxy-server=*/=proxy-server=http://{host}:{port}/'
sed -i 's/#//'

```

## 使用动态代理

```bash
docker pull typenoob/zstu:proxy
docker run -d --name zstu --restart=always -p 5000:5000 -v /home/zstu:/srv/zstu typenoob/zstu:proxy

```



## 添加企业微信id

```bash
docker exec zstu sed -i '25s/=.*/="{id}"/' /bin/report

```


