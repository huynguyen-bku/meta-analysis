"""Vietnamese label dictionaries for publication figures (academic standards)."""

COMPARISON_VI = {
    "Strong Synergy": "Cộng hưởng mạnh",
    "Human Augmentation": "AI hỗ trợ người",
    "AI Augmentation": "Người hỗ trợ AI",
}

MODERATOR_VI = {
    "Industry": "Ngành",
    "Task_Type": "Loại nhiệm vụ",
    "AI_Type_Cleaned": "Kiến trúc AI",
    "Participant_Expert": "Trình độ chuyên môn",
    "AI_Expl_Incl": "Giải thích AI",
    "Year": "Năm",
}

LEVEL_VI = {
    "Business": "Kinh doanh",
    "Communication": "Truyền thông",
    "Healthcare": "Y tế",
    "Public sector": "Khu vực công",
    "Create": "Sáng tạo",
    "Decide": "Quyết định",
    "Yes": "Có",
    "No": "Không",
    "Deep Learning": "Deep Learning",
    "Deep": "Deep Learning",
    "Rule-Based": "Dựa trên quy luật",
    "Shallow Learning": "ML truyền thống",
    "Shallow": "ML truyền thống",
    "Wizard of Oz": "Wizard of Oz",
    "Simulated-AI": "AI mô phỏng",
}


def vi_comparison(name: str) -> str:
    return COMPARISON_VI.get(name, str(name))


def vi_moderator(name: str) -> str:
    return MODERATOR_VI.get(name, str(name).replace("_", " "))


def vi_level(name: str) -> str:
    raw = str(name)
    return LEVEL_VI.get(raw, raw.replace("_", " "))
