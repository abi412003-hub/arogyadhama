import frappe


def after_insert(doc, method):
    """Called after a new patient is created."""
    # Auto-notify reception about new patient
    pass
