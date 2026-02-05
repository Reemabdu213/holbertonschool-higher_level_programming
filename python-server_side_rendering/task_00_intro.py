#!/usr/bin/env python3
"""Simple templating program for generating personalized invitations."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and attendees list.

    Args:
        template: A string containing the invitation template with placeholders.
        attendees: A list of dictionaries containing attendee information.
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        output = template
        # Replace each placeholder with the attendee's data or "N/A"
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        # Write to output file
        filename = "output_{}.txt".format(i)
        with open(filename, "w") as f:
            f.write(output)
