categoria_color(primario, [rojo,azul,amarillo]).
categoria_color(secundario, [verde,naranja,violeta]).
categoria_color(neutral, [blanco,negro,gris,plateado,marron]).
categoria_color(calido, [rojo,amarillo,naranja,dorado,rosa]).
categoria_color(frio, [verde,azul,violeta]).

publico_objetivo("1-18", a).
publico_objetivo("19-24", b).
publico_objetivo("25-35", c).
publico_objetivo("36-50", d).
publico_objetivo("51-69", e).
publico_objetivo("70+", f).

color_fav_publico(a, [rojo,rosa,azul,verde,naranja,violeta]).
color_fav_publico(b, [rojo,rosa,azul,amarillo,dorado,verde,naranja,violeta,marron,blanco]).
color_fav_publico(c, [rojo,rosa,azul,verde,naranja,violeta,marron,negro]).
color_fav_publico(d, [azul,amarillo,dorado,verde,naranja,violeta,negro]).
color_fav_publico(e, [rojo,rosa,azul,amarillo,dorado,naranja,violeta,gris,plateado,marron]).
color_fav_publico(f, [azul,blanco]).

sentimientos_positivos([confianza,serenidad,inteligencia,armonia,seguridad,serenidad,fidelidad,comunicacion,eficiencia,sinceridad,logica,reflexion,responsabilidad,calma,verdad], azul).
sentimientos_positivos([masculinidad,calor,pasion,vitalidad,atrevimiento,importancia,fuerza,exitacion,exuberancia,osadia], rojo).
sentimientos_positivos([amabilidad,felicidad,inteligencia,autoestima,amistad,alentador,extroversion,advertencia,tibieza,caluroso,precaucion,velocidad,innovacion], amarillo).
sentimientos_positivos([restauracion,naturaleza,conciencia,salud,armonia,paz,moderacion,organico,ecuanimidad,equilibrio], verde).
sentimientos_positivos([calidez,energia,confort,vitalidad,comida,diversion,entusiasmo,seguridad,creatividad,jugueton], naranja).
sentimientos_positivos([espiritualismo,serenidad,vision,verdad,autenticidad,lujo,misterio,creatividad], violeta).
sentimientos_positivos([lujo,fortaleza,vida,poder,felicidad,riqueza,abundancia,ambicion], dorado).
sentimientos_positivos([sabiduria,paz,elegancia,tenacidad,creatividad,profesionalidad,magia,exito], plateado).
sentimientos_positivos([sabiduria,sobriedad,estabilidad,imparcialidad,seguridad,practicidad,modestia,honradez], gris).
sentimientos_positivos([honestidad,practicidad,comodidad,objetividad,nobleza,acogedor,simplicidad,estabilidad], marron).
sentimientos_positivos([esterilidad,pureza,elegancia,limpieza,inocencia,fe,simplicidad,optimismo,perfeccion,sofisticacion,virtuoso,claridad,juventud], blanco).
sentimientos_positivos([glamour,silencio,sustancia,elegancia,poder,sofisticacion,proteccion], negro).
sentimientos_positivos([inocencia,amor,generosidad,entrega,sensibilidad], rosa).

sentimientos_negativos([frialdad,aficcion,distanciamiento,pesadumbre,desinteres,depresion], azul).
sentimientos_negativos([tension,desafio,impacto,agresividad], rojo).
sentimientos_negativos([agotamiento,miedo,ansiedad,irracionalidad,fragilidad], amarillo).
sentimientos_negativos([aburrimiento,estancamiento,enervacion], verde).
sentimientos_negativos([privacion,ansiedad,frustracion,frivolidad,inmadurez], naranja).
sentimientos_negativos([negatividad,supresion,jaqueca,introversion,decadencia], violeta).
sentimientos_negativos([vanidad,falsedad,fuerte], dorado).
sentimientos_negativos([frialdad,traicion,avaricia,prepotencia,vertido], plateado).
sentimientos_negativos([vejez,tristeza,conformismo,aburrimiento,mediocridad,inseguridad,crisis], gris).
sentimientos_negativos([antipatico,necedad,antieroico,pereza,desagradable,comun,vulgaridad,anticuado], marron).
sentimientos_negativos([elitismo,vulnerabilidad,frialdad,vacio,antipatia,debilidad], blanco).
sentimientos_negativos([distante,pesadez,intimidatorio,frialdad,opresion,amenaza], negro).
sentimientos_negativos([debil,ingenuidad,vulnerable,inmadurez,tonto,discriminacion,fantasia], rosa).

