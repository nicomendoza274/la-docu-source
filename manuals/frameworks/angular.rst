=======
Angular
=======

.. image:: https://angular.io/assets/images/logos/angular/angular.svg
    :width: 400px
    :alt: Logo Angular
    :align: center

.. contents:: Table de contenidos de la pagina
   :depth: 2
   :local:

Que es Angular y porque elegirlo? 
##################################

Angular mas que un framework se considera toda una plataforma, con módulos y paquetes listo para utilizar en una aplicación.

* Forms
* PWA
* Language Services
* Router
* Elements
* CDK
* Universal
* Compiler
* i18n
* Http
* Material
* CLI

Angular se reconocer por tener un gran rendimiento en las aplicaciones. 
También podemos tener aplicaciones multiplataforma (llevándolas a electron, native script, ionic)
Ademas angular tiene una gran comunidad.


Instalación
############

Instalar Node
*************

Para empezar a trabajar con Angular necesitamos tener instalado **Node.js** para ellos podemos ir a `la pagina de node <https://nodejs.org/>`_.
Lo mas recomendable es instalar la ultima version LTS (Long Term Support)

También si necesitamos una version particular podemos instalar una version particular utilizando el software para manejo de versiones **nvm**.

* `Version para Windows <https://github.com/coreybutler/nvm-windows>`_ 
* `Version para linux/mac/WSL <https://github.com/nvm-sh/nvm>`_ 

Luego con el siguiente comando podemos ver que version de node tenemos:

.. code-block:: console

    node -v

También con el siguiente comando podemos ver que version de npm (instalador de paquetes de node) tenemos:

.. code-block:: console

    npm -v


Instalación de angular
***********************

Para instalar el framework de angular tenemos que hacer uso del siguiente comando: 

.. code-block:: console

   npm i -g @angular/cli


.. note::
   Este comando nos instala la ultima version del framework disponible. Si queremos una version en particular podemos utilizar el mismo comando agregando un **@** para especificar la version. **Ejemplo: npm i -g @angular/cli@12.1.2**


Para verificar la version del CLI que tenemos instalada ejecutamos el siguiente comando:

.. code-block:: console

   ng version


Crear una aplicación
#####################

Para crear una aplicación vamos al directorio donde se va a generar la estructura de directorios de angular y usamos el siguiente comando:

.. code-block:: console

   ng new my-project

.. note::
   Especificamos que nuestra aplicación tenga **routing** y elegimos el preprocesador que utilicemos, el mas común es **SCSS**
   Automáticamente angular nos alista un proyecto listo para trabajar.

Luego entramos a la carpeta de nuestro proyecto y ejecutamos el siguiente comando:

.. code-block:: console

   ng serve -o

.. note::
   * Este comando nos genera un servidor de desarrollo en localhost en el puerto 4200 por defecto.
   * La opción -o nos permite abrir el servidor de desarrollo directamente en nuestro navegador predeterminado.
   * La opción --port=3500 nos permite abrir el servidor de desarrollo pero en el puerto 3500.
   * Para matar el proceso de la terminal podemos usar el comando **ctrl + c**.

Si volvemos a Ejecutar el comando ng version dentro de la carpeta de nuestro proyecto obtenemos la información de que dependencia y versiones tiene nuestro proyecto


Estructura de un proyecto en Angular
####################################

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Archivo/ Directorio | Descripción                                                                                                                               |
+=====================+===========================================================================================================================================+
| src/                | Aquí Esta el corazón de la aplicación (Componentes, html, css, routing)                                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| .browserslistrc     | En que versiones del navegador tiene que ser compatibles la aplicación                                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| .editorconfig       | Para escribir reglas de escritores de trabajo en equipo (Plugin editor config)                                                            |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| tsconfig.json      | Configuración de que tiene angular con typescript. Compilación, versiones de typScript, donde transpile los archivos                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| angular.json        | Se puede manejar diferentes ambientes (Staging, QA, Production) También configuraciones de compilación, tamaños de la aplicación, etc     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| karma.conf.json     | Configuración para correr pruebas unitarias.                                                                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| package.json        | Aquí tenemos los scripts, las versiones que estamos manejando                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| .nvm                | Este archivo deberíamos añadir para especificar la version de node que estamos utilizando                                                 |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

Para mejorar la experiencia de desarrollo hay una extension para vscode y otros editores de código llamada `Angular Language Service <https://marketplace.visualstudio.com/items?itemName=Angular.ng-template>`_. 


