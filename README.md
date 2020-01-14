# dnsmasq-server
Django server to maintain hosts for dnsmasq

## Install

Create basic config files for dnsmasq
```shell script
bash ./init.sh
```

Start service
```shell script
docker-compose up -d
```

```shell script
docker-compose exec server python manage.py createsuperuser
```

The Django migrations will run automatically. The django server will listen port 8000.

So you can visit http://<your-ip>:8000 to visit the website.

the modification of hosts file will be applied by dnsmasq in several seconds.
