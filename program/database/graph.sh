RRDFILE=/home/joe/templogger/Wireless-XBee-Temperature-and-Humidity-Logger/program/database/crawlspace.rrd
WEBDIR=/var/www

rrdtool graph $WEBDIR/15min_temp_humid.png -a PNG --start -15minutes -w 1000 -h 250\
--title="Crawlspace Temperature and Humidity" \
"DEF:temp=$RRDFILE:temp:AVERAGE" \
"DEF:humidity=$RRDFILE:humidity:AVERAGE" \
"LINE1:temp#ff0000:Temperature" \
"LINE1:humidity#0000ff:Humidity\\r" \
"COMMENT:\\n"


rrdtool graph $WEBDIR/1day_temp_humid.png -a PNG --start -1day -w 1000 -h 250\
--title="Crawlspace Temperature and Humidity" \
"DEF:temp=$RRDFILE:temp:AVERAGE" \
"DEF:humidity=$RRDFILE:humidity:AVERAGE" \
"LINE1:temp#ff0000:Temperature" \
"LINE1:humidity#0000ff:Humidity\\r" \
"COMMENT:\\n"

rrdtool graph $WEBDIR/1month_temp_humid.png -a PNG --start -1month -w 1000 -h 250\
--title="Crawlspace Temperature and Humidity" \
"DEF:temp=$RRDFILE:temp:AVERAGE" \
"DEF:humidity=$RRDFILE:humidity:AVERAGE" \
"LINE1:temp#ff0000:Temperature" \
"LINE1:humidity#0000ff:Humidity\\r" \
"COMMENT:\\n"

rrdtool graph $WEBDIR/1year_temp_humid.png -a PNG --start -1year -w 1000 -h 250\
--title="Crawlspace Temperature and Humidity" \
"DEF:temp=$RRDFILE:temp:AVERAGE" \
"DEF:humidity=$RRDFILE:humidity:AVERAGE" \
"LINE1:temp#ff0000:Temperature" \
"LINE1:humidity#0000ff:Humidity\\r" \
"COMMENT:\\n"

rrdtool graph $WEBDIR/1day_voltage.png -a PNG --start -1day -w 1000 -h 250\
--title="Crawlspace Temperature and Humidity" \
"DEF:temp=$RRDFILE:supply_voltage:AVERAGE" \
"LINE1:temp#ff0000:Temperature" \
"COMMENT:\\n"


