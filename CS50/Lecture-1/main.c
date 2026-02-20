#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("\n Welcome To Guess Number Game! \n");
    printf("---------------------------\n");
    printf("Guess a number between 1 and 100: \n");

    int number, guess, attempts = 0;
    number = rand() % 100 + 1; // Random number between 1 and 100
    
    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;

        if(guess < number)
        {
            printf("Too low! Try again.\n");
        }
        else if (guess > number)
        {
            printf("Too high! Try again.\n");
        }
        else {
            printf("Congratulations! You guessed the number in %d attempts!\n", attempts);
        }
    } while (guess != number);

    return 0;
}
