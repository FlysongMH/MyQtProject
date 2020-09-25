#include <iostream>
#include <vector>
#include <string>
#include "template_array.cpp"
#include "template_dataframe.cpp"

void test_array(); //不声明就定义会报警告
void test_array()
{
    std::vector<double> vec_double = {1,2,3,4,5};
    int num = 5;
    Array<> array_double(num);
    array_double = vec_double;
    
    return;
}

void test_dataframe();
void test_dataframe()
{
    //read from csv file
    DataFrame<double> d1("../../TestData0.csv");
    DataFrame<double> d2("../../TestData1.csv");
    //concat double DataFrame object vertically
//    auto d3 = d1 + d2;
    // insert one column from std::vector<T>
//    d3["h"] = d3["f"]  = d3["g"] = std::vector<double>{6,7,8,9};
    //remove one column by str
//    d3.remove("g");
    //append one row from std::vector<T>
//    d3.append(std::vector<double>(d3.column_num()));
    //concat double DataFrame object horizontally
//    d3.concat_row(d3);
    // change data
//    d3["f"][3] = 2;
    //print dataframe
//    std::cout << d3;
    //write into csv file
//    d3.to_csv("../final.csv",',');
    return;
}
int main()
{

//    test_array();
    test_dataframe();
}
