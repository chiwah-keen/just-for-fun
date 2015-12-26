#include<stdio.h>

struct node{
    struct node *left;
    struct node *right;
    int value;
};
int main(){
    struct node node1,node2,node3;
    node1.value = 1;    
    node2.value = 2;    
    node3.value = 3;    

    struct node *p; 
    p = &node1;
    node1.left = &node2;
    node1.right = &node3;
    node2.left = NULL;
    node2.right = NULL;
    node3.left = NULL;
    node3.right = NULL;
    
    //left visit.
    while(p->right != NULL){
        printf("The value:%d",p->value); 
        p = p->left;
        printf("The value:%d",p->value); 
    }
}
