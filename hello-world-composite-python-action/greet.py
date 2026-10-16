import os
from datetime import datetime, timezone

who_to_greet = os.getenv("WHO_TO_GREET")
print(f"Hello, {who_to_greet}!")

# Workflow command: show an annotation in the run summary
print(f"::notice::Greeted {who_to_greet}")

# Write outputs to the file in GITHUB_OUTPUT (not ::set-output)
with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
output.write(f"time={datetime.now(timezone.utc).isoformat()}\n")