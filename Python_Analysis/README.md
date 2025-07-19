# Python Analysis Overview
The first section of this project deals with the analysis of hurdle races using Python. By leveraging the comprehensive libraries that Python has to offer, the visualizations created provide clear insights on the essential questions listed in the main README. 
# Tools/Skills Used
- **Python**: Backbone of project; used for data cleanup, reading and transformation
- **Pandas Library**: For data analysis
- **Matplotlib Library**: For data visualization
- **Seaborn Library**: For advanced data visualization techniques
- **Jupyter Notebooks**: Used to run Python Scripts and create analyses
- **Google Sheets**: To organize data to be read into Python.

# Analysis

## How do the race strategies of Warholm, Benjamin, and dos Santos differ over the course of a race?

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

## Which part of the 400 meter hurdle race most strongly predicts final results?

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

## What varying stride patterns are used by these athletes and how do they affect their performance?

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

## How has each athlete's race strategy and overall time evolved over their careers?

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

## Overall Lessons
See full analysis in [main README](C:/Users/sunse/Hurdles_Analysis/README.md).