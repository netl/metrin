#!/bin/bash

clear
echo watching $1

for (( ;; ))
do
   #wait for new file
   filepath=$(inotifywait -qr -e close --format %w%f $1)
   echo $filepath
   file=$(echo $filepath | awk -F/ '{print $NF}')
   name=$(echo $filepath | awk -F/ '{print $(NF - 1)}')
   echo $name uploaded $file

   #try to resize if filesize too large
   if (( $(stat --printf="%s" $filepath) > 1000000 )); then
      echo file too large
      if [[ $filepath == *.jpg ]]; then
         echo trying to reduce size for jpg
         mogrify -resize 1080x1080 -quality 70 $filepath
      fi
   fi

   #try to sync alkometri.elitedekkerz.net
   token=$(grep $name tokens | awk '{print $2}')
   if [ ! -z "$token" ]; then
      echo updating alkometri with token
      echo $(curl --header "Authorization: Bearer $token" https://alkometri.elitedekkerz.net/api/drinks/add/)
   fi
   echo ready
done
