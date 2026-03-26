import subprocess
from pathlib import Path

def main():
    wav_file = Path(__file__).parent / "ulala.wav"
    subprocess.run(["afplay", str(wav_file)])

if __name__ == "__main__":
    main()
