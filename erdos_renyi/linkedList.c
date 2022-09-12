#include <stdlib.h>
#include "linkedList.h"

typedef struct node {
    int value;
    struct node *next;
} node;

struct linkedList {
    node *head;
    node *tail;
    int size;
};

linkedList *createList() {
    linkedList *list = malloc(sizeof(linkedList));
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
    return list;
}

void destroyList(linkedList *list) {
    if (list == NULL) return;

    node *current = list->head;

    while (current != NULL) {
        list->head = current->next;
        free(current);
        current = list->head;
    }

    free(list);
}

void addNode(linkedList *list, int value) {
    if (list == NULL) return;

    node *newNode = malloc(sizeof(node));
    newNode->value = value;
    newNode->next = NULL;

    if (list->head == NULL)
        list->head = newNode;
    else
        list->tail->next = newNode;
    
    list->tail = newNode;

    list->size++;
}

void printList(linkedList *list) {
    if (list == NULL) return;

    node *current = list->head;

    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}