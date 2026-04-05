---
created: 2024-09-10
up:
  - "[[Python Scripts]]"
---

# **Introduction**

In the realm of data analysis, reports often take the form of Excel files. Presenting your insights in an aesthetically pleasing and comprehensible manner can significantly elevate the impact of your findings. In this blog post, we’ll explore how to leverage the capabilities of the `openpyxl` library in Python to not just save your DataFrame to an Excel file but to transform it into a visually appealing and well-organized masterpiece.

## Data

The dummy data utilized throughout this blog post is shown below:

```python
import pandas as pd  
from openpyxl.styles import PatternFill, NamedStyle, Alignment, Font, Border, Side  
from openpyxl.utils.cell import get_column_letter
```

```python
dummy_data = [  
    {"Date": "2023-01-01", "Region": "North", "Product": "A", "Units Sold": 1000, "Revenue": 10000},  
    {"Date": "2023-01-01", "Region": "South", "Product": "B", "Units Sold": 1500, "Revenue": 25000},  
    {"Date": "2023-01-02", "Region": "East", "Product": "C", "Units Sold": 800, "Revenue": 12000},  
    {"Date": "2023-01-02", "Region": "West", "Product": "A", "Units Sold": 1200, "Revenue": 15000},  
    {"Date": "2023-01-03", "Region": "North", "Product": "B", "Units Sold": 900, "Revenue": 18000},  
    {"Date": "2023-01-03", "Region": "South", "Product": "C", "Units Sold": 1100, "Revenue": 13000},  
    {"Date": "2023-01-04", "Region": "East", "Product": "A", "Units Sold": 1300, "Revenue": 20000},  
    {"Date": "2023-01-04", "Region": "West", "Product": "B", "Units Sold": 1000, "Revenue": 15000},  
    {"Date": "2023-01-05", "Region": "North", "Product": "C", "Units Sold": 700, "Revenue": 9000},  
    {"Date": "2023-01-05", "Region": "South", "Product": "A", "Units Sold": 1800, "Revenue": 28000}  
]  
# Calculate Variance  
for i in range(1, len(dummy_data)):  
    current_revenue = dummy_data[i]["Revenue"]  
    previous_revenue = dummy_data[i - 1]["Revenue"]  
    variance = current_revenue - previous_revenue  
    dummy_data[i]["Variance"] = variance  
# Create the dataframe  
df = pd.DataFrame.from_dict(dummy_data)  
# Remove null values  
df.fillna(0, inplace=True)
```

## Saving the Data Frame to Excel

To save a Data Frame to Excel in Python, use `ExcelWriter` with the `openpyxl` engine and the `to_excel` method.

```python
with pd.ExcelWriter("Style Excel.xlsx", engine="openpyxl") as writer:  
    df.to_excel(writer, sheet_name="Sample1", index=False, freeze_panes=(2,0))
```

## Styling the Excel File

1. Inserting rows and columns

```python
# Workbook  
workbook = writer.book  
# Worksheet  
worksheet = workbook["Sample1"]  
  
# Insert a column and a row   
# Openpyxl is not zero indexed.  
worksheet.insert_cols(1)  
worksheet.insert_rows(1)  
  
# Minimize the size of row 1:  
worksheet.row_dimensions[1].height= 21.0
```

> If you wish to hide a row, you can use the code below

```python
worksheet.row_dimensions[1].hidden = True
```

2. Autofitting Column Width

Autofitting the column width ensures that your data is easy to read.

> To enable auto-fitting, iterate through each column, determine the length of values in each cell, and subsequently find the maximum value.

```python
# AutoFit column width  
for column in worksheet.columns:  
    max_length = max(len(str(cell.value)) for cell in column)  
    adjusted_width = (max_length + 2) * 1.0  
    worksheet.column_dimensions[column[0].column_letter].width = adjusted_width
```

```python
# Adjust the size of column "A"  
worksheet.column_dimensions["A"].width = 4.0
```

3. Adding Commas for Readability

