 while true;
 do
 	sudo tcpdump -c 1000 -nnvvSs 1564 -A > packet_capture.txt &
	sleep 3
	sudo kill $!
	python3 kitivela_2020.py
done
