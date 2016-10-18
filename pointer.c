#include<stdio.h>

int main(){
    int a = 100;
    int *addA;
    addA = &a;
    printf("addA:%p\n",addA); 
    printf("addA star:%d\n",*addA); 
    printf("addA and:%p\n",&addA); 
}
