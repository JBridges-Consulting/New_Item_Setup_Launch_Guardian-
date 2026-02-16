# =================================================================
# PROJECT: NEW ITEM SETUP & 90-DAY LAUNCH GUARDIAN
# MODULE: HIGH-VELOCITY MONITOR (Target: 5.0+ UPSPW)
# OPERATOR: Jenica | Principal Operations | Managed Execution
# =================================================================

def run_velocity_audit(brand, product, units, stores, weeks, msrp, target_upspw=5.0):
    # Calculate Metrics
    upspw = units / (stores * weeks)
    dpspw = upspw * msrp
    
    print(f"--- {brand} HIGH-VELOCITY AUDIT: WEEK {weeks} ---")
    print(f"Product: {product} | Target UPSPW: {target_upspw}")
    print("-" * 55)
    print(f"Actual UPSPW:   {upspw:.2f}")
    print(f"Actual DPSPW:   ${dpspw:.2f}")
    print("-" * 55)

    # Agent Trigger Logic for National Mass (Target/Walmart)
    if upspw < 3.5:
        status = "🚨 CRITICAL: AGENT ALERT - HIGH RISK OF DISCONTINUATION"
        action = "Initiating immediate store-level 'Void Audit' and requesting SOS (Share of Shelf) photos."
    elif upspw < 4.5:
        status = "🟡 WARNING: MARGINAL PERFORMANCE"
        action = "Recommend triggering TPR (Temporary Price Reduction) or social ad-spend boost."
    else:
        status = "🟢 SUCCESS: EXCEEDING VELOCITY THRESHOLDS"
        action = "Agent preparing 'Expansion Pitch' for additional shelf facings."
        
    print(f"RESULT: {status}")
    print(f"NEXT STEP: {action}")

# Demo Simulation: Heritage Harvest 8oz Chips
# Simulating Week 4 of a 600-store launch with 9,600 units sold (4.0 UPSPW)
run_velocity_audit(
    brand="Heritage Harvest",
    product="8oz Ancient Grain Chips",
    units=9600, 
    stores=600, 
    weeks=4, 
    msrp=6.49
)