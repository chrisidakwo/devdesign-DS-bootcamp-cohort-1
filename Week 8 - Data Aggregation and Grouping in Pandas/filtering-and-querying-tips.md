# Pandas Filtering and Querying: Quick Tips and Tricks

## Basic Filtering Techniques

1. **Boolean indexing**: Use `df[condition]` to filter rows based on a condition
   ```python
   high_scores = df[df['score'] > 90]
   ```

2. **Multiple conditions**: Combine conditions with `&` (AND) and `|` (OR), always use parentheses
   ```python
   selected = df[(df['score'] > 80) & (df['attendance'] > 90)]
   ```

3. **NOT operator**: Use `~` for negation
   ```python
   not_science = df[~(df['subject'] == 'Science')]
   ```

4. **Selecting multiple values**: Use `.isin()` for multiple possible values
   ```python
   selected = df[df['category'].isin(['A', 'B', 'C'])]
   ```

5. **Excluding multiple values**: Combine `~` with `.isin()`
   ```python
   excluded = df[~df['category'].isin(['D', 'F'])]
   ```

## String Operations Tips

6. **Always use `.str` accessor** for string operations on Series
   ```python
   starts_with_a = df[df['name'].str.startswith('A')]
   ```

7. **Case insensitivity**: Use `case=False` for case-insensitive matching
   ```python
   contains_math = df[df['subject'].str.contains('math', case=False)]
   ```

8. **Handle missing values** in string operations with `na=False`
   ```python
   contains_pattern = df[df['text'].str.contains('pattern', na=False)]
   ```

9. **Use regex** for complex pattern matching
   ```python
   pattern_match = df[df['text'].str.match(r'\d{3}-\d{2}-\d{4}')]
   ```

10. **Extract with capture groups** using `.str.extract()`
    ```python
    df['code'] = df['text'].str.extract(r'ID:(\d+)')
    ```

## Working with Missing Values

11. **Find missing values** with `.isna()` or `.isnull()`
    ```python
    missing_data = df[df['column'].isna()]
    ```

12. **Find non-missing values** with `.notna()` or `.notnull()`
    ```python
    has_data = df[df['column'].notna()]
    ```

13. **Combining missing/non-missing** with other conditions
    ```python
    valid_scores = df[(df['score'].notna()) & (df['score'] > 0)]
    ```

## The query() Method

14. **Basic query syntax**: Use column names directly in strings
    ```python
    high_scores = df.query('score > 90')
    ```

15. **Multiple conditions** using `and`, `or`, `not`
    ```python
    selected = df.query('score > 80 and attendance > 90')
    ```

16. **Using variables in queries** with `@` prefix
    ```python
    threshold = 85
    selected = df.query('score > @threshold')
    ```

17. **Use backticks for column names with spaces or reserved words**
    ```python
    df.query('`first name` == "John"')
    ```

18. **String operations require `.str` accessor** in query too
    ```python
    name_filter = df.query('name.str.startswith("A")')
    ```

19. **Chain multiple queries** for complex filtering
    ```python
    result = df.query('category == "A"').query('score > 90')
    ```

20. **Engine option**: Use `engine='python'` for operations not supported by numexpr
    ```python
    df.query('text.str.contains("pattern")', engine='python')
    ```

## Advanced Filtering Techniques

21. **Between range of values**: Use `.between()`
    ```python
    in_range = df[df['value'].between(10, 20)]  # Inclusive
    ```

22. **Filter by index**: Use `.loc` with Boolean conditions on index
    ```python
    idx_filter = df.loc[df.index > '2023-01-01']
    ```

23. **Filtering with functions**: Use `.apply()` for complex criteria
    ```python
    def is_valid(row):
        return row['value'] > 0 and row['status'] == 'Active'
    
    valid = df[df.apply(is_valid, axis=1)]
    ```

24. **Filtering with lambda**: For quick one-liners
    ```python
    valid = df[df.apply(lambda x: x['a'] + x['b'] > 100, axis=1)]
    ```

25. **Query with callable**: Pass functions to evaluate
    ```python
    def is_high(x):
        return x > 90
    
    df.query('score.apply(@is_high)')
    ```

## Optimization Tips

26. **Faster filtering**: Use `.loc` when possible
    ```python
    # Faster than df[df['column'] > value]
    df.loc[df['column'] > value]
    ```

27. **Create index for faster filtering**: If filtering repeatedly on a column
    ```python
    df.set_index('frequently_filtered_column', inplace=True)
    ```

