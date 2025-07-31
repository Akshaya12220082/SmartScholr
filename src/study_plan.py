# src/study_plan.py
def generate_study_plan(weak_topics):
    plan = {}
    days = ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7"]
    for i, topic in enumerate(weak_topics[:7]):
        plan[days[i]] = f"Revise {topic} with 5-min lesson + 3 practice questions"
    return plan
