# Updated Ore Generation Settings

# Corrected ore spawning thresholds
# Increased from 0.82-0.86 to 0.87-0.92 to make ores less common
ore_spawning_thresholds = (0.87, 0.92)

# Coal spawning changed from Y=64 to Y=0
coal_spawning_y = 0

# Redstone peak adjusted to Y=-32
redstone_peak_y = -32

# Added emerald ore
# Spawning for Y=-16 to 320 peaking at Y=232
emerald_ore_y_range = (232, 320)  # Peak at 232
emerald_ore_low = -16

# Function to generate ores with updated thresholds

def generate_ores():
    # Implementation of ore generation based on updated thresholds
    pass