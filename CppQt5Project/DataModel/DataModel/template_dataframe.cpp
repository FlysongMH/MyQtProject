#pragma once
#include "template_dataframe.h"

template <typename T>
DataFrame<T>::DataFrame(const std::string & filename, const char & delimiter)
    :width(0),length(0)
{
    read_csv(filename,delimiter);
}

template <typename T>
DataFrame<T>::DataFrame(long long int _width,long long int _length)
    :width(_width),length(_length)
{
    Column temp;
    for(int i = 0; i < width; i++)
        temp.emplace_back(std::to_string(i));
    column_paste(temp);
}

template <typename T>
DataFrame<T>::DataFrame(const Column& columns)
    :width(columns.size()),length(0)
{
    column_paste(columns);
}

template <typename T>
DataFrame<T>::DataFrame(const DataFrame<T> & dataframe)
{
    width = dataframe.width;
    length = dataframe.length;

    column.clear();
    index.clear();
    matrix.clear();

    column.insert(column.begin(),dataframe.column.begin(),dataframe.column.end());
    index.insert(dataframe.index.begin(),dataframe.index.end());
    for (auto i = dataframe.matrix.begin(); i < dataframe.matrix.end(); ++i) {
        matrix.emplace_back(new Array<T>(*i));
    }
}

template <typename T>
DataFrame<T>::~DataFrame()
{
    for(auto i = 0; i < matrix.size(); ++ i)
    {
        delete matrix[i];
    }
}



//init the column
template <typename T>
bool DataFrame<T>::column_paste(const Column & _column)
{
    if(!_column.empty()) {
        width = _column.size();
        column.clear();
        index.clear();
        matrix.clear();
        for(const auto & item : _column){
            column.emplace_back(item);
            index.emplace(item,index.size());
            matrix.emplace_back(new Array<T>(0));
        }
        return true;
    } else return false;
}

template <typename T>
bool DataFrame<T>::contain(const std::string & col)
{
    return index.find(col)!=index.end();
}

// insert one column
template <typename T>
bool DataFrame<T>::insert(const std::string & col)
{
    ++ width;
    column.emplace_back(col);
    index.emplace(col,index.size());
    matrix.emplace_back(new Array<T>(length));
    return true;
}

// insert one column from std::vector<T>
template <typename T>
bool DataFrame<T>::insert(const std::string & col,const Array<T> & array)
{
    if(array.size() == row_num()){
        if(!contain(col)){
            ++ width;
            column.emplace_back(col);
            index.emplace(col,index.size());
            matrix.emplace_back(new Array<T>(array));
        }else{
            Array<T> & row = this->operator[](col);
            row.insert(row.begin(),array.begin(),array.end());
        }
        return true;
    }else return false;
}
//remove one column from str
template <typename T>
bool DataFrame<T>::remove(const std::string & col)
{
    auto item = index.find(col);
    if(item != index.end()){
        -- width;
        column.erase(column.begin()+item->second);
        delete *(matrix.begin()+item->second);
        matrix.erase(matrix.begin()+item->second);
        for(auto & index_item : index){
            if(index_item.second > item->second){
                index_item.second--;
            }
        }
        index.erase(item);
        return true;
    }
    return false;
}

//operator[]是作为DataFrame的成员，因此要加DataFrame<T>
//get one column data from column str
template <typename T>
Array<T> & DataFrame<T>::operator [](const std::string & col){
    auto item = index.find(col);
    if(item != index.end()){
        return *(matrix[item->second]);
    }
    insert(col);
    return *(matrix.back());
}

//get one column data from index of column
template <typename T>
Array<T> & DataFrame<T>::operator [](const int & idx)
{
    if(idx < matrix.size())
        return *(matrix[idx]);
    std::stringstream ssTemp;
    ssTemp << idx;
    throw (std::out_of_range("the index \'" + ssTemp.str() + "\' is out of range!"));
}

//get one column data from column str
template <typename T>
const Array<T> & DataFrame<T>::operator [](const std::string & col) const
{
    auto item = index.find(col);
    if(item != index.end()){
        return *(matrix[item->second]);
    }
    insert(col);
    return *(matrix.back());
}

//get one column data from index of column
template <typename T>
const Array<T> & DataFrame<T>::operator [](const int & idx) const
{
    if(idx < matrix.size())
        return *(matrix[idx]);
    std::stringstream ssTemp;
    ssTemp << idx;
    throw (std::out_of_range("the index \'" + ssTemp.str() + "\' is out of range!"));
}


//append one row from std::vector<T>
template <typename T>
bool DataFrame<T>::append(const std::vector<T> & array)
{
    if(array.size() == width){
        length ++;
        for (int i = 0; i < array.size(); ++i) {
            matrix[i]->emplace_back(array[i]);
        }
        return true;
    }else return false;
}

template <typename T>
const long long int & DataFrame<T>::column_num() const 
{
    return width;
}

template <typename T>
const long long int & DataFrame<T>::row_num() const {
    return length;
}

