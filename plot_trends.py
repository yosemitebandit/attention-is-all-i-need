import matplotlib.pyplot as plt
import numpy as np

years = np.array([2022, 2023, 2024, 2025])
x = np.linspace(2021.5, 2025.5, 100)

np.random.seed(42)
noise = np.random.normal(0, 0.15, 100)
trend_up = 0.2 * np.exp(0.65 * (x - 2022))
trend_down = -0.5 * (x - 2022)

llm_context = 0.2 + trend_up
attention_span = 1.0 + noise + trend_down

plt.figure(figsize=(4, 3))
plt.plot(x, llm_context, label='LLM context windows', linewidth=2)
plt.plot(x, attention_span, label='my attention span', linewidth=2)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=9, loc='upper left')

plt.xlim(2021.5, 2025.5)
plt.xticks(years, fontsize=9)

plt.ylim(-0.5, 2.5)

plt.gca().set_yticks([])
plt.gca().set_ylabel('')

plt.style.use('default')
plt.tight_layout(pad=0.4)

plt.savefig('out.png', dpi=300, bbox_inches='tight')
plt.close()