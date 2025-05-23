#!/bin/sh

sply_path="$(dirname $(realpath "$0"))/.."

ai1_default="AI_1"
[ "$ai1" ] || {
    ai1="$ai1_default"
    }

ai2_default="AI_2"
[ "$ai2" ] || {
    ai2="$ai2_default"
    }

ai1_desc_default="is an LLM"
[ "$ai1_desc" ] || {
    ai1_desc="$ai1_desc_default"
    }

ai2_desc_default="is a different LLM",
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

