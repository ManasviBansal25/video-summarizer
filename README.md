# Video Summarizer

A simple Python script to fetch YouTube video transcripts and generate a short summary. Useful for educational content processing and quick previews.

## Features

- Extracts video ID from YouTube URLs or direct IDs
- Fetches transcripts using `youtube-transcript-api`
- Generates a basic summary using the first few sentences

## Prerequisites

- Python 3.7+
- `youtube-transcript-api` Python package

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ManasviBansal25/video-summarizer.git
   cd video-summarizer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   pip install transformers torch
   pip install youtube-transcript-api

## Usage

For testing sample videos, you can run:

```bash
python video-summarizer.py
```

## Output

- Prints the video ID and transcript length
- Displays a simple summary composed of the first three sentences

## Customization

- Modify `summarize_youtube_video` to implement more advanced summarization techniques (e.g., NLP models)
- Enhance error handling for missing transcripts or unavailable videos

## Requirements

youtube-transcript-api
```
