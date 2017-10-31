# Logentries Envs

## About
The Logentries Python Handler does not provide a way to get `TOKEN` from a environment variable. This is a simple project that
gives you the ability to have Logentries Token read from a Environment variable.

## Install
To install this library, use the following command:

``pip install logentries-envs``

## Usage

Considering the following code on file cool_log.py

``` python
    #!/usr/bin/env python

    import logging
    from leenvs import LogentriesHandler


    log = logging.getLogger('logentries')
    log.setLevel(logging.INFO)
    test = LogentriesHandler()

    log.addHandler(test)

    log.warn("Warning message")
    log.info("Info message")

    sleep(10)
```

``` bash
 $ export LOGENTRIES_TOKEN="1234-1234-1234-1234"
 $ python cool_log.py
```