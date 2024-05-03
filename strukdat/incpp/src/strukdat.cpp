#include <iostream>
#include "strukdat.hpp"

namespace strukdat
{
  
  template <typename T> linkedList<T>::linkedList(node<T>& head) : head(&head), tail(nullptr), size(-1)  {}
  template <typename T> linkedList<T>::linkedList(T headContent, int size) : size(size)
  {
    head = new node<T>();
    
    node<T>* trfrs = head;
    node<T>* trfrs1 = head;

    for(int i = 1; i < size; i++)
    {
      trfrs->next = new node<T>();
      trfrs = trfrs->next;
      trfrs->prev = trfrs1;
      trfrs1 = trfrs;
    }

    tail = trfrs;
  }

  template <typename T> int linkedList<T>::getSize()
  {
    if(size != -1) {return size;} 
    size = 1;
    node<T>* trfrs = head;
    while(trfrs->next != nullptr)
    {
      size++;
      trfrs = trfrs->next;
    }

    tail = trfrs;
    return size;
  }

  template <typename T> node<T>* linkedList<T>::getHead() {return &(this->head);}
  
  template <typename T> node<T>* linkedList<T>::getTail()
  {
    if(tail != nullptr) {return tail;}
    try
    {
      if(head == NULL) {throw -1;}
    }
    catch(const std::exception& e)
    {
      std::cout<<"\nHEAD IS NULL\n";
      std::cerr << e.what() << '\n';
    }

    node<T>*trfrs = head;
    
    if(size = -1)
    {
      size = 0;
      while(trfrs->next != nullptr) {trfrs = trfrs->next; size++;}
    }
    else
    {
      while(trfrs->next != nullptr) {trfrs = trfrs->next;}
    }
    
    return trfrs;
  }
  
  template <typename T> node<T>* linkedList<T>::getNode(int index)
  {
    node<T> trfrs = head;
    for(int i = 1; i < index; i++) 
    {
      try
      {
        if(trfrs->next == nullptr) {throw -1;}
      }
      catch(const std::exception& e)
      {
        std::cout<<"\nINDEX OUT OF BOUNDS\n";
        std::cerr << e.what() << '\n';
      }
      
      trfrs = trfrs->next;
    }
    return trfrs;
  }
}
