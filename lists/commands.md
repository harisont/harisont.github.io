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
yay -Scc
```

### Removing unused Python virtualenvs
1. list all virtualenvs: 
   ```bash
   locate -b '\activate' | grep "/home" | sed -e 's/bin.*//g' | uniq
   ```
2. ...remove the unused ones manually. I tried to add `| xargs rm -ir` for interactively removing them one by one, but [that doesn't work](https://stackoverflow.com/questions/18302856/removing-files-interactively-with-find-and-xargs/18302893#18302893). I understand the reason, but not the alternative solution(s)