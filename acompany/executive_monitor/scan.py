from pathlib import Path
from datetime import datetime
import json

# -------- CONFIG --------
ROOT = Path(__file__).parents[2]
STATE_FILE = Path(__file__).parent / "state.json"
IGNORE_DIRS = {".venv", "__pycache__", ".git"}
# ------------------------


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def scan_sector(path: Path, old_state: dict):
    changes = []

    old_files = old_state.get("files", {})
    old_dirs = set(old_state.get("dirs", []))

    new_files = {}
    new_dirs = set()

    for p in path.rglob("*"):
        if any(part in IGNORE_DIRS for part in p.parts):
            continue

        rel = str(p.relative_to(ROOT))

        if p.is_dir():
            new_dirs.add(rel)
            if rel not in old_dirs:
                changes.append(f"📁 NEW DIR {rel}")

        elif p.is_file():
            mtime = p.stat().st_mtime
            new_files[rel] = mtime

            if rel not in old_files:
                changes.append(f"🆕 NEW FILE {rel}")
            elif old_files[rel] != mtime:
                changes.append(f"✏️ MODIFIED {rel}")

    # Deletions
    for f in old_files:
        if f not in new_files:
            changes.append(f"🗑️ DELETED FILE {f}")

    for d in old_dirs:
        if d not in new_dirs:
            changes.append(f"🗑️ DELETED DIR {d}")

    new_state = {
        "files": new_files,
        "dirs": sorted(new_dirs),
    }

    return changes, new_state


def discover_sectors():
    """
    Auto-detect all company sectors.
    Example: b_Software-Development, c_Data-Science-AI, etc.
    """
    sectors = {}
    for p in ROOT.iterdir():
        if p.is_dir() and "_" in p.name:
            name = p.name.split("_", 1)[1].replace("-", " ")
            sectors[name] = p
    return sectors


def main():
    state = load_state()
    sectors = discover_sectors()

    print("\n📊 DAILY PROJECT SCAN")
    print(f"🕒 {datetime.now()}\n")

    for name, path in sectors.items():
        old_sector_state = state.get(name, {})
        changes, new_sector_state = scan_sector(path, old_sector_state)

        if changes:
            print(f"🔔 {name} changes:")
            for c in changes:
                print(" ", c)
        else:
            print(f"✅ {name}: no changes")

        print()
        state[name] = new_sector_state

    save_state(state)


if __name__ == "__main__":
    main()
