import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  constructor() {}

  apiCallTest() {
    const url = 'http://localhost:9001/';
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');

    fetch(url, {
      method: 'GET',
      headers: headers
    })
      .then(response => response.json())
      .then(data => {
        // Manejar la respuesta de la API aquí
        console.log(data);
      })
      .catch(error => {
        // Manejar cualquier error de la petición
        console.error(error);
      });
  }

}

