#ifndef ARRAY_H
#define ARRAY_H
/*
 * 构造Array模板类, 可以处理任意同种数据类型列表, 形式同vector.
 * 注意模板类的声明和定义分别在.h和.cpp文件时, 需要include ".cpp"文件, 而不是像一般的类那样include ".h"文件
*/
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <exception>
#include <sstream>
#include <unordered_map>


template <typename T = double> //默认类型为double
class Array
{
    typedef typename std::vector<T>::const_iterator iter;//typedef创建了存在类型的别名，而typename告诉编译器std::vector<T>::size_type是一个类型而不是一个成员。
    std::vector<T> * array = nullptr; //成员储存同一个类型的数据
    
public:
    Array(int n=0);
    explicit Array (const Array * _array);
    explicit Array (const Array & _array);
    ~Array() {delete array;}

    void insert(iter position,iter start,iter end) {array->insert(position,start,end);}

    unsigned long long int size() const { return (array == nullptr)? 0 : array->size();}
    typename std::vector<T>::const_iterator begin() const {return array->begin();}
    typename std::vector<T>::const_iterator end() const {return array->end();}

    void emplace_back(const T & item) {array->emplace_back(item);}

    /* 重载运算符 */
    Array & operator = (const Array & _array);
    Array & operator = (const std::vector<T> & _array);
    const T & operator [](unsigned long long int index) const ;
    T & operator [](unsigned long long int index) ;
    
    //不要在模板类外重载输入输出流
    friend std::ostream &operator<<(std::ostream &cout, Array & arr) {
        for(const auto & item : *arr.array){
            cout << item << ' ';
        }
        return cout;
    }
    

};

#endif // ARRAY_H
