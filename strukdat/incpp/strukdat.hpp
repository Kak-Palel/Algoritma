#ifndef STRUKDAT
#define STRUKDAT

namespace strukdat
{
  template <typename T> struct node
  {
    T content;
    node<T>* next;
    node<T>* prev;
  };
  
  template <typename T> class linkedList
  {
    private:
      node<T>* head;
      node<T>* tail;
      int size;
    public:
      linkedList(node<T>& head);
      linkedList(T headContent, int size);

      int getSize();

      node<T>* getHead();
      
      node<T>* getTail();

      node<T>* getNode(int index);
  };
} //namespace strukdat

#endif //strukdat