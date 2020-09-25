#pragma once
#include "template_array.h"

template <typename T>
Array<T>::Array (int n)
{
    this->array = new std::vector<T>(n);
}

template <typename T>
Array<T>::Array (const Array & _array)
{
    array = new std::vector<T>(_array.size());
    if(_array.size()==array->size())
    {
        array->clear();
        array->insert(array->begin(),_array.begin(),_array.end());
    }
}

template <typename T>
Array<T>::Array (const Array * _array)
{
    if(array != nullptr)
        delete array;
    array = new std::vector<T>(_array->size());
    if(_array->size()==array->size())
    {
        array->clear();
        array->insert(array->begin(),_array->begin(),_array->end());
    }
}

template <typename T> 
Array<T> &  Array<T>::operator = (const Array<T> & _array)
{
    if(_array.size()==array->size()){
        array->clear();
        array->insert(array->begin(),_array.begin(),_array.end());
    }
    return *this;
}

template <typename T> 
Array<T> &  Array<T>::operator = (const std::vector<T> & _array)
{
    if(_array.size()==array->size()){
        array->clear();
        array->insert(array->begin(),_array.begin(),_array.end());
    }
    return *this;
}

template <typename T> 
const T & Array<T>::operator [](unsigned long long int index) const 
{
    if( index < array->size())
        return (*array)[index];
    else{
        std::stringstream ssTemp;
        ssTemp << index;
        throw (std::out_of_range("the index \'" + ssTemp.str() + "\' is out of range!"));
    }
}

template <typename T> 
T & Array<T>::operator [](unsigned long long int index) 
{
    if(index < array->size())
        return (*array)[index];
    else{
        std::stringstream ssTemp;
        ssTemp << index;
        throw (std::out_of_range("the index \'" + ssTemp.str() + "\' is out of range!"));
    }
}
