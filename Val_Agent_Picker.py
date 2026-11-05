"""
Valorant Agent Picker — Interactive Slider Version
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ----- agent_name: (aggression, difficulty of mastering util, team reliability)
agent_stats = {
    "Brimstone": (40, 35, 100),
    "Viper": (20, 105, 125),
    "Omen": (70, 100, 85),
    "Killjoy": (10, 80, 120),
    "Cypher": (15, 95, 115),
    "Sova": (35, 110, 130),
    "Sage": (5, 25, 140),
    "Phoenix": (95, 20, 30),
    "Jett": (135, 85, 5),
    "Reyna": (140, 15, 0),
    "Raze": (130, 70, 20),
    "Breach": (90, 90, 135),
    "Skye": (80, 75, 110),
    "Yoru": (115, 140, 15),
    "Astra": (0, 135, 105),
    "KAY/O": (100, 65, 90),
    "Chamber": (75, 55, 10),
    "Neon": (125, 95, 25),
    "Fade": (50, 85, 95),
    "Harbor": (25, 120, 100),
    "Gekko": (65, 50, 80),
    "Deadlock": (30, 60, 75),
    "Iso": (120, 45, 35),
    "Clove": (105, 40, 50),
    "Vyse": (45, 125, 70),
    "Tejo": (55, 130, 65),
    "Waylay": (110, 115, 40),
    "Veto": (60, 100, 110),
    "Miks": (85, 90, 95),
}

CATEGORIES = ["Aggression", "Util Difficulty", "Team Reliance"]


def find_best_agent(user_aggression, user_skill, user_team):
    """Return (agent_name, score) for the closest stat match using Manhattan distance."""
    best_agent, best_score = None, float("inf")
    for agent, (a, s, t) in agent_stats.items():
        score = abs(user_aggression - a) + abs(user_skill - s) + abs(user_team - t)
        if score < best_score:
            best_agent, best_score = agent, score
    return best_agent, best_score


# ---------- Set up figure ----------
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)  # leave room for sliders

x = np.arange(len(CATEGORIES))
width = 0.35

# Initial slider values (0-100 scale, will be rescaled to 0-140 for matching)
init_aggression = 50
init_skill = 50
init_team = 50


def rescale(v):
    """0-100 slider value -> 0-140 stat scale."""
    return round(v * 140 / 100)


def get_current_match():
    a = rescale(slider_aggression.val)
    s = rescale(slider_skill.val)
    t = rescale(slider_team.val)
    return find_best_agent(a, s, t), (a, s, t)


# Initial computation (sliders not created yet, so compute manually first)
init_a, init_s, init_t = rescale(init_aggression), rescale(init_skill), rescale(init_team)
best_agent, best_score = find_best_agent(init_a, init_s, init_t)
agent_values = agent_stats[best_agent]
user_values = (init_a, init_s, init_t)

bars1 = ax.bar(x - width / 2, agent_values, width, label=best_agent, color="#ff4655")
bars2 = ax.bar(x + width / 2, user_values, width, label="Your Preferences",
               color="#0f1923", edgecolor="#ff4655")

ax.set_ylabel("Score (0–140)")
title = ax.set_title(f"{best_agent} vs Your Preferences  (Match Score: {best_score})")
ax.set_xticks(x)
ax.set_xticklabels(CATEGORIES)
ax.set_ylim(0, 150)
ax.legend(loc="upper right")

labels1 = [ax.annotate(f"{v}", xy=(b.get_x() + b.get_width() / 2, v),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
           for b, v in zip(bars1, agent_values)]
labels2 = [ax.annotate(f"{v}", xy=(b.get_x() + b.get_width() / 2, v),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
           for b, v in zip(bars2, user_values)]

# ---------- Sliders ----------
ax_aggression = plt.axes([0.25, 0.20, 0.55, 0.03])
ax_skill = plt.axes([0.25, 0.14, 0.55, 0.03])
ax_team = plt.axes([0.25, 0.08, 0.55, 0.03])

slider_aggression = Slider(ax_aggression, "Aggression", 0, 100, valinit=init_aggression, valstep=1)
slider_skill = Slider(ax_skill, "Util Skill", 0, 100, valinit=init_skill, valstep=1)
slider_team = Slider(ax_team, "Team Reliance", 0, 100, valinit=init_team, valstep=1)


def update(_):
    global bars1, bars2, labels1, labels2

    (agent, score), (a, s, t) = get_current_match()
    new_agent_values = agent_stats[agent]
    new_user_values = (a, s, t)

    for bar, val in zip(bars1, new_agent_values):
        bar.set_height(val)
    for bar, val in zip(bars2, new_user_values):
        bar.set_height(val)

    # Update value labels
    for lbl in labels1 + labels2:
        lbl.remove()
    labels1[:] = [ax.annotate(f"{v}", xy=(b.get_x() + b.get_width() / 2, v),
                               xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
                  for b, v in zip(bars1, new_agent_values)]
    labels2[:] = [ax.annotate(f"{v}", xy=(b.get_x() + b.get_width() / 2, v),
                               xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
                  for b, v in zip(bars2, new_user_values)]

    bars1.set_label(agent)
    ax.legend(loc="upper right")
    title.set_text(f"{agent} vs Your Preferences  (Match Score: {score})")
    fig.canvas.draw_idle()


slider_aggression.on_changed(update)
slider_skill.on_changed(update)
slider_team.on_changed(update)

plt.show()
