# Interactive Dashboard with Power BI
# Overview
The second section of this project is an interactive dashboard with Power BI showcasing the visualizations and analysis I did previously in Python. By making use of the varied tools built into Power BI, I created an aesthetically pleasing and easily used dashboard to help readers gain key insights about the three athletes and the 400 meter hurdles race as a whole.
# Tools/Skills Used
- **Dashboard Layout/Design**: Layed out dashboard with several visualizations to create a visually appealing and easy-to-use application.
- **Power Query (ETL/Data Cleanup)**: Cleaned and shaped data for analysis by creating new columns and cleaning formatting.
- **Data Modeling**: Established relationships between tables using Star Schema principles.
- **DAX Language**: Crafted aggregations and calculations using DAX to further insights into split times.
- **Implicit Measures and Aggregations**: Calculated measures like `Best Time` and `Most Predictive Split` to make build process more efficient.
- **Key Visualizations Utilized**:
    - **Core Charts**: Created bar, line, and box and whisker charts to display key points and overall trends in hurdle data.
    - **KPI Indicators/Tables**: Used cards to display select metrics.

# Dashboard Pages
## Page 1: Main Dashboard
![Main Dashboard](/Images/hurdle_dash_page1.png)
The main page of the dashboard serves as an overall perspective on key aspects of the 400 hurdles for all three athletes. This page displays key KPIs like **fastest athlete** (determined by median time), **average time**, and **average phase times**. Through the analysis of race splits and phases, overall trends and race shape are shown. This page also shows each athlete's yearly progression as well as how affected they are by a change in stride pattern. Data can be filtered by **Athlete** or **Year**, giving further insights into how the athletes have evolved.

## Page 2: Athlete Focus
![Athlete Focus](/Images/hurdle_dash_page2.png)
The second page of this dashboard delves into the specific statistics of one athlete. After selecting an athlete, key stats like **Best Time**, **Peak Year**, and **Stride Pattern Consistency** are displayed. The **Phases Distribution** graph provides a deep look into the average performance as well as the consistency of each athlete in the phases of the race. Combined with the **Split to Total Time Correlations** graph, this provides key insights into where each athlete does the best and where there is room for improvement. Data can also be sorted by year to view an athlete's progression over time.

## Further Analysis - Split to Time Correlation
Although the vast majority of the visualizations in this dashboard referenced existing Python visualizations that already been created, a few Power BI graphs led to further insights on each athlete's strengths.

Specifically, the **Split to Total Time Correlations** graph on the **Athlete Focus** page was created as an overall graph in Python with no ability to sort by athlete. When this data is filtered by athlete, each athlete's consistency throughout the race becomes clear.

### Karsten Warholm
![Warholm Split Correlations](/Images/correlations_warholm.png)

**Top 3 Splits for Prediction**: **H9**, **H8**, **H6**

### Insights
- Warholm's most predictive splits mostly come in the final third of his race. Specifically, his splits at **Hurdle 8** and **Hurdle 9** correlate the most to his final time (each having a R² value of over 0.6).
- This demonstrates how crucial this stage of the race is for Warholm: if his **form and strength** hold over these two splits, he is likely to have a fast final time.
-  Interestingly, his **Hurdle 1** correlation is also quite high, having a R² value over 0.5. This suggests that if Warholm is slower out of the blocks than usual, he will likely **run the entire race slower**.
- Warholm's average R² value is **0.456**, demonstrating that he runs each race methodically and consistently. Each split matters and contributes to his total performance. However, this also suggests he is less adaptable and one mistake could cost him the race.

### Rai Benjamin
![Benjamin Split Correlations](/Images/correlations_benjamin.png)

**Top 3 Splits for Prediction**: **H5**, **H8**, **H7**

### Insights
- Benjamin's most predictive splits are significantly stacked into the middle of his race (**H5-H8**), with the top split being **Hurdle 5**. Benjamin's other splits have very little correlation with his final time.
- This reveals Benjamin's consistency lies in the middle of his race; if he is able to stay with the competition or make up ground on them here, it will lead to a better final performance. 
- Correlation drops off steeply at **Hurdle 9**, showing that most of Benjamin's work is done before the final stages of the race.
- Notably, Benjamin's **Hurdle 1** split has virtually no correlation to his final time. Regardless of how fast he gets to the first hurdle, Benjamin has the capability to put up an exceptional performance.
- Benjamin's average R² value of **0.237** is extremely low and highlights how adaptive he is during the race, especially during the first half where he may chop his steps or make another mistake.

### Alison dos Santos
![dos Santos Split Correlations](/Images/correlations_dossantos.png)

**Top 3 Splits for Prediction**: **H2**, **H4**, **H5**

### Insights
- dos Santos' most predictive splits vary but lean more towards the front half of his race. His top 2 splits of **Hurdle 2** and **Hurdle 4** show his reliance on good performance in the beginning of the race. 
- dos Santos has 6 splits (**H1, H2, H4, H5, H8, and H9**) that lie above the average R² value, with **H3, H6, and H7** interestingly being under that threshold. 
- The inconsistency in R² values as well as a relatively low average value (**0.315**) highlight dos Santos' ability to recover from a misstep or other mistake. 

### See summary of analysis and conclusion in **[main README](C:/Users/sunse/Hurdles_Analysis/README.md)**.