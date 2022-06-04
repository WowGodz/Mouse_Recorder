while True:
    def sin_basic(freq, time=1, amp=1, phase=0, samplerate=44100, bitspersample=16):
        bytelist = []
        import math
        TwoPiDivSamplerate = 2 * math.pi / samplerate
        increment = TwoPiDivSamplerate * freq
        incadd = phase * increment
        for i in range(int(samplerate * time)):
            if incadd > (2 ** (bitspersample - 1) - 1):
                incadd = (2 ** (bitspersample - 1) - 1) - (incadd - (2 ** (bitspersample - 1) - 1))
            elif incadd < -(2 ** (bitspersample - 1) - 1):
                incadd = -(2 ** (bitspersample - 1) - 1) + (-(2 ** (bitspersample - 1) - 1) - incadd)
            bytelist.append(int(round(amp * (2 ** (bitspersample - 1) - 1) * math.sin(incadd))))
            incadd += increment
        return bytelist

