#include <stdio.h>
#include <stdlib.h>

// Defining a data type to store a elements info
struct Node {
    int data;
    struct Node* next;
};

// Creating a new node and returning it's pointer
struct Node* createNode(int data){
    // Allocating memory for the data
    struct Node* node = (struct Node*) malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

void addNode(struct Node** head, int data){
    struct Node* node = createNode(data);
    struct Node* currentNode = *head;

    // List is empty, set the new node as head
    if(*head == NULL) {
        *head = node;
    } else {
        // Loop thru the list until the end is found
        while (currentNode->next != NULL){
            // Move pointer to the next node
            currentNode = currentNode->next;
        }
        // Add the new node at the end of the list
        currentNode->next = node;
    } 
}

void insert(struct Node** head, int data, int idx){
    struct Node* node = createNode(data);
    struct Node* currentNode = *head;

    // List is empty
    if(*head == NULL){
        *head = node;
    }
    // Add to the front of the list
    else if (idx == 0 && *head != NULL){
        node->next = currentNode;
        *head = node;
    }
    else {
        // Loop until the end is reached and add to i
        for (int i = 1; currentNode != NULL; i++){
            // Insert the new node here and exit loop
            if (i == idx){
                node->next = currentNode->next;
                currentNode->next = node;
                break;
            }
            // Move pointer to the next node
            currentNode = currentNode->next;
        }
    }
}

void delete(struct Node **head, int data){
    struct Node *currentNode = *head;
    struct Node *previousNode = NULL;

    // Loop until first occurrence of data is found or end is reached
    while (currentNode != NULL && currentNode->data != data){
        // Move pointers
        previousNode = currentNode;
        currentNode = currentNode->next;
    }

    if (currentNode != NULL){
        // First node needs to be deleted
        if (previousNode == NULL){
            *head = currentNode->next;
        }
        // Deleting a node that is not the first elemtn
        else {
            previousNode->next = currentNode->next;
        }
        // Freeing the data from memory
        free(currentNode);
    }
}

// Printing the entire list
void printList(struct Node* head){
    struct Node* node = head;

    if(head == NULL){
        printf("List is Empty!\n");
    }

    while (node != NULL){
        printf("%d ", node->data);
        if (node->next != NULL) printf("-> ");
        node = node->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;

    // Adding data 0-9 to the list
    for (int i = 0; i < 10; i++) addNode(&head, i);
    printList(head);

    // Inserting data
    insert(&head, 20, 2);
    insert(&head, 11, 0);
    printList(head);

    //Removing data
    delete(&head, 20);
    delete(&head, 11);
    printList(head);

    return 0;
}