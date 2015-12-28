#include<stdio.h>
typedef struct node{
    int age;
    int value;
}node,*Node;

int main(){
    node node1; 
    node1.age=100;
    node1.value=100;
    Node head;
    head = & node1;
    printf("age:%d",head->age);
}
