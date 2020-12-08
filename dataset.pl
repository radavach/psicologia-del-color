:- dynamic personaje_disponible/2, personaje_asignado/2, personaje_objetivo/2, preguntas/4, caracteristicas/1, caracteristica/3.

caracteristicas(cabello).
caracteristicas(ojos).
caracteristicas(sexo).
caracteristicas(lentes).
caracteristicas(estado_animo).

personaje(mario).
personaje(alberto).
personaje(jose).
personaje(ramon).
personaje(eduardo).
personaje(daniel).
personaje(pedro).
personaje(pablo).
personaje(luis).
personaje(gabriel).
personaje(juan).
personaje(carlos).
personaje(nancy).
personaje(scarlet).
personaje(salma).
personaje(susana).
personaje(michelle).
personaje(mayra).
personaje(cristina).
personaje(carmen).
personaje(margot).
personaje(elise).
personaje(grace).
personaje(nora).

personaje_disponible(jugador1, mario).
personaje_disponible(jugador1, alberto).
personaje_disponible(jugador1, jose).
personaje_disponible(jugador1, ramon).
personaje_disponible(jugador1, eduardo).
personaje_disponible(jugador1, daniel).
personaje_disponible(jugador1, pedro).
personaje_disponible(jugador1, pablo).
personaje_disponible(jugador1, luis).
personaje_disponible(jugador1, gabriel).
personaje_disponible(jugador1, juan).
personaje_disponible(jugador1, carlos).
personaje_disponible(jugador1, nancy).
personaje_disponible(jugador1, scarlet).
personaje_disponible(jugador1, salma).
personaje_disponible(jugador1, susana).
personaje_disponible(jugador1, michelle).
personaje_disponible(jugador1, mayra).
personaje_disponible(jugador1, cristina).
personaje_disponible(jugador1, carmen).
personaje_disponible(jugador1, margot).
personaje_disponible(jugador1, elise).
personaje_disponible(jugador1, grace).
personaje_disponible(jugador1, nora).

personaje_disponible(jugador2, mario).
personaje_disponible(jugador2, alberto).
personaje_disponible(jugador2, jose).
personaje_disponible(jugador2, ramon).
personaje_disponible(jugador2, eduardo).
personaje_disponible(jugador2, daniel).
personaje_disponible(jugador2, pedro).
personaje_disponible(jugador2, pablo).
personaje_disponible(jugador2, luis).
personaje_disponible(jugador2, gabriel).
personaje_disponible(jugador2, juan).
personaje_disponible(jugador2, carlos).
personaje_disponible(jugador2, nancy).
personaje_disponible(jugador2, scarlet).
personaje_disponible(jugador2, salma).
personaje_disponible(jugador2, susana).
personaje_disponible(jugador2, michelle).
personaje_disponible(jugador2, mayra).
personaje_disponible(jugador2, cristina).
personaje_disponible(jugador2, carmen).
personaje_disponible(jugador2, margot).
personaje_disponible(jugador2, elise).
personaje_disponible(jugador2, grace).
personaje_disponible(jugador2, nora).

caracteristica(cabello, mario, rojo).
caracteristica(cabello,alberto, rubio).
caracteristica(cabello,jose, negro).
caracteristica(cabello,ramon, rubio).
caracteristica(cabello,eduardo, rubio).
caracteristica(cabello,daniel, negro).
caracteristica(cabello,pedro, negro).
caracteristica(cabello,pablo, negro).
caracteristica(cabello,luis, negro).
caracteristica(cabello,gabriel, negro).
caracteristica(cabello,juan, rojo).
caracteristica(cabello,carlos, rojo).

caracteristica(cabello,nancy, negro).
caracteristica(cabello,scarlet, rubio).
caracteristica(cabello,salma, negro).
caracteristica(cabello,susana, negro).
caracteristica(cabello,michelle, negro).
caracteristica(cabello,mayra, negro).
caracteristica(cabello,cristina, rubio).
caracteristica(cabello,carmen, rojo).
caracteristica(cabello,margot, rubio).
caracteristica(cabello,elise, rojo).
caracteristica(cabello,grace, rubio).
caracteristica(cabello,nora, negro).

