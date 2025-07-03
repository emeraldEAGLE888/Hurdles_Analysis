# Initialize everything
import streamlit as st
from ortools.sat.python import cp_model

# Set up all time slots
time_slots = []
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
hours = range(6, 23)
for day in days:
    for hour in hours:
        time_slot = f'{day}_{hour}'
        time_slots.append(time_slot)
# Set up special time slot options
morning_slots = [slot for slot in time_slots if int(slot.split('_')[1]) in range (6, 13)]
afternoon_slots = [slot for slot in time_slots if int(slot.split('_')[1]) in range (13,18)]
evening_slots = [slot for slot in time_slots if int(slot.split('_')[1]) in range (18,23)]
non_school_slots = [slot for slot in time_slots if int(slot.split('_')[1]) in [6,7,15,16,17,18,19,20,21,22,23]]

# Set up empty dicts
activities = {}
activity_times={}

model = cp_model.CpModel()
activity_vars = {}

for slot in time_slots:
    relevant_vars = [activity_vars[(act, slot)] for act in activity_times if (act, slot) in activity_vars]
    model.Add(sum(relevant_vars) <= 1)

# Title of app
st.title("Extracurricular Optimizer")
st.write("This app will help you create an optimized schedule for extracurriculars! " \
"Using our proven formula, it will determine the best time for you to attend extracurriculars to maximize performance. " \
"Note: this calculator only allows extracurriculars from 6:00 to 22:00.")

# Start of app
num_activities = st.number_input("How many activities do you want to enter?", min_value=1, max_value=10, value=3, step=1)

for i in range(num_activities):
    # Enter name and target hours
    name = st.text_input(f"Activity #{i+1} name", key=f"name_{i}")
    label = f"Target hours for {name}" if name else "Target hours"
    target = st.number_input(label, min_value=0, max_value=50, value=1, step=1, key=f"target_{i}")

    # Presets Dropdown
    preset = st.selectbox(f'Quick select time slots:',
                          ['Manual','All','Morning (6:00-12:00)','Afternoon (13:00 to 17:00)','Evening (18:00-22:00)','Non-school hours'],
                          key=f'preset_{i}'
                          )
    if preset == 'All':
        selected_times = time_slots
    elif preset == 'Morning (6:00-12:00)':
        selected_times = morning_slots
    elif preset == 'Afternoon (13:00 to 17:00)':
        selected_times = afternoon_slots
    elif preset == 'Evening (18:00-22:00)':
        selected_times = evening_slots
    elif preset == 'Non-school hours':
        selected_times = non_school_slots
    elif preset == 'Manual':
        selected_times = st.multiselect(
            f'Manually select time slots for {name}:',
            options=time_slots,
            key=f'times_{i}_{name}'
        )
    activity_times[name] = selected_times

    if name:
        activities[name] = target

for activity in activity_times:
    for time in activity_times[activity]:
        activity_vars[(activity, time)] = model.NewBoolVar(f'{activity}_{time}')

for slot in time_slots:
    relevant_vars = [activity_vars[(act, slot)] for act in activity_times if (act, slot) in activity_vars]
    model.Add(sum(relevant_vars) <= 1)

for act, target in activities.items():
    vars_for_activity = [activity_vars[(act,slot)] for slot in activity_times[act]]
    model.Add(sum(vars_for_activity)>= max(target-2,1))
    model.Add(sum(vars_for_activity)<=target+1)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for slot in time_slots:
        for act in activity_times:
            if (act, slot) in activity_vars and solver.Value(activity_vars[(act,slot)]) == 1:
                st.write(f'{slot}: {act}')

# Show final results
st.write('Your activities and targets:', activities)
st.write('Available time slots per activity:', activity_times)