"""
Demand Intelligence - Reddit Adapter

Status:
    Prototype awaiting Reddit Data API approval.

Purpose:
    Read-only retrieval of permitted public Reddit discussions for
    aggregated market-research analysis.

This adapter does not post, comment, message users, profile Redditors,
or perform advertising targeting.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def reddit_configuration():
    """Return configuration after Reddit API approval."""

    return {
        "client_id": os.getenv("REDDIT_CLIENT_ID"),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "user_agent": os.getenv(
            "REDDIT_USER_AGENT",
            "DemandIntelligenceResearch/0.1"
        ),
    }


def main():
    print(
        "Demand Intelligence Reddit Adapter\n"
        "Status: awaiting Reddit Data API approval."
    )


if __name__ == "__main__":
    main()
