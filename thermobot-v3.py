import discord
from discord import app_commands
from discord.ui import Button, View, Select
import random
import os
# ====================== QUESTIONS ======================

QUESTIONS = {
    "Novice": [
        # === OLD QUESTIONS ===
        ("Which law of thermodynamics defines temperature through thermal equilibrium?",
         ["First Law", "Second Law", "Zeroth Law", "Third Law"], 2),
        ("For an ideal gas, internal energy depends only on:",
         ["Pressure", "Volume", "Temperature", "Entropy"], 2),
        ("Work done in an isochoric process is:",
         ["Maximum", "PΔV", "Zero", "Equal to Q"], 2),
        ("An isobaric process on a PV diagram is represented by a:",
         ["Vertical line", "Horizontal line", "Hyperbola", "Steep curve"], 1),
        ("The First Law is a statement of:",
         ["Direction of processes", "Conservation of energy", "Increase of entropy", "Absolute zero"], 1),
        ("Heat capacity at constant volume is related to:",
         ["ΔH = nCpΔT", "ΔU = nCvΔT", "W = PΔV", "Q = 0"], 1),
        ("Which process has Q = 0?",
         ["Isothermal", "Isobaric", "Adiabatic", "Isochoric"], 2),
        ("Entropy is a measure of:",
         ["Temperature", "Energy dispersal / disorder", "Pressure", "Volume"], 1),
        ("Absolute zero corresponds to:",
         ["0 °C", "273 K", "0 K", "−273 °C only"], 2),
        ("Cp − Cv for an ideal gas equals:",
         ["0", "R", "γ", "1"], 1),

        # === NEW FROM SCIOLY WIKI ===
        ("According to the caloric theory, which of the following assumptions is the only one considered true?",
         ["Heat is a fluid that flows from hot to cold", "Heat is conserved", "Heat is weightless", "Sensible heat causes temperature increase"], 2),
        ("The kinetic theory of heat states that the average kinetic energy of gas particles depends only on:",
         ["Pressure", "Volume", "Temperature", "The number of collisions"], 2),
        ("Boyle’s Law states that at constant temperature, pressure and volume are:",
         ["Directly proportional", "Inversely proportional", "Equal", "Independent"], 1),
        ("Charles’ Law states that at constant pressure, volume is directly proportional to:",
         ["Celsius temperature", "Kelvin temperature", "Pressure", "Number of moles"], 1),
        ("An open thermodynamic system allows which of the following to cross its boundary?",
         ["Only heat", "Only matter", "Matter, heat, and work", "Nothing"], 2),
        ("A closed system allows heat and work to cross the boundary but does not allow:",
         ["Energy", "Matter", "Entropy", "Temperature change"], 1),

        # === NEW HISTORY QUESTIONS ===
        ("The SI unit of energy is named after:",
         ["James Clerk Maxwell", "James Prescott Joule", "Daniel Fahrenheit", "Walther Nernst"], 1),
        ("Who is often called the 'Father of Thermodynamics'?",
         ["James Joule", "Rudolf Clausius", "Sadi Carnot", "Lord Kelvin"], 2),
        ("Who introduced the concept of entropy in 1865?",
         ["Lord Kelvin", "Sadi Carnot", "Rudolf Clausius", "Walther Nernst"], 2),
        ("Which scientist formulated the Third Law of Thermodynamics?",
         ["James Joule", "Lord Kelvin", "Walther Nernst", "James Clerk Maxwell"], 2),
        ("Which famous physicist proposed the thought experiment known as 'Maxwell's Demon'?",
         ["Lord Kelvin", "James Clerk Maxwell", "Rudolf Clausius", "Sadi Carnot"], 1),
        ("Who invented the mercury thermometer?",
         ["Galileo Galilei", "Daniel Gabriel Fahrenheit", "Anders Celsius", "Lord Kelvin"], 1),
        ("The Celsius temperature scale was originally proposed by:",
         ["Carl Linnaeus", "Anders Celsius", "Daniel Fahrenheit", "Lord Kelvin"], 1),
        ("Absolute temperature is measured using the scale named after:",
         ["Joule", "Celsius", "Kelvin", "Clausius"], 2),
        ("Which scientist built the first open thermometer?",
         ["Daniel Fahrenheit", "Galileo Galilei", "Anders Celsius", "James Joule"], 1),

        # === NEW FROM BINDER ===
        ("The conversion from Celsius to Kelvin is:",
         ["T_K = T_C − 273.15", "T_K = T_C + 273.15", "T_K = (9/5)T_C + 32", "T_K = T_C × 273.15"], 1),
        ("In the sign convention ΔU = Q − W, positive W means:",
         ["Heat enters the system", "The system does work on the surroundings", "Surroundings do work on the system", "Heat leaves the system"], 1),
        ("Which of the following is a state function?",
         ["Heat", "Work", "Internal energy", "Both heat and work"], 2),
        ("For an isochoric process, work done by the system is:",
         ["PΔV", "nRT ln(V2/V1)", "Zero", "Equal to Q"], 2),
        ("The specific heat of water is approximately:",
         ["334 J/kg·K", "2256 J/kg·K", "4184 J/kg·K", "1000 J/kg·K"], 2),
        ("Latent heat of fusion of ice is approximately:",
         ["2256 kJ/kg", "334 kJ/kg", "4184 J/kg", "100 kJ/kg"], 1),
        ("An open system allows which of the following to cross its boundary?",
         ["Only energy", "Only matter", "Both matter and energy", "Neither matter nor energy"], 2),
        ("A closed system allows energy but not:",
         ["Work", "Heat", "Matter", "Temperature change"], 2),
        ("Temperature intervals in Celsius and Kelvin are:",
         ["Different by a factor of 9/5", "Identical in size", "Offset by 32", "Unrelated"], 1),
        ("Heat is best described as:",
         ["A substance stored in an object", "Energy transferred due to a temperature difference", "The same as temperature", "Internal energy"], 1),
        ("Extensive properties depend on:",
         ["The amount of matter", "The type of substance only", "Temperature only", "Pressure only"], 0),
        ("An intensive property is one that:",
         ["Depends on the size of the system", "Does not depend on the amount of matter", "Is always a state function", "Can only be temperature"], 1),
        ("In free expansion of an ideal gas into vacuum, work is:",
         ["Maximum", "Zero", "Equal to Q", "Negative"], 1),
        ("The ideal-gas law is written as:",
         ["PV = nRT", "P/V = nRT", "PV = nR/T", "P + V = nRT"], 0),
        ("On a P-V diagram the area under a process curve represents:",
         ["Heat", "Work", "Change in internal energy", "Entropy"], 1),
    ],

    "Intermediate": [
        # === OLD QUESTIONS ===
        ("An ideal gas expands isothermally. Which quantity is zero?",
         ["Q", "W", "ΔU", "ΔS"], 2),
        ("For a reversible adiabatic process on an ideal gas:",
         ["PV = constant", "TV^{γ−1} = constant", "T/V = constant", "P/T = constant"], 1),
        ("A system absorbs 300 J of heat and does 120 J of work. ΔU is:",
         ["420 J", "180 J", "−180 J", "−420 J"], 1),
        ("Carnot efficiency between 450 K and 300 K is:",
         ["25%", "33.3%", "50%", "66.7%"], 1),
        ("In an isobaric process, Q equals:",
         ["ΔU", "ΔH", "W", "0"], 1),
        ("On a PV diagram, a vertical line represents:",
         ["Isobaric", "Isothermal", "Isochoric", "Adiabatic"], 2),
        ("When ice melts reversibly at 0 °C, ΔS of the system is:",
         ["Zero", "Positive", "Negative", "Undefined"], 1),
        ("For an ideal gas in reversible adiabatic expansion:",
         ["Temperature increases", "Internal energy decreases", "Entropy of system increases", "Heat is absorbed"], 1),
        ("The Zeroth Law is most closely related to:",
         ["Energy conservation", "Definition of temperature", "Direction of heat flow", "Maximum efficiency"], 1),
        ("In an isolated system, a spontaneous irreversible process always increases:",
         ["Internal energy", "Enthalpy", "Entropy", "Gibbs free energy"], 2),

        # === NEW FROM SCIOLY WIKI ===
        ("Gay-Lussac’s Law states that at constant volume, pressure is directly proportional to:",
         ["Celsius temperature", "Kelvin temperature", "Volume", "Number of moles"], 1),
        ("Joule’s Second Law states that the internal energy of an ideal gas depends only on:",
         ["Pressure and volume", "Temperature", "The path taken", "Work done"], 1),
        ("An isolated thermodynamic system allows which of the following to cross its boundary?",
         ["Heat only", "Matter only", "Work only", "Nothing"], 3),
        ("A diathermic boundary allows:",
         ["Matter to pass", "Heat to pass", "Work to pass", "Nothing to pass"], 1),
        ("The caloric theory of heat was primarily developed by:",
         ["James Clerk Maxwell", "Antoine Lavoisier", "Sadi Carnot", "James Joule"], 1),
        ("According to the kinetic theory, collisions between gas molecules are assumed to be:",
         ["Inelastic", "Perfectly elastic", "Partially elastic", "Negligible"], 1),

        # === NEW HISTORY QUESTIONS ===
        ("Which scientist is credited with discovering the mechanical equivalent of heat, helping establish the First Law of Thermodynamics?",
         ["James Prescott Joule", "Sadi Carnot", "Rudolf Clausius", "Lord Kelvin"], 0),
        ("Which scientist first clearly formulated the Second Law of Thermodynamics?",
         ["James Joule", "Rudolf Clausius", "Lord Kelvin", "James Clerk Maxwell"], 1),
        ("Maxwell's Demon was designed to challenge which law of thermodynamics?",
         ["Zeroth Law", "First Law", "Second Law", "Third Law"], 2),
        ("The Fahrenheit temperature scale is named after:",
         ["A Swedish astronomer", "A Dutch-German physicist", "A Scottish physicist", "A German chemist"], 1),
        ("Who coined the word 'thermodynamics'?",
         ["James Joule", "Lord Kelvin", "Rudolf Clausius", "Walther Nernst"], 1),
        ("Who is credited with determining the value of absolute zero?",
         ["Lord Kelvin", "James Joule", "Sadi Carnot", "James Clerk Maxwell"], 0),
        ("Who developed the Nernst equation, widely used in electrochemistry?",
         ["Walther Nernst", "Rudolf Clausius", "James Clerk Maxwell", "Lord Kelvin"], 0),
        ("Which scientist founded the Uppsala Astronomical Observatory?",
         ["James Clerk Maxwell", "Anders Celsius", "Lord Kelvin", "Galileo Galilei"], 1),

        # === NEW FROM BINDER ===
        ("For an ideal gas, ΔU equals:",
         ["nCpΔT", "nCvΔT", "PΔV", "nR ln(V2/V1)"], 1),
        ("For an ideal gas, ΔH equals:",
         ["nCvΔT", "nCpΔT", "W", "Q − W"], 1),
        ("In an isobaric process for an ideal gas, Q equals:",
         ["nCvΔT", "nCpΔT", "Zero", "W only"], 1),
        ("The relationship Cp − Cv for an ideal gas is:",
         ["Zero", "R", "γ", "1"], 1),
        ("γ is defined as:",
         ["Cv/Cp", "Cp/Cv", "Cp − Cv", "R/Cv"], 1),
        ("During a phase change at constant pressure, temperature:",
         ["Increases steadily", "Decreases steadily", "Remains approximately constant", "Fluctuates randomly"], 2),
        ("The equation Q = mL is used for:",
         ["Temperature change with no phase change", "Phase changes", "Adiabatic processes only", "Isothermal compression"], 1),
        ("Conduction heat transfer through a slab is proportional to:",
         ["1/thickness", "Thickness squared", "The square of the temperature difference", "Surface roughness only"], 0),
        ("Newton’s law of cooling states that the rate of temperature change is proportional to:",
         ["The absolute temperature", "The temperature difference with surroundings", "The square of the temperature", "Time only"], 1),
        ("In the expression T(t) = T∞ + (T0 − T∞)e^(−kt), k is the:",
         ["Thermal conductivity", "Cooling constant", "Specific heat", "Latent heat"], 1),
        ("A diathermal boundary allows:",
         ["Matter to pass", "Heat to pass", "Work only", "Nothing to pass"], 1),
        ("An adiabatic boundary prevents:",
         ["Matter transfer", "Heat transfer", "Work transfer", "Volume change"], 1),
        ("For a cyclic process, ΔU is:",
         ["Positive", "Negative", "Zero", "Equal to Q"], 2),
        ("The First Law applied to a complete cycle gives:",
         ["ΔU = Q", "Q_net = W_net", "W = 0", "Q = 0"], 1),
        ("Coffee-cup calorimetry is approximately a:",
         ["Constant-volume process", "Constant-pressure process", "Adiabatic process", "Isothermal process"], 1),
    ],

    "Hard": [
        # === OLD QUESTIONS ===
        ("An ideal gas expands reversibly and isothermally from V to 2V. The work done by the gas is:",
         ["nRT", "nRT ln(2)", "0", "½ nRT"], 1),
        ("A Carnot refrigerator operates between −10 °C and 25 °C. Its COP is closest to:",
         ["4.5", "7.5", "10.2", "12.8"], 1),
        ("In free expansion of an ideal gas into vacuum:",
         ["W > 0 and Q > 0", "W = 0, Q = 0, ΔU = 0", "Temperature decreases", "ΔU > 0"], 1),
        ("For a reversible adiabatic process:",
         ["ΔS_system > 0", "ΔS_system = 0", "ΔU = 0", "Q ≠ 0"], 1),
        ("Heat absorbed at constant pressure is equal to the change in:",
         ["Internal energy", "Enthalpy", "Entropy", "Helmholtz free energy"], 1),
        ("Compared to an isothermal curve, an adiabatic curve on a PV diagram is:",
         ["Less steep", "Steeper", "Identical", "Horizontal"], 1),
        ("For an ideal gas, (∂U/∂V)_T equals:",
         ["R", "Cv", "0", "Cp − R"], 2),
        ("A system has ΔU = −250 J and performs 100 J of work. Heat transferred to the system is:",
         ["−350 J", "−150 J", "+150 J", "+350 J"], 1),
        ("Which of the following is a state function?",
         ["Heat", "Work", "Internal energy", "Both heat and work"], 2),
        ("In a Carnot cycle the two isothermal processes are accompanied by:",
         ["No entropy change of the universe", "Positive entropy change of the universe", "Negative entropy change of the system", "Zero heat transfer"], 0),

        # === NEW FROM SCIOLY WIKI ===
        ("In the Carnot cycle, the process in which the gas is thermally isolated and expands while its temperature decreases is:",
         ["Isothermal expansion", "Reversible adiabatic expansion", "Isothermal compression", "Adiabatic compression"], 1),
        ("Maxwell’s Demon appears to violate the Second Law by:",
         ["Creating energy from nothing", "Separating fast and slow molecules to create a temperature difference without work", "Destroying entropy", "Reaching absolute zero"], 1),
        ("The resolution to Maxwell’s Demon paradox involves the fact that the demon:",
         ["Must expend energy / increase entropy to observe and sort molecules", "Cannot exist in reality", "Violates the First Law", "Only works at absolute zero"], 0),
        ("Joule’s First Law relates heat dissipated in a resistor to:",
         ["Voltage and time only", "I²Rt", "Power only", "Resistance and voltage"], 1),
        ("An isentropic process is one that occurs at constant:",
         ["Temperature", "Pressure", "Entropy", "Volume"], 2),
        ("For a reversible process, an adiabatic process is also:",
         ["Isobaric", "Isothermal", "Isentropic", "Isochoric"], 2),

        # === NEW HISTORY QUESTIONS ===
        ("The Carnot cycle was first described in which publication?",
         ["On the Mechanical Theory of Heat", "Reflections on the Motive Power of Fire", "Experimental Researches on Electricity", "The Kinetic Theory of Gases"], 1),
        ("Walther Nernst was awarded the 1920 Nobel Prize in:",
         ["Physics", "Chemistry", "Medicine", "Mathematics"], 1),
        ("Which scientist's work on heat engines inspired much of modern thermodynamics despite being based on caloric theory?",
         ["James Joule", "Sadi Carnot", "Rudolf Clausius", "Lord Kelvin"], 1),
        ("Carnot's work on heat engines was published in:",
         ["1799", "1824", "1850", "1865"], 1),
        ("Clausius introduced the term 'entropy' in:",
         ["1824", "1850", "1865", "1905"], 2),
        ("Which scientist's work demonstrated that heat and mechanical work are equivalent?",
         ["Carnot", "Joule", "Kelvin", "Nernst"], 1),

        # === NEW FROM BINDER ===
        ("The ideal-gas entropy change at constant volume is given by:",
         ["nCv ln(T2/T1)", "nCp ln(T2/T1)", "nR ln(V2/V1)", "Zero"], 0),
        ("The ideal-gas entropy change involving pressure is:",
         ["nCv ln(T2/T1) + nR ln(V2/V1)", "nCp ln(T2/T1) − nR ln(P2/P1)", "nR ln(T2/T1)", "Cv ln(P2/P1)"], 1),
        ("For a reversible phase change at temperature T_trans, ΔS equals:",
         ["mL / T_trans", "m c ΔT", "Zero", "nR ln(V2/V1)"], 0),
        ("Carnot efficiency is given by:",
         ["1 − Qc/Qh", "1 − Tc/Th (temperatures in kelvin)", "W/Qc", "Th/Tc"], 1),
        ("COP of a refrigerator is defined as:",
         ["W/Qc", "Qc/W", "Qh/W", "W/Qh"], 1),
        ("COP of a heat pump is:",
         ["Qc/W", "Qh/W", "W/Qh", "The same as refrigerator COP"], 1),
        ("On a P-V diagram a clockwise cycle represents:",
         ["Net work input", "Net work output", "Zero net work", "An isentropic process"], 1),
        ("The Otto cycle models:",
         ["A steam power plant", "A spark-ignition engine with constant-volume heat addition", "A gas turbine", "A refrigerator"], 1),
        ("The Diesel cycle features heat addition at:",
         ["Constant volume", "Constant pressure", "Constant temperature", "Constant entropy"], 1),
        ("Thermal resistance for conduction is:",
         ["kA/L", "L/(kA)", "hA", "1/(hA)"], 1),
        ("In series thermal resistances, total resistance is:",
         ["The reciprocal of the sum", "The sum of the individual resistances", "The product of the resistances", "The average resistance"], 1),
        ("Wien’s displacement law relates:",
         ["Pressure and volume", "Wavelength of maximum emission and temperature", "Heat capacity and temperature", "Entropy and volume"], 1),
        ("The Stefan-Boltzmann law gives net radiation heat transfer proportional to:",
         ["T", "T²", "T³", "T⁴"], 3),
        ("For an isolated system, a spontaneous process always results in:",
         ["ΔS_universe < 0", "ΔS_universe = 0", "ΔS_universe > 0", "ΔU > 0"], 2),
        ("The Third Law states that the entropy of a perfect crystal approaches zero as:",
         ["Pressure approaches zero", "Temperature approaches absolute zero", "Volume approaches zero", "The system becomes isolated"], 1),
    ],

    "Very Hard": [
        # === OLD QUESTIONS ===
        ("An ideal gas is taken through a cycle consisting of isothermal expansion, isochoric cooling, and adiabatic compression back to the original state. Net work is:",
         ["Positive (engine)", "Negative (refrigerator)", "Zero", "Cannot be determined without numbers"], 0),
        ("For a reversible process, ∮ dQ/T equals:",
         ["ΔS_system", "0", "ΔS_universe", "Q_net / T"], 1),
        ("A heat engine absorbs 800 J from a 600 K reservoir and rejects heat to a 300 K reservoir. Maximum possible work output is:",
         ["200 J", "400 J", "500 J", "600 J"], 1),
        ("In a throttling process (Joule-Thomson expansion) for an ideal gas:",
         ["Temperature always drops", "Enthalpy is constant", "Entropy is constant", "Internal energy increases"], 1),
        ("The Maxwell relation derived from dU = T dS − P dV is:",
         ["(∂T/∂V)_S = (∂P/∂S)_V", "(∂T/∂V)_S = −(∂P/∂S)_V", "(∂T/∂P)_S = (∂V/∂S)_P", "(∂S/∂V)_T = (∂P/∂T)_V"], 1),
        ("An ideal gas undergoes a process in which PV² = constant. The molar heat capacity for this process is:",
         ["Cv + R/2", "Cv + 2R", "Cp − R", "Cv + R"], 0),
        ("For a van der Waals gas, the internal pressure (∂U/∂V)_T is equal to:",
         ["0", "a/V_m²", "b", "R/V_m"], 1),
        ("The efficiency of a Carnot engine is 40%. If the temperature of the sink is 27 °C, the temperature of the source is:",
         ["227 °C", "327 °C", "500 °C", "77 °C"], 0),
        ("During a reversible adiabatic process for an ideal gas, which remains constant?",
         ["TV^{γ−1}", "T/V", "PV", "P/T"], 0),
        ("The change in entropy of the universe when 1 mole of ideal gas expands freely into vacuum to double its volume is:",
         ["0", "R ln 2", "−R ln 2", "Cv ln 2"], 1),

        # === NEW FROM SCIOLY WIKI ===
        ("In the Carnot cycle, the net change in entropy of the universe is:",
         ["Positive", "Negative", "Zero", "Dependent on the temperatures"], 2),
        ("The two adiabatic processes in the Carnot cycle are characterized by:",
         ["ΔS = 0 (isentropic)", "Q ≠ 0", "ΔU = 0", "Constant pressure"], 0),
        ("According to the Third Law, the entropy of a perfect crystal approaches zero as temperature approaches:",
         ["0 °C", "The melting point", "Absolute zero", "Room temperature"], 2),
        ("van der Waals’ equation corrects the ideal gas law for:",
         ["Only molecular volume", "Only attractive forces", "Both attractive forces and molecular volume", "Temperature dependence of R"], 2),
        ("Carnot’s Principle states that no heat engine operating between two temperatures can be more efficient than a:",
         ["Real irreversible engine", "Reversible engine operating between the same temperatures", "Steam engine", "Engine using ideal gas"], 1),
        ("In the caloric theory, “frigoric” referred to:",
         ["A type of work", "The absence or lack of caloric (cold)", "Latent heat", "Sensible heat"], 1),

        # === NEW HISTORY QUESTIONS ===
        ("The Third Law of Thermodynamics is also commonly called:",
         ["Joule's Law", "Nernst Heat Theorem", "Kelvin Principle", "Carnot Principle"], 1),
        ("Which early theory of heat was replaced by Joule's experiments?",
         ["Atomic theory", "Wave theory", "Caloric theory", "Kinetic theory"], 2),
        ("Before Joule's experiments, Carnot's original analysis of heat engines was based primarily on:",
         ["The kinetic theory of gases", "The caloric theory of heat", "Statistical mechanics", "Electromagnetism"], 1),
        ("Which pair of scientists are most directly associated with the Second and Third Laws of Thermodynamics, respectively?",
         ["Joule and Kelvin", "Clausius and Nernst", "Carnot and Maxwell", "Fahrenheit and Celsius"], 1),

        # === NEW FROM BINDER ===
        ("The Clapeyron equation is:",
         ["dP/dT = ΔH_trans / (T ΔV)", "dP/dT = ΔV / (T ΔH)", "ln(P2/P1) = −ΔH/R (1/T2 − 1/T1)", "Both A and C are related forms"], 0),
        ("The integrated Clausius-Clapeyron equation is most often used for:",
         ["Solid-solid transitions", "Vaporization or sublimation", "Isothermal compression", "Adiabatic expansion"], 1),
        ("Gibbs phase rule for a non-reacting system is:",
         ["F = C + P − 2", "F = C − P + 2", "F = C − P − 2", "F = P − C + 2"], 1),
        ("At the triple point of a single-component system, the number of degrees of freedom F is:",
         ["2", "1", "0", "3"], 2),
        ("For a reversible adiabatic process on an ideal gas, which is true?",
         ["PV = constant", "TV^{γ−1} = constant", "T/V = constant", "P/T^γ = constant"], 1),
        ("The work done in a reversible adiabatic process for an ideal gas can be written as:",
         ["nRT ln(V2/V1)", "nCv(T1 − T2)", "PΔV", "Zero"], 1),
        ("In Newton’s law of cooling, after one time constant τ the remaining temperature difference is approximately:",
         ["50%", "36.8%", "25%", "10%"], 1),
        ("The time constant τ for a lumped thermal system is:",
         ["hA / mc", "mc / hA", "kA / L", "L / kA"], 1),
        ("A plot of ln|T − T∞| versus time should be approximately linear with slope:",
         ["+k", "−k", "k²", "1/k"], 1),
        ("Bomb calorimetry is carried out at constant:",
         ["Pressure", "Volume", "Temperature", "Entropy"], 1),
        ("Coffee-cup calorimetry approximates constant:",
         ["Volume", "Pressure", "Temperature", "Entropy"], 1),
        ("When calculating final temperature of several objects mixed with no phase change:",
         ["Tf = Σ (mi ci Ti) / Σ (mi ci)", "Tf = Σ mi Ti / Σ mi", "Tf = average of all Ti", "Tf is always the highest Ti"], 0),
        ("Net radiation heat transfer between a surface and large surroundings is:",
         ["εσA(Ts − Tsur)", "εσA(Ts⁴ − Tsur⁴)", "σA(Ts⁴ − Tsur⁴) only", "hA(Ts − Tsur)"], 1),
        ("An isentropic process is equivalent to a reversible:",
         ["Isothermal process", "Isobaric process", "Adiabatic process", "Isochoric process"], 2),
        ("For a heat engine exchanging heat only with two reservoirs, ΔS of the reservoirs is:",
         ["−QH/TH + QC/TC ≥ 0", "QH/TH − QC/TC ≥ 0", "Always zero", "Always negative"], 0),
    ],

    "Impossible": [
        # === OLD QUESTIONS ===
        ("An ideal gas follows the process TV^{x} = constant. For the molar heat capacity to be 4R, the value of x is: (take γ = 1.4)",
         ["0.5", "1.0", "1.5", "2.0"], 0),
        ("A Carnot engine operates between T and T/2. Another identical engine operates between T/2 and T/4. The ratio of their efficiencies is:",
         ["1 : 1", "1 : 2", "2 : 1", "3 : 1"], 0),
        ("One mole of a van der Waals gas expands isothermally from V1 to V2. The work done is:",
         ["RT ln((V2−b)/(V1−b))", "RT ln(V2/V1)", "RT ln((V2−b)/(V1−b)) + a(1/V1 − 1/V2)", "None of these"], 2),
        ("For a thermodynamic system, the Helmholtz free energy F = U − TS. The natural variables of F are:",
         ["S, V", "T, V", "T, P", "S, P"], 1),
        ("In a reversible polytropic process PV^n = constant, the expression for work done by the gas is:",
         ["(P1V1 − P2V2)/(n−1)", "nR(T1 − T2)/(n−1)", "Both A and B are equivalent", "R(T1 − T2) ln(V2/V1)"], 2),
        ("The Joule-Thomson coefficient μ = (∂T/∂P)_H. For an ideal gas μ is:",
         ["Positive", "Negative", "Zero", "Infinite"], 2),
        ("A system goes from state A to B via two different paths. The difference in heat absorbed along the two paths equals the difference in:",
         ["Internal energy", "Work done", "Enthalpy", "Entropy"], 1),
        ("For a photon gas (blackbody radiation), the pressure P is related to energy density u by:",
         ["P = u/3", "P = u", "P = 3u", "P = u/2"], 0),
        ("The critical compressibility factor Zc = PcVc / RTc for a van der Waals gas is:",
         ["0.375", "0.25", "0.5", "0.125"], 0),
        ("In the T-S diagram of a Carnot cycle, the heat absorbed during the isothermal expansion is represented by:",
         ["Area under the upper horizontal line", "Height of the rectangle", "Width of the rectangle", "Diagonal of the rectangle"], 0),

        # === NEW FROM SCIOLY WIKI ===
        ("In the detailed Carnot cycle analysis, the relationship Q₂ / Q₁ = T_C / T_H is derived by combining the isothermal work expressions with the adiabatic condition that:",
         ["V₂ / V₁ = V₃ / V₄", "V₂ / V₄ = V₃ / V₁", "T_H V₂^{γ−1} = T_C V₃^{γ−1}", "Both the volume ratios and the adiabatic relation"], 3),
        ("Maxwell’s Demon decreases the entropy of the gas by sorting molecules, but the total entropy of the universe still increases because:",
         ["The demon must acquire information (using energy) and the mechanism itself gains entropy", "The First Law is violated", "Absolute zero is reached", "The process is irreversible by definition"], 0),
        ("According to the Scioly wiki treatment of the Third Law, two objects at different temperatures can never reach exactly the same temperature because:",
         ["Heat transfer stops completely", "The approach is asymptotic (exponential decay/growth)", "The Second Law forbids it", "Measurement tools are imperfect"], 1),
        ("Hess’ Law (mentioned in the gas-laws section) is essentially a consequence of:",
         ["The First Law (enthalpy is a state function)", "The Second Law", "The Third Law", "Boyle’s Law"], 0),
        ("In the Carnot cycle, the entropy change of the hot reservoir is +Q₁/T_H while the cold reservoir is −Q₂/T_C. Their sum is zero because:",
         ["Q₁/T_H = Q₂/T_C", "The processes are adiabatic", "No heat is transferred", "The cycle is irreversible"], 0),
        ("Statistical thermodynamics (as contrasted with classical) explains macroscopic laws by considering:",
         ["Only measurable laboratory properties", "Microscopic molecular motions and statistical distributions", "Chemical reaction pathways only", "Non-equilibrium systems exclusively"], 1),

        # === NEW HISTORY QUESTIONS ===
        ("Which of the following scientists died before the concept of entropy was introduced?",
         ["Rudolf Clausius", "Sadi Carnot", "Lord Kelvin", "Walther Nernst"], 1),
        ("Which scientist proposed a temperature scale that was later modified into the modern Celsius scale after his death?",
         ["Daniel Fahrenheit", "Anders Celsius", "Lord Kelvin", "Galileo Galilei"], 1),
        ("Which scientist's original heat engine theory remained largely correct even though its underlying assumption—that heat was a conserved fluid—was incorrect?",
         ["James Joule", "Sadi Carnot", "James Clerk Maxwell", "Walther Nernst"], 1),
        ("Arrange these historical developments from earliest to latest:",
         ["Kelvin scale → Carnot cycle → Entropy",
          "Carnot cycle → Joule's mechanical equivalent of heat → Entropy",
          "Entropy → Carnot cycle → Kelvin scale",
          "Mechanical equivalent of heat → Carnot cycle → Entropy"], 1),

        # === NEW FROM BINDER ===
        ("For an ideal gas undergoing a polytropic process PV^n = constant, the molar heat capacity is:",
         ["Cv + R/(1−n)", "Cv + R/(n−1)", "Cp − R", "Cv only"], 0),
        ("The efficiency of an ideal Otto cycle with compression ratio r is:",
         ["1 − 1/r", "1 − 1/r^{γ−1}", "1 − r^{γ−1}", "1 − (γ−1)/r"], 1),
        ("The efficiency of an ideal Brayton cycle with pressure ratio rp is:",
         ["1 − 1/rp", "1 − 1/rp^{(γ−1)/γ}", "1 − rp^{(γ−1)/γ}", "1 − (γ−1)/rp"], 1),
        ("In the expression for reversible adiabatic work of an ideal gas, W = (P1V1 − P2V2)/(γ−1) is equivalent to:",
         ["nR(T1 − T2)", "nCv(T1 − T2)", "nCp(T1 − T2)", "PΔV"], 1),
        ("When two objects at different temperatures are placed in contact inside an otherwise isolated system, the final common temperature is reached when:",
         ["Their internal energies become equal", "The entropy of the universe is maximized", "Their heat capacities become equal", "No more energy is available"], 1),
        ("The change in entropy of the universe for any real (irreversible) process is:",
         ["Zero", "Negative", "Positive", "Equal to ΔS_system"], 2),
        ("A system’s entropy can decrease only if:",
         ["The process is adiabatic", "The surroundings increase in entropy by at least as much", "The process is isothermal", "Absolute zero is approached"], 1),
        ("For radiation, a surface with low emissivity is most effective at reducing heat transfer when it faces:",
         ["A solid conductor", "An air gap or vacuum", "A high-conductivity metal", "A phase-change material"], 1),
        ("In the derivation of Carnot efficiency, the key step that produces η = 1 − TC/TH is the recognition that for the reversible cycle:",
         ["QH/TH = QC/TC", "QH = QC", "W = QH", "ΔS_universe > 0"], 0),
        ("The Gibbs phase rule F = C − P + 2 implies that at a triple point of a pure substance the system is:",
         ["Bivariant", "Univariant", "Invariant", "Trivariant"], 2),
        ("When using the Clausius-Clapeyron equation, the approximation that ΔH is constant is most reasonable over:",
         ["Very large temperature ranges", "Narrow temperature ranges", "Only at the critical point", "Only for solids"], 1),
        ("In Newton cooling analysis, a sudden increase in air speed over an object primarily increases:",
         ["Thermal conductivity k", "The convection coefficient h", "The specific heat c", "The latent heat"], 1),
        ("If a calorimeter’s heat capacity is ignored when calculating the specific heat of a hot object, the calculated value is usually:",
         ["Too high", "Too low", "Unaffected", "Randomly wrong"], 1),
        ("The statement “an adiabatic process is isentropic” is true only when the process is also:",
         ["Isothermal", "Reversible", "Isobaric", "Irreversible"], 1),
        ("For a cyclic device operating between two reservoirs, the equality ΔS_reservoirs = 0 holds only for:",
         ["Any real engine", "A reversible engine", "A refrigerator", "A heat pump with COP > 1"], 1),
    ]
}