28. **Vectorize conditions** instead of row-by-row operations
    ```python
    # Faster than apply
    mask = (df['a'] > 0) & (df['b'] < 100)
    filtered = df.loc[mask]
    ```

29. **Use categorical data type** for string columns with few unique values
    ```python
    df['category'] = df['category'].astype('category')
    # Filtering is now faster
    ```

30. **Use NumPy for complex numerical conditions**
    ```python
    import numpy as np
    mask = np.logical_and(df['a'] > 0, np.sqrt(df['b']) > 5)
    filtered = df.loc[mask]
    ```

## Common Gotchas and Fixes

31. **Chained indexing pitfalls**: Avoid `df['col'][condition]`, use `.loc` instead
    ```python
    # Wrong (chained indexing)
    df['value'][df['category'] == 'A'] = 100
    
    # Correct
    df.loc[df['category'] == 'A', 'value'] = 100
    ```

32. **Modifying filtered data**: Use `.loc` for assignment
    ```python
    df.loc[df['score'] < 60, 'status'] = 'Failed'
    ```

33. **Copy vs. View warnings**: Use `.copy()` when creating a filtered DataFrame
    ```python
    subset = df[df['score'] > 90].copy()
    ```

34. **Handling NaN in numeric comparisons**: NaN fails all comparisons
    ```python
    # This misses rows where score is NaN
    low_scores = df[df['score'] <= 60]
    
    # Include NaN rows explicitly if needed
    low_or_missing = df[(df['score'] <= 60) | (df['score'].isna())]
    ```

35. **Boolean vs. Bitwise operators**: Use `&` and `|`, not `and` and `or`
    ```python
    # Wrong
    df[df['a'] > 0 and df['b'] < 100]  # Error!
    
    # Correct
    df[(df['a'] > 0) & (df['b'] < 100)]
    ```

## Working with MultiIndex DataFrames

36. **Filter on MultiIndex level**: Use `.xs()` or `.loc`
    ```python
    # Filter on first index level
    df.loc[pd.IndexSlice['level_value', :]]
    
    # Using xs
    df.xs('level_value', level=0)
    ```

37. **Cross-section selection**: Use `pd.IndexSlice`
    ```python
    idx = pd.IndexSlice
    df.loc[idx['A', 'B'], :]
    ```

38. **Query with MultiIndex**: Reference index levels
    ```python
    df.query('index.get_level_values(0) == "A"')
    ```

## Filtering Tricks for Data Analysis

39. **Top/Bottom N values**: Use `.nlargest()` and `.nsmallest()`
    ```python
    top_5 = df.nlargest(5, 'value')
    bottom_5 = df.nsmallest(5, 'value')
    ```

40. **Filter by percentile**: Combine filters with quantiles
    ```python
    q75 = df['value'].quantile(0.75)
    top_25pct = df[df['value'] >= q75]
    ```

41. **Filter on aggregated results**: Filter after groupby
    ```python
    # Get groups where the mean is above threshold
    high_avg_groups = df.groupby('group').filter(lambda x: x['value'].mean() > 90)
    ```

42. **Find duplicates**: Filter for duplicate or unique rows
    ```python
    duplicates = df[df.duplicated()]
    unique_rows = df[~df.duplicated()]
    ```

43. **Filter by count**: Find groups with minimum occurrences
    ```python
    # Categories that appear at least 5 times
    common = df.groupby('category').filter(lambda x: len(x) >= 5)
    ```

44. **Filter one DataFrame based on another**: Use `.isin()`
    ```python
    df1[df1['id'].isin(df2['id'])]
    ```

45. **Filter with nearest values**: Find closest matches
    ```python
    target = 42
    df['distance'] = (df['value'] - target).abs()
    closest = df.nsmallest(5, 'distance')
    ```

46. **Create flag/indicator variables**: For complex conditions
    ```python
    df['is_valid'] = (df['score'] > 60) & (df['attendance'] > 80)
    valid_records = df[df['is_valid']]
    ```

47. **Filter with time windows**: For time series data
    ```python
    last_30_days = df[df['date'] > (pd.Timestamp.now() - pd.Timedelta(days=30))]
    ```

48. **Filter by row position**: Using `.iloc`
    ```python
    # Skip first 10 rows, take next 20
    subset = df.iloc[10:30]
    ```

49. **Random sampling**: Filter to random subset
    ```python
    sample = df.sample(n=100)  # 100 random rows
    sample = df.sample(frac=0.1)  # 10% random rows
    ```

50. **Combine filter and transformation**: Use `.loc` with multiple columns
    ```python
    df.loc[df['category'] == 'A', ['score', 'grade', 'status']]
    ```
