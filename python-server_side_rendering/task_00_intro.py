#!/usr/bin/python3
"""
Simple templating program.
"""


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and attendees list.
    """

    # Check template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Empty attendees
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            content = content.replace(
                "{" + placeholder + "}",
                str(value)
            )

        filename = f"output_{index}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
