echo "MASUKAN IP"
read ip
echo "MASUKAN PORT"
read port
echo "MASUKAN TURBO/KECEPATAN"
read turbo
echo
python ham.py -s $ip -p $port -t $turbo