//concat double DataFrame object vertically
template <typename T>
bool DataFrame<T>::concat_line(const DataFrame<T> & dataframe)
{
    if(dataframe.width==width){
        length += dataframe.length;
        for (int i = 0; i < width; ++i) {
            matrix[i]->insert(matrix[i]->end(),dataframe[i].begin(),dataframe[i].end());
        }
        return true;
    }else return false;
}

//concat double DataFrame object horizontally
template <typename T>
bool DataFrame<T>::concat_row(const DataFrame<T> & dataframe)
{
    if(dataframe.length==length){
        std::string repeat;
        auto last_width = dataframe.width;
        for (int i = 0; i < last_width; ++i) {
            repeat = contain(dataframe.column[i]) ? "_r" : "";
            index.insert({dataframe.column[i] + repeat,index.size()});
            column.emplace_back(dataframe.column[i] + repeat);
            matrix.emplace_back(new Array<T>(dataframe.matrix[i]));
        }
        width += dataframe.column_num();
        return true;
    }else return false;
}

// is empty or not
template <typename T>
bool DataFrame<T>::empty() const {
    return width == 0;
}

//read from csv file
template <typename T>
void DataFrame<T>::read_csv(const std::string & filename, const char & delimiter)
{
    std::ifstream Reader(filename.data());
    if(!Reader){
        throw (std::invalid_argument("filename is invalid!"));
    }

    std::string strLine;
    StringVector vecValue;
    if(getline(Reader, strLine)){
        vecValue.clear();
        if(splite_line(strLine, vecValue ,delimiter)) {
            column_paste(vecValue);
        }
    }

    while (getline(Reader, strLine)){
        vecValue.clear();
        if(splite_line(strLine, vecValue ,delimiter)) {
            append_from_str(vecValue);
        }
    }
    Reader.close();
}

//write into csv file
template <typename T>
void DataFrame<T>::to_csv(const std::string & filename, const char & delimiter) const 
{
    std::ofstream cout = std::ofstream(filename.data(), std::ios::out | std::ios::trunc);
    for (auto item = column.begin(); item < column.end() - 1; ++item) {
        cout << *item << delimiter;
    }
    cout << column.back() << '\n';
    for (int i = 0; i < row_num(); ++i) {
        for (auto array = matrix.begin(); array < matrix.end() - 1; ++array) {
            cout << (**array)[i] << delimiter;
        }
        cout << (*matrix.back())[i] << '\n';
    }
    cout.close();
}



template <typename T>
void DataFrame<T>::show_columns()
{
    for(const auto & item : index){
        std::cout << item.first << ',' << item.second << std::endl;
    }
}

//concat double DataFrame object vertically
//operator+作为友元不加DataFrame<T>
template <typename T>
DataFrame<T> operator + (const DataFrame<T> & dataframe1,const DataFrame<T> & dataframe2)
{
    if(!dataframe1.empty() && !dataframe2.empty() &&
        dataframe1.column_num() == dataframe2.column_num())
    {
        DataFrame<T> dataFrame(dataframe1.column);
        dataFrame.concat_line(dataframe1);
        dataFrame.concat_line(dataframe2);
        return std::move(dataFrame);
    }
    return std::move(DataFrame<T>(0));
}

//print dataframe //operator<<作为友元不加DataFrame<T>
template <typename T>
std::ostream & operator<<(std::ostream & cout, const DataFrame<T> &dataFrame) 
{
    cout << "width : " << dataFrame.width << std::endl;
    cout << "length : " << dataFrame.length << std::endl;
    for (int j = 0; j < dataFrame.width; ++j) {
        cout << dataFrame.column[j] << "\t";
    }
    cout << '\n';
    for (int i = 0; i < dataFrame.length; ++i) {
        for (int j = 0; j < dataFrame.width; ++j) {
            cout << (*dataFrame.matrix[j])[i] << "\t";
        }
        cout << '\n';
    }
    return cout;
}

template <typename T>
bool DataFrame<T>::splite_line(const std::string & strLine, StringVector & stringVector, const char & delimiter) 
{
    unsigned long long nBegin = 0;
    unsigned long long nEnd = 0;
    bool flag = false;
    std::string strtemp;
    while ((nEnd = strLine.find_first_of(delimiter, nBegin)) != std::string::npos)
    {
        strtemp = strLine.substr(nBegin, nEnd - nBegin);
        stringVector.emplace_back(strtemp);
        nBegin = nEnd + 1;
    }
    if ((nBegin = strLine.find_last_of(delimiter, strLine.length() - 1)) != std::string::npos)
    {
        strtemp = strLine.substr(nBegin + 1, strLine.length() - nBegin -1);
        stringVector.emplace_back(strtemp);
        flag = true;
    }
    return flag;
}

template <typename T>
bool DataFrame<T>::append_from_str(const StringVector & array)
{
    if(array.size() == column.size()){
        length ++;
        std::stringstream stream;
        T item;
        for (unsigned int i = 0; i < array.size(); ++i) {
            stream.clear();
            stream << array[i];
            stream >> item;
            matrix[i]->emplace_back(item);
        }
        return true;
    }else return false;
}
