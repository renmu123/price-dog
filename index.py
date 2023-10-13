from src import MasadoraSuruga


def main():
    suruga = MasadoraSuruga()
    data = suruga.parse("602247898")
    print(data)


if __name__ == "__main__":
    main()
