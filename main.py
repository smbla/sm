import sentry_sdk


def main():
    # TODO get sentry code from env var
    sentry_sdk.init()

    division_by_zero = 1 / 0
    print(division_by_zero)


if __name__ == "__main__":
    main()