Conceptos básicos de typescript
################################

TypeScript puede inferir tipos como por ejemplo:

.. code-block:: typescript

   const userName = 'Hola Mundo'

Pero con Typescript puedo asegurarme el tipado de la variable para asegurarme:

.. code-block:: typescript

   const userName: string = 'Hola Mundo'

.. note::
   * Esto evitaría cometer errores de querer agregar a la variable **userName** el valor 1 por ejemplo.
   * El tipado puede corregir hasta el 60% de 🐛bugs que cometemos como desarrolladores. 

También es posible indicar que una variable es de 2 tipos

.. code-block:: typescript

   const userName: string | number = 'Hola Mundo'

También se puede proteger a las funciones con un tipado. Lo cual nos da un feedback temprano de que tipos de valores espera la función: 

.. code-block:: typescript

   const sum = (a: number, b: number) => {
       return a + b
   }

Ademas nos permite crear clases de una manera mas simple pasando de esto:

.. code-block:: typescript

   class Person{
       age: number
       lastName: string

       constructor(age: number, lastName: string){
           this.age = age
           this.lastName = lastName
       } 
   }

   const nico = new Person(28, 'Mendoza')

A esto:

.. code-block:: typescript

   class Person{
       constructor(public age: number, public lastName: string){}
   }

   const nico = new Person(28, 'Mendoza')


Comunicación de datos en Angular
#################################

String Interpolation
********************

Es la forma que nosotros desde nuestra lógica escrita en TypeScript podemos pasar datos a la renderizar a nuestro template. 
Es la forma en que nosotros con doble llaves podemos poner una expresión dentro de ella como una función o una variable que este en TypeScript.

Por ejemplo:

.. code-block:: typescript
   :caption: Código TypeScript

   export class AppComponent {
       name = 'Nicolás'
       age = 18
       url = 'https://angular.io/assets/images/logos/angular/angular.svg'
   }

.. warning::
   Para poder renderizar las variables del TypeScript de nuestro componente tienen que ser de acceso publico 🔓

.. code-block:: html
   :caption: Código HTML

   <h2>{{ 'Hola Mundo '.repeat(5) }}</h2>   
   <p> 3 + 3 =  {{ 3 + 3 }} </p>
   <h3>Hola soy {{ name }} y tengo {{ age }} años</h3>
   <img src={{url}} alt="img">

Property Binding
****************

Es la forma en la que podemos modificar atributos desde el controlador, y mandar a los atributos en el HTML.
Por ejemplo: El tag de una imagen, el href de un link, el estado de un botón

.. code-block:: typescript
   :caption: Código TypeScript

   export class AppComponent {
       name = 'Nicolás'
       age = 18
       url = 'https://angular.io/assets/images/logos/angular/angular.svg'
       btnDisabled = true
   }

.. code-block:: html+ng2
   :caption: Código HTML

   <button [disabled]="btnDisabled"> Enviar </button>
   <input type="text" [value]="name" />
   <progress max="100" [value]="age"></progress>
   <img width="100" [src]="url" alt="img">

.. note::
   El string interpolation nos sirve mas para ingresar contenido como en párrafos, h1, h2, etc.
   El Property Binding son específicamente para propiedades. Es recomendable para valores que no son un string.


Event Binding
*************

Sirve para ejecutar una función que definamos en el componente desde el template.
El evento que queremos capturar esta encerrado entre paréntesis.

.. code-block:: typescript
   :caption: Código TypeScript

   export class AppComponent {
       btnDisabled = true

       toggleButton(){
           this.btnDisabled = ! this.btnDisabled 
       }

       onScroll(event: Event){
           const element = event.target as HTMLElement
           console.log(element.strollTop)
       }

       changeName(event: Event){
           const element = event.target as HTMLInputElement
           this.name = element.value
       }
   }

.. code-block:: scss
   :caption: Código SCSS

   .box{
       height: 200px;
       width: 200px;
       overflow: auto;
       background: red;
   }

.. code-block:: html+ng2
   :caption: Código HTML

   <button [disabled]="btnDisabled"> Enviar </button>
   <button (click)="toggleButton()"> Toggle Button</button>

   <div class="box" (scroll)="onScroll($event)">
    <p>Lorem..</p>
   </div>

   <input type="text" [value]="name" (keyup)=changeName($event) />
   <p>Nombre: {{ name }}</p>

