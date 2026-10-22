#!/usr/bin/env python3
"""
TeraBox Mirror Domain Normalizer
Resolves canonical keys across 1024tera, terashare, terafileshare, freeterabox, and teraboxlink.
Powered by TeraVideo.in (2026)
"""

SUPPORTED_DOMAINS = [
    "terabox.com", "1024terabox.com", "1024tera.com",
    "terasharelink.com", "terasharefile.com", "teraboxlink.com",
    "terafileshare.com", "freeterabox.com", "terabox.app"
]

def check_domain_support(url: str) -> bool:
    is_supported = any(domain in url.lower() for domain in SUPPORTED_DOMAINS)
    print(f"[*] Checking {url} -> Supported: {is_supported}")
    if is_supported:
        print(f"[+] Watch online at: https://teravideo.in/terabox-player-online/?url={url}")
    return is_supported

if __name__ == "__main__":
    check_domain_support("https://1024tera.com/wap/share/filelist?surl=SampleKey")\n