# =================================================================
# PROJECT: NEW ITEM SETUP & 90-DAY LAUNCH GUARDIAN
# MODULE: RETAILER VOID & GHOST INVENTORY AUDIT
# OPERATOR: Jenica | Principal Operations | Managed Execution
# =================================================================

import pandas as pd

def run_void_audit(store_data):
    print(f"--- RETAIL VOID AUDIT: HERITAGE HARVEST 8oz ---")
    print(f"{'Store ID':<10} | {'On-Hand':<8} | {'7-Day Sales':<12} | {'Status'}")
    print("-" * 55)
    
    voids_found = 0
    
    for store in store_data:
        store_id = store['id']
        oh = store['on_hand']
        sales = store['last_7_days_sales']
        
        # Logic: If OH > 12 (one case) and Sales are 0, it's a Ghost Inventory Void
        if oh >= 12 and sales == 0:
            status = "🚨 VOID: GHOST INVENTORY"
            voids_found += 1
        elif oh < 6 and sales == 0:
            status = "⚠️ OOS: REPLENISHMENT ISSUE"
            voids_found += 1
        else:
            status = "✅ ACTIVE"
            
        print(f"{store_id:<10} | {oh:<8} | {sales:<12} | {status}")

    print("-" * 55)
    print(f"TOTAL VOIDS DETECTED: {voids_found}")
    if voids_found > 0:
        print("ACTION: Exporting 'Store-Level Action Plan' for Field Team.")

# Simulated Store Data (Target Midwest Region)
target_stores = [
    {"id": "T-1102", "on_hand": 24, "last_7_days_sales": 35}, # Healthy
    {"id": "T-1105", "on_hand": 18, "last_7_days_sales": 0},  # Ghost Inventory (Void)
    {"id": "T-1240", "on_hand": 2,  "last_7_days_sales": 0},  # True OOS
    {"id": "T-1301", "on_hand": 48, "last_7_days_sales": 110}, # Power Store
    {"id": "T-1402", "on_hand": 30, "last_7_days_sales": 0}   # Ghost Inventory (Void)
]

run_void_audit(target_stores)