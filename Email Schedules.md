# Email Schedules

**User Guide**

**Product:** SnowIQ
**Document Version:** 1.0
**Last Updated:** December 2024

---

## 1. Overview

The **Email Schedules** feature allows you to automate the delivery of SnowIQ insights directly to your inbox. Instead of logging into the dashboard manually, you can configure reports to be generated and emailed on a recurring schedule or on demand.

This helps teams:

* Stay informed without manual effort
* Monitor cost, performance, and security proactively
* Share insights with stakeholders automatically

---

## 2. Managing Schedules

### 2.1 Schedules List

The **Email Schedules** page displays all configured schedules along with their current status and details.

Each schedule includes the following information:

* **Name**
  Friendly name assigned to the report

* **Status**

  * **Active:** Emails are being sent as scheduled
  * **Paused:** Emails are temporarily stopped

* **Frequency**
  How often the report runs (Daily, Weekly, or Monthly)

* **Recipients**
  Email addresses or distribution lists receiving the report

* **Last Run / Next Run**
  Timestamps for tracking report execution

---

### 2.2 Available Actions

Each schedule supports the following actions:

* **Edit (✏️)**
  Modify the schedule name, recipients, frequency, or report content

* **Run Immediately (🚀)**
  Trigger the report instantly (useful for testing or one-time updates)

* **Pause / Resume (▶️ / ⏸️)**
  Temporarily stop or restart email delivery without deleting the schedule

* **Delete (🗑️)**
  Permanently remove the schedule

> ⚠️ **Warning:** Deleted schedules cannot be recovered.

---

## 3. Creating a New Schedule

Click **➕ Create Schedule** to open the schedule configuration wizard.

---

### 3.1 Basic Information

Provide the following details:

* **Schedule Name**
  A clear and descriptive name
  *Example:* `Weekly Executive Summary`

* **Recipient Emails**
  Comma-separated list of email addresses
  *Example:*
  `manager@company.com, team@company.com`

* **Snowflake Accounts**
  Select the accounts from which data will be included:

  * **All Accounts**, or
  * Specific accounts (e.g., `PROD` only)

---

### 3.2 Schedule & Triggers

Configure when and how often the report runs.

#### Frequency Options

* **Daily** – Runs every day at a specified time
* **Weekly** – Runs on a selected day of the week
* **Monthly** – Runs on a selected day of the month

#### Additional Settings

* **Timezone**
  Defaults to server time but can be customized

* **Data Range**
  Determines how far back the report analyzes data
  *Example:* `Last 7 Days`

---

#### Conditional Sending (Smart Alerts)

Optional conditions control when emails are sent:

* **Only send if issues are detected**
  Emails are sent only if critical issues or anomalies are found

* **Only send if cost exceeds $X**
  Useful for cost monitoring and budget alerts

> 💡 **Tip:** Smart alerts help reduce unnecessary emails when systems are healthy.

---

### 3.3 Report Content Builder

The **Report Content Builder** allows you to customize exactly what information appears in the email.

You may include only the sections that are relevant to your audience.

---

#### Available Sections

* **Edition & Account Type**
  High-level account inventory and edition details

* **Cost Intelligence**
  Spend trends and financial forecasting

* **Compute & Warehouses**
  Warehouse usage, inefficiencies, and top cost drivers

* **Query Performance**
  Slow queries and performance bottlenecks

* **Security & Governance**
  Failed logins, privilege analysis, and policy effectiveness

* **Data Sharing**
  Usage statistics for shared data

* **Data Transfer**
  Ingress and egress data volumes

* **Storage**
  Storage growth trends and unused table identification

* **AI Advisor**
  Cortex-powered narrative insights and recommendations

---

#### Customization Options

* Enable or disable individual metrics within each section
* Drag and drop sections to reorder them based on priority

---

## 4. Workflow Example: Monday Morning Briefing

This example demonstrates how to create a weekly executive report.

1. Click **Create Schedule**
2. Set **Schedule Name:**
   `Monday Morning Snowflake Brief`
3. Set **Frequency:**
   **Weekly**, every **Monday at 08:00 AM**
4. Set **Data Range:**
   `Last 7 Days`
5. Select report content:

   * **Cost Intelligence** – Review last week’s spend
   * **Compute & Warehouses → Recommendations** – Identify optimization opportunities
   * **Security → Failed Logins** – Perform a security check
6. Click **Save Schedule**

The report will now be delivered automatically every Monday morning.