caracteristica(ojos,mario, azules).
caracteristica(ojos,alberto, verdes).
caracteristica(ojos,jose, cafes).
caracteristica(ojos,ramon, cafes).
caracteristica(ojos,eduardo, verdes).
caracteristica(ojos,daniel, cafes).
caracteristica(ojos,pedro, cafes).
caracteristica(ojos,pablo, cafes).
caracteristica(ojos,luis, verdes).
caracteristica(ojos,gabriel, cafes).
caracteristica(ojos,juan, verdes).
caracteristica(ojos,carlos, verdes).

caracteristica(ojos,nancy, cafes).
caracteristica(ojos,scarlet, azules).
caracteristica(ojos,salma, cafes).
caracteristica(ojos,susana, azules).
caracteristica(ojos,michelle, azules).
caracteristica(ojos,mayra, cafes).
caracteristica(ojos,cristina, verdes).
caracteristica(ojos,carmen, verdes).
caracteristica(ojos,margot, azules).
caracteristica(ojos,elise, verdes).
caracteristica(ojos,grace, grises).
caracteristica(ojos,nora, cafes).

caracteristica(sexo,mario, hombre).
caracteristica(sexo,alberto, hombre).
caracteristica(sexo,jose, hombre).
caracteristica(sexo,ramon, hombre).
caracteristica(sexo,eduardo, hombre).
caracteristica(sexo,daniel, hombre).
caracteristica(sexo,pedro, hombre).
caracteristica(sexo,pablo, hombre).
caracteristica(sexo,luis, hombre).
caracteristica(sexo,gabriel, hombre).
caracteristica(sexo,juan, hombre).
caracteristica(sexo,carlos, hombre).

caracteristica(sexo,nancy, mujer).
caracteristica(sexo,scarlet, mujer).
caracteristica(sexo,salma, mujer).
caracteristica(sexo,susana, mujer).
caracteristica(sexo,michelle, mujer).
caracteristica(sexo,mayra, mujer).
caracteristica(sexo,cristina, mujer).
caracteristica(sexo,carmen, mujer).
caracteristica(sexo,margot, mujer).
caracteristica(sexo,elise, mujer).
caracteristica(sexo,grace, mujer).
caracteristica(sexo,nora, mujer).

caracteristica(lentes,mario, no).
caracteristica(lentes,alberto, si).
caracteristica(lentes,jose, no).
caracteristica(lentes,ramon, si).
caracteristica(lentes,eduardo, si).
caracteristica(lentes,daniel, no).
caracteristica(lentes,pedro, no).
caracteristica(lentes,pablo, no).
caracteristica(lentes,luis, no).
caracteristica(lentes,gabriel, no).
caracteristica(lentes,juan, no).
caracteristica(lentes,carlos, no).

caracteristica(lentes,nancy, si).
caracteristica(lentes,scarlet, no).
caracteristica(lentes,salma, si).
caracteristica(lentes,susana, si).
caracteristica(lentes,michelle, si).
caracteristica(lentes,mayra, si).
caracteristica(lentes,cristina, no).
caracteristica(lentes,carmen, no).
caracteristica(lentes,margot, no).
caracteristica(lentes,elise, no).
caracteristica(lentes,grace, no).
caracteristica(lentes,nora, si).

caracteristica(estado_animo,mario, triste).
caracteristica(estado_animo,alberto, feliz).
caracteristica(estado_animo,jose, feliz).
caracteristica(estado_animo,ramon, enojado).
caracteristica(estado_animo,eduardo, triste).
caracteristica(estado_animo,daniel, enojado).
caracteristica(estado_animo,pedro, triste).
caracteristica(estado_animo,pablo, triste).
caracteristica(estado_animo,luis, feliz).
caracteristica(estado_animo,gabriel, feliz).
caracteristica(estado_animo,juan, feliz).
caracteristica(estado_animo,carlos, triste).

caracteristica(estado_animo,nancy, enojado).
caracteristica(estado_animo,scarlet, enojado).
caracteristica(estado_animo,salma, feliz).
caracteristica(estado_animo,susana, triste).
caracteristica(estado_animo,michelle, triste).
caracteristica(estado_animo,mayra, enojado).
caracteristica(estado_animo,cristina, enojado).
caracteristica(estado_animo,carmen, enojado).
caracteristica(estado_animo,margot, triste).
caracteristica(estado_animo,elise, enojado).
caracteristica(estado_animo,grace, feliz).
caracteristica(estado_animo,nora, feliz).