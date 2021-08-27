#include<iostream>
#include<vector>
#include "eigen3/Eigen/Dense"
#include<cmath>
#include <fstream> 
#include <set>
using namespace std;
using namespace Eigen;

vector<vector<double>> getCordinate(string fileName) {
	std::ifstream in;
	in.open(fileName);
	int data;
	vector<double> x, y;
	while (in >> data)
	{
		x.push_back((double)data);
		in >> data;
		y.push_back((double)data);
	}
	vector<vector<double>> ans;
	ans.push_back(x);
	ans.push_back(y);
	return ans;
}
bool check(double x1, double x2, double xx) {
	if (x1 > x2)
		return x2 <= xx;
	return x2 >= xx;
}
void generate(vector<double> x, vector<double> y) {
	int size = x.size();
	
	set<int> points;
	vector<double> dx;
    vector<double> dy;
	for (int i = 0; i < size - 1; i++) {
		double temp_dx = x[i + 1] - x[i];
		dx.push_back(temp_dx);
		double temp_dy = y[i + 1] - y[i];
		dy.push_back(temp_dy);
	}
	
	MatrixXd H = MatrixXd::Zero(size, size);
	VectorXd Y(size);
	for (int i = 0; i < size; i++) {
		Y(i) = 0;
	}
	VectorXd M(size);
	for (int i = 0; i < size; i++) {
		M(i) = 0;
	}
 
	H(0, 0) = 1;
	H(size - 1, size - 1) = 1;
	for (int i = 1; i < size - 1; i++) {
		H(i, i - 1) = dx[i - 1];
		H(i, i) = 2 * (dx[i - 1] + dx[i]);
		H(i, i + 1) = dx[i];
		Y(i) = 3 * (dy[i] / dx[i] - dy[i - 1] / dx[i - 1]);
	}
 
	M = H.colPivHouseholderQr().solve(Y);
 
	vector<double> ai, bi, ci, di;
	for (int i = 0; i < size - 1; i++) {
		ai.push_back(y[i]);
		di.push_back((M(i + 1) - M(i)) / (3 * dx[i]));
		bi.push_back(dy[i] / dx[i] - dx[i] * (2 * M(i) + M(i + 1)) / 3);
		ci.push_back(M(i));
	}
 
	for (int i = 0; i < size - 1; i++) {
		double x1 = x[i], x2 = x[i + 1], y1 = y[i], y2 = y[i + 1];
		double dis = 0;
		if (x1 > x2) {
			dis = x1 - x2;
		}
		else {
			dis = x2 - x1;
		}
		if (y1 > y2) {
			dis += y1 - y2;
		}
		else {
			dis += y2 - y1;
		}
		dis *= 2;
		int num = (int) dis;
		double length = (x2 - x1) / (double) num;
		double xx = x1;
		// std::cout << xx << '\t' << x2 << '\t' << length << '\t' << num << '\n';
		for (xx; check(x1, x2, xx); xx += length) {
			// std::cout << xx << '\t';
			double yy = ai[i] + bi[i] * (xx - x[i]) + M(i) * pow((xx - x[i]), 2) + di[i] * pow((xx - x[i]), 3);
			// std::cout << yy << '\n'; 
			int X = (int)xx, Y = (int) yy;
			if (xx - (double)X > 0.5) {
				X++;
			}
			if (yy - (double)Y > 0.5) {
				Y++;
			}
			std::cout << X << ' ' << Y << '\n'; 
			if (points.find(X * 500 + Y) == points.end()) {
				points.insert(X * 500 + Y);
			}
		}	
		// std::cout << '\n';
	}
	std::ofstream output;
	output.open("Spline.txt");
	for (int i : points) {
		output << i / 500 << ' ' << i % 500 << std::endl;
		// output << i % 500 << ' ' << i / 500 << std::endl;
	}
	output.close();
	return;
}

int main() {
	vector<vector<double>> points = getCordinate("test.txt");
	generate(points[0], points[1]);
	return 0;
}