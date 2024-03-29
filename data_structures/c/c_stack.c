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

// Adding the data to the stack
void addNode(struct Node** head, int data){
    struct Node* node = createNode(data);

    // Add node to the front of the list
    node->next = *head;
    *head = node;
}

int pop(struct Node **head){
    struct Node *currentNode = *head;
    
    if (*head != NULL){
        // Stack is not empty
        int data = currentNode->data;
        // Move pointer to the next node
        *head = currentNode->next;
        // Free the memory of removed node
        free(currentNode);
        return data;
    }
}

// Printing the entire stack
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

    // Adding data 0-9 to the stack
    for (int i = 0; i < 10; i++) addNode(&head, i);
    printList(head);

    //Removing data
    pop(&head);
    pop(&head);
    printList(head);

    return 0;
}