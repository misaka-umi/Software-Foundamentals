def is_valid_score(score):
    try :
        if score >= 0 and score <= 100 :
            return 'True'
        else :
            raise ValueError()
    except TypeError:
        return "ERROR: Invalid score!"
    except ValueError:
        return "ERROR: Invalid score!"
