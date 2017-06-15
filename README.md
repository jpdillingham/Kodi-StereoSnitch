# Kodi-StereoSnitch

A Python script which searches a directory of files for Kodi metadata and reports any files with a stereo (two channel) audio track.

## Why?

Certain files were making their way into my collection with 2 channel audio tracks, while my preferred format is AC3 or DTS 6 channel.  I couldn't find a
quick and easy way to identify these files, so I wrote this script.  

## Usage

Download and install Python 3.x.  From a command line:

```
python stereosnitch.py <path\to\kodi\TV\>
```

Note that the script is intended for NFOs matching TV episodes.