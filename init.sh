mkdir -p ./conf/dnsmasq/hosts

touch ./conf/dnsmasq/hosts/dnsmasqhosts
echo "nameserver 114.114.114.114" > ./conf/dnsmasq/resolv.dnsmasq
echo "nameserver 8.8.8.8" >> ./conf/dnsmasq/resolv.dnsmasq

echo "resolv-file=/etc/dnsmasq.d/resolv.dnsmasq" > ./conf/dnsmasq/dnsmasq.conf
