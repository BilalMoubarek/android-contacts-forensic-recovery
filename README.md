# 📱 Android Contacts Forensic & Recovery Solution

A production-ready forensic utility engineered by **Bilal Moubarek (Mr_Spy)** to extract and recover system contacts directly from Android's internal database architecture (`contacts2.db`).

## 🚨 System Operations
This solution interfaces with the core SQLite database layers of the Android OS, bypassing standard interface restrictions to dump contact records into a universal restoration **vCard (.vcf)** profile.

## 🛠️ How to Deploy
1. Dump the target partition file from the smartphone via ADB terminal:
```bash
   adb pull /data/data/com.android.providers.contacts/databases/contacts2.db .
