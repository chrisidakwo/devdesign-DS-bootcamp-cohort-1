import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define subjects for each stream
arts_subjects = [
    "English Language",
    "Literature in English",
    "Government",
    "Economics",
    "History",
    "Mathematics",
    "Civic Education",
    "Agriculture"
]

science_subjects = [
    "English Language",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Further Mathematics",
    "Computer Science",
    "Agriculture",
    "Geography"
]

# Nigerian languages
nigerian_languages = ["French", "Yoruba", "Igbo", "Hausa"]

# Lists for random selections
study_groups = ["Arts", "Science"]
gender_options = ["M", "F"]
income_levels = ["Low", "Lower Middle", "Upper Middle", "High"]
study_hours = ["0-1 Hour", "1-2 Hours", "2-3 Hours", "More than 3 hours"]
gaming_hours = ["0-1 Hour", "1-2 Hours", "2-3 Hours", "More than 3 hours"]
yes_no = ["Yes", "No"]
class_levels = ["SS1", "SS2", "SS3"]

# List of common Nigerian first names
male_first_names = [
    "Adebayo", "Chukwudi", "Ibrahim", "Oluwaseun", "Emmanuel", "Adebisi", "Chinua",
    "Adewale", "Samuel", "Victor", "Olusegun", "David", "Chinedu", "Mohammed", "Tunde",
    "Emeka", "Yusuf", "Olufemi", "Obinna", "Kayode", "Hakeem", "Gbenga", "Uche", "Abiodun",
    "Chidi", "Idris", "Olamide", "Kelechi", "Segun", "Onyeka", "Abdul", "Nnamdi", "Olanrewaju",
    "Temitope", "Damilola", "Ikenna", "Babatunde", "Ayodele", "Chibuike", "Adekunle"
]

female_first_names = [
    "Amina", "Chioma", "Fatima", "Oluwaseyi", "Blessing", "Titilayo", "Ngozi",
    "Aisha", "Grace", "Folake", "Victoria", "Halima", "Precious", "Yetunde", "Sarah",
    "Omolara", "Zainab", "Chiamaka", "Bunmi", "Nneka", "Rasheedat", "Olabisi", "Bukola",
    "Adaeze", "Hadiza", "Funmilayo", "Ifeoma", "Oluwakemi", "Maryam", "Temitayo", "Chinyere",
    "Omolola", "Habiba", "Ebele", "Bisi", "Ogechi", "Ronke", "Khadija", "Adenike", "Chinwe"
]

# List of common Nigerian last names
last_name_options = [
    "Okafor", "Ibrahim", "Adeyemi", "Nwachukwu", "Mohammed", "Okonkwo", "Adewale",
    "Musa", "Oluwaseun", "Adebayo", "Abubakar", "Eze", "Adegoke", "Nwosu", "Obasanjo",
    "Chukwu", "Ahmed", "Okoro", "Usman", "Adekunle", "Onwuka", "Abdullahi", "Afolabi",
    "Ogunleye", "Nduka", "Aliyu", "Olanrewaju", "Chukwuma", "Ismail", "Adesina", "Njoku",
    "Yusuf", "Adeniyi", "Amadi", "Bello", "Okoye", "Lawal", "Oludipe", "Nwankwo", "Hassan"
]

# List of common Nigerian middle names
middle_name_options = [
    "Chukwu", "Ade", "Chidi", "Tunde", "Abdul", "Ola", "Chima", 
    "Segun", "Ngozi", "Bello", "Chibuike", "Adewale", "Emeka", "Oluwafemi",
    "Chinwe", "Abiodun", "Chioma", "Oluseyi", "Folake", "Onyeka", 
    "", "", "", "", "", "", "", "", "", ""  # Include empty strings for no middle name
]

# List of common occupations
occupations = [
    "Teacher", "Doctor", "Engineer", "Lawyer", "Accountant", "Business Owner", 
    "Civil Servant", "Nurse", "Farmer", "Driver", "Police Officer", "Shopkeeper", 
    "Banker", "Tailor", "Mechanic", "Chef", "Electrician", "Plumber", "Security Guard",
    "Market Trader", "Professor", "Journalist", "Pharmacist", "Artist", "Musician",
    "IT Specialist", "Sales Representative", "Barber/Hairdresser", "Construction Worker",
    "Fisherman", "Restaurant Owner", "Real Estate Agent", "Secretary", "Cleaner",
    "Store Manager", "Carpenter", "Painter", "Architect", "Contractor", "Pastor/Imam",
    "At home", "At home", "At home"  # Added multiple "At home" to increase frequency but not too much
]

def generate_student_id(admission_date, seq_number):
    """Generate student ID based on admission date and a sequential number"""
    prefix = "ALA-"
    year = admission_date.year
    month = admission_date.month
    day = admission_date.day
    
    student_id = f"{prefix}{year}{month:02d}{day:02d}{seq_number:03d}"
    return student_id

