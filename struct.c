#include<stdio.h>

struct node{
    struct node *link;
    int value;
};


int main(){
    struct node node1,node2,node3;
    node1.value=1;
    node2.value=2;
    node3.value=3;
    
    struct node *p;
    p = &node1;
    node1.link = &node2;
    node2.link = &node3;
    node3.link = NULL;
    while(p != NULL){
        printf("The value is:%d\n",p->value);
        p = p->link;
    }

}
