from video_processing import extract_key_frames, extract_features
from blockchain_access import verify_access
from gen_ai_summary import audio_to_text, generate_summary

def main():
    # Verify user access
    user_id = "user123"  # Placeholder
    has_access = verify_access(user_id)
    if not has_access:
        print("Access Denied: User not authorized.")
        return
    print("Access Granted: User authorized.")

    # Process video
    video_path = "path/to/sample_video.mp4"  # Placeholder
    frames = extract_key_frames(video_path)
    if not frames:
        print("Video processing failed: Provide a valid video file.")
        return
    features = extract_features(frames)
    print(f"Extracted {len(frames)} key frames with features shape: {features.shape}")

    # Generate summary
    audio_text = audio_to_text(video_path)
    print(f"Audio Transcript: {audio_text}")
    summary = generate_summary(audio_text, features)
    print(f"Video Summary: {summary}")

if __name__ == "__main__":
    main()
