from datetime import datetime

from langchain_core.tools import tool

from database import SessionLocal
import models


@tool
def log_interaction(
    hcp_id: str,
    interaction_type: str,
    interaction_date: str,
    topics_discussed: str,
    sentiment: str,
    summary: str,
    follow_up_date: str = ""
) -> str:
    """Log a new interaction with a healthcare professional."""

    db = SessionLocal()

    try:
        hcp_id_int = int(hcp_id)
        hcp = db.query(models.HCP).filter(
            models.HCP.id == hcp_id
        ).first()
        if not hcp:
            return f"HCP with ID {hcp_id} not found."
        new_interaction = models.Interaction(
            hcp_id=hcp_id,
            interaction_type=interaction_type,
            interaction_date=datetime.strptime(
                interaction_date,
                "%Y-%m-%d"
            ).date(),
            topics_discussed=topics_discussed,
            sentiment=sentiment,
            summary=summary,
            follow_up_date=(
                datetime.strptime(
                    follow_up_date,
                    "%Y-%m-%d"
                ).date()
                if follow_up_date
                else None
            )
        )
        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)
        return (
            f"Interaction logged successfully. "
            f"Interaction ID: {new_interaction.id}"
        )
    except Exception as error:
        db.rollback()
        return f"Error logging interaction: {str(error)}"
    finally:
        db.close()
@tool
def edit_interaction(
    interaction_id: int,
    sentiment: str = "",
    summary: str = "",
    topics_discussed: str = ""
) -> str:
    """Edit an existing HCP interaction."""
    db = SessionLocal()
    try:
        interaction = db.query(models.Interaction).filter(
            models.Interaction.id == interaction_id
        ).first()
        if not interaction:
            return f"Interaction {interaction_id} not found."
        if sentiment:
            interaction.sentiment = sentiment
        if summary:
            interaction.summary = summary
        if topics_discussed:
            interaction.topics_discussed = topics_discussed
        db.commit()
        return f"Interaction {interaction_id} updated successfully."
    except Exception as error:
        db.rollback()
        return f"Error editing interaction: {str(error)}"
    finally:
        db.close()
@tool
def search_hcp(name: str) -> str:
    """Search for a healthcare professional by name."""
    db = SessionLocal()
    try:
        hcps = db.query(models.HCP).filter(
            models.HCP.name.like(f"%{name}%")
        ).all()
        if not hcps:
            return f"No HCP found with name {name}."
        results = []
        for hcp in hcps:
            results.append(
                f"ID: {hcp.id}, "
                f"Name: {hcp.name}, "
                f"Specialization: {hcp.specialization}, "
                f"Hospital: {hcp.hospital}, "
                f"Location: {hcp.location}"
            )
        return "\n".join(results)
    finally:
        db.close()
@tool
def get_interaction_history(hcp_id: str) -> str:
    """Get previous interactions for a healthcare professional using the HCP ID."""
    db = SessionLocal()
    try:
        # Convert LLM-provided string ID to integer
        hcp_id_int = int(hcp_id)
        interactions = db.query(models.Interaction).filter(
            models.Interaction.hcp_id == hcp_id_int
        ).all()
        if not interactions:
            return f"No interactions found for HCP ID {hcp_id_int}."
        results = []
        for interaction in interactions:
            results.append(
                f"Interaction ID: {interaction.id}, "
                f"Type: {interaction.interaction_type}, "
                f"Date: {interaction.interaction_date}, "
                f"Topics: {interaction.topics_discussed}, "
                f"Sentiment: {interaction.sentiment}, "
                f"Summary: {interaction.summary}, "
                f"Follow-up: {interaction.follow_up_date}"
            )
        return "\n".join(results)
    except ValueError:
        return "Invalid HCP ID. Please provide a numeric HCP ID."
    except Exception as error:
        return f"Error retrieving interaction history: {str(error)}"
    finally:
        db.close()
@tool
def schedule_followup(
    interaction_id: int,
    follow_up_date: str
) -> str:
    """Schedule a follow-up date for an existing interaction."""

    db = SessionLocal()

    try:
        interaction = db.query(models.Interaction).filter(
            models.Interaction.id == interaction_id
        ).first()

        if not interaction:
            return f"Interaction {interaction_id} not found."

        interaction.follow_up_date = datetime.strptime(
            follow_up_date,
            "%Y-%m-%d"
        ).date()

        db.commit()

        return (
            f"Follow-up for interaction {interaction_id} "
            f"scheduled successfully for {follow_up_date}."
        )

    except Exception as error:
        db.rollback()
        return f"Error scheduling follow-up: {str(error)}"

    finally:
        db.close()


tools = [
    log_interaction,
    edit_interaction,
    search_hcp,
    get_interaction_history,
    schedule_followup
]