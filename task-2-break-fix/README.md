# Task 2 - Break and Fix

Removed HTTP (port 80) from EC2 security group.

Result: Website became unreachable.

Fix: Re-added HTTP rule (0.0.0.0/0).

Outcome: Website restored successfully.
