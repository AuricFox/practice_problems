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

void push(struct Node** head, int data){
    struct Node* node = createNode(data);
    struct Node* currentNode = *head;

    // Queue is empty, set the new node as head
    if(*head == NULL) {
        *head = node;
    } else {
        // Loop thru the Queue until the end is found
        while (currentNode->next != NULL){
            // Move pointer to the next node
            currentNode = currentNode->next;
        }
        // Add the new node at the end of the Queue
        currentNode->next = node;
    } 
}

int pop(struct Node **head){
    struct Node *currentNode = *head;

    if (currentNode != NULL){
        // Queue is not empty
        int data = currentNode->data;
        // Move pointer to the next node
        *head = currentNode->next;
        // Free the memory of removed node
        free(currentNode);
        return data;
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
    for (int i = 0; i < 10; i++) push(&head, i);
    printList(head);

    //Removing data
    pop(&head);
    pop(&head);
    printList(head);

    return 0;
}