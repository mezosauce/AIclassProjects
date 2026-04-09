% Model Smart home system to Define Probablistic facts that includes all devices
% •	Motion sensors in the living room and hallway: they report if motion detected or not
% •	Light sensors:  they report if the light is on or off.
% •	Temperature sensor:  Occasionally it may fail.
% •	Thermostat: can fail to turn on the heating system.
% •	Power supply: can occasionally be unstable

% Instruments: 
motion_sensor(living_room, detected).
motion_sensor(hallway, detected).
light_sensor(living_room, on).
temperature_sensor(failed).
thermostat(failed).
power_supply(unstable).

% Probablistic Facts
movement(living_room).
movement(hallway).


light_switch_on.

% The thermostat is set to call for heat (setpoint > room temp)
thermostat_calls_heat.

% A valid temperature reading is expected
temp_read_requested.

% Probablistic Facts for device failures

0.05::faulty_motion_sensor(living_room). 
0.05::faulty_motion_sensor(hallway).
0.02::faulty_light_sensor.
0.03::faulty_temp_sensor.
0.01::faulty_thermostat.
0.01::power_failure.


% Rules Sets
motion_detected(Room) :- 
	not(faulty_motion_sensor(Room)), 
	movement(Room).

light_on :- 
	not(faulty_light_sensor), 
	light_switch_on.

heating_on :- 
	not(faulty_thermostat), 
	not(power_failure).


% Observation Rule Sets

% Motion is reported in Room only if the sensor isn't faulty
% and there is genuine movement.
motion_detected(Room) :-
    \+ faulty_motion_sensor(Room),
    movement(Room).

% Light appears on only if the light sensor isn't faulty
% and the switch is physically on.
light_on :-
    \+ faulty_light_sensor,
    light_switch_on.

% Heating activates only if the thermostat isn't faulty,
% there is no power failure, and the thermostat is calling for heat.
heating_on :-
    \+ faulty_thermostat,
    \+ power_failure,
    thermostat_calls_heat.

% A temperature reading is valid only if the sensor isn't faulty.
temp_reading_valid :-
    \+ faulty_temp_sensor,
    temp_read_requested.

% A sensor is "silent" (no reading at all) when it is faulty.
sensor_silent(motion, Room) :-
    faulty_motion_sensor(Room).

sensor_silent(light) :-
    faulty_light_sensor.

sensor_silent(temp) :-
    faulty_temp_sensor.



% Useful for diagnosing why heating or lighting failed entirely.

% Heating is unavailable for ANY of these reasons:
no_heating :-
    faulty_thermostat.
no_heating :-
    power_failure.

% Lights are off despite the switch being on → sensor fault
lights_stuck_off :-
    light_switch_on,
    \+ light_on.

% Motion never detected in a room despite real movement → sensor fault
motion_not_reported(Room) :-
    movement(Room),
    \+ motion_detected(Room).

% Evidence 
evidence(motion_detected(living_room), false).
evidence(motion_detected(hallway), false).


% Queries
query(no_heating).
query(lights_stuck_off).
query(motion_not_reported(living_room)).
query(sensor_silent(light)).
query(faulty_motion_sensor(living_room)).
query(power_failure).
query(faulty_light_sensor).
