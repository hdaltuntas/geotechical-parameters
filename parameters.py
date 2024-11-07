import math


def undrained_shear_strength(sptn, pi, effective_stress, cbr, plnet, cpt):

    cu_1 = (
    	98.1 
    	+ 0.06 
    	* sptn
    )
    
    cu_2 = (
    	(0.11 + 0.0037 * pi) 
    	* effective_stress
    )
    
    cu_3 = (
    	((8910 / math.pow(pi, 3)) + 4.36) 
    	* sptn
    )
    
    cu_4 = (
    	cbr 
    	/ 0.09
    )
    
    cu_5 = (
    	98.1 
    	* 0.29 
    	* math.pow(sptn, 0.72)
    )
    
    cu_6 = (
    	(cpt - effective_stress) 
    	/ 1.7
    )
    
    cu_7 = (
    	(98.1 * 0.29) 
    	* math.pow(sptn60, 0.6)
    )
    
    cu_8 = (
    	6.25 
    	* sptn
    )
    
    cu_9 = (
    	12 
    	* sptn
    )
    
    cu_10 = (
    	4.43 
    	* sptn 
    	+ 8.07
    )
    
    cu_11 = (
    	12.5 
    	* sptn
    )
    
    cu_12 = (
    	15 
    	* sptn60
    )

    if plnet < 300:
        cu_13 = plnet / 5.5

    else:
        cu_13 = plnet / 10

    if pi > 30:
        cu_14 = 4.2 * sptn

    elif pi < 20:
        cu_14 = 6.5 * sptn

    else:
        cu_14 = 4.5 * sptn

    if pi > 20:
        cu_15 = 12 * sptn

    elif pi < 10:
        cu_15 = 7.25 * sptn

    else:
        cu_15 = 3.63 * sptn

    cu_16 = (
        25
        + (plnet / 10)

    )

    cu_17 = (
        98.1
        * 0.21
        * math.pow ((plnet / 98.1), 0.75)

    )

    return {
        "Kulhawy-Mayne (1990)": round(cu_1, 0),
        "Skempton-Bjerrum (1957)": round(cu_2, 0),
        "Stroud": round(cu_3, 0),
        "Carter ve Bentley (1990)": round(cu_4, 0),
        "Hara vd (1974)": round(cu_5, 0),
        "Lunne vd. (1997)": round(cu_6, 0),
        "Hara vd. (1971)": round(cu_7, 0),
        "Terzaghi ve Peck (1967)": round(cu_8, 0),
        "Nixon (1982)": round(cu_9, 0),
        "İyisan ve Ansal (1990)": round(cu_10, 0),
        "Decourt (1990)": round(cu_11, 0),
        "Decourt (1990)": round(cu_12, 0),
        "Amar vd. (1991)": round(cu_13, 0),
        "Stroud (1974)": round(cu_14, 0),
        "Sowers ()": round(cu_15, 0),
        "Amar and Jezequel (1972)": round(cu_16, 0),
        "Baguelin et. al. (1978)": round(cu_16, 0),
    }


def effective_phi(pi):
    phi_1 = (
    	43 
    	- ((11 * (math.log10(pi))))
    )
    
    phi_2 = (
    	(0.0058 * math.pow(pi, 1.73) - 0.32 * pi) 
    	+ 36.2
    )
    
    phi_3 = (
    	(0.084 * math.pow(pi, 1.4) - 0.75 * pi) 
    	+ 31.9
    )

    return {
        "Sorensen ve Okkels (2013)": round(phi_1, 1),
        "Gibson (1953)": round(phi_2, 1),
        "Gibson (1953)": round(phi_3, 1),  # residual phi
    }


def cc(liquid_limit, pi, wn, e0):
    cc1 = (
    	0.007 
    	* (liquid_limit - 10)
    )
    
    cc2 = (
    	pi 
    	/ 74
    )
    
    cc3 = (
    	0.01 
    	* (liquid_limit - 13)
    )
    
    cc4 = (
    	0.012 
    	* wn
    )
    
    cc5 = (
    	1.15 
    	* (e0 - 0.35)
    )
    
    cc6 = (
    	0.65 
    	* (e0 - 0.35)
    )

    return {
        "Skempton (1944)": round(cc1, 3),
        "Kulhawy-Mayne (1990)": round(cc2, 3),
        "USACE (1990)": round(cc3, 3),
        "USACE (1990)": round(cc4, 3),
        "Azzouz (1976)": round(cc5, 3),
        "Nishida (1956)": round(cc6, 3),
    }


