#!/bin/bash

if ! command -v youtube-comment-downloader &>/dev/null; then
    echo "Error: youtube-comment-downloader is not installed. Please install it before running this script."
    exit 1
fi

CSV_FILE="videos.csv"

if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file $CSV_FILE not found."
    exit 1
fi

OUTPUT_DIR="downloaded_comments"
mkdir -p "$OUTPUT_DIR"

download_comments() {
    local youtube_id="$1"
    local output_file="$OUTPUT_DIR/$youtube_id.json"
    
    youtube-comment-downloader --youtubeid "$youtube_id" --output "$output_file" --limit 1000 --sort 0 --pretty
    echo "Downloaded comments for $youtube_id"
}

while IFS=',' read -r youtube_id _ || [ -n "$youtube_id" ]; do    
    if [ "$youtube_id" != "youtube_id" ]; then
        download_comments "$youtube_id"
    fi
done < "$CSV_FILE"
