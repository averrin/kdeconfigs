#!/bin/bash
if [ "$(wmctrl -xl | grep qutebrowser)" != "" ] ; then
  QW=$(xdotool search --all --class qutebrowser | tail -1)
  echo "qute is here: $QW"
  xdotool windowactivate $QW
else
  echo "$(wmctrl -xl | grep qutebrowser)"
  qutebrowser
fi
