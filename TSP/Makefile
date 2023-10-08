CC = g++
FLAGS = -Wall -Wextra -m64
EXEC = main.cpp

build: $(EXEC)
	$(CC) $(FLAGS) -g $(EXEC) -o main -I $(GUROBI_HOME)/include -L $(GUROBI_HOME)/lib -lgurobi_c++ -lgurobi100 -lm

