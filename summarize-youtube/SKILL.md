---
name: summarize-youtube
description: Extract YouTube video captions in original language and generate Thai summary following CLAUDE.md guidelines. Use when user asks to summarize a YouTube video, extract video transcripts, or mentions /summarize-youtube command. Handles auto-generated captions in any language and creates formatted Thai summaries with English keywords, informal tone, and detailed explanations. Output consists of a transcript txt file and a summary md file, both named after the video title.
---

# Summarize YouTube

## Overview

This skill extracts captions from YouTube videos and creates structured Thai summaries. It automatically detects the original video language, uses auto-generated captions, and produces summaries following specific formatting guidelines.

## Workflow

### Step 1: Extract Captions

Use the provided script to download and extract captions from the YouTube URL:

```bash
python3 scripts/extract_caption.py "<youtube_url>" .
```

The script will:
- Get the video title (sanitized for filename)
- Detect available caption languages
- Download auto-generated captions
- Create `{video-title}.txt` with the raw transcript

**Example output:**
```json
{
  "success": true,
  "title": "วิธีใช้ Git สำหรับมือใหม่",
  "language": "th",
  "transcript_file": "วิธีใช้ Git สำหรับมือใหม่.txt",
  "transcript_length": 8057
}
```

### Step 2: Create Thai Summary

Create a summary following these CLAUDE.md guidelines:

1. **Clear and concise** - Summarize content efficiently
2. **Original language only** - Use ONLY the transcript content, no external information
3. **Thai sentences with English keywords** - Keep technical terms in English (Git, Commit, Repository, etc.)
4. **Informal tone** - Use casual, conversational Thai
5. **Detailed explanation** - Cover all important points from the transcript
6. **Single complete summary** - Don't split into parts, create one comprehensive .md file

**Summary structure:**
```markdown
# สรุปวิดีโอ: [Video Title]

## ภาพรวม
[Brief overview of the video content]

## ส่วนที่ 1: [Section Name]
[Detailed content...]

## ส่วนที่ 2: [Section Name]
[Detailed content...]

...

## คำศัพท์สำคัญ (Keywords)
| คำศัพท์ | ความหมาย |
|----------|------------|
| **Keyword** | Explanation |
```

**Output filename:** `{video-title}-summary.md`

### Step 3: Git Operations

After creating both files, commit and push to GitHub:

```bash
git add "{video-title}.txt" "{video-title}-summary.md"
git commit -m "Add transcript and summary for: {video-title}"
git push origin main
```

### Step 4: Cleanup

Remove temporary files:
- Any `.srt` files
- YouTube page HTML dumps
- Caption URL files

## Important Guidelines

### Content Rules
- **ONLY use transcript content** - Do not add information from external sources
- **Include timestamps or speaker names** if present in transcript
- **Preserve original meaning** - Don't interpret or add personal opinions

### Formatting Rules
- **Use Thai for explanations**, keep technical terms in English
- **Use informal tone** - Write as if explaining to a friend
- **Structure clearly** - Use headings, bullet points, and tables
- **Include keyword table** - Define English terms used

### Filename Rules
- Use the **original video title** (sanitized)
- Maximum 100 characters for filename
- Remove invalid characters: `< > : " / \ | ? *`

## Resources

### scripts/extract_caption.py

Python script that:
- Fetches YouTube video title using yt-dlp
- Detects available caption languages
- Downloads auto-generated captions (not manual)
- Converts SRT format to plain text
- Outputs JSON with file information

**Usage:**
```bash
python3 scripts/extract_caption.py <youtube_url> [output_dir]
```

**Requirements:**
- Python 3
- yt-dlp (`pip3 install yt-dlp`)

## Error Handling

If captions are not available:
- Try different language codes in the script
- Check if video has auto-generated captions enabled
- Verify video URL is accessible
- Inform user if extraction fails

## Examples

**User request:** `/summarize-youtube https://www.youtube.com/watch?v=gG9ir16Kl3Y`

**Workflow:**
1. Run extract_caption.py → Gets "วิธีใช้ Git สำหรับมือใหม่.txt"
2. Read transcript and create summary → "วิธีใช้ Git สำหรับมือใหม่-summary.md"
3. Commit and push to GitHub
4. Clean up temporary files

**Expected output:**
- Raw transcript: `วิธีใช้ Git สำหรับมือใหม่.txt`
- Thai summary: `วิธีใช้ Git สำหรับมือใหม่-summary.md`
