from pathlib import Path
import csv


# --------------------------------------------------
# Lesson 10 Build 2: Google Sheets Table Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate CSV templates for AppSheet low-code apps
# --------------------------------------------------


def create_csv(file_path, headers, sample_rows):
    """
    Create a CSV file with headers and sample rows.
    """

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in sample_rows:
            writer.writerow(row)


def generate_research_project_tracker(output_dir):
    """
    Generate CSV tables for a Research Project Tracker app.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    # MainRecords table
    main_records_headers = [
        "RecordID",
        "Title",
        "ProjectType",
        "ResearchTheme",
        "LeadResearcher",
        "Status",
        "Priority",
        "DueDate",
        "NextAction",
        "TargetJournalOrFunder",
        "Notes",
        "CreatedDate",
        "LastUpdated"
    ]

    main_records_samples = [
        [
            "RP001",
            "AI-enabled harvest maturity assessment in LMIC horticulture",
            "Literature Review",
            "Postharvest Technology and AI",
            "Professor Ola",
            "In Progress",
            "High",
            "2026-06-30",
            "Refine review question and search strategy",
            "Postharvest Biology and Technology",
            "Focus on AI, maturity assessment, LMIC deployment barriers",
            "2026-05-21",
            "2026-05-21"
        ],
        [
            "RP002",
            "Edible coatings for tomato shelf-life extension",
            "Manuscript",
            "Postharvest Loss Reduction",
            "Professor Ola",
            "Planning",
            "Medium",
            "2026-07-15",
            "Develop manuscript outline",
            "Scientia Horticulturae",
            "Consider warm-chain framing",
            "2026-05-21",
            "2026-05-21"
        ]
    ]

    # People table
    people_headers = [
        "PersonID",
        "FullName",
        "Role",
        "Email",
        "Phone",
        "Organization"
    ]

    people_samples = [
        [
            "P001",
            "Professor Ola",
            "Lead Researcher",
            "example@email.com",
            "",
            "ResearchLab"
        ],
        [
            "P002",
            "Collaborator Name",
            "Collaborator",
            "collaborator@email.com",
            "",
            "Partner Institution"
        ]
    ]

    # ActivityLog table
    activity_headers = [
        "LogID",
        "RecordID",
        "ActionDate",
        "ActionType",
        "Comment",
        "UpdatedBy"
    ]

    activity_samples = [
        [
            "L001",
            "RP001",
            "2026-05-21",
            "Created",
            "Project record created",
            "Professor Ola"
        ],
        [
            "L002",
            "RP001",
            "2026-05-22",
            "Updated",
            "Added literature review focus",
            "Professor Ola"
        ]
    ]

    # Documents table
    documents_headers = [
        "DocumentID",
        "RecordID",
        "DocumentName",
        "DocumentType",
        "Link",
        "UploadDate"
    ]

    documents_samples = [
        [
            "D001",
            "RP001",
            "Initial Review Outline",
            "Outline",
            "https://example.com/document-link",
            "2026-05-21"
        ],
        [
            "D002",
            "RP002",
            "Edible Coatings Notes",
            "Research Notes",
            "https://example.com/document-link",
            "2026-05-21"
        ]
    ]

    create_csv(output_dir / "MainRecords.csv", main_records_headers, main_records_samples)
    create_csv(output_dir / "People.csv", people_headers, people_samples)
    create_csv(output_dir / "ActivityLog.csv", activity_headers, activity_samples)
    create_csv(output_dir / "Documents.csv", documents_headers, documents_samples)


print("\nGoogle Sheets Table Generator")
print("Lesson 10: Build 2")
print("Type 'exit' anytime to stop.\n")

solution_name = input("Enter solution name, for example Research Project Tracker: ")

if solution_name.lower().strip() in ["exit", "quit", "stop"]:
    print("Table generator ended.")
else:
    base_dir = Path(__file__).parent
    output_dir = base_dir / "generated_google_sheets_tables" / solution_name.replace(" ", "_")

    generate_research_project_tracker(output_dir)

    print("\nGenerated Google Sheets CSV templates:\n")
    print(output_dir / "MainRecords.csv")
    print(output_dir / "People.csv")
    print(output_dir / "ActivityLog.csv")
    print(output_dir / "Documents.csv")

    print("\nNext step:")
    print("1. Upload these CSV files into Google Sheets.")
    print("2. Use each CSV as a separate sheet tab.")
    print("3. Connect the Google Sheet to AppSheet.")
    print("4. Let AppSheet generate the app interface.")