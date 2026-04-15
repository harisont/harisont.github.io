---
title: Frequently forgotten shell commands
layout: post
---

This is a growing (but eventually, hopefully, shrinking) collection of shell commands I periodically need but have to look up every time. 

- [Scheduling a shutdown](#scheduling-a-shutdown)
  - [At a specific time](#at-a-specific-time)
  - [After `n` minutes](#after-n-minutes)
- [Sending desktop notifications](#sending-desktop-notifications)
  - [At a specific time](#at-a-specific-time-1)
  - [After `n` minutes, hours, days, or weeks](#after-n-minutes-hours-days-or-weeks)
  - [Making the notification more (or less) annoying](#making-the-notification-more-or-less-annoying)
- [Spring cleaning](#spring-cleaning)
  - [Cleaning the Yay package cache](#cleaning-the-yay-package-cache)
  - [Cleaning up the pip package cache](#cleaning-up-the-pip-package-cache)
  - [Removing unused Python virtualenvs](#removing-unused-python-virtualenvs)
- [Copying files via ssh](#copying-files-via-ssh)
- [Text processing](#text-processing)
  - [Removing the diabolical non-unix newline characters](#removing-the-diabolical-non-unix-newline-characters)
- [Audio processing](#audio-processing)
  - [Splitting a flac file into tracks based on a cue file](#splitting-a-flac-file-into-tracks-based-on-a-cue-file)
- [Configuring the i3 window manager](#configuring-the-i3-window-manager)
  - [Figuring out the ID of a key (aka `keysym`)](#figuring-out-the-id-of-a-key-aka-keysym)
  - [Figuring out the class of a desktop application](#figuring-out-the-class-of-a-desktop-application)

## Scheduling a shutdown

### At a specific time
```bash
shutdown hh:mm
```

### After `n` minutes
```bash
shutdown +n
```

## Sending desktop notifications

### At a specific time
```bash
echo 'notify-send "notification text"' | at hh:mm
```

### After `n` minutes, hours, days, or weeks
```bash
echo 'notify-send "notification text"' | at now + n unit
```

### Making the notification more (or less) annoying

Use the `-u` flag:

```bash
notify-send "notification text" -u level # level: critical|normal|low
```

## Spring cleaning

### Cleaning the Yay package cache

```bash
yay -Scc
```

### Cleaning up the pip package cache

```bash
pip cache purge
```

### Removing unused Python virtualenvs
Use [Herb](https://github.com/daherb)'s heroic interactive one-liner:

```bash
for filename in $(find . -path '*/bin/activate.csh'); do filepath=$(echo $filename | sed 's/\/bin\/activate.csh//g'); echo "Remove $filepath? (y/n)" ; read result; if [[ $result = "y" ]]; then rm -R $filepath; fi; done
```

## Copying files via ssh
Use `scp`, which is just like `cp` but can take path to remote machines as well. 
For example, to copy a local file to a remote host:

```
scp scp -r loxal/path hostname:remote/path
```

## Text processing

### Removing the diabolical non-unix newline characters

```bash
tr -d '\r'
```

## Audio processing

### Splitting a flac file into tracks based on a cue file
```bash
shnsplit -f path/to.cue -t %n-%t -o flac path/to.flac
```

This particular command assumes that the flac is an album and that the cue file contains the names of its tracks, which will be written to files named `n-title.flac`.

## Configuring the i3 window manager
These are commands I only use when I edit the config file for my window manager, [i3](https://i3wm.org/), but they definitely have other use cases as well.

### Figuring out the ID of a key (aka `keysym`)
Run

```bash
xev | grep keysym
```

and then type something in the event window that will open. 
Every time you press a key, you will get some output like

```
state 0x2, keycode 133 (keysym 0xffeb, Super_L), same_screen YES,
```

(when you release the key, you will see a similar line with the same `keysym` again because `xev` detects two separate events, a `KeyPress` and a `KeyRelease`).

In this example, the keysym to use in the i3 config is `Super_L` (my left Windows key). 

### Figuring out the class of a desktop application
Open the application, run 

```bash
xprop | grep WM_CLASS
```

and then click on the application window. 
The output will be something like

```
WM_CLASS(STRING) = "vscodium", "VSCodium"
```

where the class to be used in the i3 config is the second one, `VSCodium`.