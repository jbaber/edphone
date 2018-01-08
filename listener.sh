#!/usr/bin/env bash

COUNTER=1
SOFAR=""
while true; do
  read -r -s -t 0.5; RETVAL=$?
  [ $RETVAL -eq 0 ] && echo -E "$REPLY" && SOFAR="$SOFAR"$'\n'"$REPLY" && continue
  if [ "$SOFAR" ]; then
    echo "$SOFAR" > $(printf "%03d.txt" $COUNTER)
    COUNTER=$(($COUNTER + 1))
    SOFAR=""
  fi
  # no timeout ? (EOF or error) break
  [ $RETVAL -gt 128 ] || break
done