def generate_admission_date(class_level):
    """Generate appropriate admission date based on class level"""
    if class_level == "SS1":
        # Between 1st July 2024 and 30th September 2024
        start_date = datetime(2024, 7, 1)
        end_date = datetime(2024, 9, 30)
        admission_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    elif class_level == "SS2":
        # Either between 25th June 2023 and 30th September 2023 or 1st July 2024 and 30th September 2024
        if random.choice([True, False]):
            start_date = datetime(2023, 6, 25)
            end_date = datetime(2023, 9, 30)
        else:
            start_date = datetime(2024, 7, 1)
            end_date = datetime(2024, 9, 30)
        admission_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    else:  # SS3
        # Three possible date ranges
        date_range = random.choice([1, 2, 3])
        if date_range == 1:
            start_date = datetime(2022, 6, 14)
            end_date = datetime(2022, 9, 30)
        elif date_range == 2:
            start_date = datetime(2023, 6, 25)
            end_date = datetime(2023, 9, 30)
        else:
            start_date = datetime(2024, 7, 1)
            end_date = datetime(2024, 9, 30)
        admission_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    return admission_date

def generate_date_of_birth(class_level, admission_date):
    """Generate appropriate date of birth based on class level"""
    admission_year = admission_date.year
    
    if class_level == "SS1":
        # 13-16 years old, rarely up to 18
        min_age = 13
        max_age = 16
        rare_max_age = 18
    elif class_level == "SS2":
        # 14-17 years old, rarely up to 20
        min_age = 14
        max_age = 17
        rare_max_age = 20
    else:  # SS3
        # 18-20 years old, rarely up to 21
        min_age = 18
        max_age = 20
        rare_max_age = 21
    
    # Decide if it's a rare case of older student (1 in 20 chance)
    if random.random() < 0.05:
        age = random.randint(max_age + 1, rare_max_age)
    else:
        age = random.randint(min_age, max_age)
    
    # Calculate birth date by subtracting age from admission date
    # Add random month and day variations
    birth_year = admission_date.year - age
    birth_month = random.randint(1, 12)
    max_day = 28 if birth_month == 2 else 30 if birth_month in [4, 6, 9, 11] else 31
    birth_day = random.randint(1, max_day)
    
    return datetime(birth_year, birth_month, birth_day)

def generate_score():
    """Generate a realistic subject score (out of 100)"""
    # Normal distribution with mean 75 and standard deviation 12
    score = int(np.random.normal(78, 12))
    # Clip to ensure it's between 0 and 100
    return max(min(score, 100), 0)

