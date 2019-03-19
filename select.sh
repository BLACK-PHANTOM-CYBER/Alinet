clear
blue='\033[34;1m'
green='\033[32;1m'  
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'                                           
yellow='\033[33;1m'
clear
figlet "          A L i N e t        " | lolcat
echo
echo $yellow"========================================"
echo $red"=            WEAPON DDOS               = "
echo $yellow"========================================"
echo $yellow"=         [1].PING OF DEAHT            ="
echo $yellow"=                                      ="
echo $yellow"=         [2].CRYPTO                   ="
echo $yellow"=                                      ="
echo $yellow"=         [3].LORIS                    ="
echo $yellow"========================================"
echo
echo $green"PILIH SALAH SATU WEAPON UNTUK PROSES LAUCH DDOS"
read -p "Weapon#>>>>>>" wea;
echo

if [ $wea = 1 ] || [ $wea = 1 ]
then
clear
python2 ddos1.py
fi


if [ $wea = 2 ] || [ $wea = 2 ]
then
clear
python2 cry.py
fi

if [ $wea = 3 ] || [ $wea = 3 ]
then
clear
perl LORIS.pl
fi

