import sqlite3
import os

def recover_contacts(db_path):
    if not os.path.exists(db_path):
        print(f"[-] File {db_path} not found! Put contacts2.db here.")
        return

    print(f"[+] Extracting from: {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # SQL Query to pull contacts data
        query = "SELECT display_name, normalized_number FROM phone_lookup JOIN raw_contacts ON raw_contacts.version = phone_lookup.raw_contact_id;"
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("[-] No contacts found.")
            return

        # Create the restoration file (.vcf)
        with open("recovered_contacts.vcf", "w", encoding="utf-8") as vcf:
            for name, phone in rows:
                if name and phone:
                    vcf.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL;TYPE=CELL:{phone}\nEND:VCARD\n")
        
        print(f"[+] Done! Saved {len(rows)} contacts to recovered_contacts.vcf")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    recover_contacts("contacts2.db")
