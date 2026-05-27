# 📱 Android Contacts Forensic & Recovery Solution

A hardcore Python-based forensic utility engineered by **Bilal Moubarek (Mr_Spy)** to parse, extract, and recover lost or deleted phone numbers directly from Android's internal infrastructure database (`contacts2.db`).

## 🚨 The Science Behind the Solution
When you delete a contact on Android, the system doesn't immediately overwrite the hardware block. Instead, it flags the row in the SQLite database (`raw_contacts.deleted = 1`). This tool bypasses the standard UI and queries the internal SQL layer directly to reconstruct a universal **vCard (.vcf)** restoration file.

## 🛠️ Operational Protocol
1. **Pull the Database**: Root or use ADB backup to pull the system database file:
   ```bash
   adb pull /data/data/com.android.providers.contacts/databases/contacts2.db .
