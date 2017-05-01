% PuzzlOR December 2016 - Galaxy on fire

% variables

var 1..350: c; % Cargo
var 1..60: w; % Weapon
var 1..8: e; % equipment


% constraints
constraint 25*c + 2*w + 6*e >=51975;
constraint 350*c + 0*w + 8*e >=168900;
constraint 38*c + 4*w + 5*e >=235600;
constraint 28*c + 2*w + 8*e >=171900;
constraint 45*c + 2*w + 7*e >=150000;
constraint 80*c + 2*w + 8*e >=250000;
constraint 60*c + 4*w + 6*e >=294900;
constraint 50*c + 3*w + 5*e >=100100;
constraint 65*c + 2*w + 7*e >=125400;
constraint 30*c + 2*w + 6*e >=72500;



% objective function
% solve maximize 0.25*a + 0.15*b + 0.1*c + 0.09*d + 0.03*e + 0.04*f + 0.02*g + 0.04*h;

solve minimize c + w + e;

% output
output ["Cargo = ", show(c), "\n",
        "Weapon = ", show(w), "\n",
        "Equipment = ",show(e),"\n",
        "Cicero = ", show(25*c+2*w+6*e),"\n",
        "Cormorant = ", show(350*c+0*w+8*e),"\n",
        "Dace = ", show(38*c+4*w+5*e),"\n",
        "Hatsuyuki = ", show(28*c+2*w+8*e),"\n",
        "HSoc   = ", show(45*c+2*w+7*e),"\n",
        "NTirrk = ", show(80*c+2*w+8*e),"\n",
        "Razor6 = ", show(60*c+4*w+6*e),"\n",
        "Taipan = ", show(50*c+3*w+5*e),"\n",
        "Teneta = ", show(65*c+2*w+7*e),"\n",
        "Type43 = ", show(30*c+2*w+6*e),"\n",
        "Max val = ",show(c + w + e),"\n"]