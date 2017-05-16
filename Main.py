from PIL import Image
import numpy as np
import HelpingFunction as HF
import Solver
from Constants import *
import Picture
import random
import os


def main_type_comparison(min_n=3, max_n=0):
    image_address = HF.randomly_choose_file()
    random_num = random.randint(1000, 9999)  # random number for file name
    name = HF.address_to_name(image_address) + " type comparison " + str(random_num)
    comparison(image_address, ALGO_INDEX, min_n, max_n, name, 'Results/' + name + '/')


def main_run_check(min_n=3, max_n=0):
    image_address = HF.randomly_choose_file()
    random_num = random.randint(1000, 9999)  # random number for file name
    name = HF.address_to_name(image_address) + " 10 single type " + str(random_num)
    print(name)
    comparison(image_address, [BETTER], min_n, max_n, name, 'Results/' + name + '/')


def comparison(image_address, solver_type_list, min_n, max_n=0, result_file_name='', subfolder_name=SUBFOLDER):
    '''
    :param image_address: adress of desired image 
    :param solver_type_list: solver types to be checked
    :param min_n: min_n^2 is the minimal number of puzzle_pieces to be cut
    :param max_n: max_n^2 is the maximal number of puzzle pieces to be cut
    :param result_file_name: file name for result to be kept in. If not given, choose according to image picture
    :param subfolder_name: name of folder for results to be kept in
    All result pictures are saved, and running parameters are saved in the following format:
    Picture size (nXn)
    parameter (running time, cost, etc...)
    solver_type: result
    '''
    # creation of file and directory
    picture_name = HF.address_to_name(image_address)
    if result_file_name == "":
        result_file_name = picture_name
    if not os.path.exists(subfolder_name):
        os.makedirs(subfolder_name)
    result_file = open(subfolder_name + "/" + result_file_name, "w")

    # run
    if max_n == 0:  # only once
        max_n = min_n
    for n in range(min_n, max_n + 1):
        result_file.write("Piece Number: " + str(n) + "X" + str(n) + "\n")
        for solver_type in solver_type_list:
            result_file.write(ALGO_NAME[solver_type] + ":\n")
            results = single_run(image_address, n, solver_type, subfolder_name)
            for result_param in TUPLE_RESULT_INDEXES:
                result_file.write(PARAMETER_NAME[result_param] + ": " + str(results[result_param]) + "\n")
            result_file.write("\n")
        result_file.write("\n\n")
    result_file.close()


def single_run(image_address, n, solver_type, subfolder_name):
    '''
    :param image_address: address of desired image 
    :param n: n^2 is the number of puzzle pieces to be cut
    :param solver_type: type of solver to be used
    :param subfolder_name: name of folder for results to be kept in
    '''
    square_puzzle = Picture.Picture(image_address, n, n)
    picture_name = HF.address_to_name(image_address)
    solution_name = (picture_name + " - " + str(n) + "X" + str(n) + " pieces - " + ALGO_NAME[solver_type])
    solver = Solver.Solver(square_puzzle, solver_type)
    Image.fromarray(solver.get_results()[4]).save(subfolder_name + solution_name + ".jpeg", "jpeg")
    return solver.get_results()


def create_square_puzzle(image_address, n):
    return Picture.Picture(image_address, n, n)


# ame = HF.address_to_name("Lenna.jpg") + "BETTER"
# comparison("Lenna.jpg", [BETTER], 10, 10, name, 'Results/' + name + '/')

main_run_check(8, 8)
main_run_check(9, 9)