# ====================== UI CLASSES ======================

class AnswerButton(Button):
    def __init__(self, label: str, index: int, correct_index: int, options: list):
        super().__init__(label=label, style=discord.ButtonStyle.secondary)
        self.index = index
        self.correct_index = correct_index
        self.options = options

    async def callback(self, interaction: discord.Interaction):
        view: QuestionView = self.view
        if view.answered:
            await interaction.response.send_message("This question has already been answered.", ephemeral=True)
            return

        view.answered = True
        selected = chr(65 + self.index)
        correct = chr(65 + self.correct_index)

        # Disable all buttons
        for item in view.children:
            item.disabled = True
            if isinstance(item, AnswerButton):
                if item.index == self.correct_index:
                    item.style = discord.ButtonStyle.success
                elif item.index == self.index:
                    item.style = discord.ButtonStyle.danger

        if self.index == self.correct_index:
            msg = f"✅ **Correct!**\nYou selected **{selected}) {self.options[self.index]}**"
        else:
            msg = (f"❌ **Wrong.**\n"
                   f"You selected **{selected}) {self.options[self.index]}**\n"
                   f"Correct answer: **{correct}) {self.options[self.correct_index]}**")

        await interaction.response.send_message(msg, ephemeral=True)

        # Update public message
        embed = interaction.message.embeds[0]
        embed.set_footer(text=f"Answered by {interaction.user.display_name}")
        await interaction.message.edit(view=view)