> To enhance readability, commas are added to numeric values.

```python
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=2, max_col=worksheet.max_column):  
    for cell in row:  
        # Add the , to separate the numbers and make them readable  
        cell.number_format = "#,##0"  
        # Extra: Styling percentages  
        # cell.number_format = "0.00%"  
        cell.alignment = Alignment(horizontal="center")
```

4. Adding borders

```python
# Iterate through rows and cells to apply styling  
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=2, max_col=worksheet.max_column):  
    for cell in row:          
        # Add borders to all cells for a neat appearance  
        cell.border = Border(left=Side(border_style="thin"),   
                             right=Side(border_style="thin"),  
                             top=Side(border_style="thin"),  
                             bottom=Side(border_style="thin"))  
# Add a thick outer border  
# 1. Add a thick outer border to the leftmost column  
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=2, max_col=2):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="medium"),   
                              right=Side(border_style="thin"),  
                              top=Side(border_style="thin"),  
                              bottom=Side(border_style="thin"))  
  
# 2. Add a thick outer border to the rightmost column  
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=worksheet.max_column, max_col=worksheet.max_column):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="thin"),   
                              right=Side(border_style="medium"),  
                              top=Side(border_style="thin"),  
                              bottom=Side(border_style="thin"))  
  
# 3. Add a thick outer border to the top row  
for row in worksheet.iter_rows(min_row=2, max_row=2, min_col=2, max_col=worksheet.max_column):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="thin"),   
                              right=Side(border_style="thin"),  
                              top=Side(border_style="medium"),  
                              bottom=Side(border_style="thin"))  
  
# Add a thick outer border to the bottom row  
for row in worksheet.iter_rows(min_row=worksheet.max_row, max_row=worksheet.max_row, min_col=2, max_col=worksheet.max_column):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="thin"),   
                      right=Side(border_style="thin"),  
                      top=Side(border_style="thin"),  
                      bottom=Side(border_style="medium"))  
  
# 4. Add a thick border to the top-left cell that was overwritten  
for row in worksheet.iter_rows(min_row=2, max_row=2, min_col=2, max_col=2):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="medium"),   
                              top=Side(border_style="medium"))  
  
# Add a thick border to the bottom-left cell that was overwritten  
for row in worksheet.iter_rows(min_row=worksheet.max_row, max_row=worksheet.max_row, min_col=2, max_col=2):  
    for cell in row:  
        cell.border = Border(left=Side(border_style="medium"),   
                              bottom=Side(border_style="medium"))  
  
# 5. Add a thick border to the top-right cell that was overwritten  
for row in worksheet.iter_rows(min_row=2, max_row=2, min_col=worksheet.max_column, max_col=worksheet.max_column):  
    for cell in row:  
        cell.border = Border(right=Side(border_style="medium"),   
                              top=Side(border_style="medium"))  
  
# 6. Add a thick border to the bottom-right cell that was overwritten  
for row in worksheet.iter_rows(min_row=worksheet.max_row, max_row=worksheet.max_row, min_col=worksheet.max_column, max_col=worksheet.max_column):  
    for cell in row:  
        cell.border = Border(right=Side(border_style="medium"),   
                              bottom=Side(border_style="medium"))
```

5. Styling Variances

The code provides a method to colorize and adjust the font of the variance column, making negative values red and positive values green.

```python
# Style variance coloumn  
for row in worksheet.iter_rows(min_row=3, max_row=worksheet.max_row, min_col=worksheet.max_column, max_col=worksheet.max_column):  
    for cell in row:  
        if cell.value < 0:  
            cell.font = Font(color="FF0000", size=12, bold=True)  
        else:  
            cell.font = Font(color="00B050", size=12, bold=True)  
  
        # Align all the cell values to the center  
        cell.alignment = Alignment(horizontal="center")
```

6. Add Fill

This code adds a solid color fill to the header row.

```python
for row in worksheet.iter_rows(min_row=2, max_row=2, min_col=2, max_col=worksheet.max_column):  
    for cell in row:  
        cell.fill = PatternFill(fill_type="solid", start_color="CC99FF", end_color="CC99FF")
```

