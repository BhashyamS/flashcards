
import streamlit as st

st.set_page_config(
    page_title="Interview Flashcards",
    page_icon="🧠",
    layout="wide",
)

FLASHCARDS = [
    {
        "category": "SQL & Data",
        "question": "Explain one SQL query you optimized.",
        "answer": """At Fox, I worked with a SQL query that pulled camera-device and storage information for a Tableau dashboard. The query joined several tables, extracted attributes from XML fields, calculated storage usage over a 30-day period, and handled devices that appeared in multiple locations.

The original query took several minutes to run because it repeatedly scanned the same data and performed calculations before filtering the records.

I reviewed the joins and execution logic to identify where duplicate rows were being created. I then used CTEs to separate the process into clear steps, filtered the date range earlier, removed unnecessary columns, and used ROW_NUMBER() to retain one valid record for each device and date. I also replaced repeated calculations with reusable aggregated results.

After validating the old and new outputs, the optimized version ran much faster and produced cleaner data for the dashboard. The main lesson was that query optimization is not just about speed—it is also about preserving the accuracy and meaning of the results.

Follow-up — What specifically improved performance?

The biggest improvements came from filtering early, reducing duplicate rows before joining large datasets, avoiding repeated calculations, and aggregating the data at the correct grain before sending it to Tableau."""
    },
    {
        "category": "Dashboards & Reporting",
        "question": "Tell me about a dashboard you built.",
        "answer": """At Fox, I built Tableau dashboards to monitor an enterprise camera ecosystem. One dashboard focused on device health and included location, camera type, firmware, stream availability, recording status, and retention settings.

Another dashboard analyzed daily camera storage usage. It included daily and weekly usage trends, 30-day totals, changes in storage consumption, and filters for location, device, and IP address.

I started by meeting with stakeholders to understand the decisions they wanted to make from the dashboard. I then wrote the SQL queries, validated the data, developed calculated fields, and designed the dashboard so users could move from a high-level summary into specific devices.

The dashboards reduced the need for manual investigation and gave the team a centralized view of operational performance."""
    },
    {
        "category": "Data Quality",
        "question": "How do you validate data quality?",
        "answer": """I validate data quality at several levels.

First, I check completeness by identifying null or missing values in required fields. Second, I check uniqueness to make sure records that should be unique are not duplicated. Third, I validate accuracy by reconciling dashboard totals against the source system or an approved report.

I also check referential integrity between related tables, review valid ranges and accepted values, and compare results across different time periods to identify unexpected changes.

At Fox, I validated ETL data by comparing record counts, totals, and individual sample records between the source database and reporting output. When I found differences, I traced the data through each transformation instead of only correcting the final dashboard.

Before publishing, I also test filters, calculations, date logic, and edge cases such as missing devices or devices appearing in multiple locations."""
    },
    {
        "category": "Automation & Process",
        "question": "Tell me about a process you automated.",
        "answer": """At Visionyle Solutions, I worked on automating backend processes that supported a student information system. Some recurring data-processing activities required manual intervention, so I used Python and Bash scripts to standardize and automate parts of the workflow.

The automation reduced repetitive work, improved consistency, and made the process easier to rerun when new data became available.

I followed a similar approach at Fox by moving manual reporting logic into reusable SQL queries and Tableau dashboards. Instead of employees collecting and comparing information manually, the dashboard refreshed from the underlying data source and provided the necessary KPIs automatically.

When I automate a process, I first document the current workflow, identify repetitive steps, determine where human review is still necessary, and then automate only the stable and clearly defined portions."""
    },
    {
        "category": "Dashboards & Reporting",
        "question": "Explain a time business users asked for a report.",
        "answer": """At Fox, business and technical stakeholders needed a report showing camera storage usage and system health across multiple locations.

Before building anything, I asked what problem they were trying to solve, which metrics they trusted, how frequently they needed the information, and what level of detail was useful. I learned that they needed both a high-level summary and the ability to investigate individual devices.

I translated those requirements into SQL logic and Tableau views. I included overall usage, daily and weekly trends, retention information, device-level details, and filters for location and IP address.

After building the initial version, I reviewed it with users and incorporated their feedback. That process taught me that a technically correct report is not automatically a useful report. It must align with the user's workflow and the decisions they need to make."""
    },
    {
        "category": "SQL & Data",
        "question": "What is the difference between an INNER JOIN and a LEFT JOIN?",
        "answer": """An INNER JOIN returns only records that have a match in both tables.

A LEFT JOIN returns every record from the left table and matching records from the right table. When there is no match, the right-table columns contain null values.

For example, with a loans table and a payments table, an INNER JOIN returns only loans with a matching payment. A LEFT JOIN returns all loans, including loans with no payments.

I would use a LEFT JOIN when I specifically want to identify missing activity, such as active loans that do not have a payment or required document.

```sql
SELECT
    l.loan_id,
    l.borrower_name,
    p.payment_date
FROM loans l
LEFT JOIN payments p
    ON l.loan_id = p.loan_id
WHERE p.loan_id IS NULL;
```

This query identifies loans without matching payment records."""
    },
    {
        "category": "SQL & Data",
        "question": "Explain window functions.",
        "answer": """Window functions perform calculations across a related set of rows without collapsing the individual rows.

For example, GROUP BY might return one row per customer, while a window function allows me to retain every transaction and display the customer's total transaction amount beside each transaction.

Common window functions include:

- ROW_NUMBER() for numbering records or removing duplicates.
- RANK() and DENSE_RANK() for ranking values.
- SUM() OVER() for running totals.
- LAG() and LEAD() for comparing current records with previous or future records.

Example: most recent status for each loan.

```sql
WITH ranked_status AS (
    SELECT
        loan_id,
        status,
        status_date,
        ROW_NUMBER() OVER (
            PARTITION BY loan_id
            ORDER BY status_date DESC
        ) AS row_num
    FROM loan_status_history
)
SELECT
    loan_id,
    status,
    status_date
FROM ranked_status
WHERE row_num = 1;
```"""
    },
    {
        "category": "SQL & Data",
        "question": "What is the difference between GROUP BY and PARTITION BY?",
        "answer": """GROUP BY combines rows and returns one summarized row for each group.

PARTITION BY is used inside a window function. It creates groups for the calculation but preserves the individual rows.

For example, GROUP BY customer_id can calculate one total balance for each customer.

SUM(balance) OVER (PARTITION BY customer_id) retains each loan record while displaying the customer's combined balance beside every loan.

I use GROUP BY when the report needs summary-level results. I use PARTITION BY when the report needs both detailed rows and group-level calculations."""
    },
    {
        "category": "Dashboards & Reporting",
        "question": "How would you design a KPI dashboard?",
        "answer": """I would begin with the business decisions the dashboard needs to support rather than immediately selecting charts.

First, I would speak with stakeholders to determine the audience, purpose, reporting frequency, and definition of each KPI. I would confirm the source system and expected level of detail.

I would place the most important KPIs at the top, such as total loan volume, outstanding balance, delinquency rate, exception count, and average processing time.

The middle section would show trends over time and comparisons by loan type, region, status, or servicing team. The bottom would provide detailed records for users who need to investigate individual accounts.

I would include useful filters without making the dashboard confusing, document KPI definitions, and validate every total against the source data before release.

My goal is to answer three questions quickly: What is happening? Why is it happening? What requires action?"""
    },
    {
        "category": "Data Quality",
        "question": "How do you debug incorrect numbers in a report?",
        "answer": """I start by determining the scope of the issue. I check whether the number is incorrect for every user and time period or only under a particular filter.

Next, I verify the KPI definition. Sometimes the report is technically correct, but business and development teams are using different definitions.

I then trace the number backward:

1. Check dashboard calculations and filters.
2. Check the query output.
3. Check joins for duplicated or missing records.
4. Check aggregation grain.
5. Check date filters and null handling.
6. Reconcile against the source system.
7. Test individual sample records.

For example, if a total balance is too high, I would check whether a one-to-many join duplicated each loan for every payment or status record.

After correcting the logic, I rerun validation, document the cause, and test related metrics."""
    },
    {
        "category": "Behavioral",
        "question": "How do you prioritize multiple stakeholder requests?",
        "answer": """I prioritize requests based on business impact, urgency, risk, dependencies, and required effort.

I first determine whether the request affects a regulatory deadline, customer experience, financial reporting, or a production issue. Those normally receive higher priority than general enhancements.

I clarify the actual deadline rather than assuming everything is urgent. I communicate estimated completion expectations and discuss tradeoffs when priorities conflict.

For larger requests, I break the work into stages. For example, I may provide a validated core report first and add lower-priority visual enhancements afterward.

I also keep stakeholders updated so they understand what is being worked on, what is blocked, and what comes next."""
    },
    {
        "category": "Loan Operations",
        "question": "Why are you interested in loan administration or banking operations?",
        "answer": """I am interested in loan administration because it combines data analysis, operational accuracy, risk awareness, and cross-functional problem-solving.

Although my previous experience was not specifically within loan servicing, I have worked with operational datasets where accuracy, system reliability, exception identification, and clear reporting were important.

I enjoy investigating why numbers do not match, improving inefficient processes, and creating reporting that helps teams take action. Those skills transfer well to loan operations, where teams need accurate account information, timely processing, documented controls, and visibility into exceptions.

I am also interested in learning the full loan lifecycle and understanding how data supports servicing, payments, compliance, and customer outcomes."""
    },
    {
        "category": "Loan Operations",
        "question": "You do not have direct loan experience. Why should we hire you?",
        "answer": """I would not claim to already know every loan-administration process, but I bring the technical and analytical foundation required to learn it quickly.

I have experience with SQL, databases, dashboards, ETL validation, operational KPIs, process improvement, and technical documentation. I have also translated business requirements into reports and solutions.

At Fox, I had to learn a specialized camera-management environment and unfamiliar operational data before I could report on it. I became comfortable with the systems, relationships, and stakeholder requirements by asking questions, documenting definitions, and validating my work carefully.

I would take the same approach in loan administration: learn the lifecycle, understand the controls and terminology, and use my technical skills to improve reporting and operational processes."""
    },
    {
        "category": "Loan Operations",
        "question": "What is the loan lifecycle?",
        "answer": """My general understanding is that the loan lifecycle begins with application and underwriting, followed by approval, documentation, funding, servicing, payment processing, account maintenance, and eventually payoff, closure, collections, or another resolution.

Loan administration supports the accuracy and completeness of records throughout that lifecycle. This can include verifying documentation, maintaining account information, processing transactions, monitoring exceptions, reconciling balances, supporting audits, and ensuring activity follows company policies and regulatory requirements.

The exact responsibilities and systems differ depending on whether the position supports consumer, mortgage, commercial, or auto loans."""
    },
    {
        "category": "Loan Operations",
        "question": "What metrics would you track for loan operations?",
        "answer": """I would confirm the team's priorities first, but possible loan-operations KPIs include:

- Number and value of active loans
- New loans funded
- Average processing or funding time
- Payment processing accuracy
- Delinquency rate
- Past-due balance
- Exception volume
- Document-completion rate
- Queue aging
- Accounts requiring manual review
- Reconciliation differences
- Error or rework rate
- SLA compliance

I would also separate leading indicators from final outcomes. For example, increasing queue age or document exceptions may be an early warning that processing times or customer outcomes could worsen."""
    },
    {
        "category": "SQL & Data",
        "question": "How would you identify delinquent loans using SQL?",
        "answer": """I would first confirm the company's business definition of delinquency because it may depend on days past due, grace periods, account status, and payment rules.

A simplified approach would compare the scheduled due date with the latest valid payment date.

```sql
SELECT
    l.loan_id,
    l.customer_id,
    l.payment_due_date,
    MAX(p.payment_date) AS latest_payment_date,
    DATEDIFF(
        DAY,
        l.payment_due_date,
        CURRENT_DATE
    ) AS days_past_due
FROM loans l
LEFT JOIN payments p
    ON l.loan_id = p.loan_id
WHERE l.loan_status = 'Active'
GROUP BY
    l.loan_id,
    l.customer_id,
    l.payment_due_date
HAVING
    MAX(p.payment_date) IS NULL
    OR MAX(p.payment_date) < l.payment_due_date;
```

In a real environment, I would also account for payment amount, reversed transactions, partial payments, holidays, grace periods, and approved extensions."""
    },
    {
        "category": "SQL & Data",
        "question": "How would you detect duplicate loan payments?",
        "answer": """I would first establish what makes a payment potentially duplicate. It could be the same loan, amount, transaction date, and payment method, but I would not delete anything based only on those values because two legitimate payments can sometimes be identical.

```sql
WITH possible_duplicates AS (
    SELECT
        payment_id,
        loan_id,
        payment_amount,
        payment_date,
        payment_method,
        ROW_NUMBER() OVER (
            PARTITION BY
                loan_id,
                payment_amount,
                payment_date,
                payment_method
            ORDER BY payment_id
        ) AS occurrence_number
    FROM payments
)
SELECT *
FROM possible_duplicates
WHERE occurrence_number > 1;
```

I would validate flagged records using transaction IDs, timestamps, source systems, reversal indicators, and processing logs before taking action."""
    },
    {
        "category": "Loan Operations",
        "question": "How would you reconcile loan balances between two systems?",
        "answer": """I would begin by confirming that both systems use the same effective date and balance definition. For example, one system may include accrued interest while another shows principal only.

I would extract the loan identifier and balance from both systems, standardize formats, and perform a full comparison.

I would classify differences into:

- Exists in both systems and balances match
- Exists in both systems but balances differ
- Exists only in the first system
- Exists only in the second system

I would quantify the number and dollar value of differences, investigate representative records, identify the root cause, and create an exception report.

I would never force the numbers to match without understanding whether the issue came from timing, missing transactions, incorrect mappings, duplicates, or different business definitions."""
    },
    {
        "category": "Data Quality",
        "question": "What would you do if you discovered a significant reporting discrepancy?",
        "answer": """I would first verify the discrepancy independently and determine its scope. I would avoid changing production data or distributing an unverified conclusion.

Once confirmed, I would notify the appropriate manager or data owner, explain which reports or accounts may be affected, and provide the evidence I found.

I would trace the issue through the data pipeline, identify the root cause, and help determine whether it affected operational processing, financial reporting, customers, or compliance requirements.

After correction, I would validate the results, document the incident, and recommend a preventive control such as an automated reconciliation, threshold alert, or additional validation rule."""
    },
    {
        "category": "Risk & Compliance",
        "question": "How do you handle confidential customer and financial data?",
        "answer": """I follow least-access principles and only use the information necessary to perform the assigned task.

I would not download, copy, email, or share customer information outside approved systems. When developing or testing reports, I would use masked or nonproduction data whenever possible.

I would follow access-control procedures, secure file-transfer requirements, retention policies, and clean-desk or screen-lock practices.

If I were uncertain whether data could be shared or used for a particular purpose, I would stop and confirm with the appropriate manager, data owner, security team, or compliance team rather than making an assumption."""
    },
    {
        "category": "Automation & Process",
        "question": "How would you improve an inefficient loan-administration process?",
        "answer": """I would first observe and document the current process instead of assuming I already knew the solution.

I would map each step, system, handoff, approval, manual entry, and exception. I would then quantify where the process slows down or creates errors.

For example, if employees manually compare a payment file against the servicing system every morning, I might develop a SQL reconciliation report that automatically flags missing, duplicated, or mismatched transactions.

I would test the new process with a small group, measure its effect on processing time and accuracy, document it, and retain human review for exceptions or high-risk decisions.

The goal is not to automate everything. It is to remove repetitive work while strengthening accuracy and controls."""
    },
    {
        "category": "Loan Operations",
        "question": "What would you do if a loan document or required field was missing?",
        "answer": """I would first verify whether the document or field is truly required for that loan type and stage.

I would check the source system, document repository, and processing history to determine whether it was never received, incorrectly indexed, or not transferred between systems.

I would document the exception and route it to the appropriate owner according to the team's procedure. I would avoid making assumptions or changing the loan status without authorization.

If missing information became recurring, I would analyze the pattern by source, loan type, team, or process stage and recommend a validation rule or exception dashboard to catch it earlier."""
    },
    {
        "category": "Loan Operations",
        "question": "How would you calculate a delinquency rate?",
        "answer": """The exact definition should be confirmed with the business.

A basic account-based delinquency rate is:

Number of delinquent active loans ÷ Total number of active loans × 100

A balance-based delinquency rate is:

Outstanding balance of delinquent loans ÷ Total outstanding loan balance × 100

These answer different questions. The account-based rate shows the percentage of affected accounts, while the balance-based rate shows financial exposure.

I would clearly label the calculation and ensure excluded accounts, charge-offs, grace periods, and reporting dates are handled consistently."""
    },
    {
        "category": "Risk & Compliance",
        "question": "Describe a control you would build for payment processing.",
        "answer": """I would build a daily reconciliation control comparing the source payment file, processing system, and general-ledger or downstream posting results.

The control would check:

- Record counts
- Total payment amounts
- Duplicate transaction IDs
- Missing transactions
- Reversed or rejected transactions
- Amount differences
- Processing dates
- Accounts with invalid statuses

The output would separate successful records from exceptions and assign each exception a reason category. I would include thresholds and escalation rules so significant discrepancies are reviewed promptly.

The control should create a clear audit trail showing when the reconciliation ran, who reviewed it, which exceptions were resolved, and what remained outstanding."""
    },
    {
        "category": "Loan Operations",
        "question": "What is the difference between principal, interest, and outstanding balance?",
        "answer": """Principal is the original amount borrowed or the remaining portion of that amount that has not yet been repaid.

Interest is the cost charged for borrowing the money.

Outstanding balance is the total amount currently owed. Depending on the institution's definition, it may include remaining principal, accrued interest, fees, or other charges.

When building a report, I would not assume that “balance” always means the same thing. I would confirm whether the metric refers to principal balance, payoff balance, current balance, or another defined amount."""
    },
    {
        "category": "Loan Operations",
        "question": "What would you do if a customer says a payment was made, but the system does not show it?",
        "answer": """I would treat it as an investigation rather than immediately assuming the customer or system was incorrect.

I would check the payment-processing system, transaction history, pending or rejected payment queues, external payment references, posting dates, account identifiers, and reversal activity.

I would also consider timing differences, weekends, holidays, incorrect account numbers, or payments posted to another account.

I would document the findings and follow the approved escalation process. Because this affects customer and financial information, I would not manually alter the account unless I had proper authorization and supporting evidence."""
    },
    {
        "category": "Behavioral",
        "question": "Why should we hire you?",
        "answer": """You should hire me because I combine technical analytics skills with a strong focus on business outcomes and accuracy.

I have hands-on experience using SQL to analyze operational data, building dashboards for stakeholders, validating ETL outputs, and improving manual processes. I am also comfortable learning unfamiliar systems and asking the questions necessary to understand the business context.

I am early in my career, but I bring initiative, curiosity, and a willingness to take ownership. I would contribute through my SQL, reporting, and problem-solving experience while continuing to learn the organization's financial and operational processes."""
    },
    {
        "category": "Behavioral",
        "question": "What is your greatest strength?",
        "answer": """One of my greatest strengths is my ability to investigate a problem methodically.

When a number is incorrect or a report is slow, I do not immediately apply a quick fix. I break the problem into smaller parts, review the data flow, test assumptions, and validate the final result.

That approach helped me with SQL optimization and data-quality work at Fox, and I believe it is especially valuable in financial or loan operations, where small errors can have a larger impact."""
    },
    {
        "category": "Behavioral",
        "question": "What is one weakness you are working on?",
        "answer": """Earlier in my career, I sometimes spent too much time trying to make an analysis or dashboard perfect before sharing it.

I have learned that it is more effective to confirm the core requirements, build a validated first version, and get stakeholder feedback early.

I still care strongly about accuracy, but I now separate essential validation from lower-priority formatting or enhancements."""
    },
    {
        "category": "Behavioral",
        "question": "Tell me about a mistake you made.",
        "answer": """While working with reporting data, I once noticed that totals increased after joining two datasets. The query ran successfully, but the output was not logically correct because one table contained multiple records for each device.

I recognized the issue during validation, stopped the report from being published, and investigated the grain of both tables. I corrected it by deduplicating and aggregating the data before performing the join.

That experience reinforced the importance of checking expected row count and data grain before trusting a query simply because it executes without errors."""
    },
    {
        "category": "Behavioral",
        "question": "Why are you looking for a new opportunity?",
        "answer": """I recently completed my master's degree and my internship at Fox, and I am looking for a full-time position where I can continue building my career in data analysis.

I am especially interested in roles where analytics supports real operational and financial decisions rather than being limited to one-off reporting.

I want to join a team where I can contribute with SQL, dashboards, and process improvement while learning more about the business."""
    },
    {
        "category": "Behavioral",
        "question": "Tell me about yourself.",
        "answer": """I recently completed my master's degree in Computer Science from UC Riverside. My experience is primarily in data analysis, SQL, business intelligence, and process improvement.

Most recently, I worked as a Data Analyst and Developer Intern at Fox Corporation, where I wrote and optimized SQL queries, built Tableau dashboards, validated ETL data, and reported on operational KPIs.

Before that, I worked with Power BI and Excel dashboards at Code Ninjas and used SQL, Python, and Bash to support a student information system at Visionyle Solutions.

I enjoy taking an unclear business problem, understanding the data behind it, and turning it into a report or process that helps people make decisions. I am now looking for a full-time data-focused role where I can apply those skills and continue learning, particularly in a structured financial or operational environment."""
    },

    {
        "category": "Behavioral",
        "question": "Why are you interested in BRG and this Data Analyst role?",
        "answer": """I am interested in this role because it combines the technical work I enjoy—SQL, reporting, dashboards, and automation—with direct business impact.

What stood out to me is that the team supports finance and accounting while also working with IT, operations, and legal. That cross-functional environment fits my experience because I have worked with both technical teams and business users to turn reporting needs into practical solutions.

I am also drawn to BRG's entrepreneurial culture. I like roles where I can learn the business, take ownership of problems, and continuously improve how work is done rather than only producing one-time reports."""
    },
    {
        "category": "Behavioral",
        "question": "Why do you want to work in a finance and accounting organization?",
        "answer": """I am interested in finance and accounting because the data has a direct connection to business performance, operational decisions, and risk.

I enjoy working in environments where accuracy matters and where analysts need to understand not only how to calculate a number, but also what that number means to the business.

My background gives me the technical foundation in SQL, dashboards, data validation, and automation. I see this role as an opportunity to apply those skills while building deeper knowledge of financial processes and reporting."""
    },
    {
        "category": "Behavioral",
        "question": "Tell me about a time you had to learn an unfamiliar business process quickly.",
        "answer": """At Fox, I joined a team working with an enterprise camera-management environment that was completely new to me.

Before I could build meaningful reports, I had to understand how devices, streams, storage, firmware, retention, and locations related to one another. I reviewed the available documentation, asked focused questions, examined sample records, and validated my understanding with the team.

Once I understood the process and data model, I was able to write SQL queries and build dashboards that helped users monitor system health and storage trends.

That experience showed me that I can learn a specialized business process quickly by combining curiosity, documentation, and hands-on validation."""
    },
    {
        "category": "Behavioral",
        "question": "Tell me about a time you disagreed with a stakeholder.",
        "answer": """When I disagree with a stakeholder, I try to separate the person from the issue and focus on the business requirement and the evidence.

For example, if a stakeholder believes a report total is incorrect, I would first ask how they expect the metric to be defined and what source they are comparing it against. I would then walk through the data logic, test sample records, and identify whether the difference comes from filters, timing, or business definitions.

If their interpretation is correct, I adjust the report. If the report logic is correct, I explain the difference clearly and document the agreed definition.

My goal is not to prove that I am right. It is to make sure the final output is accurate and trusted."""
    },
    {
        "category": "Behavioral",
        "question": "How do you communicate technical information to nontechnical stakeholders?",
        "answer": """I start with the business meaning rather than the technical implementation.

Instead of saying that a join created duplicate rows, I might explain that one loan or device was being counted multiple times because it had several related records.

I use simple examples, show the impact on the report, and avoid unnecessary technical terms. I also confirm understanding by asking whether the explanation matches how the stakeholder views the process.

If more detail is needed, I can then explain the SQL or data model behind the result. This layered approach helps different audiences understand the same issue at the right level."""
    },
    {
        "category": "Behavioral",
        "question": "How do you work effectively in a remote environment?",
        "answer": """I work effectively remotely by being organized, responsive, and clear about progress.

I keep track of priorities and deadlines, document decisions, and communicate early when I have a question or encounter a blocker. I also avoid waiting until a project is complete before showing progress. I prefer to share an early version, confirm that I am moving in the right direction, and then continue refining it.

For collaborative work, I summarize requirements and next steps after meetings so everyone has the same understanding.

Remote work requires visibility and trust, so I make sure stakeholders know what I am working on, what has been completed, and where I need input."""
    },
    {
        "category": "Documentation",
        "question": "How do you create technical documentation?",
        "answer": """I write documentation so that another person can understand, use, and maintain the solution without relying entirely on me.

For a report or dashboard, I would document its purpose, source systems, refresh schedule, table relationships, KPI definitions, filters, calculations, assumptions, known limitations, and troubleshooting steps.

For SQL or an automated process, I would also include dependencies, input and output formats, validation checks, and ownership information.

I try to keep documentation practical and current. A long document is not useful if users cannot quickly find the information they need."""
    },
    {
        "category": "Documentation",
        "question": "What would you include in a report specification?",
        "answer": """I would include the report's business purpose, intended audience, required KPIs, detailed metric definitions, source systems, filters, reporting grain, refresh frequency, security requirements, and expected output format.

I would also document acceptance criteria, such as how totals will be validated and what conditions must be met before the report is considered complete.

If multiple teams are involved, I would identify the business owner, technical owner, and data owner.

A clear specification reduces rework because it creates agreement on what the report should do before development begins."""
    },
    {
        "category": "Excel & Reporting",
        "question": "How have you used Excel for analysis?",
        "answer": """I have used Excel for data review, reconciliation, and summary reporting.

I am comfortable with formulas such as VLOOKUP, XLOOKUP, IF statements, SUMIFS, and COUNTIFS, as well as pivot tables, filters, sorting, and conditional formatting.

For example, I can use a pivot table to summarize transactions by department or month, and use lookup formulas to compare records between two files.

I see Excel as especially useful for quick validation, ad hoc analysis, and stakeholder-friendly outputs, while SQL and Power BI are better for repeatable and scalable reporting."""
    },
    {
        "category": "Excel & Reporting",
        "question": "When would you use Excel instead of Power BI?",
        "answer": """I would use Excel when the analysis is small, temporary, highly interactive, or requires detailed manual review by the user.

I would use Power BI when the report needs automated refreshes, a governed data model, consistent KPI definitions, broader distribution, drill-downs, or ongoing monitoring.

Sometimes the best solution uses both. Power BI can provide the standardized dashboard, while Excel can support detailed follow-up analysis or exception review.

The choice should depend on the business need, scale, frequency, and audience rather than personal preference."""
    },
    {
        "category": "Dashboards & Reporting",
        "question": "How do you decide which visualization to use?",
        "answer": """I choose the visualization based on the question the user needs to answer.

I use line charts for trends over time, bar charts for comparing categories, KPI cards for key totals, tables for detailed investigation, and scatter plots for relationships between variables.

I avoid using a chart simply because it looks interesting. The visualization should make the pattern easier to understand than the raw data.

I also consider the audience, the amount of data, and whether the user needs a summary or detailed action list."""
    },
    {
        "category": "Dashboards & Reporting",
        "question": "What makes a dashboard effective?",
        "answer": """An effective dashboard is accurate, focused, easy to understand, and connected to a business decision.

It should highlight the most important information first, use consistent definitions, avoid unnecessary visual clutter, and allow users to investigate exceptions.

It should also load quickly and provide enough context for users to understand what the numbers mean.

A dashboard is successful when stakeholders actually use it to make decisions or take action, not simply when it looks polished."""
    },
    {
        "category": "SQL & Data",
        "question": "What is the difference between WHERE and HAVING?",
        "answer": """WHERE filters rows before aggregation, while HAVING filters groups after aggregation.

For example, WHERE can restrict the data to active loans before calculating totals. HAVING can then return only customers whose total outstanding balance is greater than a certain amount.

```sql
SELECT
    customer_id,
    SUM(outstanding_balance) AS total_balance
FROM loans
WHERE loan_status = 'Active'
GROUP BY customer_id
HAVING SUM(outstanding_balance) > 100000;
```"""
    },
    {
        "category": "SQL & Data",
        "question": "What is a CTE, and when would you use one?",
        "answer": """A CTE, or Common Table Expression, is a named temporary result set used within a SQL statement.

I use CTEs to break complex logic into readable steps, such as filtering data, ranking records, aggregating results, and then joining the final outputs.

CTEs make queries easier to understand and maintain. They can also help with recursive logic, although I most often use them to structure reporting queries.

I still review performance because a CTE does not automatically make a query faster. Its main benefit is organization and clarity."""
    },
    {
        "category": "SQL & Data",
        "question": "How would you find duplicate records in a table?",
        "answer": """I would first define which columns should make a record unique.

Then I could use GROUP BY with HAVING to identify duplicate combinations.

```sql
SELECT
    loan_id,
    transaction_date,
    amount,
    COUNT(*) AS record_count
FROM payments
GROUP BY
    loan_id,
    transaction_date,
    amount
HAVING COUNT(*) > 1;
```

I could also use ROW_NUMBER() if I need to identify the specific duplicate rows.

Before deleting or changing anything, I would confirm whether the duplicates are truly invalid and investigate how they were created."""
    },
    {
        "category": "SQL & Data",
        "question": "How do you handle NULL values in SQL?",
        "answer": """I first determine what the null means because it may represent missing data, not applicable data, or an incomplete process.

I use IS NULL or IS NOT NULL to filter nulls, because comparisons such as equals NULL do not work as expected.

I may use COALESCE to provide a fallback value, but only when that replacement is meaningful.

For example, replacing a missing payment amount with zero could be misleading if the payment record itself is missing. I try to preserve the difference between a true zero and an unknown value."""
    },
    {
        "category": "Data Quality",
        "question": "How would you test a new report before releasing it?",
        "answer": """I would test the report at several levels.

First, I would validate the source data and compare row counts and totals with an approved source. Then I would test calculations, joins, filters, date ranges, null values, duplicates, and boundary cases.

I would also test performance and verify that users only see data they are authorized to access.

Finally, I would ask the business owner to review sample results and confirm that the report meets the agreed requirements.

I would document the test results and any known limitations before release."""
    },
    {
        "category": "Data Quality",
        "question": "What would you do if two departments define the same KPI differently?",
        "answer": """I would not choose one definition on my own.

I would bring the stakeholders together, document both definitions, and ask what business question each version is intended to answer.

Sometimes both metrics are valid but need different names. For example, Finance may define revenue based on posted transactions, while Operations uses processed transactions.

Once the owners agree on the definitions, I would document them clearly in the report and data model so users understand exactly what each KPI represents."""
    },
    {
        "category": "Finance & Accounting",
        "question": "If Finance and Accounting totals do not match, how would you investigate?",
        "answer": """I would first confirm that both teams are using the same reporting period, source systems, currency, account scope, and metric definition.

Then I would compare totals at a high level and progressively break the difference down by account, department, transaction type, and date until I isolated the affected records.

I would check for timing differences, missing postings, duplicate transactions, reversed entries, mapping issues, and different treatment of accruals or adjustments.

I would document the reconciliation and avoid changing either report until the root cause was understood and validated by the appropriate owners."""
    },
    {
        "category": "Finance & Accounting",
        "question": "How would you validate a monthly financial report?",
        "answer": """I would confirm the reporting period and compare the report totals with the relevant source systems or general ledger.

I would perform record-count and amount reconciliations, compare results with the prior month, investigate material variances, and review missing or duplicate transactions.

I would also test account mappings, date logic, signs, currency conversions, and late adjustments.

Any unresolved differences would be documented as exceptions and reviewed with the report owner before the report was finalized."""
    },
    {
        "category": "Finance & Accounting",
        "question": "What is a reconciliation?",
        "answer": """A reconciliation is the process of comparing two data sources or sets of records to confirm that they agree.

The goal is to identify missing, duplicated, delayed, or incorrectly recorded transactions.

A good reconciliation does more than show that totals differ. It categorizes the differences, identifies the affected records, assigns ownership, and creates an audit trail showing how each exception was resolved."""
    },
    {
        "category": "Automation & Process",
        "question": "How do you decide whether a process should be automated?",
        "answer": """I look for processes that are repetitive, rules-based, time-consuming, and prone to manual error.

I also consider the stability of the process. Automating a process that changes every week can create more maintenance than value.

Before automating, I estimate the current effort, error rate, frequency, and business impact. I also identify exceptions that still require human judgment.

The best candidates are usually high-volume tasks with clear rules, such as recurring reconciliations, file validation, report refreshes, or exception identification."""
    },
    {
        "category": "Automation & Process",
        "question": "How would you improve a manual monthly reporting process?",
        "answer": """I would first map the current process from data collection through final distribution.

I would identify which steps are manual, where files are copied or reformatted, which calculations are repeated, and where errors commonly occur.

Then I would centralize the source data, move repeatable logic into SQL or Power Query, automate refreshes where appropriate, add validation checks, and create a documented review workflow.

I would measure improvement using time saved, reduction in errors, and faster report delivery."""
    },
    {
        "category": "SSRS & Reporting",
        "question": "Have you worked with SQL Server Reporting Services?",
        "answer": """I have not yet used SSRS directly in a production environment.

My reporting experience has primarily been with Tableau and Power BI, where I have connected to SQL data sources, created calculated fields and KPIs, built interactive reports, and validated outputs.

Because the core reporting concepts are transferable—datasets, parameters, filters, calculations, refreshes, and distribution—I am confident I could learn SSRS quickly.

I would be honest about the gap while emphasizing that I already understand the underlying SQL and reporting workflow."""
    },
    {
        "category": "SSRS & Reporting",
        "question": "What is the difference between an interactive dashboard and a paginated report?",
        "answer": """An interactive dashboard is designed for exploration. Users can filter, drill down, and compare KPIs visually.

A paginated report is designed for structured, printable output with precise formatting, repeated headers, and detailed tables that may span multiple pages.

Power BI and Tableau are often used for interactive dashboards, while SSRS is commonly used for operational or paginated reporting.

I would choose based on whether users need exploration and visualization or a fixed, detailed report for distribution and recordkeeping."""
    },
    {
        "category": "Scenario",
        "question": "A stakeholder asks for an urgent report by the end of the day, but the requirements are unclear. What do you do?",
        "answer": """I would quickly clarify the decision the report needs to support, the required metrics, the data source, and the minimum acceptable output.

I would explain what can realistically be delivered by the deadline and separate essential requirements from optional enhancements.

I would provide a validated first version, clearly label any assumptions, and schedule follow-up work for improvements.

I would not rush an unvalidated report simply to meet the deadline, especially if the numbers could affect financial or operational decisions."""
    },
    {
        "category": "Scenario",
        "question": "A report is due, but one source system has not refreshed. What do you do?",
        "answer": """I would first confirm the refresh status and determine which metrics are affected.

I would notify the report owner, explain the issue, and provide options. Depending on the business need, that could mean delaying the report, publishing unaffected sections, or using the latest available data with a clear disclosure.

I would never present stale data as current without informing users.

Afterward, I would investigate whether monitoring or an automated freshness alert could prevent the same problem in the future."""
    },
    {
        "category": "Scenario",
        "question": "What would you do if a manager asked you to change a number without supporting data?",
        "answer": """I would respectfully ask for the business reason and supporting documentation.

I would explain that I need to preserve the accuracy and auditability of the report, especially when financial information is involved.

If the change is a legitimate adjustment, I would make sure it follows the approved process and is clearly documented.

If I still had concerns, I would escalate to the appropriate data owner or manager rather than making an unsupported change."""
    },
    {
        "category": "Behavioral",
        "question": "What would your manager say about you?",
        "answer": """I believe my manager would say that I am dependable, curious, and willing to take ownership.

When I receive a task, I try to understand the business purpose, not just complete the technical request. I also communicate when I need clarification and validate my work before presenting it.

I think they would also say that I learn quickly. At Fox, I had to become comfortable with an unfamiliar system and data model before I could build useful reporting, and I was able to do that successfully."""
    },
    {
        "category": "Behavioral",
        "question": "Where do you see yourself in three to five years?",
        "answer": """In three to five years, I would like to be a well-rounded data analyst who understands both the technical and business sides of reporting and process improvement.

I want to deepen my skills in SQL, Power BI, financial data, and automation while becoming someone stakeholders trust to solve complex reporting problems.

Over time, I would also like to take ownership of larger initiatives and help improve the team's reporting standards and processes."""
    },
    {
        "category": "Behavioral",
        "question": "Do you have any questions for us?",
        "answer": """Yes. I would ask two or three questions such as:

- What would be the most important priorities for this person during the first three to six months?
- What types of reports or business processes would this analyst support most frequently?
- How does the team collaborate with finance, accounting, IT, operations, and legal?
- How do you measure success in this role?
- Could you walk me through the remaining steps and expected hiring timeline?

I would avoid directly asking how many candidates are being interviewed. Asking about the process and timeline is more professional."""
    },
]

