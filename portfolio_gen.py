import json

def generate_summary():
    print("--- GENERATING RECRUITER-READY SUMMARY ---")
    try:
        with open("intuition_log.json", "r") as f:
            logs = f.readlines()
        
        count = len(logs)
        print(f"Analyzing {count} instances of Recursive Intuition...")
        
        # This is where we 'Force Multiply' your experience
        summary = f"Expert System Integrator: Logged {count} unique anomaly patterns. "
        summary += "Specializing in Acoustic Variance & Human-AI Behavioral Calibration."
        
        print("\n[RESUME HOOK]:")
        print(summary)
        
    except FileNotFoundError:
        print("Error: No data logs found. Run calibration.py first!")

if __name__ == "__main__":
    generate_summary()
