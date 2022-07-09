# squid-authentication-helper
squid authentication helper script

This is a proof-of-concept for squid authentication helper. Please feel free to edit for your own usage.

## Usage

Place the helper in /usr/local/bin and make it an executable
```bash
chmod +x squid-helper.py
```

Add the following lines in your squid.conf.
```
auth_param basic program /usr/local/bin/squid-helper.py
auth_param basic children 5
```

Restart your squid server
