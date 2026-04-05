---
title: "¡Al fin! Ya Puedes Desbloquear tu hoja Excel."
snippet: ""
cluster: false
draft: false
description: "Desbloquear una hoja de Exel con contraseña puede ser difícil.. ¡Si no sabes la contraseña! ¿Solución? Entérate aquí."
publishDate: "2014-03-17"
category: "Herramientas en Excel"
tags:
  ["Macros (VBA)", "Seguridad", "Trucos Excel", "🤖 Automatización con Excel"]
images: []
resources:
  - name: "featured-image"
image:
  {
    src: "/src/assets/images/2023/ry-portada-generica.png",
    alt: "Raymundo Ycaza",
  }
cover: "/src/assets/images/2023/ry-portada-generica.png"
featuredImage: "images/ry-portada-generica.png"
coverAlt: "Raymundo Ycaza"
domainGroup: automatizacion-con-excel
slug: automatizacion-con-excel/desbloquear
---

Editado el: 17/3/2014

¿Te ha pasado que el anterior empleado dejó una planilla de Excel que hacía varios cálculos, pero la hoja está **bloqueada con contraseña**? Seguramente has tratado de adivinarla, incluso de contactar a esa persona para poder usar tu tan preciado formato y no tener que hacerlo todo de nuevo.

Sin embargo, **existe una solución** al alcance de todos. No es necesario invertir dinero en un programa especializado para poder recuperar el control de tu archivo.

Con estos 8 pasos podrás **desbloquear tu archivo hoja en 5 minutos** (o menos)

##  Desbloquear la hoja de Excel

1. Pincha con el botón derecho del mouse sobre el nombre de la hoja que pretendes desbloquear y selecciona la opción "Ver Código" o accede directamente al editor de VBA, (http://raymundoycaza.com/escribe-tu-primera-macro-en-excel/ "#03 Escribe tu primera Macro en Excel.")\ ALT + F11\
2. En la nueva ventana que se abrió, puedes hacer un doble clic sobre el nombre de la hoja que quieres desbloquear.
3. Una vez hecho esto, en la parte derecha, en la zona blanca, pega el código que te proporciono al final de la presente entrada.
4. Cierra la ventana, pues hemos terminado con esta parte y ya puedes volver a tu hoja de Excel.
5. En la cinta, selecciona la opción View (Ver)
6. Dirígete a la opción de Macros y selecciona View Macros (Ver Macros)
7. La macro ‘DesbloquearHoja’ debe aparecer listada en el cuadro de diálogo que se muestra. Lo que vas a hacer será seleccionarla y pinchar en el botón Run (Ejecutar)
8. Dentro de unos instantes (generalmente demora muy poco) te aparecerá un mensaje como el de la siguiente imagen. No te preocupes por la contraseña que muestra, lo importante es que ha conseguido desbloquear tu hoja y está lista para que la guardes en un lugar seguro.¡Listo! Esa hoja que tenías guardada por ahí durante tanto tiempo ahora está operativa nuevamente. ¿No te esperabas que fuera tan sencillo, verdad?

\Lo que te explico en esta entrada solo te sirve para desbloquear HOJAS que están protegidas con contraseña. Para desbloquear LIBROS o ARCHIVOS que están bloqueados, deberás usar otra solución.\

## El código

A continuación te dejo el código que debes pegar en la ventana del editor de Visual Basic. Cópialo tal cual lo tienes dentro del siguiente recuadro y pégalo donde corresponde, siguiendo las instrucciones.

Option Explicit

Sub DesbloquearHoja()

Dim Contrasenia As String
Dim a As Integer, b As Integer, c As Integer
Dim d As Integer, e As Integer, f As Integer
Dim a1 As Integer, a2 As Integer, a3 As Integer
Dim a4 As Integer, a5 As Integer, a6 As Integer
On Error Resume Next

For a \= 65 To 66: For b \= 65 To 66: For c \= 65 To 66
For d \= 65 To 66: For e \= 65 To 66: For a1 \= 65 To 66
For a2 \= 65 To 66: For a3 \= 65 To 66: For a4 \= 65 To 66
For a5 \= 65 To 66: For a6 \= 65 To 66: For f \= 32 To 126

Contrasenia \= Chr(a) & Chr(b) & Chr(c) & Chr(d) & Chr(e) & Chr(a1) \_
& Chr(a2) & Chr(a3) & Chr(a4) & Chr(a5) & Chr(a6) & Chr(f)

ActiveSheet.Unprotect Contrasenia
If ActiveSheet.ProtectContents \= False Then
MsgBox "¡Lo he logrado!" & vbCr & \_
"La Contraseña es:" & vbCr & Contrasenia
Exit Sub
End If
Next: Next: Next: Next: Next: Next
Next: Next: Next: Next: Next: Next

End Sub

## El secreto ha sido revelado

Ahora que ya sabes el secreto, haz el bien. Que esto te sirva también para que hagas conciencia del nivel de seguridad que te da un sencillo bloqueo a nivel de hoja.

Generalmente, este tipo de protección la debemos destinar para uso interno de la empresa, como por ejemplo enviar listados, informes, requisiciones, etc. donde la seguridad no juega un papel crítico.

\La finalidad de la protección a nivel de hoja, es evitar las alteraciones por acciones involuntarias del usuario. En ningún momento debe considerarse una medida de seguridad propiamente dicha ya que, como has visto, cualquiera puede saltarse esta protección.\

## ¿Y tú, ya usas este método?

Yo ya he contado mi parte, ahora te toca a ti. Cuéntame acerca de tu experiencia con los bloqueos a nivel de hoja en Excel. ¿Ya has usado antes esta técnica?

Seguramente has pasado alguna vez por esta situación y tu experiencia enriquecería la conversación.

¡Nos vemos!

\

\