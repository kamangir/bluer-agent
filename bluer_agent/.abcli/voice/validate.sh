#! /usr/bin/env bash

function bluer_agent_voice_validate() {
    local options=$1
    local do_play=$(bluer_ai_option_int "$options" play 1)

    curl -X 'POST' \
        $BLUER_AGENT_VOICE_ENDPOINT \
        -H "gateway-token: $BLUER_AGENT_VOICE_TOKEN" \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
  "text": "سلام، من رنگین هستم. چطور می‌تونم کمکتون کنم؟",
  "speaker": "shahrzad",
  "speed": 1,
  "timestamp": false
}'
}
