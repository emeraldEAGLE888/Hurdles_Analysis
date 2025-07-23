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

## Further Analysis
Although the vast majority of the visualizations in this dashboard referenced existing Python visualizations that already been created, a few Power BI graphs led to further insights on each athlete's strengths.

Specifically, the **Split to Total Time Correlations** graph on the **Athlete Focus** page was created as an overall graph in Python with no ability to sort by athlete. When this data is filtered by athlete, each athlete's consistency throughout the race becomes clear.

### Karsten Warholm
![Warholm Split Correlations](/Images/correlations_warholm.png)


### Rai Benjamin
![Benjamin Split Correlations](/Images/correlations_benjamin.png)


### Alison dos Santos
![dos Santos Split Correlations](/Images/correlations_dossantos.png)
