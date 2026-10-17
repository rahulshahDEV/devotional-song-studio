#!/usr/bin/env python3
"""Probe a loopback Chromium debugging endpoint without reading browser tabs."""

import argparse
import ipaddress
import json
import sys
import urllib.error
import urllib.parse
import urllib.request


def loopback_endpoint(value):
    parsed = urllib.parse.urlsplit(value)
    try:
        local = parsed.hostname == 'localhost' or ipaddress.ip_address(
            parsed.hostname or ''
        ).is_loopback
    except ValueError:
        local = False
    try:
        port = parsed.port
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Invalid endpoint port') from exc
    if (parsed.scheme != 'http' or not local or port is None
            or parsed.username is not None or parsed.password is not None
            or parsed.path not in ('', '/') or parsed.query or parsed.fragment):
        raise argparse.ArgumentTypeError(
            'Use a loopback HTTP origin with an explicit port, e.g. http://127.0.0.1:9222'
        )
    return value.rstrip('/')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--endpoint', type=loopback_endpoint,
                        default='http://127.0.0.1:9222')
    args = parser.parse_args()
    # Ignore system proxies and redirects: inspect only the specified local endpoint.
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({}), NoRedirect()
    )
    try:
        with opener.open(args.endpoint + '/json/version', timeout=3) as response:
            raw = response.read(65537)
        if len(raw) > 65536:
            raise ValueError('Unexpectedly large version response')
        version = json.loads(raw)
        if not isinstance(version, dict):
            raise ValueError('Version response is not an object')
        websocket = urllib.parse.urlsplit(version.get('webSocketDebuggerUrl', ''))
        if not version.get('Browser') or websocket.scheme != 'ws' or not websocket.hostname:
            raise ValueError('Response does not expose a browser CDP websocket')
        # Do not print the websocket URL/session identifier.
        print(json.dumps({'status': 'available', 'endpoint': args.endpoint,
                          'browser': version['Browser'],
                          'protocol_version': version.get('Protocol-Version')}))
        return 0
    except (OSError, ValueError, urllib.error.URLError) as exc:
        print(json.dumps({'status': 'unavailable', 'endpoint': args.endpoint,
                          'reason': str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
