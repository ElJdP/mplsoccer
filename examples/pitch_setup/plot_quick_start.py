"""
===========
Quick start
===========
"""
from mplsoccer import Pitch
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()
