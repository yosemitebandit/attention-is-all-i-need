import matplotlib.pyplot as plt
import numpy as np

# Create data points
years = np.array([2022, 2023, 2024, 2025])

# Generate random lines with trends
x = np.linspace(2021.5, 2025.5, 100)  # Extended to match x-axis limits

# Create random noise with a trend
np.random.seed(42)  # For reproducibility
noise = np.random.normal(0, 0.15, 100)  # Increased noise amplitude
trend_up = 0.2 * np.exp(0.65 * (x - 2022))  # Pure exponential trend
trend_down = -0.5 * (x - 2022)  # Downward trend

llm_context = 0.2 + trend_up  # No noise for LLM context
attention_span = 1.0 + noise + trend_down

# Create the plot
plt.figure(figsize=(4, 3))  # Smaller figure size
plt.plot(x, llm_context, label='LLM context windows', linewidth=2)
plt.plot(x, attention_span, label='my attention span', linewidth=2)

# Customize the plot
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=9, loc='upper left')  # Increased font size

# Set x-axis limits and ticks with padding
plt.xlim(2021.5, 2025.5)
plt.xticks(years, fontsize=9)  # Increased font size

# Add some padding to y-axis
plt.ylim(-0.5, 2.5)

# Remove y-axis ticks and label
plt.gca().set_yticks([])
plt.gca().set_ylabel('')

# Make the plot look nice
plt.style.use('default')
plt.tight_layout(pad=0.4)  # Slightly more padding for text

# Save the plot
plt.savefig('out.png', dpi=300, bbox_inches='tight')
plt.close()