armonia(rojo, ["FF530D","E82C0C","FF0000","E80C7A","FF0DFF"], analogo).
armonia(rojo, ["800000","FF4D4D","FF0000","802626","CC0000"], monocromatico).
armonia(rojo, ["B31212","FFFC19","FF0000","19A6FF","0971B3"], triada).
armonia(rojo, ["B30000","FF1919","FF0000","00B333","00FF48"], complementario).
armonia(rojo, ["4AB312","61FF0D","FF0000","12B319","0DFFDA"], separacion_complementaria).
armonia(rojo, ["FF530D","6AFF19","FF0000","19FFDC","FF0DFF"], doble_separacion_complementaria).
armonia(rojo, ["FF1919","FFCE19","FF0000","FF195A","0D22FF"], cuadro).

armonia(azul, ["910DFF","480DE8","0000FF","0C46E8","0D8CFF"], analogo).
armonia(azul, ["000080","4D4DFF","0000FF","262680","0000CC"], monocromatico).
armonia(azul, ["1212B3","FF6819","0000FF","4FFF19","30B309"], triada).
armonia(azul, ["0000B3","1919FF","0000FF","B39200","FFD100"], complementario).
armonia(azul, ["B37512","FFA20D","0000FF","A7B312","EEFF0D"], separacion_complementaria).
armonia(azul, ["910DFF","FFA719","0000FF","EFFF19","0D8CFF"], doble_separacion_complementaria).
armonia(azul, ["1919FF","FF2519","0000FF","FFD519","0DFF68"], cuadro).

armonia(verde, ["0DFF96","0CE84A","00FF00","59E80C","B6FF0D"], analogo).
armonia(verde, ["008000","4DFF4D","00FF00","268026","00CC00"], monocromatico).
armonia(verde, ["12B312","4319FF","00FF00","FF7E19","B35309"], triada).
armonia(verde, ["00B300","19FF19","00FF00","B30059","FF0080"], complementario).
armonia(verde, ["8712B3","BD0DFF","00FF00","B32912","FF300D"], separacion_complementaria).
armonia(verde, ["0DFF96","C019FF","00FF00","FF3B19","B6FF0D"], doble_separacion_complementaria).
armonia(verde, ["19FF19","196AFF","00FF00","FF198C","FFB20D"], cuadro).

armonia(rosa, ["FF300D","E80C0C","FF0080","E80CE8","BD0DFF"], analogo).
armonia(rosa, ["800040","FF4DA6","FF0080","802653","CC0066"], monocromatico).
armonia(rosa, ["B31262","FFE519","FF0080","19E3FF","099EB3"], triada).
armonia(rosa, ["B30059","FF198C","FF0080","00B300","00FF00"], complementario).
armonia(rosa, ["82B312","B6FF0D","FF0080","12B36D","0DFF96"], separacion_complementaria).
armonia(rosa, ["FF300D","BAFF19","FF0080","19FF9B","BD0DFF"], doble_separacion_complementaria).
armonia(rosa, ["FF198C","FFB719","FF0080","FF0080","0D22FF"], cuadro).

armonia(marron, ["8C6807","966108","804000","963A08","8C2307"], analogo).
armonia(marron, ["CC6600","95612D","804000","CC853D","4D2600"], monocromatico).
armonia(marron, ["331C05","0D801B","804000","2F0D80","110333"], triada).
armonia(marron, ["331A00","CC7014","804000","002733","006180"], complementario).
armonia(marron, ["14CC93","06805A","804000","1440CC","062380"], separacion_complementaria).
armonia(marron, ["805E06","0D805C","804000","0D2880","802006"], doble_separacion_complementaria).
armonia(marron, ["80460D","4C800D","804000","0D6480","6D0680"], cuadro).

armonia(amarillo, ["56FF0D","9BE80C","FFFF00","E8D20C","FFCE0D"], analogo).
armonia(amarillo, ["808000","FFFF4D","FFFF00","808026","CCCC00"], monocromatico).
armonia(amarillo, ["B3B312","199EFF","FFFF00","FF1E19","B30C09"], triada).
armonia(amarillo, ["B3B300","FFFF19","FFFF00","5800B3","7F00FF"], complementario).
armonia(amarillo, ["121AB3","0D1AFF","FFFF00","B312A8","FF0DEF"], separacion_complementaria).
armonia(amarillo, ["56FF0D","1926FF","FFFF00","FF19F0","FFCE0D"], doble_separacion_complementaria).
armonia(amarillo, ["FFFF19","19FFE5","FFFF00","8A19FF","FF580D"], cuadro).

armonia(naranja, ["FFBD0D","E8960C","FF8000","E85A0C","FF3F0D"], analogo).
armonia(naranja, ["804000","FFA64D","FF8000","805326","CC6600"], monocromatico).
armonia(naranja, ["B36212","19FF35","FF8000","5E19FF","3C09B3"], triada).
armonia(naranja, ["B35900","FF8C19","FF8000","0088B3","00C3FF"], complementario).
armonia(naranja, ["12B380","0DFFB3","FF8000","1238B3","0D46FF"], separacion_complementaria).
armonia(naranja, ["FFBD0D","19FFB7","FF8000","1950FF","FF3F0D"], doble_separacion_complementaria).
armonia(naranja, ["FF8C19","97FF19","FF8000","19C9FF","D90DFF"], cuadro).

