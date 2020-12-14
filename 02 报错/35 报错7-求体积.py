def get_volume(radius, height):
    try :
        if radius < 0 and height < 0 :
            raise HRError()
        elif radius < 0 :
            return 'ERROR: Radius must be positive.'
        elif height < 0 :
            return 'ERROR: Height must be positive.'
        elif height == 0 or radius == 0 :
            return 'ERROR: Not a cylinder.'
        else :
            num = 3.1415926535 * radius * radius * height
            return int(num+0.5)
    except TypeError :
        return 'ERROR: Invalid input.'
    except HRError :
        return 'ERROR: Height and radius must be positive.'