def generate_student_data(total_students):
    """Generate data for the specified number of students"""
    
    # Ensure we have at least 750 students per class level
    min_per_class = 750
    ss1_count = min_per_class
    ss2_count = min_per_class
    ss3_count = min_per_class
    
    # If total_students > 3*min_per_class, distribute the excess evenly
    excess = total_students - 3*min_per_class
    if excess > 0:
        ss1_count += excess // 3
        ss2_count += excess // 3
        ss3_count += excess - 2*(excess // 3)
    
    # Initialize empty lists for each column
    student_ids = []
    first_names = []
    middle_names = []
    last_names = []
    genders = []
    dates_of_birth = []
    admission_dates = []
    class_levels_list = []
    study_groups_list = []
    attendance_rates = []
    disciplinary_counts = []
    suspension_counts = []
    family_income_levels = []
    daily_study_hours_list = []
    daily_gaming_hours_list = []
    computers_at_home = []
    smartphones = []
    has_jobs = []
    mother_occupations = []
    father_occupations = []
    
    # Create dictionaries for subject scores (initialized as empty lists)
    subject_scores = {}
    for subject in set(arts_subjects + science_subjects + nigerian_languages):
        subject_scores[subject] = []
    
    # Generate student data for each class level
    class_counts = {"SS1": ss1_count, "SS2": ss2_count, "SS3": ss3_count}
    
    # Make sure each class level has at least 2 students with jobs
    job_quotas = {"SS1": 2, "SS2": 2, "SS3": 2}
    
    seq_counter = 1
    
    for class_level, count in class_counts.items():
        jobs_assigned = 0
        
        for i in range(count):
            # Generate basic information
            gender = random.choice(gender_options)
            if gender == "M":
                first_name = random.choice(male_first_names)
            else:
                first_name = random.choice(female_first_names)
            
            middle_name = random.choice(middle_name_options)
            last_name = random.choice(last_name_options)
            
            # Generate dates
            admission_date = generate_admission_date(class_level)
            date_of_birth = generate_date_of_birth(class_level, admission_date)
            
            # Generate ID
            student_id = generate_student_id(admission_date, seq_counter)
            seq_counter += 1
            
            # Decide study group (approximately 50/50 distribution)
            study_group = random.choice(study_groups)
            
            # Generate attendance (normally distributed around 88% with 5% std dev)
            attendance = round(min(max(np.random.normal(88, 5), 60), 100), 1)
            
            # Generate disciplinary and suspension counts
            # Most students have 0-1 disciplinary counts, few have more
            disciplinary_count = np.random.choice([0, 1, 2, 3, 4], p=[0.6, 0.25, 0.1, 0.04, 0.01])
            
            # Suspensions are rare, and only happen with disciplinary counts
            if disciplinary_count > 0:
                suspension_count = np.random.choice([0, 1], p=[0.8, 0.2])
            else:
                suspension_count = 0
            
            # Generate family income level (slightly weighted towards middle income)
            family_income = random.choices(income_levels, weights=[0.3, 0.35, 0.25, 0.1])[0]
            
            # Generate daily study and gaming hours
            daily_study = random.choices(study_hours, weights=[0.2, 0.4, 0.3, 0.1])[0]
            daily_gaming = random.choices(gaming_hours, weights=[0.4, 0.3, 0.2, 0.1])[0]
            
            # Generate number of computers at home (weighted towards lower numbers)
            computers = random.choices(range(5), weights=[0.2, 0.4, 0.25, 0.1, 0.05])[0]
            
            # Almost all students have smartphones (90%)
            smartphone = random.choices(yes_no, weights=[0.9, 0.1])[0]
            
            # Assign jobs (rarely)
            if jobs_assigned < job_quotas[class_level]:
                has_job = "Yes"
                jobs_assigned += 1
            else:
                # After meeting the quota, only 1% chance of having a job
                has_job = random.choices(yes_no, weights=[0.01, 0.99])[0]
            
            # Generate parent occupations (mother more likely to be "At home")
            if random.random() < 0.25:  # 25% chance mother is "At home"
                mother_occupation = "At home"
            else:
                mother_occupation = random.choice([occ for occ in occupations if occ != "At home"])
            
            if random.random() < 0.05:  # 5% chance father is "At home"
                father_occupation = "At home"
            else:
                father_occupation = random.choice([occ for occ in occupations if occ != "At home"])
            
            # Add data to lists
            student_ids.append(student_id)
            first_names.append(first_name)
            middle_names.append(middle_name)
            last_names.append(last_name)
            genders.append(gender)
            dates_of_birth.append(date_of_birth.strftime("%Y-%m-%d"))
            admission_dates.append(admission_date.strftime("%Y-%m-%d"))
            class_levels_list.append(class_level)
            study_groups_list.append(study_group)
            attendance_rates.append(attendance)
            disciplinary_counts.append(disciplinary_count)
            suspension_counts.append(suspension_count)
            family_income_levels.append(family_income)
            daily_study_hours_list.append(daily_study)
            daily_gaming_hours_list.append(daily_gaming)
            computers_at_home.append(computers)
            smartphones.append(smartphone)
            has_jobs.append(has_job)
            mother_occupations.append(mother_occupation)
            father_occupations.append(father_occupation)
            
            # Generate subject scores based on study group
            for subject in set(arts_subjects + science_subjects + nigerian_languages):
                if study_group == "Arts":
                    if subject in arts_subjects:
                        subject_scores[subject].append(generate_score())
                    elif subject in nigerian_languages:
                        # For Arts students, assign exactly one language
                        selected_language = random.choice(nigerian_languages)
                        if subject == selected_language:
                            subject_scores[subject].append(generate_score())
                        else:
                            subject_scores[subject].append("")
                    else:
                        subject_scores[subject].append("")
                else:  # Science
                    if subject in science_subjects:
                        subject_scores[subject].append(generate_score())
                    else:
                        subject_scores[subject].append("")
    
    # Create DataFrame
    data = {
        "student_id": student_ids,
        "first_name": first_names,
        "middle_name": middle_names,
        "last_name": last_names,
        "gender": genders,
        "date_of_birth": dates_of_birth,
        "admission_date": admission_dates,
        "class_level": class_levels_list,
        "study_group": study_groups_list,
        "attendance": attendance_rates,
        "disciplinary_count": disciplinary_counts,
        "suspension_count": suspension_counts,
        "family_income_level": family_income_levels,
        "daily_study_hours": daily_study_hours_list,
        "daily_gaming_hours": daily_gaming_hours_list,
        "computers_at_home": computers_at_home,
        "smartphone": smartphones,
        "has_job": has_jobs,
        "mother_occupation": mother_occupations,
        "father_occupation": father_occupations
    }
    
    # Add subject scores
    for subject, scores in subject_scores.items():
        data[subject] = scores
    
    # Create and return DataFrame
    return pd.DataFrame(data)

# Generate the complete dataset with 2,400 students (800 per class level)
students_df = generate_student_data(2400)

# Save to CSV
students_df.to_csv("students.csv", index=False)
print(f"Dataset generated with {len(students_df)} students.")
print(f"SS1: {len(students_df[students_df['class_level'] == 'SS1'])} students")
print(f"SS2: {len(students_df[students_df['class_level'] == 'SS2'])} students")
print(f"SS3: {len(students_df[students_df['class_level'] == 'SS3'])} students")
print(f"Arts: {len(students_df[students_df['study_group'] == 'Arts'])} students")
print(f"Science: {len(students_df[students_df['study_group'] == 'Science'])} students")
print(f"Students with jobs: {len(students_df[students_df['has_job'] == 'Yes'])} students")
