def read_scores(filename):
    try:
        if type(filename) != str :
            raise TypeError()
        if filename == '':
            raise NameError()
        input_file = open(filename, "r")
        scores = input_file.read().split()


        new_list = scores
        length = len(new_list)
        if length == 0:
            raise ZeroDivisionError()
        check = 0
        for i in range(0,length):
            if float(new_list[i]) > 0 :
                check += 1
        if check == 0 :
            raise ZeroDivisionError()


        numbers = [float(score) for score in scores if float(score) >= 0 ]
        input_file.close()
        number_of_marks = len(numbers)
        total_marks = sum(numbers)
        print("There are {} score(s).".format(number_of_marks))
        print("The total is {:.2f}.".format(total_marks))
        print("The average is {:.2f}.".format(total_marks/number_of_marks))

    except TypeError :
        return print("ERROR: Invalid input!")
    except FileNotFoundError:
        return print("ERROR: The file \'{}\' does not exist.".format(filename))
    except NameError:
        return print("ERROR: Invalid filename!")
    except ZeroDivisionError :
        return print("ERROR: No positive scores in the input file.")
    except OSError:
        return print("ERROR: Invalid input!")
    except ValueError:
        return print("ERROR: The input file contains invalid values.")
