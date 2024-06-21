def generate_primes_up_to(limit):
    # This function generates prime numbers up to the given limit
    primes = []
    if limit >= 2:
        primes.append(2)
    for num in range(3, limit + 1, 2):
        is_prime = True
        for divisor in range(3, int(num**0.5) + 1, 2):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def main():
    try:
        upper_limit = int(input("Enter the upper limit to find prime numbers: "))
        if upper_limit < 2:
            raise ValueError("The limit must be 2 or greater.")
    except ValueError as error:
        print(f"Input error: {error}")
    else:
        primes = generate_primes_up_to(upper_limit)
        print(f"Prime numbers up to {upper_limit}: {primes}")

if __name__ == "__main__":
    main()
