// ============================================================
// 03_powerquery_m_code.m
// Power Query M Code — Transformations for Employee Productivity
// In Power BI: Home → Transform Data → Advanced Editor → Paste
// ============================================================

let
    // Step 1: Load CSV
    Source = Csv.Document(
        File.Contents("C:\YourPath\data\raw\employee_productivity_dataset.csv"),
        [Delimiter=",", Columns=8, Encoding=1252, QuoteStyle=QuoteStyle.None]
    ),

    // Step 2: Promote headers
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),

    // Step 3: Set column data types
    TypedTable = Table.TransformColumnTypes(PromotedHeaders, {
        {"Employee_ID",     type text},
        {"Employee_Name",   type text},
        {"Department",      type text},
        {"Date",            type date},
        {"Tasks_Completed", Int64.Type},
        {"Target_Tasks",    Int64.Type},
        {"Quality_Score",   type number},
        {"Hours_Worked",    Int64.Type}
    }),

    // Step 4: Add Productivity_Pct column
    AddedProductivity = Table.AddColumn(
        TypedTable,
        "Productivity_Pct",
        each Number.Round([Tasks_Completed] / [Target_Tasks] * 100, 2),
        type number
    ),

    // Step 5: Add Efficiency column
    AddedEfficiency = Table.AddColumn(
        AddedProductivity,
        "Efficiency",
        each Number.Round([Tasks_Completed] / [Hours_Worked], 2),
        type number
    ),

    // Step 6: Add Month_Name column
    AddedMonthName = Table.AddColumn(
        AddedEfficiency,
        "Month_Name",
        each Date.ToText([Date], "MMM yyyy"),
        type text
    ),

    // Step 7: Add Month_Num for sorting
    AddedMonthNum = Table.AddColumn(
        AddedMonthName,
        "Month_Num",
        each Date.Month([Date]),
        Int64.Type
    ),

    // Step 8: Add Year column
    AddedYear = Table.AddColumn(
        AddedMonthNum,
        "Year",
        each Date.Year([Date]),
        Int64.Type
    ),

    // Step 9: Add Performance Category
    AddedCategory = Table.AddColumn(
        AddedYear,
        "Performance_Category",
        each if [Productivity_Pct] >= 110 then "Excellent"
             else if [Productivity_Pct] >= 100 then "Good"
             else if [Productivity_Pct] >= 90  then "Average"
             else if [Productivity_Pct] >= 80  then "Below Average"
             else "Poor",
        type text
    ),

    // Step 10: Add Quality Category
    AddedQualityCategory = Table.AddColumn(
        AddedCategory,
        "Quality_Category",
        each if [Quality_Score] >= 95 then "High Quality (>=95%)"
             else if [Quality_Score] >= 90 then "Good (90-95%)"
             else if [Quality_Score] >= 85 then "Average (85-90%)"
             else if [Quality_Score] >= 80 then "Below Avg (80-85%)"
             else "Poor (<80%)",
        type text
    ),

    // Step 11: Sort by Date
    SortedTable = Table.Sort(AddedQualityCategory, {{"Date", Order.Ascending}})
in
    SortedTable
