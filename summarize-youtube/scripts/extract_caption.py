#!/usr/bin/env python3
"""
Extract captions from YouTube video using yt-dlp.
Usage: python3 extract_caption.py <youtube_url> <output_dir>
"""

import sys
import os
import subprocess
import re
import json
import urllib.request


def get_video_title(url):
    """Get YouTube video title."""
    try:
        result = subprocess.run(
            ['python3', '-m', 'yt_dlp', '--get-title', '--no-playlist', url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            title = result.stdout.strip()
            # Clean filename: remove invalid characters
            title = re.sub(r'[<>:"/\\|?*]', '', title)
            title = title[:100]  # Limit length
            return title
    except Exception as e:
        print(f"Error getting title: {e}", file=sys.stderr)
    return "video"


def extract_captions(url, output_dir):
    """Extract captions from YouTube video."""
    # Get video title first
    title = get_video_title(url)
    print(f"Video title: {title}", file=sys.stderr)

    # Try to detect language and get auto-generated captions
    try:
        # First, try to get available languages
        result = subprocess.run(
            ['python3', '-m', 'yt_dlp', '--list-subs', '--no-playlist', url],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Look for available auto-generated languages
        available_langs = []
        if 'Available' in result.stderr or 'Available' in result.stdout:
            output = result.stderr + result.stdout
            # Look for language codes in the output
            lang_pattern = r'(\w{2,3})\s*\('
            matches = re.findall(lang_pattern, output)
            available_langs = list(set(matches))

        print(f"Available languages: {available_langs}", file=sys.stderr)

        # Try to get auto-generated captions in available language
        # Default to 'en' but try detected languages
        langs_to_try = ['en', 'th', 'ja', 'ko', 'es', 'fr', 'de'] + available_langs

        for lang in langs_to_try:
            try:
                print(f"Trying language: {lang}", file=sys.stderr)
                subprocess.run(
                    [
                        'python3', '-m', 'yt_dlp',
                        '--write-auto-subs',
                        '--sub-lang', lang,
                        '--sub-format', 'srt',
                        '--skip-download',
                        '--no-playlist',
                        '--no-check-formats',
                        '-o', os.path.join(output_dir, 'transcript'),
                        url
                    ],
                    capture_output=True,
                    timeout=60
                )

                # Check if caption file was created
                srt_file = os.path.join(output_dir, f'transcript.{lang}.srt')
                if os.path.exists(srt_file):
                    print(f"Found captions in language: {lang}", file=sys.stderr)
                    # Convert SRT to plain text
                    transcript_text = srt_to_text(srt_file)
                    return title, transcript_text, lang

            except Exception as e:
                print(f"Failed for lang {lang}: {e}", file=sys.stderr)
                continue

    except Exception as e:
        print(f"Error extracting captions: {e}", file=sys.stderr)

    return None, None, None


def srt_to_text(srt_file):
    """Convert SRT file to plain text."""
    with open(srt_file, 'r', encoding='utf-8') as f:
        srt_content = f.read()

    # Extract text from SRT format
    blocks = re.split(r'\n\d+\n', srt_content)[1:]

    transcript_parts = []
    for block in blocks:
        lines = block.split('\n')
        text_lines = [l for l in lines if l and not re.match(r'\d{2}:\d{2}:\d{2}', l)]
        text = ' '.join(text_lines)

        # Remove SRT formatting tags
        text = re.sub(r'\{[^}]+\}', '', text)

        if text.strip():
            transcript_parts.append(text.strip())

    return ' '.join(transcript_parts)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_caption.py <youtube_url> [output_dir]", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else '.'

    title, transcript, lang = extract_captions(url, output_dir)

    if transcript:
        # Save transcript
        transcript_file = os.path.join(output_dir, f"{title}.txt")
        with open(transcript_file, 'w', encoding='utf-8') as f:
            f.write(transcript)

        # Output JSON result
        result = {
            "success": True,
            "title": title,
            "language": lang,
            "transcript_file": transcript_file,
            "transcript_length": len(transcript)
        }
        print(json.dumps(result))
    else:
        result = {
            "success": False,
            "error": "Could not extract captions"
        }
        print(json.dumps(result))
        sys.exit(1)


if __name__ == '__main__':
    main()
