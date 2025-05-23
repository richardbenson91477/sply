#!/bin/sh

sply_path="$(dirname $(realpath "$0"))/.."

ai1_default="Geni"
[ "$ai1" ] || {
    ai1="$ai1_default"
    }

ai2_default="Desi"
[ "$ai2" ] || {
    ai2="$ai2_default"
    }

ai1_desc_default="is a programmer who wants to implement $ai2's designs. If any of $ai2's requests are unclear, $ai1 will ask for details; otherwise, $ai1 will use python and pygame, sharing source code for $ai2 to examine in the chat"
[ "$ai1_desc" ] || {
    ai1_desc="$ai1_desc_default"
    }

ai2_desc_default="is a brilliant designer who wants to create a game with code by $ai1. The game will use no external assets, so that it can be fully designed and tested during the chat. It will have a modern and original design, within reasonable limits. $ai2 will be clear and concise with feature requests and when answering any follow-up questions",
[ "$ai2_desc" ] || {
    ai2_desc="$ai2_desc_default"
    }

PYTHONPATH="$sply_path" \
  $sply_path/bin/sply_double_chat.py \
    c1_backend="llama-server" \
    c1_model_id="" \
    c1_hostname="localhost" \
    c1_port=8080 \
    c1_user_name="$ai2" \
    c1_user_desc="$ai2_desc" \
    c1_ai_name="$ai1" \
    c1_ai_desc="$ai1_desc" \
    c1_in_suffix="$ai1:" \
    c1_in_suffix_enabled="False" \
    c1_rev_prompt="$ai2:" \
    c1_temp=0.6 \
    c1_num_ctx=16384 \
    c2_backend="llama-server" \
    c2_model_id="" \
    c2_hostname="localhost" \
    c2_port=8081 \
    c2_user_name="$ai1" \
    c2_user_desc="$ai1_desc" \
    c2_ai_name="$ai2" \
    c2_ai_desc="$ai2_desc" \
    c2_in_suffix="$ai2:" \
    c2_in_suffix_enabled="False" \
    c2_rev_prompt="$ai1:" \
    c2_temp=0.9 \
    c2_num_ctx=16384 \
    "$@"