.. note::
   Los eventos que son nativos del html o DOM los enviamos con **$event**

Data Binging
************

Es una fusion entre escuchar un evento con ``Event Binding`` y ``setear una propiedad`` (En angular utilizamos el ``NgModel``)

Sirve mucho para los input, siempre esta pendiente del estado del input, si el campo es valido o no y sincroniza el valor.

También Nos permite saber si una propiedad es valida utilizando un **#template** 

.. code-block:: typescript
   :caption: Código TypeScript
   
   export class AppComponent {
       name = 'Nicolás'
   }
   
.. code-block:: html+ng2
   :caption: Código HTML

   <p>Nombre {{ name }}</p>
   <input type="text" required #nameInput="ngModel" [(ngModel)]="name" ></input>
   <p>Valid: {{ nameInput.valid }}</p>

.. warning::
   Para poder habilitar el **NgModel** tenemos que ir a **app,.modules.ts**, importar el modulo **FormsModule** y colocar lo en el array de imports.

   .. code-block:: typescript
      :caption: Código TypeScript
   
      import { FromsModules } from '@angular/forms'

      @NgModule({
        declarations: [
            AppComponent
        ],
        imports: [
            BrowserModule,
            AppRoutingModule,
            FromsModules
        ],
        providers: [],
        bootstrap: [AppComponent]
      })
   
Estructuras de control en Angular
#################################

ngIf
*****

Tenemos la directiva **ngIf** la cual, si se cumple la condición booleana del contenido, se renderiza el elemento html.

.. code-block:: html+ng2
   :caption: Código HTML

   <p *ngIf="name === 'Nicolas'"></p>

También se puede utilizar else en la condición:

.. code-block:: html+ng2
   :caption: Código HTML

   <p *ngIf="name === 'Nicolas'; else myBlock"></p>

   <ng-template #myBlock>
    <p>Bloque de else</p>
   </ng-template>


ngFor
*****

La directiva **ngFor** la cual nos sirve para iterar un array. También nos permite utilizar el indice o posición de cada elemento del array.

.. code-block:: typescript
   :caption: Código TypeScript
   
   export class AppComponent {
       names: string[] = ['Nicolás', 'Julian', 'Santiago']
   }

.. code-block:: html+ng2
   :caption: Código HTML

   <ul>
    <li *ngFor="let name of names; index as i">
        {{ i }} {{ name }}
    </li>
   </ul>

   <ng-template #myBlock>
    <p>Bloque de else</p>
   </ng-template>

.. note::
   No se pueden iterar objetos, solo se iteran arrays. Si queremos iterar arrays de objetos podemos definir interfaces.


ngSwitch
********

Esta directiva nos sirve para no tener que hacer tantas cadenas de ngIf.
Se escribe como un Data Binding y cada case como una estructura de control.

.. code-block:: html+ng2
   :caption: Código HTML

   <div [ngSwitch]="name">
    <p *ngSwitchCase="'nicolas'">La persona es Nicolas</p>
    <p *ngSwitchCase="'julian'">La person a es Julian</p>
    <p *ngSwitchCase="'camilo'">La person a es Camilo</p>
    <p *ngSwitchDefault>No hace match</p>
   </div>


Estilos en Angular
##################

En angular tenemos un archivo con extension **.scss** donde podemos poner nuestros estilos y utilizarlos en el componente que necesitemos.

.. code-block:: 
   :caption: Código SCSS

   .products--grid {
       display: flex;
       flex-direction: column;
       div {
           img {
               width: 100%;
               border-radius: 10px;
           }
           h2, p{
               margin: 0;
           }
       }
   }

   @media screen and (min-width: 40em){
       products--grid{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            grid-gap: 15px;
       }
   }

.. code-block:: html+ng2
   :caption: Código HTML
   
   <div class="products--grid">
    <div *ngFor="let product of product">
        <img [src]="product.image" alt="img">
        <h2>{{ product.price }}</h2>
        <p>{{ product.name }}</p>
    </div>
   </div>


Dynamic class & Styles
**********************

Para hacer estilos dinámicos necesitamos poner la **Property Binding** class seguida de un punto y el nombre de la clase que queremos añadir si la condición se cumple ``[class.nombre_clase]="condition"``.

.. code-block:: scss
   :caption: Código SCSS

   .message-error {
       background: red;
       color: white;
       opacity: 0;
       transition: all linear .5s;
       &.invalid {
           opacity: 1:
       }

   }