armonia(violeta, ["89258F","742899","4C2882","362899","25348F"], analogo).
armonia(violeta, ["7940CF","745C97","4C2882","9E7ECF","2E194F"], monocromatico).
armonia(violeta, ["1C0B36","826035","4C2882","1B8233","0E3617"], triada).
armonia(violeta, ["1C0B36","8555CD","4C2882","363406","827F28"], complementario).
armonia(violeta, ["CFB255","826E2F","4C2882","70CF2B","4A8222"], separacion_complementaria).
armonia(violeta, ["7E2F82","827035","4C2882","46821B","222F82"], doble_separacion_complementaria).
armonia(violeta, ["441B82","824935","4C2882","827F1B","22826E"], cuadro).

armonia(plateado, ["CCBEB8","D6C4C1","C0C0C0","D6C1CB","CCB8CC"], analogo).
armonia(plateado, ["404040","CA8D8D","C0C0C0","402D2D","8C8C8C"], monocromatico).
armonia(plateado, ["736767","BFBFAC","C0C0C0","ACB8BF","676E73"], triada).
armonia(plateado, ["736767","FFFFFF","C0C0C0","5C7362","BFBFBF"], complementario).
armonia(plateado, ["6B7367","B9BFB6","C0C0C0","677371","ACBFBC"], separacion_complementaria).
armonia(plateado, ["BFB8B6","B3BFAC","C0C0C0","ACBFBC","BFACBF"], doble_separacion_complementaria).
armonia(plateado, ["BFACAC","BFBBAC","C0C0C0","ACBFB2","ACAEBF"], cuadro).

armonia(dorado, ["E0DB2F","EBD231","D4AF37","EBAD31","E0922F"], analogo).
armonia(dorado, ["544616","DBC47B","D4AF37","544C2F","A1852A"], monocromatico).
armonia(dorado, ["876D16","4CD4B8","D4AF37","CB22D4","821C87"], triada).
armonia(dorado, ["B35900","FFD95C","D4AF37","081987","374CD4"], complementario).
armonia(dorado, ["316A87","42A2D4","D4AF37","441687","702CD4"], separacion_complementaria).
armonia(dorado, ["D4CF42","4CA6D4","D4AF37","6A22D4","D48A2C"], doble_separacion_complementaria).
armonia(dorado, ["D4AA22","4CD46C","D4AF37","223AD4","D42C3C"], cuadro).

armonia(gris, ["A89C97","B3A3A1","9B9B9B","B3A1AA","A897A8"], analogo).
armonia(gris, ["E8E8E8","AC7878","9B9B9B","E8A2A2","696969"], monocromatico).
armonia(gris, ["4F4747","9C9B8C","9B9B9B","8C969C","474C4F"], triada).
armonia(gris, ["4F4747","E8E8E8","9B9B9B","3F4F44","9C9C9C"], complementario).
armonia(gris, ["D9E8D1","969C94","9B9B9B","D1E8E5","8C9C99"], separacion_complementaria).
armonia(gris, ["9C9694","919C8C","9B9B9B","8C9C99","9C8C9C"], doble_separacion_complementaria).
armonia(gris, ["9C8C8C","9C988C","9B9B9B","8C9C90","8C8D9C"], cuadro).

armonia(blanco, ["FFEDE6","E8D4DA","FFFFFF","E8DADC","FFE6FF"], analogo).
armonia(blanco, ["808080","FFB3B3","FFFFFF","805959","CCCCCC"], monocromatico).
armonia(blanco, ["B3A1A1","FFFFE6","FFFFFF","E6F5FF","A1ACB3"], triada).
armonia(blanco, ["B3A1A1","FFFFFF","FFFFFF","8FB399","FFFFFF"], complementario).
armonia(blanco, ["A7B3A1","F7FFF2","FFFFFF","A1B3B0","E6FFFFB"], separacion_complementaria).
armonia(blanco, ["FFF6F2","EEFFE6","FFFFFF","E6FFFB","FFE6FF"], doble_separacion_complementaria).
armonia(blanco, ["FFE6E6","FFFAE6","FFFFFF","E6FFED","E6E8FF"], cuadro).

armonia(negro, ["332F2E","332F2E","000000","332E30","332E30"], analogo).
armonia(negro, ["4D4D4D","332424","000000","4D3636","999999"], monocromatico).
armonia(negro, ["4D4545","000000","000000","000000","454A4D"], triada).
armonia(negro, ["4D4545","4D4D4D","000000","3D4D42","000000"], complementario).
armonia(negro, ["484D45","000000","000000","454D4B","000000"], separacion_complementaria).
armonia(negro, ["000000","000000","000000","000000","000000"], doble_separacion_complementaria).
armonia(negro, ["000000","000000","000000","000000","000000"], cuadro).