To customize the fill color of a specific column header, you can utilize the following code.

> In this code, the `Variance` column is filled with a distinct color.

```python
# Make the fill color for column `Variance` different  
for row in worksheet.iter_rows(min_row=2, max_row=2, min_col=2, max_col=worksheet.max_column):  
    for cell in row:  
        if cell.value == "Variance":  
            cell.fill = PatternFill(fill_type="solid", start_color="FFFF00", end_color="FFFF00")
```


To highlight rows containing a specific value, you can fill those rows with a distinct color. In the following code snippet, we fill the rows where the ‘`Region`’ is ‘`East`’ with a unique color for better visibility

```python
# Distinguish rows where `Region` is `East`  
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=3, max_col=3):  
    for cell in row:  
        if cell.value == "East":  
            for row in worksheet.iter_rows(min_row=row[0].row, max_row=row[0].row, min_col=2, max_col=worksheet.max_column):  
                for cell in row:  
                    cell.fill = PatternFill(fill_type="solid", start_color="DAEEF3", end_color="DAEEF3")
```

7. Tab color

```python
# Add a tab color to distinguish your sheet  
worksheet.sheet_properties.tabColor = "002060"
```

8. Add a title

```python
# Adding a captivating title to your sheet  
worksheet.cell(1, 1).value = "STYLING EXCEL SHEETS"  
worksheet.cell(1, 1).font = Font(bold=True, color="FF0000", size=13)  
worksheet.cell(1, 1).alignment = Alignment(horizontal="left")
```

8. Merging, Unmerging, and Removing Styles

Although we haven’t implemented these actions in our Excel sheet, you can utilize the following code to merge or unmerge cells, remove all styles from your sheet, and even perform additional operations like moving a specific range one row down.

```python
# If you had merged cells, you can unmerge them using this code  
for cells in list(worksheet.merged_cells):  
    worksheet.unmerge_cells(range_string=str(cells))
```

```python
# If you wish to merge cells, you can use the code below  
worksheet.merge_cells(start_row=2, end_row=2, start_column=3, end_column=5)
```

```python
# Remove the applied styles in your sheet  
for rows in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=2, max_col=worksheet.max_column):  
    for cell in rows:  
        cell.style = "Normal"
```

```python
# Make sure you import this:   
# from openpyxl.utils.cell import get_column_letter  
  
# Move the range one row down  
last_column_letter = get_column_letter(worksheet.max_column)  
worksheet.move_range(f'B2:{last_column_letter}2', rows=1)
```

In scenarios where one style might unintentionally overwrite another, preserving the previous style becomes crucial. This becomes even more relevant if you had previously styled your Data Frame using `.styler` and wish to retain those existing styles.

The code snippet below shows how this can be done.

```python
# This color is stored before applying the `num_comma_style` because it will be overwritten by it  
existing_font_color = cell.font.color  
existing_font_weight = cell.font.bold  
existing_alignment = cell.alignment.horizontal   
  
# Add the comma to separate the numbers and enhance readability  
cell.style = num_comma_style  
  
# Reapply the font color and bold style  
cell.font = Font(color=existing_font_color, bold=existing_font_weight)
```

**A Snapshot of the Styled Excel Sheet**
![[1_VBBeqYK6ZqzjHRtesCB8vw.webp]]

Incorporating these styling techniques into your Excel files not only enhances visual appeal but also communicates your data with clarity and precision. Python, combined with the versatility of `openpyxl`, empowers you to go beyond data analysis and create compelling data stories.

I hope you were able to pick up something from this blog post. If you have any questions you check out the full analysis in this [juypter notebook](https://github.com/FridahKimathi/Blog-Posts/blob/main/stlying%20excel%20files.ipynb) or reach me through my [LinkedIn](https://www.linkedin.com/in/fridah-kimathi-91608418b/).

Thanks For Reading, Follow me for more!