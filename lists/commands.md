---
title: Frequently forgotten shell commands
layout: post
---

- [Scheduling a shutdown](#scheduling-a-shutdown)
  - [At a specific time](#at-a-specific-time)
  - [After `n` minutes](#after-n-minutes)
- [Spring cleaning](#spring-cleaning)
  - [Cleaning the Yay package cache](#cleaning-the-yay-package-cache)
  - [Cleaning up the pip package cache](#cleaning-up-the-pip-package-cache)
  - [Removing unused Python virtualenvs](#removing-unused-python-virtualenvs)

## Scheduling a shutdown

### At a specific time
```bash
shutdown hh:mm
```

### After `n` minutes
```bash
shutdown +n
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
for filename in $(find . -path '*/bin/activate.csh'); do filepath=$(echo $filename | sed 's/\/bin\/activate.csh//g'); echo "Remove $filepath? (y/n)" ; read result; if [[ $result = "y" ]]; then rm -R $filepath; fi; done```