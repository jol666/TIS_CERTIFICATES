import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Certificate


class Command(BaseCommand):
    help = "Import certificates from Excel file"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs["file"]

        # Read Excel
        df = pd.read_excel(file_path)

        # Clean column names
        df.columns = df.columns.str.strip().str.lower()

        print("\nDetected columns:", df.columns.tolist())
        print("Total rows:", len(df), "\n")

        created_count = 0

        for _, row in df.iterrows():

            cert_no = str(row.get("certificate_number", "")).strip().upper()

            if not cert_no or cert_no == "NAN":
                continue

            Certificate.objects.update_or_create(
                certificate_number=cert_no,
                defaults={
                    "company_name": row.get("company_name"),
                    "standard": row.get("standard"),
                    "scope": row.get("scope"),
                    "issue_date": row.get("issue_date"),
                    "expiry_date": row.get("expiry_date"),
                    "validity": row.get("validity"),
                }
            )

            created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Imported {created_count} certificates successfully"
        ))
