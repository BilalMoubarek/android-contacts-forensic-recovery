import sqlite3
import os

# ====================================================================
# PROJECT   : Android Contacts Forensic & Recovery Tool
# DEVELOPER : Bilal Moubarek (aka Mr_Spy)
# INSTAGRAM : @mr_._spy
# YEAR      : 2026
# ====================================================================

def print_banner():
    """Prints the official terminal branding for Mr_Spy."""
    print("====================================================")
    print("      Mr_Spy's Android Contact Recovery v1.0        ")
    print("   Engineered by: Bilal Moubarek | IG: @mr_._spy    ")
    print("====================================================")

def recover_contacts(db_path):
    if not os.path.exists(db_path):
        print(f"[-] Error: System database '{db_path}' not found!")
        print("[*] Instruction: Please place 'contacts2.db' in this folder.")
        print("[*] For support, contact developer on IG: @mr_._spy")
        return

    print(f"[+] Connected to Android Database target: {db_path}")
    print("[*] Mr_Spy's extraction query initializing...")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Forensics query to dump display names and numbers
        query = """
        SELECT raw_contacts.display_name, phone_lookup.normalized_number 
        FROM raw_contacts 
        JOIN phone_lookup ON raw_contacts.version = phone_lookup.raw_contact_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("[-] No contact architecture found inside this database.")
            return

        output_file = "recovered_contacts.vcf"
        
        # Compiling the universal restoration format (.vcf)
        with open(output_file, "w", encoding="utf-8") as vcf:
            for name, phone in rows:
                if name and phone:
                    vcf.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL;TYPE=CELL:{phone}\nEND:VCARD\n")
        
        print("\n" + "="*50)
        print(f"[+] SUCCESS! {len(rows)} contacts recovered successfully.")
        print(f"[+] Output compiled into: {output_file}")
        print(f"[+] Curated and secured by Bilal Moubarek (Mr_Spy)")
        print("="*50)
        
    except sqlite3.Error as e:
        print(f"[-] Database extraction error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print_banner()
    recover_contacts("contacts2.db")
