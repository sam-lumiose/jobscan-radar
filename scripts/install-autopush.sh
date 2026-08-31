#!/bin/bash
# Install the jobscan autopush launchd agent (publishes every 5 minutes).
#
#   bash ~/Documents/jobscan-digest/scripts/install-autopush.sh
#
# Safe to re-run. Reports any pre-existing autopush schedule before installing,
# so you can see whether something is already doing this job.

set -uo pipefail

LABEL="com.sam.jobscan-autopush"
REPO="$HOME/Documents/jobscan-digest"
SRC="$REPO/scripts/com.sam.jobscan-autopush.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"
UID_NUM="$(id -u)"

echo "== checking for an existing autopush schedule =="

# Other launch agents/daemons pointing at the same script.
FOUND=0
for dir in "$HOME/Library/LaunchAgents" /Library/LaunchAgents /Library/LaunchDaemons; do
  [ -d "$dir" ] || continue
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    if [ "$(basename "$f")" != "$LABEL.plist" ]; then
      echo "  ! another agent references autopush: $f"
      FOUND=1
    fi
  done < <(grep -rls "jobscan-autopush" "$dir" 2>/dev/null)
done

# A crontab entry doing the same thing.
if crontab -l 2>/dev/null | grep -q "jobscan-autopush"; then
  echo "  ! crontab also runs autopush — see 'crontab -l'"
  FOUND=1
fi

[ "$FOUND" -eq 0 ] && echo "  none found (other than this one, if already installed)"

echo
echo "== installing $LABEL =="
[ -f "$SRC" ] || { echo "ERROR: plist not found at $SRC"; exit 1; }
[ -x "$REPO/scripts/jobscan-autopush.sh" ] || chmod +x "$REPO/scripts/jobscan-autopush.sh"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DEST"

# Replace any previous load of this label, then start one run now.
launchctl bootout "gui/$UID_NUM/$LABEL" 2>/dev/null
launchctl bootstrap "gui/$UID_NUM" "$DEST" || {
  echo "ERROR: bootstrap failed — check $DEST"; exit 1; }
launchctl kickstart "gui/$UID_NUM/$LABEL" >/dev/null 2>&1

echo "installed and started."
echo
echo "It now publishes within ~5 minutes of any change to $REPO."
echo
echo "  status:     launchctl print gui/$UID_NUM/$LABEL | head -20"
echo "  log:        tail -f ~/Library/Logs/jobscan-autopush.log"
echo "  stop:       launchctl bootout gui/$UID_NUM/$LABEL"
echo "  uninstall:  launchctl bootout gui/$UID_NUM/$LABEL && rm $DEST"