CUSTOM_CSS = """
<style>
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    .hero {
        padding: 1.35rem 1.5rem;
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 18px;
        margin-bottom: 1rem;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.1rem;
    }

    .hero p {
        margin: 0.35rem 0 0;
        opacity: 0.75;
    }

    .answer-card {
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 18px;
        padding: 1.4rem 1.5rem;
    }

    .category-pill {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        background: rgba(128, 128, 128, 0.14);
        font-size: 0.82rem;
        margin-bottom: 0.75rem;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        min-height: 3.2rem;
        text-align: left;
        justify-content: flex-start;
        white-space: normal;
        border-radius: 12px;
        padding: 0.65rem 0.8rem;
    }

    div[data-testid="stButton"] > button:hover {
        transform: translateY(-1px);
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "selected_card" not in st.session_state:
    st.session_state.selected_card = 0

st.markdown(
    """
    <div class="hero">
        <h1>🧠 Interview Flashcards</h1>
        <p>Click a question, think through your answer, and reveal the prepared response.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

categories = ["All"] + sorted({card["category"] for card in FLASHCARDS})

filter_col, search_col, count_col = st.columns([1.1, 2.2, 0.7])
with filter_col:
    selected_category = st.selectbox("Category", categories)

with search_col:
    search_text = st.text_input(
        "Search questions",
        placeholder="Try: SQL, delinquency, dashboard, weakness...",
    )

