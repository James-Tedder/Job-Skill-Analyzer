import csv

def analyze_all_jobs():
    # 1. Load your skills (Standardizing to lowercase for better matching)
    with open('skills.txt', 'r') as f:
        my_skills = {line.strip().lower() for line in f if line.strip()}

    # 2. Open and read the job dataset
    with open('jobs.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        print(f"{'JOB TITLE':<20} | {'COMPANY':<15} | {'MATCH SCORE'}")
        print("-" * 50)

        for row in reader:
            # Split the semicolon-separated string into a list
            req_skills = [s.strip().lower() for s in row['skills'].split(';')]
            
            # Find intersection and difference
            matches = [s for s in req_skills if s in my_skills]
            missing = [s for s in req_skills if s not in my_skills]
            
            # Calculate Score (Handle division by zero just in case)
            score = (len(matches) / len(req_skills) * 100) if req_skills else 0
            
            # Output row summary
            print(f"{row['title'][:20]:<20} | {row['company'][:15]:<15} | {score:.1f}%")
            
            if missing:
                print(f"   --> Missing: {', '.join(missing)}")

if __name__ == "__main__":
    analyze_all_jobs()