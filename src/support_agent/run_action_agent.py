from support_agent.agent import SupportAgent


def main():
    agent = SupportAgent()

    result = agent.run(
        """
        Customer C002 says:

        I was charged twice for my subscription this month.
        Please create a high priority billing ticket for this
        issue.
        """
    )

    print("\nFinal response:")

    for block in result.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()