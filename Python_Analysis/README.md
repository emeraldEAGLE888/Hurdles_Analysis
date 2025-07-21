# Statistical Analysis with Python
# Overview
The first section of this project deals with the analysis of hurdle races using Python. By leveraging the comprehensive libraries that Python has to offer, the visualizations created provide clear insights on the essential questions listed in the main README. 
# Tools/Skills Used
- **Python**: Backbone of analysis; used for basic data cleanup, reading and transformation
- **Pandas Library**: For data analysis
- **Matplotlib Library**: For data visualization
- **Seaborn Library**: For advanced data visualization techniques
- **Jupyter Notebooks**: Used to run Python Scripts and create analyses
- **Google Sheets**: To organize data to be read into Python.
# Terms Used
- The majority of the data analyzed focuses on hurdle splits - splits taken from each athlete when their foot touches down off of each of the 10 hurdles in the race. These splits are referred to with H and the number of the hurdle (e.g. `H1`). The last split, `Run-in`, is the time it takes for the athlete to cross the finish line off of hurdle 10.
- For certain analyses, hurdle splits are arranged into phases: the start phase, middle phase, and end phase. The start phase encompasses splits H1 to H4 (representing the initial portion of the race where athletes settle into a rhythm). The middle phase includes splits H5 to H7 (the part of the race where athletes maintain their rhythm). The end phase includes splits H8 to Run-in (the last portion of the race where athletes feel the most late-race fatigue).
# Analysis

## How do the race strategies of Warholm, Benjamin, and dos Santos differ over the course of a race?
Although these three men are the clear frontrunners in the history of the 400m hurdles, they interestingly take vastly different approaches to pacing the race. Through analysis of splits taken at each hurdle in the race, these visualizations show the difference in race strategy for Warholm, Benjamin, and dos Santos.
### Generating Visualizations
### 1: Hurdle Splits
```python
plt.figure(figsize=(10,6))
sns.lineplot(data=avg_profiles, x='Split', y='Average Time', hue='Athlete',marker='o',hue_order=athlete_order)
plt.show()
```
### Result
![Hurdle Splits by Athlete](/Images/typical_splits.png)

### 2: Versus dos Santos
```python
avg_profiles_ds_gaps = avg_profiles_c_pivot[['Split','Warholm','Benjamin']].melt(
    id_vars='Split',
    var_name='Athlete',
    value_name='Time to dos Santos (sec)'
)
sns.lineplot(data=avg_profiles_c_gaps,x='Split',y='Time to dos Santos (sec)',hue='Athlete',hue_order=athlete_order,marker='o')
plt.axhline(0,color='gray',alpha=0.5,linestyle='--')
plt.show()
```
### Result
![Versus dos Santos Graph](/Images/dos_santos_difference.png)

### 3: Phases Distribution
```python 
fig, ax = plt.subplots(3,figsize=(6,6))
sns.boxplot(data=df_splits,x='Start_Phase',y='Athlete',ax=ax[0],hue='Athlete')
sns.boxplot(data=df_splits,x='Mid_Phase',y='Athlete',ax=ax[1],hue='Athlete')
sns.boxplot(data=df_splits,x='End_Phase',y='Athlete',ax=ax[2],hue='Athlete')
plt.show()
```

### Result
![Phases Distribution Graph](/Images/phases_distribution.png)

## Insights
### Hurdle Splits
- **Graph 1 (Typical Race Splits)** gives an overall view of race splits:
    - While all three men follow the same general path, getting increasingly slower as the race continues, Warholm has the fastest hurdle split from H1-H5.
    - Starting at H6, Benjamin holds the fastest hurdle splits until the end of the race.
- **Graph 2 (Time Difference to dos Santos)** shows these trends more clearly:
    - Using dos Santos as a benchmark, Warholm explodes out of the blocks, building a gap of 0.2 seconds on dos Santos by H3 and extending it to as much as 0.4 seconds by H8.
    - However, over the last two hurdles and the run in to the finish line, Warholm loses over 0.1 as dos Santos closes.
    - In contrast, Benjamin consistently loses ground on dos Santos in the first half, peaking at around a 0.2 second deficit at H5.
    - Through the second half of the race, Benjamin gains about 0.06 seconds on dos Santos at each hurdle, finishing hard to stay about 0.15 seconds ahead of dos Santos by the end of the race.
