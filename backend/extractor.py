from backend.utils import assign_priority, extract_person, extract_deadline, clean_task

def extract_insights(text):
    lines = text.split("\n")

    summary = []
    actions = []
    decisions = []
    risks = []

    for line in lines:
        l = line.lower().strip()

        if not l:
            continue

        # ACTIONS
        if "will" in l or "todo" in l or "need to" in l or "action" in l:
            actions.append({
                "person": extract_person(line),
                "task": clean_task(line),
                "deadline": extract_deadline(line),
                "priority": assign_priority(line)
            })

        # DECISIONS
        if "decided" in l or "finalized" in l or "agreed" in l:
            decisions.append(line)

        # RISKS
        if "risk" in l or "issue" in l or "problem" in l or "delay" in l:
            risks.append(line)

        # SUMMARY
        if len(line.split()) > 6:
            summary.append(line)

    # 🔥 SCORES
    total_actions = len(actions)
    total_decisions = len(decisions)
    total_risks = len(risks)

    confidence_score = max(0, 100 - (total_risks * 10))
    meeting_health = min(100, (total_decisions * 15 + total_actions * 5))

    # 🔥 SMART INSIGHTS
    insights = []

    if total_risks > 2:
        insights.append("⚠ High number of risks detected")

    if total_decisions > 0:
        insights.append("✅ Decisions are clearly defined")

    if total_actions > 3:
        insights.append("🔥 Highly actionable meeting")

    return {
        "summary": summary[:5],
        "actions": actions,
        "decisions": decisions,
        "risks": risks,
        "confidence_score": confidence_score,
        "meeting_health": meeting_health,
        "insights": insights
    }