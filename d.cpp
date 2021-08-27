#include <iostream>
#include <set>
#include <fstream>
using namespace std;

// 读取坐标
set<int> getCordinate(string fileName) {
	std::ifstream in;
	in.open(fileName);
	int x, y;
    set<int> ans;
	while (in >> x)	{
		in >> y;
        x--, y--;
        ans.insert(x * 500 + y);
	}	
    cout << ans.size() << endl;
	return ans;
}
// 得到曲线外部的所有点
set<int> generateOutPoint(string file) {
    int table[250000];
    int neighbor[4];
    set<int> spline = getCordinate(file);
    set<int> ans;
    int left = 0, right = 1;
    table[0] = 0;
    while (left < right) {
        int current = table[left];
        left++;
        neighbor[0] = current - 1;
        neighbor[1] = current + 1;
        neighbor[2] = current - 500;
        neighbor[3] = current + 500;
        for (int i = 0; i < 4; i++) {
            if (neighbor[i] >= 0 && neighbor[i] < 250000 && spline.find(neighbor[i]) == spline.end() && ans.find(neighbor[i]) == ans.end()) {
                table[right] = neighbor[i];
                ans.insert(neighbor[i]);
                right++;
            }
        }
    }
    cout << right <<endl;
    return ans;
}
// 判断file1和file2中曲线的包含关系，返回1表示file1>file2
// 返回-1表示file2>file1，返回0表示无包含关系。
int check(string file1, string file2) {
    set<int> a = generateOutPoint(file1), b = generateOutPoint(file2);
    int num = 0;
    for (int i : a) {
        if (b.find(i) != b.end()) {
            num++;
        }
    }
    if (num == a.size()) {//a的外点都在b的外点中，所以b在a内部
        return 1;
    }
    if (num == b.size()) {
        return -1;
    }
    return 0;
}

int main() {
    cout << check("edges/1.txt", "edges/2.txt") << endl;
    return 0;
}
