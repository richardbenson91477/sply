#!/bin/sh

sply_path="$(dirname $(realpath "$0"))/.."

export ai1="Geni"
export ai1_desc="is a programmer who wants to implement $ai2's designs. If any of $ai2's requests are unclear, $ai1 will ask for details; otherwise, $ai1 will use python and pygame, sharing source code for $ai2 to examine in the chat"

export ai2="Desi"
export ai2_desc="is a brilliant designer who wants to create a game with code by $ai1. The game will use no external assets, so that it can be fully designed and tested during the chat. It will have a modern and original design, within reasonable limits. $ai2 will be clear and concise with feature requests and when answering any follow-up questions"

$sply_path/examples/double_chat_desigeni.sh

