#!/bin/bash
API_URL="https://available-after-deploymenet.ngrok-free.app/api/send"  
AUTHORIZATION="PUT_YOUR_AUTHORIZATION_CODE_PROVIVED_BY_BOT"             
SCREENSHOT_PATH="/tmp/screenshot.png"

scrot $SCREENSHOT_PATH

response=$(curl -s -o /tmp/response.txt \
    -H "Authorization: $AUTHORIZATION" \
    -F "file=@${SCREENSHOT_PATH}" \
    $API_URL)

if [ "$response" -eq 200 ]; then
  echo "Screenshot sent successfully."
else
  echo "Failed to send screenshot. API response code: $response"
  cat /tmp/response.txt
fi

rm $SCREENSHOT_PATH
echo "Screenshot process complete."

