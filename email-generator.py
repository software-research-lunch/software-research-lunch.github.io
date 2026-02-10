#!/usr/bin/env python3
"""
Email generator for Software Research Lunch announcements.
Reads from _data/schedule.yml and generates email announcements.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
import yaml


def parse_date(date_str):
    """Parse date from MM/DD/YYYY format to datetime object."""
    try:
        return datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        print(f"Error: Invalid date format '{date_str}'. Expected MM/DD/YYYY", file=sys.stderr)
        sys.exit(1)


def format_date_for_email(dt):
    """Format datetime object as 'Month Day, Year' for email."""
    return dt.strftime("%B %d, %Y")


def find_talk(schedule_data, target_date):
    """Find a talk matching the target date in the schedule data."""
    # Try both with and without leading zeros
    target_date_str_with_zeros = target_date.strftime("%Y-%m-%d")
    target_date_str_no_zeros = f"{target_date.year}-{target_date.month}-{target_date.day}"

    # Search through all quarters/years in the schedule
    for quarter_key, quarter_data in schedule_data.items():
        if not isinstance(quarter_data, dict) or 'talks' not in quarter_data:
            continue

        for talk in quarter_data['talks']:
            talk_date = talk.get('date')
            if talk_date in (target_date_str_with_zeros, target_date_str_no_zeros):
                return talk

    return None


def generate_email(talk, date_str):
    """Generate the email content from talk data."""
    name = talk.get('speaker', 'TBD')
    title = talk.get('title', 'TBD')
    abstract = talk.get('abstract', 'TBD')
    bio = talk.get('bio', 'TBD')

    email = f"""
[software-research-lunch] Thursday {date_str}, {name} on \"{title}\"

Hi everyone,

This Thursday at noon, {name} will be presenting the talk \"{title}\" (abstract below).

We will be meeting in person at CODA E401 at 12:10 pm. The zoom room will remain available:
https://stanford.zoom.us/j/6404351384?pwd=QkZ3SlpDZyszVVZDQkU4ZWR5TjMwdz09
Meeting ID: 640 435 1384
Passcode: 841042

For a schedule of upcoming talks, please see our website: software-research-lunch.stanford.edu

See you there,

Rohan

==========================================
Abstract:

{abstract}

Bio:

{bio}
"""
    return email


def main():
    parser = argparse.ArgumentParser(
        description='Generate email announcements for Software Research Lunch talks'
    )
    parser.add_argument(
        'date',
        type=str,
        help='Date of the talk in MM/DD/YYYY format'
    )
    parser.add_argument(
        '--repo-path',
        type=str,
        default='.',
        help='Path to the software-research-lunch.github.io repository (default: current directory)'
    )

    args = parser.parse_args()

    # Parse the date
    talk_date = parse_date(args.date)
    date_formatted = format_date_for_email(talk_date)

    # Construct path to schedule.yml
    repo_path = Path(args.repo_path)
    schedule_path = repo_path / '_data' / 'schedule.yml'

    if not schedule_path.exists():
        print(f"Error: Schedule file not found at {schedule_path}", file=sys.stderr)
        sys.exit(1)

    # Load the schedule data
    try:
        with open(schedule_path, 'r') as f:
            schedule_data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading schedule file: {e}", file=sys.stderr)
        sys.exit(1)

    # Find the talk for the given date
    talk = find_talk(schedule_data, talk_date)

    if talk is None:
        print(f"Error: No talk found for date {args.date}", file=sys.stderr)
        sys.exit(1)

    # Generate and print the email
    email = generate_email(talk, date_formatted)
    print(email)


if __name__ == '__main__':
    main()
