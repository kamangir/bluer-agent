#! /usr/bin/env bash

function bluer_agent_voice_validate() {
    local options=$1
    local do_play=$(bluer_ai_option_int "$options" play 1)

    curl -X 'POST' \
        $BLUER_AGENT_VOICE_ENDPOINT \
        -H f"gateway-token: $BLUER_AGENT_VOICE_TOKEN" \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
  "text": "وزیر بهداشت در گفت و گو با ایسنا، آزمون دستیاری در کمال سلامت برگزار شد. هزار نفر در آزمون دستیاری امسال پذیرفته می شوند.",
  "speaker": "shahrzad",
  "speed": 1,
  "timestamp": false
}'
}