with count_col:
    st.metric("Total cards", len(FLASHCARDS))

filtered_indices = []
for index, card in enumerate(FLASHCARDS):
    category_match = selected_category == "All" or card["category"] == selected_category
    search_match = (
        not search_text
        or search_text.lower() in card["question"].lower()
        or search_text.lower() in card["answer"].lower()
    )
    if category_match and search_match:
        filtered_indices.append(index)

st.divider()

questions_col, answer_col = st.columns([1.05, 1.55], gap="large")

with questions_col:
    st.subheader(f"Questions ({len(filtered_indices)})")

    if not filtered_indices:
        st.warning("No questions match the current filters.")
    else:
        for display_number, index in enumerate(filtered_indices, start=1):
            card = FLASHCARDS[index]
            button_type = "primary" if index == st.session_state.selected_card else "secondary"

            if st.button(
                f"{display_number}. {card['question']}",
                key=f"question_{index}",
                type=button_type,
                use_container_width=True,
            ):
                st.session_state.selected_card = index
                st.rerun()

with answer_col:
    selected = FLASHCARDS[st.session_state.selected_card]

    st.markdown('<div class="answer-card">', unsafe_allow_html=True)
    st.markdown(
        f'<span class="category-pill">{selected["category"]}</span>',
        unsafe_allow_html=True,
    )
    st.subheader(selected["question"])
    st.divider()
    st.markdown(selected["answer"])

    if st.button("🎲 Random card", use_container_width=True):
        import random

        possible = filtered_indices if filtered_indices else list(range(len(FLASHCARDS)))
        st.session_state.selected_card = random.choice(possible)
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

with st.expander("How to run this app"):
    st.code(
        "pip install streamlit\nstreamlit run interview_flashcards.py",
        language="bash",
    )
