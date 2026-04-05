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