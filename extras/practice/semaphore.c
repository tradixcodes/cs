#include <stdio.h>
#include <time.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

//Declare a semaaphore
sem_t semaphore;

// Function executed by each thread
void *thread_function(void* arg){
    int thread_id = *(int*)arg;

    // Wait (lock) the semaphore to enter the critical section
    sem_wait(&semaphore);

    //Critical section begins
    printf("Thread %d is entering the critical section.\n", thread_id);
    sleep(3); //Simulate work
    printf("Thread %d is leaving the critical section.\n", thread_id);
    // Critical section ends

    // Signal (unlock) the semaphore to exit the critical section
    sem_post(&semaphore);

    pthread_exit(NULL);

    return NULL;

}

int main()
{
    pthread_t thread1, thread2;
    int id1 = 1, id2 = 2;

    // Initialize the semaphore with an initial value of 1
    sem_init(&semaphore, 0, 1);

    // Create two threads
    pthread_create(&thread1, NULL, thread_function, &id1);
    pthread_create(&thread2, NULL, thread_function, &id2);

    // Wait for the threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    // Destroy the semaphore
    sem_destroy(&semaphore);

    printf("Both threads have finished execution.\n");
    return 0;
}
