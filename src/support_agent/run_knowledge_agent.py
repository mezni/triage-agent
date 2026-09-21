from support_agent.agent import SupportAgent


def main():
    agent = SupportAgent()

    result = agent.run(
        """
        Does your application support dark mode?
        """
    )

    print("\nFinal response:")

    for block in result.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()