# Flatbot 2026 - Python/RobotPy

FRC Team 4973's robot code in Python using RobotPy.

## Robot Controls

| Control | Action |
|---------|--------|
| A button (hold) | Spin motor at current speed |
| A button (release) | Stop motor |
| D-pad up | Increase speed by 0.05 |
| D-pad down | Decrease speed by 0.05 |

Starting speed: 0.1

## Setup

### Option 1: uv (Recommended)

[uv](https://docs.astral.sh/uv/) manages Python and dependencies automatically - no global installs needed.

```bash
# Install uv (one time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run simulation (uv installs dependencies automatically)
uv run python -m robotpy sim
```

### Option 2: pip

If you prefer using system Python directly:

```bash
# Install dependencies
pip install robotpy[commands2,sim] phoenix6

# Run simulation
python3 -m robotpy sim
```

### Option 3: Docker

For consistent environments across team members.

```bash
# Build (first time only)
docker compose build

# Run simulation
docker compose run --rm robotpy sim
```

## Running Simulation

1. Run: `uv run python -m robotpy sim` (or `python3 -m robotpy sim` if using pip)
2. The simulation GUI opens
3. In the GUI:
   - Go to **Joysticks** panel
   - Map a virtual joystick to port 0
   - Enable **Teleop** mode
4. Test the controls:
   - Press A button → motor output appears
   - Use D-pad up/down → check console for speed changes

## Deploying to Robot

When connected to the robot (via WiFi or USB):

```bash
# Using uv:
uv run python -m robotpy sync    # First time: sync dependencies to roboRIO
uv run python -m robotpy deploy  # Deploy code

# Or using pip:
python3 -m robotpy sync
python3 -m robotpy deploy
```

Then in Driver Station:
1. Connect to robot
2. Enable Teleop
3. Test controls

## Project Structure

```
flatbot2026-python/
├── robot.py            # Main entry point & Robot class
├── robot_container.py  # Hardware setup & button bindings
├── pyproject.toml      # RobotPy config & dependencies
├── Dockerfile          # Dev environment
├── docker-compose.yml  # Easy Docker usage
└── README.md           # This file
```

## Troubleshooting

**Simulation won't start:**
- If using uv: try `uv sync --refresh` to reinstall dependencies
- If using pip: reinstall with `pip install --force-reinstall robotpy[commands2,sim] phoenix6`
- Check Python version: `python3 --version` (need 3.12+)

**Motor not responding in simulation:**
- Check the Joysticks panel - make sure a joystick is mapped to port 0
- Make sure Teleop is enabled (not Disabled or Autonomous)

**Deploy fails:**
- Make sure you're connected to the robot network
- Run sync first: `uv run python -m robotpy sync` (or `python3 -m robotpy sync`)