def cr(pi):
    cr1 = (
    	pi 
    	/ 370
    )

    return {
        "Kulhawy-Mayne (1990)": round(cr1, 3),
    }


def cs(pi):
    cs = (
    	0.00194 
    	* (pi - 4.6)
    )

    return {
        "Nakase (1988)": round(cs, 3),
    }


def cv(liquid_limit):
    cv = (
    	103.97 
    	* math.pow(liquid_limit, -2.8535)
    )

    return {
        "Cv": round(cs, 3),
    }


def mv(pi, sptn):
    mv = (
    	math.pow(pi, 2.07) 
    	/ (sptn * (56000 + 435 * math.pow(pi, 2.07)))
    )

    return {
        "Midland Geotechnical Society": round(mv, 6),
    }


def ocr(sptn, effective_stress):
    ocr = (
    	0.193 
    	* math.pow((sptn * 1000 / effective_stress), 0.689)
    )

    return {
        "Mayne ve Kemper (1988)": round(ocr, 6),
    }


def swelling(pi, liquid_limit):
    swelling1 = (
        3.6
        * math.pow(10, -5)
        * math.pow((pi / liquid_limit), 2.44)
        * math.pow(liquid_limit, 3.44)
    )
    
    swelling2 = (
    	3.6 
    	* math.pow(10, -5) 
    	* math.pow(pi, 2.44) 
    	* 60
    	
    )
    	

    return {
        "Seed et al. (1962)": round(swelling1, 2),
        "Seed, Woodwars ve Ludgren": round(swelling2, 2),
    }


def deformation_modulus(sptn, cu, cpt):
    deformation_modulus_1 = (
    	900 
    	* sptn
    )
    
    deformation_modulus_2 = (
    	270 
    	* cu
    )
    
    deformation_modulus_3 = (
    	3 
    	* cpt
    )
    
    deformation_modulus_4 = (
    	6 
    	* sptn 
    	* 100
    )

    

    return {
        "Seed et al. (1962)": round(deformation_modulus_1, 0),
        "Stroud (1975)": round(deformation_modulus_2, 0),
        "Bowles (1997)": round(deformation_modulus_3, 0),
        "Yoshida ve Yoshinaka (1972)": round(deformation_modulus_4, 0),
        
    }


def sigma_c(sptn):
    sigma_c = (
    	98.1 
    	* 67 
    	* math.pow(sptn, 0.83)
    )

    return {
        "Seed": round(sigma_c, 3),
    }


def phi(sptn, sptn160, effective_stress, cpt):
    phi_1 = (
    	25 
    	+ ((math.sqrt((100 * sptn) / (70 + effective_stress))) * 3.2)
    )
    
    phi_2 = (
    	27.1 
    	+ (0.3 * sptn160) 
    	- (0.00054 * math.pow(sptn160, 2))
    )
    
    phi_3 = (
    	math.sqrt(15 * sptn160) 
    	+ 15
    )
    
    phi_4 = (
    	math.sqrt(20 * sptn160) 
    	+ 20
    )
    
    phi_5 = (
    	17.6 
    	+ 11 
    	* math.log10(cpt)
    )

    return {
        "OCDI Japan (2002)": round(phi_1, 1),
        "Wollf (1989)": round(phi_2, 1),
        "JRA (1996)": round(phi_3, 1),
        "Hatanaka-Uchida (1996)": round(phi_4, 1),
        "Kulhawy-Mayne (1990)": round(phi_5, 1),
    }


def elastic_modulus(sptn, sptn60, poisson):
    elastic_modulus = (
    	718 
    	* (1 - math.pow(poisson, 2)) 
    	* sptn
    )

    return {
        "Ferrent (1963)": round(elastic_modulus, 0),
    }


def phi_d(sptn160, effective_stress):
    phi_d = (
    	0.83 
    	* sptn160
    )

    return {
        "Srbulov (2005)": round(phi_d, 1),
    }


choice = input(
    """
    Which parameter do you want to calculate?

    Cohesive soil
    
    1.Undrained shear strength
    2.Effective friction angle
    3.The compression index
    4.Recompression index
    5.Swelling index
    6.Coefficient of consolidation
    7.The coefficient of volume compressibility
    8.OCR
    9.Swelling potential
    10.Deformation Modulus
    11.Pre consolidation pressure

    Cohesionless soil

    12. Friction angle
    13. Elasticitiy modulus
    14. Dynamic friction angle

    """
)

