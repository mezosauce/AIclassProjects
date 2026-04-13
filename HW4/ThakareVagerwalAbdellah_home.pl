% Smart Home Fault Diagnosis Model (ProbLog)
% This program models the probabilistic relationships between device failures and observed symptoms.

% --- Probabilistic Facts: Component Failures ---
% These represent the prior probability that a specific component is in a failed state.
0.05::faulty_motion_sensor(living_room). 
0.05::faulty_motion_sensor(hallway).
0.02::faulty_light_sensor.
0.03::faulty_temp_sensor.
0.01::faulty_thermostat.
0.01::power_failure.

% --- Environmental Facts (World State) ---
% These represent the actual state of the world. In a diagnostic scenario, 
% we assume these are the intended or actual conditions.
movement(living_room).
movement(hallway).
light_switch_on.
thermostat_calls_heat.
temp_read_requested.

% --- Observation Rules ---
% These rules define how sensors and systems behave based on their health and the world state.

% Motion is reported only if the sensor is NOT faulty AND there is genuine movement.
motion_detected(Room) :-
    not(faulty_motion_sensor(Room)),
    movement(Room).

% Light is reported as ON only if the light sensor is NOT faulty AND the switch is ON.
light_on :-
    not(faulty_light_sensor),
    light_switch_on.

% Heating is ON only if the thermostat is NOT faulty, there is NO power failure,
% and the thermostat is actually calling for heat.
heating_on :-
    not(faulty_thermostat),
    not(power_failure),
    thermostat_calls_heat.

% A temperature reading is valid only if the sensor is NOT faulty.
temp_reading_valid :-
    not(faulty_temp_sensor),
    temp_read_requested.

% --- Diagnostic Rules ---
% These rules help identify failure modes or aggregate symptoms for easier querying.

% A sensor is considered "silent" when it is faulty.
sensor_silent(motion, Room) :- faulty_motion_sensor(Room).
sensor_silent(light)        :- faulty_light_sensor.
sensor_silent(temp)         :- faulty_temp_sensor.

% Heating is unavailable if either the thermostat is faulty OR there is a power failure.
no_heating :- faulty_thermostat.
no_heating :- power_failure.

% Lights are "stuck off" if the switch is on but the sensor doesn't report light.
lights_stuck_off :-
    light_switch_on,
    not(light_on).

% Motion is not reported despite real movement (indicates a sensor issue).
motion_not_reported(Room) :-
    movement(Room),
    not(motion_detected(Room)).

% --- Evidence Scenarios ---
% To generate results for your report, uncomment ONE scenario at a time and run ProbLog.

% Scenario 1: Basic Sensor Fault (Motion sensors report nothing despite movement)
evidence(motion_detected(living_room), false).
evidence(motion_detected(hallway), false).

% Scenario 2: Potential Power Outage (Multiple unrelated systems failing)
% evidence(heating_on, false).
% evidence(light_on, false).

% Scenario 3: Isolated Heating Issue (Power is fine, but no heat)
% evidence(heating_on, false).
% evidence(light_on, true).

% Scenario 4: Sensor Inconsistency (Light switch is on, but light is off)
% evidence(light_on, false).
% evidence(light_switch_on, true).


% --- Queries ---
% These calculate the probability of each fault given the evidence above.

% Direct Fault Diagnosis
query(faulty_motion_sensor(living_room)).
query(faulty_motion_sensor(hallway)).
query(faulty_light_sensor).
query(faulty_thermostat).
query(faulty_temp_sensor).
query(power_failure).

% Symptom Analysis
query(no_heating).
query(lights_stuck_off).
query(temp_reading_valid).