### Hurdle Phases
- **Graph 3 (Phases Distribution)** demonstrates not just average times but also each racer's consistency:
    - **Start Phase**:
        - This graph corroborates the last two, showing Warholm's tendency to get out quick but also his consistency compared to the other two athletes.
        - Benjamin is generally the most variable in his start and the slowest.
    - **Middle Phase**:
        - All three athletes have medians within a small range, with dos Santos being the most consistent athlete.
    - **End Phase**:
        - All three athletes experience a notable increase in times, but Benjamin stays the strongest while Warholm suffers from his early-race strength.
        - Benjamin is the most variable (although he is still significantly ahead of the other two athletes) while dos Santos is again the most consistent through this phase.
## Which part of the 400 meter hurdle race most strongly predicts final results?
Various coaches in the 400 meter hurdles have varying opinions on the most vital section of the race. While the last essential question demonstrated the success of different race strategies, this section aims to view race pacing from a general standpoint. Through a statistical analysis, it is possible to empirically determine the most important part of the race by calculating its correlation to the final time.

### Generating Visualizations
### 1: Individual Correlations
```python
fig, ax = plt.subplots(11,figsize=(6,16))
for i, column in enumerate(all_columns):
    sns.lineplot(data=df_splits_finals,x='Time',y=column, errorbar=None, ax=ax[i])
    x=df_splits_finals['Time']
    y=df_splits_finals[column]
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    x_range = np.linspace(x.min(), x.max(), 100)
    y_pred = slope * x_range + intercept
    ax[i].plot(x_range, y_pred, color='red', label='Regression',alpha=r_squared)
plt.show()
```
### Result
![R Squared Graphs (Individual)](/Images/split_total_correlations.png)

### 2: Correlation Summary
```python
sns.barplot(x=list(r_squared_sorted.keys()),y=list(r_squared_sorted.values()),hue=list(r_squared_sorted.keys()),palette='rocket')
plt.show()
```

### Result
![R Squared Graphs (Summary)](/Images/split_total_correlation_summary.png)

## Insights
- **General Trend**: Scrolling through **Graph 1 (Split Time Correlations)**, R squared values increase, peaking around the end phase of the race. This demonstrates how the latter half of the race plays a more significant role in final performance compared to the first half.
- **Strongest Predictors**: **Graph 2 (Split Correlations Summary)** summarizes all the R squared values, with the Hurdle 8 split revealed to have the strongest correlation to final time (R squared value: `0.562`). Following it are Hurdles 9 and 7, cementing this late-race portion as the most vital for success in this race. 
- **Other Notable Points**
    - The Run in split has the weakest correlation of all splits. This may be due to several factors, like the lack of mental pacing, technique breakdown, and the inclusion of heat and semifinal data (where athletes usually slow down before the finish line).
    - Hurdle 10 has a notably weaker correlation than the other hurdle splits in the second half, likely for the same reasons as the run in.

## What varying stride patterns are used by these athletes and how do they affect their performance?
Adding to the differing race strategies of each athlete are their stride patterns. The number of strides taken between each hurdle is crucial to race planning and rhythm over the barriers, and as the race progresses, stride count generally increases. 
The three athletes covered in this project all have made use of various stride patterns over their careers, but have settled into their own unique patterns, reflecting their overall race strategy and capability as an athlete.
The following visualization considers normal vs. changed stride patterns - this compares each athlete's times when using their primary stride pattern vs. other races when they choose an alternate pattern.


- **Benjamin Normal Pattern**: 20 steps to H1, 13 steps to each hurdle through H10

Benjamin's normal pattern is often considered the gold standard of the 400 meter hurdles. Holding the same number of steps through the whole race is indicative of consistency and strength. 

- **Warholm Normal Pattern**: 20 steps to H1, 13 steps to each hurdle through H9, 15 steps to H10