.. code-block:: html+ng2
   :caption: Código HTML

   <input type="text" required #nameInput="ngModel" [(ngModel)]="name">

   <p class="message-error" [class.invalid]="nameInput.invalid" >El campo es requerido</p>


Si queremos modificar el estilo directamente de algo en particular, necesitamos poner una **Property Binding** style seguida de un punto y el nombre del estilo que queremos modificar seguida del valor que le queremos asignar, este puede contener una expresión ternaria ``[style.nombre_estilo]="valor_estilo"``. (Es un estilo inline)

.. code-block:: html+ng2
   :caption: Código HTML

   <p [style.font-style]="nameInput.invalid ? 'italic': 'normal' ">texto texto texto</p>
   
.. note::
   Si queremos modificar los estilos de una etiqueta html antes de definir el valor de la condición por ejemplo el valor de **ngModel** nos va a dar un error.

NgClass & NgStyle
*****************

**NgClass** sirve para agrupar todos los estilos dinámicos [class] de la siguiente manera:

.. code-block:: 
   :caption: Código HTML

   <hr class="line-error"
        [ngClass]="{
            'valid': nameInput.valid,
            'invalid': nameInput.invalid
        }"/>

**NgStyle** podemos agrupar todos los estilo en linea de la siguiente manera: 

.. code-block:: typescript
   :caption: Código TypeScript
   
   export class AppComponent {
       box = {
           name: 'Nicolás',
           height: 100,
           background: 'red'
       }
   }

.. code-block:: 
   :caption: Código HTML

   <div [ngStyle]="{
      'width.px': box.width,
      'height.px': box.height,
      'background-color': box.background,
      'display': 'block'
    }"></div>


Crear un Formulario
###################

Para crear un formulario en Angular utilizamos la directiva **ngForm**. Cuando se presione el botón de enviar formulario se invocara a la función asignada al **ngsubmit**.

.. code-block:: typescript
   :caption: Código TypeScript

   export class AppComponent {
       register = {
           name: '',
           email: '',
           password: ''
       }
   }

.. code-block:: html+ng2
   :caption: Código HTML

   <form  (ngSubmit)="onRegister()" #myForm="ngForm">
    <div class="input.group">
        <label for="name">Nombre</label>
        <input type="text" required id="name" name="name" [(ngModel)]="register.name">
        <p>Mensajes de Error</p>
    </div>
    <div class="input.group">
        <label for="email">Email</label>
        <input type="email" required id="email" name="email" [(ngModel)]="register.email">
        <p>Mensajes de Error</p>
    </div>
    <div class="input.group">
        <label for="password">Password</label>
        <input type="password" required id="password" name="password" [(ngModel)]="register.password">
        <p>Mensajes de Error</p>
    </div>
    <button [disabled]="myForm.invalid" type="submit" >Registrar</button>
   </form>
   
.. warning::
   A los botones dentro de formularios es necesario ponerles un type del tipo **button** para evitar que los tome del tipo **submit** y se envié el formulario de forma involuntaria.


Deployment con firebase
#######################

Los pasos para subir un proyecto en firebase son los siguientes

1. Ir a firebase.google.com 
2. Crear una cuenta de GMail y hacer LogIn
3. Ir a la consola de desarrollo
4. Seleccionar nuevo proyecto
5. Colocar el nombre de nuestro proyecto
6. Le podemos agregar google analytics
7. Seguimos en continuar
8. Seleccionamos build Hosting y le damos empezar
9. Seguir los 3 pasos que nos indica Firebase

.. code-block:: console

   npm install -g firebase-tools


.. code-block:: console

   firebase -V


.. code-block:: console

   firebase login
    

.. code-block:: console

   firebase init

* Si deseamos crear los archivos de firebase en el directorio actual
* Que servicios queremos utilizar --> hosting: configure files
* Queremos crear un proyecto o usar existente --> user an existing 
* Lista de nuestros proyectos --> el que creamos al inicio
* Que carpeta queremos publicar --> ponemos public por defecto
* Reescribir url para single page application --> yes
* Queremos habilitar deployment con github actions --> No
* Borramos el directorio public 
* Crea los archivos de firebase 

10. Compilar nuestro proyecto ng build --> crea directorio dist/nombre_proyecto
11. Cambiamos el parámetro public del archivo firebase.json por el directorio anterior
12. Ultimo paso de firebase ejecutar --> firebase deploy 
13. Listo nos devuelve la URL de nuestro proyecto