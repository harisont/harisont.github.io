---
title: Nodenotes
layout: post
---

Modern web dev stuff I'm (reluctantly) learning.

- [Setting up `nvm` (Node Version Manager)](#setting-up-nvm-node-version-manager)
- [Installing version `n` of Node](#installing-version-n-of-node)
- [Using version `n` of Node](#using-version-n-of-node)
- [Installing a TypeScript project](#installing-a-typescript-project)
- [Using a local module in a TypeScript project](#using-a-local-module-in-a-typescript-project)


## Setting up `nvm` (Node Version Manager)
1. install `nvm` from your package manager
2. add
   ```
    . /usr/share/nvm/init-nvm.sh
   ```
   to the shell config file.


## Installing version `n` of Node
```
nvm install n
```

## Using version `n` of Node
```
nvm use n
```

## Installing a TypeScript project
```
npm install
```

## Using a local module in a TypeScript project
1. package the module into a `.tgz`:
   ```
   npm pack
   ```
2. move to the project folder and install the package:
   ```
   npm install --save PATH-TO-TGZ
   ```