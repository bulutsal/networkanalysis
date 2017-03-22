#!/bin/bash 
# format nfcapd.201211062105
#-t <time>       time window for filtering packets
#                yyyy/MM/dd.hh:mm:ss[-yyyy/MM/dd.hh:mm:ss]

source="2013-03-10.dump";

#for i in {0..1440..5} 
for i in {0..35..5} 
	do
	start=$(date --date="2013/03/10 +$i min -5 min" +%Y/%m/%d.%H:%M:00);
	end=$(date --date="2013/03/10 +$i min" +%Y/%m/%d.%H:%M:00);
	dirname=$(date --date="2013/03/10 +$i min" +./%Y/%m/%d/);
	mkdir -p $dirname;
	filename=nfcapd.$(date --date="2013/03/10 +$i min" +%Y%m%d%H%M)
	if [ -f $dirname$filename ]
	then
		echo "++ nfdump -r$source -t$start-$end -w $dirname$filename"; 
	else 
		echo "nfdump -r$source -t$start-$end -w $dirname$filename"; 
		nfdump -r$source -t$start-$end -w $dirname$filename; 
	fi;

	done;
