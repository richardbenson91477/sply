#!/bin/sh

sply_path="$(dirname $(realpath "$0"))/.."

export ai1="Peng"
export ai2="Desi"

export ai1_desc="is a prompt engineer who wants to form $ai2's designs into a programming prompt for an LLM. If any of $ai2's requests are not entirely clear, $ai1 will ask for details; otherwise, $ai1 will use markdown, sharing specs for $ai2 to review in the chat"

export ai2_desc="wants to design a single-file pygame using a prompt crafted by $ai1. It will have a modern and original design. $ai2 will try to be clear and concise with feature requests and when asking or answering follow-up questions"

$sply_path/examples/double_chat_examples.sh

