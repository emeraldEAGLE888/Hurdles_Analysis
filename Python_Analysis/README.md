# Python Analysis Overview

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
```python

```
### Result

### Insights

## Which part of the 400 meter hurdle race most strongly predicts final results?

### Generating Visualizations
### Individual Correlations
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
![R Squared Graphs (Individual)](Images/split_total_correlations.png)

### Correlation Summary
```python
sns.barplot(x=list(r_squared_sorted.keys()),y=list(r_squared_sorted.values()),hue=list(r_squared_sorted.keys()),palette='rocket')
plt.show()
```

### Result
![R Squared Graphs (Summary)](Images/split_total_correlation_summary.png)

### Insights

## What varying stride patterns are used by these athletes and how do they affect their performance?

### Generating Visualizations
```python
fig, ax = plt.subplots(2)
sns.boxplot(data=df_splits_normal,x='Time',y='Athlete',ax=ax[0],hue='Athlete')
sns.boxplot(data=df_splits_off,x='Time',y='Athlete',ax=ax[1],hue='Athlete')
plt.show()
```
### Result
![Year Over Year Time and Stride Pattern](Images/normal_vs_changed_stride_distributions.png)
### Insights

## How has each athlete's race strategy and overall time evolved over their careers?

### Generating Visualizations
### Year Over Year Time and Stride Pattern
```python
fig, ax = plt.subplots(2,figsize=(9,7))
sns.lineplot(data=df_warholm_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='Warholm',marker='o')
sns.lineplot(data=df_benjamin_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='Benjamin',marker='o')
sns.lineplot(data=df_dossantos_s_2024_finals,x='Year',y='Time', errorbar=None, ax=ax[0], label='dos Santos',marker='o')
sns.lineplot(data=df_stride_percents,x='Year',y='Normal_Stride',hue='Athlete',ax=ax[1],marker='o')
plt.show()
```
### Result
![Year Over Year Time and Stride Pattern](Images/time_and_stride_consistency_yoy.png)

### Year Over Year Phases
```python
fig, ax = plt.subplots(1, 3, figsize=(15,6))
sns.lineplot(data=df_splits_2024,x='Year',y='Start_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[0])
sns.lineplot(data=df_splits_2024,x='Year',y='Mid_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[1])
sns.lineplot(data=df_splits_2024,x='Year',y='End_Phase',hue='Athlete',errorbar=None, marker='o', ax=ax[2])
plt.show()
```
### Result
![Year Over Year Phases](Images/phases_yoy.png)

### Insights