from support_agent.extraction import (
    extract_ticket_information,
)


def main():

    message = """
    My customer ID is C002.

    I was charged twice for my subscription this month
    and I'm really frustrated about it.
    """

    result = extract_ticket_information(message)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()