# Data dictionary

Indices are 0-based. A session is one participant playing one scenario, and `step` runs from 0 to 19.

## Agents
Agents `R0`-`R5` are robots and `H` is the human participant. The same labels are used in every table.

`agents.csv` gives each agent's capability. `capability_even_tasks` applies to tasks 0, 2, 4, 6 and 8, and `capability_odd_tasks` to tasks 1, 3, 5, 7 and 9.

## Tasks and sites
There are 10 tasks at 5 sites: tasks `2k` and `2k+1` are at site `k`. A task's level runs from 4 down to 0, where 0 means complete.

## participant_scenarios.csv
One row per participant. `scenario_1`-`scenario_6` are 1 when the dataset has that participant's session for that scenario, and 0 otherwise. `n_scenarios` counts the scenarios with data.

## sessions.csv
One row per session.

| Column | Meaning |
|---|---|
| `n_active_steps` | Steps before every task reached level 0 |

## scenario_N/ (one folder per scenario)
All four tables are keyed by `participant_id` and `step`.

| File | One row per | Columns |
|---|---|---|
| `states.csv` | step | `done` (1 when every task is at level 0; later steps are padding), `task_0`-`task_9` (task levels) |
| `actions.csv` | step | One column per agent, with the action code below |
| `beliefs.csv` | step, agent and task | `p_level_0`-`p_level_4`: the agent's probability that the task is at each level; sums to 1 |
| `q_values.csv` | step and agent | `q_task_0`-`q_task_9` (value of working on each task) and `q_idle` (value of idling) |

## Action codes
| Code | Meaning |
|---|---|
| 1-10 | Work on task `code - 1` |
| 11-15 | Idle at site `code - 11` |

## Scenarios
TODO: describe what differs across scenarios 1-6. All six start from the same state, beliefs and Q-values.
