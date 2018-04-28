sudo kill $(pgrep -f 'Image_capture2.py')

a=1
for i in /home/pi/Gecko_main/image_bin/*.jpg; do
  new=$(printf "%04d.jpg" "$a") #04 pad to lenght of 4
  mv -i -- "$i" "/home/pi/Gecko_main/image_bin/${new}"
  let a=a+1
done

DATE=$(date +"%Y-%m-%d-%H:%M")

/usr/bin/ffmpeg -r 12 -i /home/pi/Gecko_main/image_bin/%04d.jpg -r 12 -vcodec libx264 /home/pi/Gecko_main/video_bin/$DATE.mp4 &> ~/Gecko_main/logs/renderlogs/Renderlog_$DATE.txt 

sleep 60s #gives 60s delay, avoids render-upload conflict 

/usr/local/bin/youtube-upload --title=$DATE --description="Night timelapse of Crested Gecko in custom varvarium. Raspberry pi, NoIR Camera, 4 Channel Relay+36 IR LED Illuminator board"  --client-secrets=/home/pi/Gecko_main/client_secrets.json --credentials-file=/home/pi/.youtube-upload-credentials.json --playlist "Gek_vids" /home/pi/Gecko_main/video_bin/$DATE.mp4 &> ~/Gecko_main/logs/uploadlogs/uploadlog_$DATE.txt

sudo rm /home/pi/Gecko_main/image_bin/*.jpg 
sudo rm /home/pi/Gecko_main/video_bin/*.mp4