class QuestionView(View):
    def __init__(self, correct_index: int, options: list, owner_id: int):
        super().__init__(timeout=120)
        self.correct_index = correct_index
        self.options = options
        self.owner_id = owner_id
        self.answered = False

        for i, letter in enumerate(["A", "B", "C", "D"]):
            self.add_item(AnswerButton(letter, i, correct_index, options))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who requested this question can answer it.", ephemeral=True
            )
            return False
        return True


class DifficultySelect(Select):
    def __init__(self, owner_id: int):
        self.owner_id = owner_id
        options = [
            discord.SelectOption(label="Novice", description="Fundamentals", emoji="🟢"),
            discord.SelectOption(label="Intermediate", description="Solid intermediate", emoji="🟡"),
            discord.SelectOption(label="Hard", description="Advanced", emoji="🟠"),
            discord.SelectOption(label="Very Hard", description="Very challenging", emoji="🔴"),
            discord.SelectOption(label="Impossible", description="Brutal", emoji="🟣"),
        ]
        super().__init__(placeholder="Choose difficulty...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who ran the command can choose the difficulty.", ephemeral=True
            )
            return

        difficulty = self.values[0]
        q_text, options, correct = random.choice(QUESTIONS[difficulty])

        embed = discord.Embed(
            title=f"🔥 HeatSO Thermodynamics — {difficulty}",
            description=q_text,
            color=0xE85D04
        )
        option_text = "\n".join(f"**{chr(65+i)})** {opt}" for i, opt in enumerate(options))
        embed.add_field(name="Options", value=option_text, inline=False)
        embed.set_footer(text="(Only the user who requested the question can answer this question)")

        view = QuestionView(correct, options, interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)


class DifficultyView(View):
    def __init__(self, owner_id: int):
        super().__init__(timeout=60)
        self.owner_id = owner_id
        self.add_item(DifficultySelect(owner_id))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.owner_id:
            await interaction.response.send_message(
                "Only the person who used the command can select a difficulty.", ephemeral=True
            )
            return False
        return True


# ====================== BOT ======================

class ThermoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


client = ThermoBot()


@client.tree.command(name="thermo", description="Get a thermodynamics question")
async def thermo(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 HeatSO Thermodynamics",
        description="Select a difficulty:",
        color=0xE85D04
    )
    await interaction.response.send_message(embed=embed, view=DifficultyView(interaction.user.id))


@client.tree.command(name="random", description="Alias for /thermo")
async def random_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔥 HeatSO Thermodynamics",
        description="Select a difficulty:",
        color=0xE85D04
    )
    await interaction.response.send_message(embed=embed, view=DifficultyView(interaction.user.id))


client.run(os.getenv("DISCORD_TOKEN"))