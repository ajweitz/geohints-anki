#!/bin/bash

GEO_HINTS_URL=https://geohints.com/Bollards.html
TEMP_FILE=bollards_temp.html
TEMP_FILE2=bollards_temp2.html
TEMP_FILE3=bollards_temp3.html

# Leave just URLs and Country Names
curl $GEO_HINTS_URL | \
    tail -n +20 | \
    sed 's/\<img.*src="\(.*\)".*/\1/' | \
    sed  -E 's/<div.*>|<a .*|<h3 .*//' | \
    sed 's/<[^>]*>//g' | \
    sed -E 's/&#127757;|&nbsp//' | \
    sed 's/" alt.*//' | \
    sed 's/&Aring;land/Finland/' | \
    sed 's/ .*$//g'>$TEMP_FILE
START_POSITION=$(grep -n Sources/ $TEMP_FILE | awk -F : '{print $1}'  | head -n1 | awk '{print $1;}')
tail -n +$START_POSITION $TEMP_FILE>$TEMP_FILE2
rm $TEMP_FILE

# Remove empty lines
sed '/^$/d' $TEMP_FILE2>$TEMP_FILE3
rm $TEMP_FILE2