#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>

typedef struct linkedList linkedList;

linkedList *createList();
void destroyList(linkedList *);
void addNode(linkedList *, int);
void printList(linkedList *);

#endif