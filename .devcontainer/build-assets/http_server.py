# Simple wrapper for http.server
# to switch off caching for users
#
# Matt Rudge
# 20th April, 2023

import http.server


class NoCacheHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        """
        Overrides default end_headers method
        """
        self.send_cache_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_cache_headers(self):
        """
        New method to send cache control headers
        """
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")


if __name__ == '__main__':
    http.server.test(HandlerClass=NoCacheHTTPHandler)
