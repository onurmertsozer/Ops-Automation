import pandas as pd

# NOTE: ALL DATA IS SYNTHETIC FOR DEMONSTRATION PURPOSES!
# This logic represents an operational 'Go/No-Go' decision engine.

def get_detailed_status(row):
    missing = []
    if str(row['Compliance']).strip() != 'True': missing.append("Legal/Compliance")
    if str(row['Mapping']).strip() != 'True': missing.append("HD Mapping")
    if str(row['Fleet_Ready']).strip() != 'True': missing.append("Fleet Calibration")
    
    return "READY" if not missing else "MISSING: " + ", ".join(missing)

def run_orchestrator():
    try:
        df = pd.read_csv('launch_manifest.csv')
        df['Status'] = df.apply(get_detailed_status, axis=1)
        
        print("\n--- 🛰️ REGIONAL LAUNCH READINESS REPORT ---")
        for _, row in df.iterrows():
            icon = "✅" if row['Status'] == "READY" else "❌"
            print(f"{icon} {row['City']}: {row['Status']}")
            
    except FileNotFoundError:
        print("Error: launch_manifest.csv not found.")

if __name__ == "__main__":
    run_orchestrator()
