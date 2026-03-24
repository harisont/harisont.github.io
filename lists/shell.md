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
- [Spring cleaning](#spring-cleaning)
  - [Cleaning the Yay package cache](#cleaning-the-yay-package-cache)
  - [Cleaning up the pip package cache](#cleaning-up-the-pip-package-cache)
  - [Removing unused Python virtualenvs](#removing-unused-python-virtualenvs)
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

## Text processing

### Removing the diabolical non-unix newline characters

```bash
tr -d '\r'
```