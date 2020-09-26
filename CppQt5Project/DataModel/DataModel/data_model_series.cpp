#include "data_model_series.h"


template <typename T>
Series<T>::Series()
{
    array = new std::vector<T>(0);
}


template <typename T>
Series<T>::Series (int n)
{
    array = new std::vector<T>(n); //n<0??
}

template <typename T>
Series<T>::Series (const Series & _Series)
{
    if(array != nullptr)
        delete array;
    array = new std::vector<T>(_Series.size());
    array->clear();
    array->insert(array->begin(),_Series.begin(),_Series.end());
}

template <typename T>
Series<T>::Series (const Series * _Series)
{
    if(array != nullptr)
        delete array;
    array = new std::vector<T>(_Series->size());
    array->clear();
    array->insert(array->begin(),_Series->begin(),_Series->end());
}

//用另一个Series来赋值, 需同一类型
template <typename T>
Series<T> &  Series<T>::operator = (const Series<T> & _Series)
{
    array->clear();
    array->insert(array->begin(),_Series.begin(),_Series.end());
    return *this;
}

template <typename T>
Series<T> &  Series<T>::operator = (const std::vector<T> & _array)
{
    array->clear();
    array->insert(array->begin(),_array.begin(),_array.end());
    return *this;
}

//按照索引取值
template <typename T>
const T & Series<T>::operator [](unsigned long long int index) const
{
    if( index < array->size())
        return (*array)[index];
    else{
        //TODO:报错
    }
}

template <typename T>
T & Series<T>::operator [](unsigned long long int index)
{
    if(index < array->size())
        return (*array)[index];
    else{
        //TODO:报错
    }
}