if choice == "1":
    sptn = float(input("SPT-N?: "))
    sptn60 = float(input("SPT-N 60?: "))
    effective_stress = float(input("Effective stress (kPa)?: "))
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    cbr = float(input("CBR?: "))
    plnet = float(input("PLnet?: "))
    cpt = float(input("qc (kPa)?: "))
    pi = liquid_limit - plastic_limit

    result = undrained_shear_strength(sptn, pi, effective_stress, cbr, plnet, cpt)
    print("Calculated undrained shear strength values (kPa):")
    for method, cu in result.items():
        print(f"- {method}: {cu:.2f}")


if choice == "2":
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit

    result = effective_phi(pi)
    print("Calculated effective phi values:")
    for method, effective_phi in result.items():
        print(f"- {method}: {effective_phi:.2f}")


if choice == "3":
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit
    wn = float(input("Su muhtevası (%)?: "))
    e0 = float(input("e0?: "))

    result = cc(liquid_limit, pi, wn, e0)
    print("Calculated cc values:")
    for method, cc in result.items():
        print(f"- {method}: {cc:.2f}")


if choice == "4":
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit

    result = cr(pi)
    print("Calculated cr values:")
    for method, cr in result.items():
        print(f"- {method}: {cr:.2f}")


if choice == "5":
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit

    result = cs(pi)
    print("Calculated cr values:")
    for method, cs in result.items():
        print(f"- {method}: {cs:.2f}")


if choice == "6":
    liquid_limit = float(input("Liquid limit?: "))

    result = cv(liquid_limit)
    print("Calculated cv values:")
    for method, cv in result.items():
        print(f"- {method}: {cv:.2f}")


if choice == "7":
    liquid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit
    sptn = float(input("SPT-N?: "))

    result = mv(pi, sptn)
    print("Calculated cr values:")
    for method, mv in result.items():
        print(f"- {method}: {mv:.2f}")


if choice == "8":
    sptn = float(input("SPT-N?: "))
    effective_stress = float(input("Effective stress (kPa)?: "))

    result = ocr(sptn, effective_stress)
    print("Calculated ocr values:")
    for method, ocr in result.items():
        print(f"- {method}: {ocr:.2f}")

    if ocr == 1:
        print("This soil is normally consolidated")

    elif ocr > 1:
        print("This soil is overconsolidated")

    else:
        print("This soil is underconsolidated")


if choice == "9":
    liguid_limit = float(input("Liquid limit?: "))
    plastic_limit = float(input("Plastic limit?: "))
    pi = liquid_limit - plastic_limit

    result = swelling(pi, liquid_limit)
    print("Calculated swelling values:")
    for method, swelling in result.items():
        print(f"- {method}: {swelling:.2f}")


if choice == "10":
    sptn = float(input("SPT-N?: "))

    result = deformation_modulus(sptn, cu, cpt)
    print("Calculated deformation_modulus values:")
    for method, deformation_modulus in result.items():
        print(f"- {method}: {deformation_modulus:.2f}")


if choice == "11":
    sptn = float(input("SPT-N?: "))

    result = sigma_c(sptn)
    print("Calculated sigma_c values:")
    for method, sigma_c in result.items():
        print(f"- {method}: {sigma_c:.2f}")


if choice == "12":
    sptn = float(input("SPT-N?: "))
    sptn160 = float(input("SPT-N1 60?: "))
    effective_stress = float(input("Effective stress (kPa)?: "))
    cpt = float(input("qc (kPa)?: "))

    result = phi(sptn, sptn160, effective_stress, cpt)
    print("Calculated phi values:")
    for method, phi in result.items():
        print(f"- {method}: {phi:.2f}")


if choice == "13":
    sptn = float(input("SPT-N?: "))
    sptn60 = float(input("SPT-N 60?: "))
    poisson = float(input("Poisson ratio?: "))

    result = elastic_modulus(sptn, sptn60, poisson)
    print("Calculated elastic modulus values:")
    for method, elastic_modulus in result.items():
        print(f"- {method}: {elastic_modulus:.2f}")


if choice == "14":
    sptn160 = float(input("SPT-N1 60?: "))
    effective_stress = float(input("Effective stress (kPa)?: "))

    result = phi_d(sptn160, effective_stress)
    print("Calculated dynamic friction angle values:")
    for method, phi_d in result.items():
        print(f"- {method}: {phi_d:.2f}")
