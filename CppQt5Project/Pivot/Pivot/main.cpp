#include "pivot.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Pivot w;
    w.show();
    
    return a.exec();
}
