#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <math.h>

#include "gurobi_c++.h"

#define MASK(n) ((1ULL << n) - 1)
#define SET_BIT(mask, bit) (mask |= 1ULL << bit)
#define TEST_BIT(mask, bit) ((mask & (1ULL << bit)))
#define INVERSE_BIT(mask, bit) (mask ^= (1ULL << bit))

auto get_data_from_file(const int n) -> std::vector<std::vector<int>> {
	std::ifstream input("data/" + std::to_string(n) + ".txt");
	std::vector<std::vector<int>> a(n, std::vector<int>(n));

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j)
			input >> a[i][j];
		a[i][i] = 1;
	}

	return a;
}

auto create_chosen_matrix(GRBModel& model, const std::vector<std::vector<int>>& a) -> std::vector<std::vector<GRBVar>> {
	const int n = a.size();
	std::vector<std::vector<GRBVar>> x(n, std::vector<GRBVar>(n));

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			x[i][j] = model.addVar(0, 1, a[i][j], GRB_BINARY);

	return x;
}

auto find_minium_cycle(GRBModel& model, const std::vector<std::vector<GRBVar>>& x) -> std::vector<int> {
	const int n = x.size();
	std::vector<int> mapping(n);
		
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (std::round(x[i][j].get(GRB_DoubleAttr_X)))
				mapping[i] = j;

	unsigned long long unused = MASK(n);
	std::vector<int> result;
	int min_length = 1e7 + 1;
	for (int i = 0; i < n; ++i) {
		if (!TEST_BIT(unused, i))
			continue;
			
		std::vector<int> cycle = {i};
		INVERSE_BIT(unused, i);

		for (int ptr = mapping[i]; ptr != i; ptr = mapping[ptr]) {
			cycle.push_back(ptr);
			INVERSE_BIT(unused, ptr);
		}

		if (cycle.size() < min_length) {
			result = std::move(cycle);
			min_length = cycle.size();
		}
	}

	return result;
}

void add_mapping_constraints(GRBModel& model, const std::vector<std::vector<GRBVar>>& x) {
	const int n = x.size();
	for (int i = 0; i < n; ++i) {
		GRBLinExpr row = 0, col = 0;
		for (int j = 0; j < n; ++j) {
			if (i == j) continue;
			row += x[i][j];
			col += x[j][i];
		}

		model.addConstr(row == 1);
		model.addConstr(col == 1);
	}
}

void add_subtour_elimination_constrains(GRBModel& model, const std::vector<std::vector<GRBVar>>& x, const std::vector<int>& cycle_) {
	const int n = cycle_.size();
	GRBLinExpr cycle = 0, reverse_cycle = 0;

	for (int i = 0; i < n; ++i) {
		cycle += x[cycle_[i]][cycle_[(i + 1) % n]];
		reverse_cycle += x[cycle_[(i + 1) % n]][cycle_[i]];
	}

	model.addConstr(cycle <= cycle_.size() - 1);
	model.addConstr(reverse_cycle <= cycle_.size() - 1);
}

int32_t main(int argc, char** argv) {
	assert(argc > 1);
	const int n = atoi(argv[1]);

	try {
		GRBEnv env = GRBEnv();
		env.set("OutputFlag", "0");

		GRBModel model = GRBModel(env);
		std::cout << "Starting...\n";

		std::vector<std::vector<int>> a = std::move(get_data_from_file(n));
		std::vector<std::vector<GRBVar>> x = std::move(create_chosen_matrix(model, a));

		add_mapping_constraints(model, x);

		while (true) {
			model.optimize();
			assert(model.get(GRB_IntAttr_Status) == GRB_OPTIMAL);

			const std::vector<int> cycle = find_minium_cycle(model, x);
			
			std::cout << '[';
			for (const int& v : cycle)
				std::cout << v << ' ';
			
			std::cout << "]\n";
			if (cycle.size() == n) break;
			add_subtour_elimination_constrains(model, x, cycle);
		}	

		std::cout << '\n';
		std::cout << "Objective: " << model.get(GRB_DoubleAttr_ObjVal) << '\n';
	}
	catch (GRBException e) {
		std::cout << "Error" << e.getErrorCode() << '\n';
		std::cout << e.getMessage() << '\n';
	}
	catch (...) {
		std::cout << "An error has occured\n";
	}

	return 0;
}
