#ifndef DATAFRAME_H
#define DATAFRAME_H

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <exception>
#include <sstream>
#include <unordered_map>
#include "template_array.cpp"


template <typename T = double>
class DataFrame
{
    typedef std::vector<Array<T> *> Matrix;  //存储类型T的数据结构
    typedef std::vector<std::string> Column;
    typedef std::vector<std::string> StringVector;

public:
    explicit DataFrame(const std::string & filename, const char & delimiter=',');
    explicit DataFrame(long long int _width,long long int _length = 0);
    explicit DataFrame(const Column& columns);
    DataFrame(const DataFrame & dataframe);
    ~DataFrame();

    //init the column
    bool column_paste(const Column & _column);
    bool contain(const std::string & col);
    // insert one column
    bool insert(const std::string & col);
    // insert one column from std::vector<T>
    bool insert(const std::string & col,const Array<T> & array);

    //remove one column from str
    bool remove(const std::string & col);

    //get one column data from column str
    Array<T> & operator [](const std::string & col);
    //get one column data from index of column
    Array<T> & operator [](const int & idx);
    //get one column data from column str
    const Array<T> & operator [](const std::string & col) const;
    //get one column data from index of column
    const Array<T> & operator [](const int & idx) const;
    
    //append one row from std::vector<T>
    bool append(const std::vector<T> & array);
    
    const long long int & column_num() const ;
    const long long int & row_num() const ;
    
    //concat double DataFrame object vertically
    bool concat_line(const DataFrame & dataframe);
    //concat double DataFrame object horizontally
    bool concat_row(const DataFrame & dataframe);
    
    // is empty or not
    bool empty() const;
    
    //read from csv file
    void read_csv(const std::string & filename, const char & delimiter = ',');
    //write into csv file
    void to_csv(const std::string & filename, const char & delimiter = ',') const;
    
    void show_columns();
    

    //concat double DataFrame object vertically
    friend DataFrame operator + (const DataFrame & dataframe1,const DataFrame & dataframe2);
    //print dataframe
    friend std::ostream & operator<<(std::ostream & cout, const DataFrame &dataFrame);

    
private:
    bool splite_line(const std::string & strLine, StringVector & stringVector, const char & delimiter);
    bool append_from_str(const StringVector & array);
    
    Column column;
    Matrix matrix;
    long long int width;
    long long int length;
    std::unordered_map<std::string,unsigned long long int> index;
};

#endif // DATAFRAME_H
