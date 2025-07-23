# Simple learning suggestions for each skill

RESOURCE_MAP = {
    "python": "https://docs.python.org/3/tutorial/",
    "sql": "https://www.khanacademy.org/computing/computer-programming/sql",
    "excel": "https://exceljet.net/",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "deep learning": "https://www.fast.ai/",
    "docker": "https://docker-curriculum.com/",
    "mlops": "https://madewithml.com/mlops/",
    "power bi": "https://learn.microsoft.com/en-us/power-bi/",
    "tableau": "https://www.tableau.com/learn/training",
    "pandas": "https://pandas.pydata.org/docs/",
    "numpy": "https://numpy.org/learn/",
    "data visualization": "https://www.interviewbit.com/blog/data-visualization-tools/",
    "statistics": "https://www.khanacademy.org/math/statistics-probability",
    "data structures": "https://www.geeksforgeeks.org/data-structures/",
    "algorithms": "https://www.khanacademy.org/computing/computer-science/algorithms",
    "scikit-learn": "https://scikit-learn.org/stable/tutorial/",
}

def suggest_resources(missing_skills):
    suggestions = {}
    for skill in missing_skills:
        skill_lower = skill.lower()
        for keyword in RESOURCE_MAP:
            if keyword in skill_lower:
                suggestions[skill] = RESOURCE_MAP[keyword]
                break
        else:
            suggestions[skill] = "Search on Google or YouTube"
    return suggestions