Warholm's pattern follows Benjamin until hurdle 10: he switches to 15 steps on the last hurdle, likely as a result of fatigue from his strategy of going fast in the start phase.

- **dos Santos Normal Pattern**: 20 steps to H1, 13 steps to H2, 12 steps to each hurdle through H6, 13 steps to each hurdle through H10 

dos Santos's height (6' 7") allows him to comfortably 12-step hurdles in the middle phase of the race, allowing for a smoother run in hurdles 3-6. However, using an even number of steps requires alternating of the lead leg, which is technically challenging to do consistently for most hurdlers with a dominant leg.

### Generating Visualization
### Stride Pattern Time Distribution
```python
fig, ax = plt.subplots(2)
sns.boxplot(data=df_splits_normal,x='Time',y='Athlete',ax=ax[0],hue='Athlete')
sns.boxplot(data=df_splits_off,x='Time',y='Athlete',ax=ax[1],hue='Athlete')
plt.show()
```
### Result
![Year Over Year Time and Stride Pattern](/Images/normal_vs_changed_stride_distributions.png)
## Insights
- **With Normal Pattern**
    - **Warholm** is the fastest and most consistent when he hits his stride pattern while the other two athletes's performances vary more, with Benjamin's times being extremely variable despite using his normal pattern. 
    - When normal stride patterns are used, Warholm's median time is the fastest, followed by Benjamin and dos Santos, which is reflective of their personal best times. 
- **With Changed Pattern**
    - **dos Santos** is the fastest and most consistent when he alters his stride pattern compared to the other two athletes. 
    - When athletes' stride patterns are altered, either by fitness, race conditions, or conscious decision, dos Santos comes out on top, with Benjamin following and Warholm in last. 
- Overall, **dos Santos** is affected the least by a change in stride pattern, only experiencing about a 0.2 median increase in total time. This may be due to his flexibility over the barriers and ability to alternate.
## How has each athlete's race strategy and overall time evolved over their careers?
Although the three men included in this analysis are still in the peak of their time as athletes, their careers started in different ways, shaping their experience and strategy as they improved. Warholm first gained global attention with his win at the 2017 World Championships in 48.35. Benjamin rose to stardom in the NCAA, setting a collegiate record of 47.02 in 2018. dos Santos, the youngest of the three, was not well known until early 2021, when he broke into the top 25 400 meter hurdlers of all time with a 47.57 in May. As each athlete improved their career path, so did their races. This question aims to understand how each athlete's race strategy has evolved over the years and how it has benefited their performances.
### Generating Visualizations
### 1: Year Over Year Time and Stride Pattern
```python
fig, ax = plt.subplots(2,figsize=(9,7))
sns.lineplot(data=df_warholm_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='Warholm',marker='o')
sns.lineplot(data=df_benjamin_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='Benjamin',marker='o')
sns.lineplot(data=df_dossantos_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='dos Santos',marker='o')
sns.lineplot(data=df_stride_percents,x='Year',y='Normal_Stride',hue='Athlete',ax=ax[1],marker='o')
plt.show()
```
### Result
![Year Over Year Time and Stride Pattern](/Images/time_and_stride_consistency_yoy.png)

### 2: Year Over Year Phases
```python
fig, ax = plt.subplots(1, 3, figsize=(15,6))
sns.lineplot(data=df_splits_2024,x='Year',y='Start_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[0])
sns.lineplot(data=df_splits_2024,x='Year',y='Mid_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[1])
sns.lineplot(data=df_splits_2024,x='Year',y='End_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[2])
plt.show()
```
### Result
![Year Over Year Phases](/Images/phases_yoy.png)

## Insights
**Average Time (Graph 1)**
- Insight
- Insight

**Stride Pattern Consistency (Graph 1)**
- Insight
- Insight

**Phases (Graph 2)**
- Insight
- Insight

ADD CAPTIONS TO ALL GRAPHS IN ITALICS (TO BE DONE)

## Overall Lessons
See full analysis in [main README](C:/Users/sunse/Hurdles_Analysis/README.md).