# Description
- A simple log parser for access log (E.g Apache access log) based on IP/CIDR

# Usage
- `--ip`: IP address or CIDR block (work with both v4 and v6). For instance, `192.168.23.1` or `192.168.3.0/24`
- `--file`: access log file location.

```
./bootstrap.sh
log_parser --ip 192.158.23.1 --file public_access.log
log_parser --ip 180.76.15.0/24 --file public_access.log
```

- check `output.txt`
# Test
```
py.test test/test_log_parser.py
```

# Contact
Binh Nguyen
