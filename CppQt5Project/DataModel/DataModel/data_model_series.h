#ifndef SERIES_H
#define SERIES_H
/*
 * Series类说明
 * *仿Python中Series数据类型
 * *一个对象可处理任意单一类型的一系列数据
*/

#include <vector>
#include <string>

template <typename T = int>
class Series
{
    typedef typename std::vector<T>::const_iterator iter;//typedef创建了存在类型的别名，而typename告诉编译器std::vector<T>::size_type是一个类型而不是一个成员。
    std::vector<T> * array = nullptr; //成员储存同一个类型的数据

public:
    Series();
    Series(int n=0);
    explicit Series (const Series * _Series);
    explicit Series (const Series & _Series);
    ~Series() {delete array;}

    void insert(iter position,iter start,iter end) {array->insert(position,start,end);}

    unsigned long long int size() const { return (array == nullptr)? 0 : array->size();}
    typename std::vector<T>::const_iterator begin() const {return array->begin();}
    typename std::vector<T>::const_iterator end() const {return array->end();}

    void emplace_back(const T & item) {array->emplace_back(item);}

    /* 重载运算符 */
    Series & operator = (const Series & _array);
    Series & operator = (const std::vector<T> & _array);
    const T & operator [](unsigned long long int index) const ;
    T & operator [](unsigned long long int index) ;

};

#endif // SERIES_H
