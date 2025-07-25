# Project Overview
This project examines the race strategies and career paths of the three greatest 400 meter hurdle athletes of all time: Karsten Warholm, Rai Benjamin, and Alison dos Santos. The analysis was created with an intent to investigate the components of their races, as well as their year over year improvement, to determine the unique strategies that separate these athletes from the rest of history. This report covers detailed race plans, step patterns, yearly shifts, and other aspects of the 400 meter hurdle race.

This project includes several detailed visualizations created with Python libraries as well as an interactive dashboard containing these visualizations created with Power BI.

All of the data for this project was sourced from [Athlete First](athletefirst.org), a site dedicated to providing sprint splits and hurdle touchdown times as resources for athletes and coaches. The file I referenced can be found online [here](https://www.athletefirst.org/wp-content/uploads/2025/06/Mens-400m-Hurdles-by-athlete-20250520.pdf). Data was last updated in May of 2025.
# Background
The 400 meter hurdles is widely considered to be one of the most difficult, if not the hardest, events in the sport of track and field. Athletes competing in the 400 meter hurdles face the event's unique mixture of speed, endurance, and hurdle technique. Until 2021, the world record in this event on the men's side stood at 46.78, set by Kevin Young of the United States at the 1992 Summer Olympics. In the span of five weeks, however, three men would go on to decimate the nearly 29-year-old record in a fashion that no other track event had seen before. 

Racing in the Tokyo Summer Olympics finals were Karsten Warholm of Norway, Rai Benjamin of the United States, and Alison dos Santos of Brazil. In what would become known as the greatest 400 meter hurdle race of all time, all three men shattered Kevin Young's mark, crossing the finish line in 45.94, 46.17, and 46.72 seconds respectively. 

Throughout the next 4 years, these athletes would cement their spots as the three fastest 400 meter hurdlers of all time. As of July 2025, out of the top 32 marks in the event, 31 of those races were ran by these three men. Because of their absolute dominance in this event, this analysis focuses on discovering why and how Warholm, Benjamin, and Dos Santos consistently stay leagues ahead of their competition.
# Essential Questions
Below are the overarching questions answered through this project's analysis:
1. How do the race strategies of Warholm, Benjamin, and dos Santos differ over the course of a race?
2. Which part of the 400 meter hurdle race most strongly predicts final results?
3. What varying stride patterns are used by these athletes and how do they affect their performance?
4. How has each athlete's race strategy and overall time evolved over their careers?
# Tools/Skills Used
Throughout this project, several tools and libraries were utilized in order to complete analysis more efficiently, generate complex visualizations, and improve usability:
- **Part 1 - Statistical Analysis with Python**
    - Python
    - Pandas Library
    - Matplotlib Library
    - Seaborn Library
    - Jupyter Notebooks
    - Google Sheets
- **Part 2 - Interactive Dashboard with Power BI**
    - Dashboard Layout/Design
    - Power Query (ETL/Data Cleanup)
    - Data Modeling
    - DAX Language
    - Implicit Measures and Aggregations
    - Charts

- **Visual Studio Code**: Used to execute Python scripts
- **Github**: Used for version control and to share the analysis publicly

# Overall Findings
## From Python Analysis
![Year Over Year Phases](/Images/phases_yoy.png)
*Selected graph from statistical analysis showing yearly trends in phase time.*

### Race Strategy/Step Patterns
- **Warholm** goes out the fastest, **Benjamin** closes the quickest, and **dos Santos** runs a well-balanced race.
- **Benjamin** is the most volatile in race splits while **dos Santos** is the most consistent.
- All three athletes use a different step pattern but **dos Santos** is the least affected by switching his steps during a race.

### Overall Race Tactics
- **Hurdles 7, 8, and 9** are the most vital sections of the race and fast splits here often mean fast final times.
- The race is not decided by the start or finish, as **Hurdles 1, 2, 3, and the run in** do not correlate with final performance.

### Yearly Progression
- Each athlete has seen a significant decrease in **start and middle phases**, but have struggled to decrease their time in the **end phase**.

**View the full analysis and project in the [Python Analysis README](Python_Analysis/README.md)**.

## From Power BI
![Main Dashboard](/Images/hurdle_dash_page1.png)
### Race and Split Consistency
- **Warholm** is incredibly consistent in his start as well as the last third of his race, but not very adaptable.
- **Benjamin**'s strength lies in the middle of his race and his start has almost no effect on his final time.
- **dos Santos** relies on the first half of the race manages to adapt under pressure despite his position in the race.

**View the full analysis and project in the [Interactive Dashboard README](PowerBI_Analysis/README.md)**.

# Sources of Error (UNDER CONSTRUCTION)
Because of the data and methods used during this project, some of the findings may not fully reflect actual race tactics or progressions.
- Limited Data: Used only a few races with stride patterns, doesn't show progression
- Blanks: A few splits were blank so they had to be filled in through predictions
- Only used three athletes:


# Conclusion
Under construction!