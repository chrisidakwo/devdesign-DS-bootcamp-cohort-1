### String Filtering and Text Operations

```python
# Filter students with names starting with 'A'
a_names = students_df[students_df['first_name'].str.startswith('A')]
print("Students with names starting with 'A':")
print(a_names[['first_name', 'last_name']].head())

# Filter students with names containing 'ola'
ola_names = students_df[students_df['first_name'].str.contains('ola', case=False)]
print("\nStudents with 'ola' in their name (case insensitive):")
print(ola_names[['first_name', 'last_name']].head())

# Find students where father's occupation contains "Engineer"
engineer_fathers = students_df[students_df['father_occupation'].str.contains('Engineer', na=False)]
print("\nStudents whose fathers are engineers:")
print(engineer_fathers[['first_name', 'last_name', 'father_occupation']].head())
```

### Numeric Range Filtering

```python
# Students with Mathematics scores between 75 and 85 (inclusive)
mid_range_math = students_df[(students_df['Mathematics'] >= 75) & (students_df['Mathematics'] <= 85)]
print("Students with Mathematics scores between 75 and 85:")
print(mid_range_math[['first_name', 'last_name', 'Mathematics']].head())

# Alternative using between method
mid_range_math_alt = students_df[students_df['Mathematics'].between(75, 85)]
print("\nSame result using between method:")
print(mid_range_math_alt[['first_name', 'last_name', 'Mathematics']].head())

# Students who scored either below 60 or above 90 in English Language
english_extremes = students_df[(students_df['English Language'] < 60) | (students_df['English Language'] > 90)]
print("\nStudents with extreme English scores (below 60 or above 90):")
print(english_extremes[['first_name', 'last_name', 'English Language']].head())
```

### Working with NaN Values

```python
# Find students missing Physics scores (common in Arts students)
missing_physics = students_df[students_df['Physics'].isna()]
print("Students without Physics scores:")
print(missing_physics[['first_name', 'last_name', 'study_group']].head())

# Find Science students with complete STEM subject scores
complete_science = students_df[
    (students_df['study_group'] == 'Science') & 
    students_df['Mathematics'].notna() & 
    students_df['Physics'].notna() & 
    students_df['Chemistry'].notna() & 
    students_df['Biology'].notna()
]
print("\nScience students with complete STEM subject scores:")
print(complete_science[['first_name', 'last_name']].head())
```

### Filtering with isin() for Multiple Values

```python
# Students in certain class levels
specific_levels = students_df[students_df['class_level'].isin(['SS1', 'SS3'])]
print("Students in SS1 or SS3:")
print(specific_levels[['first_name', 'last_name', 'class_level']].head())

# Students with specific daily study hours
study_hours_filter = students_df[students_df['daily_study_hours'].isin(['1-2 Hours', 'More than 3 hours'])]
print("\nStudents who study either 1-2 hours or more than 3 hours:")
print(study_hours_filter[['first_name', 'last_name', 'daily_study_hours']].head())

# Students not in these income levels
not_middle_income = students_df[~students_df['family_income_level'].isin(['Lower Middle', 'Upper Middle'])]
print("\nStudents not in middle income brackets:")
print(not_middle_income[['first_name', 'last_name', 'family_income_level']].head())
```

### Complex Multi-condition Filtering

```python
# High-performing students from low-income families
exceptional_students = students_df[
    (students_df['family_income_level'] == 'Low') & 
    (
        (students_df['Mathematics'] > 85) | 
        (students_df['English Language'] > 85)
    ) &
    (students_df['attendance'] > 90)
]
print("High-performing students from low-income families:")
print(exceptional_students[['first_name', 'last_name', 'Mathematics', 'English Language']].head())

# At-risk students (multiple risk factors)
at_risk = students_df[
    (students_df['attendance'] < 85) &
    (
        (students_df['Mathematics'] < 70) |
        (students_df['English Language'] < 70)
    ) &
    (students_df['disciplinary_count'] > 0)
]
print("\nAt-risk students with multiple concerns:")
print(at_risk[['first_name', 'last_name', 'attendance', 'disciplinary_count']].head())
```

## Advanced Query() Method Examples

The `query()` method offers a more readable syntax for filtering, especially with complex conditions:

```python
# Simple condition
high_math = students_df.query('Mathematics > 90')
print("Students with Math scores above 90 (using query):")
print(high_math[['first_name', 'last_name', 'Mathematics']].head())

# Multiple conditions with AND
good_students = students_df.query('Mathematics > 80 and English Language > 80 and attendance > 90')
print("\nStudents excelling in core subjects with good attendance:")
print(good_students[['first_name', 'last_name']].head())

# OR conditions
science_or_arts = students_df.query('study_group == "Science" or class_level == "SS3"')
print("\nScience students or SS3 students:")
print(science_or_arts[['first_name', 'last_name', 'study_group', 'class_level']].head())

# Parentheses for complex logic
complex_query = students_df.query('(Mathematics > 80 or English Language > 80) and attendance > 95')
print("\nStudents with high core subject scores AND excellent attendance:")
print(complex_query[['first_name', 'last_name', 'attendance']].head())
```

### Using Variables in Query

```python
# Using variables in query expressions
min_score = 75
max_score = 85
range_query = students_df.query('Mathematics >= @min_score and Mathematics <= @max_score')
print("Students with Math scores between variables min_score and max_score:")
print(range_query[['first_name', 'last_name', 'Mathematics']].head())

# Using multiple variables
subject = 'Mathematics'
threshold = 80
class_level = 'SS2'
dynamic_query = students_df.query('`@subject` > @threshold and class_level == @class_level')
print(f"\nSS2 students with {subject} scores above {threshold}:")
print(dynamic_query[['first_name', 'last_name', subject]].head())
```

### String Operations in Query

```python
# String operations using str accessor
name_query = students_df.query('first_name.str.startswith("A") or last_name.str.startswith("O")')
print("Students with first name starting with A or last name starting with O:")
print(name_query[['first_name', 'last_name']].head())

# Case-insensitive string contains
pattern_query = students_df.query('mother_occupation.str.contains("teacher", case=False)', engine='python')
print("\nStudents whose mothers are teachers (case insensitive):")
print(pattern_query[['first_name', 'last_name', 'mother_occupation']].head())
```

### Using isin() in Query

```python
# Using the isin function in a query
levels = ['SS1', 'SS3']
level_query = students_df.query('class_level.isin(@levels)')
print("Students in SS1 or SS3 using query with isin:")
print(level_query[['first_name', 'last_name', 'class_level']].head())

# Negating isin with ~
not_in_query = students_df.query('~family_income_level.isin(["Lower Middle", "Upper Middle"])')
print("\nStudents not in middle income brackets using query:")
print(not_in_query[['first_name', 'last_name', 'family_income_level']].head())
```

### Working with Missing Values in Query

```python
# Finding missing values
missing_physics_query = students_df.query('Physics.isna()')
print("Students without Physics scores using query:")
print(missing_physics_query[['first_name', 'last_name', 'study_group']].head())

# Finding non-missing values
has_literature_query = students_df.query('`Literature in English`.notna()')
print("\nStudents with Literature scores using query:")
print(has_literature_query[['first_name', 'last_name', 'Literature in English']].head())
```

### Complex Educational Analysis Queries

```python
# Students who do well in humanities but struggle in STEM
humanities_vs_stem = students_df.query(
    '`English Language` > 85 and `Literature in English` > 85 and '
    '(Mathematics < 70 or Physics < 70)'
)
print("Students excelling in humanities but struggling in STEM:")
print(humanities_vs_stem[['first_name', 'last_name', 'English Language', 'Literature in English', 'Mathematics']].head())

# Finding potential tutors for younger students
potential_tutors = students_df.query(
    'class_level == "SS3" and '
    'Mathematics > 90 and '
    'attendance > 95 and '
    'disciplinary_count == 0'
)
print("\nPotential peer tutors for Mathematics:")
print(potential_tutors[['first_name', 'last_name', 'Mathematics']].head())

# High-performing students from challenging backgrounds
resilient_students = students_df.query(
    'family_income_level == "Low" and '
    'daily_study_hours == "More than 3 hours" and '
    '(Mathematics > 85 or `English Language` > 85) and '
    'attendance > 90'
)
print("\nResilient high-performing students from low-income backgrounds:")
print(resilient_students[['first_name', 'last_name', 'Mathematics', 'English Language']].head())
```
