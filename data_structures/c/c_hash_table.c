#include <stdio.h>
#include <stdlib.h>

// Size of the hash table
#define SIZE 20

// Stores data of each node
typedef struct Node{
    int key;
    int data;
    struct Node *next;
}Node;

// Hash Table that stores all the nodes
typedef struct HashTable{
    struct Node *ht[SIZE];
}HashTable;

void initHashTable(HashTable *table){
    for(int i = 0; i < SIZE; i++){
        table->ht[i] = NULL;
    }
}

void addNode(int data, HashTable *table){
    // Hash function
    int key = data % SIZE;
    // Initializing memory for node
    Node *node = malloc(sizeof(Node));

    node->key = key;
    node->data = data;
    node->next = NULL;
    
    if(table->ht[key] == NULL){// No entries yet
        table->ht[key] = node;
    } else{ // Location is populated (collision)
        Node *head = table->ht[key];
        // Loop thru the list until the end is reached
        while (head->next != NULL){
            // Move pointer to the next node
            head = head->next;
        }
        // Add the new data to the table
        head->next = node;
    }
}

void removeNode(int data, HashTable *table){
    // Hash function
    int key = data % SIZE;
    Node *head = table->ht[key];

    // Delete first element
    if(head != NULL && head->data == data){
        Node *node = head;
        table->ht[key] = head->next;
        // Free node from memory
        free(node);
    } 
    else if (head != NULL && head->data != data){
        // loop to element needing deletion
        while (head->next != NULL) {
            // Remove this element from the table
            if (head->next->data == data){
                Node *node = head->next;
                head->next = head->next->next;
                // Free node from memeory
                free(node);
                break;
            }
            // Move pointer to the next node
            head = head->next;
        }
    }
}

// Get first instantance of the key
int get(int key, HashTable *table){
    int data = table->ht[key]->data;
    return data;
}

// Get all instantances of the key
int* getAll(int key, HashTable *table){
    int size = 0;
    Node *head = table->ht[key];

    // Count the number of nodes in the list
    while (head != NULL){
        size++;
        head = head->next;
    }

    // Intialize data to be returned
    int* data = malloc(size * sizeof(int));
    // Reset head
    head = table->ht[key];
    for(int i = 0; i < size; i++){
        data[i] = head->data;
        head = head->next;
    }

    return data;
}

int main(){
    HashTable *table = malloc(sizeof(HashTable));
    initHashTable(table);

    // Adding nodes to the hash table
    printf("Element(s) added:");
    for(int i = 0; i < SIZE; i++) {
        addNode(i, table);
        printf(" %d", i);
    }
    printf("\n");

    // Adding nodes that collide to the hash table
    printf("Element(s) collided:");
    for (int i = 20; i < SIZE+20; i++){
        addNode(i, table);
        printf(" %d", i);
    }
    printf("\n");

    int k = get(3, table);
    printf("Getting %d from key 3\n", k);

    int *j = getAll(3, table);
    printf("All elements retreived from key 3:");
    int length = sizeof(j) / sizeof(j[0]);
    for(int i = 0; i < length; i++){
        printf(" %d", j[i]);
    }

    return 0;
}