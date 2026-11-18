"""Load the released data, e.g. tables = load_scenario(1)."""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
TABLES = ("states", "actions", "beliefs", "q_values")


def load_scenario(scenario_id):
    """Return a dict of DataFrames for one scenario."""
    folder = DATA / f"scenario_{scenario_id}"
    tables = {name: pd.read_csv(folder / f"{name}.csv") for name in TABLES}
    tables["sessions"] = pd.read_csv(DATA / "sessions.csv").query("scenario_id == @scenario_id")
    return tables


def belief_array(beliefs):
    """Reshape one session's beliefs to steps x agents x tasks x levels."""
    cols = [c for c in beliefs.columns if c.startswith("p_level_")]
    b = beliefs.sort_values(["step", "agent", "task"])
    n_agents, n_tasks = b["agent"].nunique(), b["task"].nunique()
    return b[cols].to_numpy().reshape(-1, n_agents, n_tasks, len(cols))
