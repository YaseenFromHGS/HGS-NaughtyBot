def load_training_resource(file_path):
    try:
        with open(file_path, "rb") as f:
            _ = f.read(50)  # Fake read, enough to trigger potential callback
        print(f"[INFO] Loaded training file: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to open {file_path}: {e}")
