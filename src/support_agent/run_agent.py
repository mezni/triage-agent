from support_agent.agent import SupportAgent


def main():
    agent = SupportAgent()

    result = agent.run(
        """
        Customer C001 says:
        I cannot log into my account.
        Can you check whether my account is active?
        """
    )

    print("\nFinal response:")

    for block in result.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()