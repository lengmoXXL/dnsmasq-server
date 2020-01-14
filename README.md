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

![Screen Shot 2020-01-14 at 2 26 29 PM](https://user-images.githubusercontent.com/19929075/72319393-06054300-36da-11ea-87e7-352eb83868be.png)

![Screen Shot 2020-01-14 at 2 28 53 PM](https://user-images.githubusercontent.com/19929075/72319484-36e57800-36da-11ea-909c-55e54597b1b8.png)
