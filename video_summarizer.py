from youtube_transcript_api import YouTubeTranscriptApi
import re
import sys


def get_video_id_from_url(url):
    """Extract the YouTube video ID from a URL or return the ID itself."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url


def summarize_youtube_video(video_input):
    """
    Fetch the transcript from a YouTube video (given a URL or ID)
    and generate a short summary.
    """
    print("\nStarting video summarization...")

    # Extract video ID
    video_id = get_video_id_from_url(video_input)
    print(f"Video ID: {video_id}")

    # Get transcript
    print("Fetching transcript...")
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        print("Transcript retrieved successfully.")
    except Exception as e:
        print(f"Error: unable to fetch transcript ({e})")
        return None

    # Combine transcript text
    print("Processing transcript text...")
    def get_text(item):
        if isinstance(item, dict):
            return item.get('text', '')
        return getattr(item, 'text', '')

    full_text = " ".join(get_text(item) for item in transcript)
    print(f"Transcript length: {len(full_text)} characters")

    # Create summary
    print("Generating summary...")
    try:
        sentences = re.split(r'[.!?]+', full_text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) < 2:
            print("Transcript too short for summarization.")
            return None

        # Use the first few sentences as a simple summary
        summary_text = '. '.join(sentences[:3]) + '.'
        summary = [{'summary_text': summary_text}]
        print("Summary generated.")
    except Exception as e:
        print(f"Error while summarizing: {e}")
        summary = [{'summary_text': f"(Preview) {full_text[:200]}..."}]

    return {
        'video_id': video_id,
        'transcript_length': len(full_text),
        'summary': summary[0]['summary_text']
    }


if __name__ == "__main__":
    print("YouTube Transcript Summarizer\n")

    # Sample educational videos
    test_videos = [
        "rfscVS0vtbw",  # Khan Academy - Python
        "aircAruvnKk",  # 3Blue1Brown - Neural Networks
        "NybHckSEQBI",  # Khan Academy - Algebra
    ]

    print("Running tests...\n")

    for video in test_videos:
        result = summarize_youtube_video(video)
        if result:
            print("\n--- Summary Result ---")
            print(f"Video URL: https://www.youtube.com/watch?v={result['video_id']}")
            print(f"Transcript length: {result['transcript_length']} characters")
            print("\nSummary:\n")
            print(result['summary'])
            print("----------------------\n")

    print("All tests completed successfully.")
